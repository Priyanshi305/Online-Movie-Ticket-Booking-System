from flask import Flask, request, jsonify, render_template
import oracledb
from datetime import datetime
import random

app = Flask(__name__)

# -------------------------------------------
# 🔗 ORACLE DATABASE CONNECTION (THICK MODE)
# -------------------------------------------
try:
    # Path to your Instant Client (must contain oci.dll)
    oracledb.init_oracle_client(lib_dir=r"C:\Users\Priyanshi\Downloads\oraclexe\instantclient_23_9")

    # Connect to Oracle Database
    connection = oracledb.connect(
        user="priyanshi123",
        password="ppr108",
        dsn="localhost/XE"  
    )
    print("✅ Connected to Oracle Database")

except Exception as e:
    print("❌ Database connection failed:", e)


# -------------------------------------------
# 🏠 HOME ROUTE (Render frontend)
# -------------------------------------------
@app.route('/')
def home():
    return render_template('loginhome.html')


# -------------------------------------------
# 👤 USER REGISTRATION
# -------------------------------------------
@app.route('/register_user', methods=['POST'])
def register_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    phone = data.get('phone')

    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO users (user_id, name, email, password, phone)
            VALUES ((SELECT NVL(MAX(user_id), 0) + 1 FROM users), :1, :2, :3, :4)
        """, (name, email, password, phone))
        connection.commit()
        cursor.close()
        return jsonify({"message": "User registered successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# -------------------------------------------
# 🎬 ADD MOVIE
# -------------------------------------------
@app.route('/add_movie', methods=['POST'])
def add_movie():
    data = request.get_json()
    title = data.get('title')

    # 🎬 Genre options
    genres = ['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Thriller', 'Romance', 'Horror','Crime']
    genre = random.choice(genres)

    # 📝 Description options
    descriptions = [
        'An unforgettable cinematic experience.',
        'A story that touches your heart.',
        'A thrilling adventure from start to finish.',
        'A journey through emotions and action.',
        'A masterpiece of modern storytelling.'
    ]
    description = random.choice(descriptions)

    # ⏱️ Random duration between 1 and 3 hours (float)
    duration = round(random.uniform(1.0, 3.0), 1)

    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO movie (movie_id, title, genre, duration, description)
            VALUES ((SELECT NVL(MAX(movie_id), 0) + 1 FROM movie), :1, :2, :3, :4)
        """, (title, genre, duration, description))
        connection.commit()
        cursor.close()
        return jsonify({
            "message": "Movie added successfully!",
            "title": title,
            "genre": genre,
            "duration": duration,
            "description": description
        }), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 400
# -------------------------------------------
# 🕒 ADD SHOW
# -------------------------------------------
@app.route('/add_show', methods=['POST'])
def add_show():
    data = request.get_json()
    title = data.get('title')
    movie_id=data.get('movie_id',1)
    theater_id = data.get('theater_id', 1)  # default 1 if not passed
    show_date = data.get('show_date')
    show_time = data.get('show_time')

    try:
        cursor = connection.cursor()
        # 2️⃣ Insert the new show (show_date is DATE, show_time is VARCHAR)
        cursor.execute("""
            INSERT INTO show (show_id, movie_id, theater_id, show_date, show_time)
            VALUES (
                (SELECT NVL(MAX(show_id), 0) + 1 FROM show),
                :movie_id,
                :theater_id,
                TO_DATE(:show_date, 'YYYY-MM-DD'),
                :show_time
            )
        """, 
        {
            'movie_id': movie_id,
            'theater_id': theater_id,
            'show_date': show_date,
            'show_time': show_time
        })

        connection.commit()
        cursor.close()
        return jsonify({'message': 'Show added successfully!'}), 200

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({'error': str(e)}), 400

# -------------------------------------------
#  THEATER
# -------------------------------------------
@app.route('/add_theater', methods=['POST'])
def add_theater():
    try:
        # 🎭 Random theater names and locations
        theater_names = [
            "Cineplex Galaxy", "Regal Cinemas", "PVR Grand", "Inox Prime",
            "Majestic Screen", "FunSquare", "SilverCity", "CineWorld", "StarLight", "DreamTheater"
        ]

        theater_locations = [
            "Bangalore", "Chennai", "Delhi", "Hyderabad", "Mumbai",
            "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Chandigarh"
        ]

        # Randomly select name and location
        name = random.choice(theater_names)
        location = random.choice(theater_locations)

        cursor = connection.cursor()

        # ✅ Insert with auto-incremented ID
        cursor.execute("""
            INSERT INTO theater (theater_id, name, location)
            VALUES (
                (SELECT NVL(MAX(theater_id), 0) + 1 FROM theater),
                :name,
                :location
            )
        """, {"name": name, "location": location})

        connection.commit()
        cursor.close()

        return jsonify({
            "message": "🎬 Random theater added successfully!",
            "name": name,
            "location": location
        }), 200

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"error": str(e)}), 400

# 💳 ADD PAYMENT
@app.route('/add_payment', methods=['POST'])
def add_payment():
    data = request.get_json()
    booking_id = data.get('booking_id')
    cardname = data.get('cardname')
    cardnumber = data.get('cardnumber')
    expirydate = data.get('expirydate')
    cvv = data.get('cvv')

    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO payment (payment_id, booking_id, cardname, cardnumber, expirydate, cvv)
            VALUES (
                (SELECT NVL(MAX(payment_id), 0) + 1 FROM payment),
                :1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5
            )
        """, (booking_id, cardname, cardnumber, expirydate, cvv))
        connection.commit()
        cursor.close()
        return jsonify({"message": "Payment added successfully!"}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 400


# -------------------------------------------
# 🧾 VIEW BOOKINGS
# -------------------------------------------
@app.route('/bookings/<int:user_id>', methods=['GET'])
def get_user_bookings(user_id):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT b.booking_id, m.title, s.show_date, s.show_time, b.total_tickets, b.total_amount, b.status
            FROM booking b
            JOIN show s ON b.show_id = s.show_id
            JOIN movie m ON s.movie_id = m.movie_id
            WHERE b.user_id = :1
        """, (user_id,))
        rows = cursor.fetchall()
        cursor.close()

        bookings = []
        for r in rows:
            bookings.append({
                "booking_id": r[0],
                "movie_title": r[1],
                "show_date": str(r[2]),
                "show_time": r[3],
                "tickets": r[4],
                "amount": float(r[5]),
                "status": r[6]
            })
        return jsonify(bookings)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# -------------------------------------------
# 🚀 RUN APP
# -------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
