# Online-Movie-Ticket-Booking-System
Online Movie Ticket Booking System is a full-stack web application which allows the user to browse the movies, select a movie, book the tickets with selecting seats, and includes the payment integration.

**Features**
- View currently available movies
- User registration (name, email, phone)
- Seat selection with real-time UI updates
- Show date and time selection
- Payment simulation system
- Booking confirmation page

**Technologies Used**
- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- Database: Oracle DB (oracledb)

## How to Run the Project

1. Clone the repository:
   git clone <your-repo-link>

2. Install dependencies:
   pip install flask oracledb flask-cors

3. Run the backend server:
   python python.py (backend file)

4. Open the frontend in browser:
   http://127.0.0.1:5000

Ensure that you've installed Run SQL Command Line and have your own username and password, and replace my details with your username and password created.

**Project Highlights:**
-Designed a responsive UI for better user experience
-Integrated frontend with backend APIs using Fetch API
-Connected Oracle database for storing users, bookings, and payments
-Implemented validation for user inputs and payment details

**Screenshots:**

##Home Page
<img width="1421" height="890" alt="Screenshot 2026-04-20 012736" src="https://github.com/user-attachments/assets/52abe5f9-fc89-4e73-bac3-3f4145556634" />

##Login Page
<img width="726" height="609" alt="Screenshot 2026-04-20 012805" src="https://github.com/user-attachments/assets/e6f67888-b332-419d-ba1c-178b9edcc3ea" />

##Booking details page
<img width="1799" height="712" alt="Screenshot 2026-04-20 012849" src="https://github.com/user-attachments/assets/7b51a2c7-e2de-4fe6-8c4d-1c190a1e90d5" />

##Payments page
<img width="783" height="590" alt="Screenshot 2026-04-20 012921" src="https://github.com/user-attachments/assets/33863123-9257-4fdd-89f1-8e5d99558213" />

##Booking Confirmation Page
<img width="665" height="439" alt="Screenshot 2026-04-20 012930" src="https://github.com/user-attachments/assets/0cdbcb3a-d6e6-409d-9301-75558987357b" />


**Future Improvements:**
-Add login authentication system
-Store show and booking details in the tables in database
-Add admin dashboard
-Integrate real payment gateway
-Deploy project online
