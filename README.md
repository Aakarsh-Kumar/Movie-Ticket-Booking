
# <div align="center"> Movie Ticket Booking System </div>

## <div align="center"> A Streamlined Ticket Booking Platform 🎭 </div>

An efficient and user-friendly ticket booking system for theatres, built using Flask. This application allows users to view available shows, book tickets, book beverages, and cancel tickets seamlessly. It is entirely backend-driven, leveraging SQLAlchemy for database interactions and providing REST APIs for all functionalities.

## 🚀 Features
- **Show Listings**: Browse shows with timings, availability, and pricing.
- **Reservation Management**: Book or cancel reservations with API endpoints.
- **Admin Operations**: Add Theaters, Screens, Shows and manage bookings.
- **REST API**: Comprehensive Postman collection included for seamless testing.
- **Waiting List**: When there are no available seats for the show, the booking request is sent to waiting list, which updates till 30mins before the start of the show depending on the cancellation of existing booking.

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.8 or higher
- Flask and SQLAlchemy installed on your system
- Postman (for testing API endpoints)

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/Aakarsh-Kumar/Movie-Ticket-Booking.git
   ```
   ```
   cd Movie-Ticket-Booking
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
   
4. Configure your `.env` file with necessary environment variables like database uri and secret keys.

5. Set up the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```


## 🗂️ Project Structure
```
Movie-Ticket-Booking/
├── app/                                  # Application Code
│   ├── __init__.py                       # App Initialization and Configuration
│   ├── models.py                         # SQLAlchemy Models
│   └── routes/                           # API Endpoints
│       ├── booking_routes.py             # Booking Route
│       ├── cacncel_booking_routes.py     # Cancel Booking Route
│       ├── food_routes.py                # Food Route
│       ├── movie_routes.py               # Shows in the Screen Route
│       ├── screen_routes.py              # Screen in the Theater Route
│       ├── theater_routes.py             # Theater Route
│       └── user_routes.py                # User Route
├── instance/                             # Instance-Specific Configuration
├── migrations/                           # Database Migrations
├── config.py                             # Application Configuration
├── app.py                                # Main Flask Application Server
├── requirements.txt                      # Python Dependencies
├── postman/                              # Postman Collection for API Testing
└── README.md                             # Project Documentation
```
## 🛢 Database Structure

![Database Structure](https://raw.githubusercontent.com/Aakarsh-Kumar/Movie-Ticket-Booking/refs/heads/main/SQLAlchemy_Database_Flowchart.png)


---  

## ⚙️ Running the Application

1. Start the Flask server:
   ```
   flask run
   ```

2. Access the application locally at:
   ```
   http://127.0.0.1:5000
   ```

---

## 📩 API Testing with Postman

To test the REST API endpoints:

1. Open Postman and import the provided Postman collection from the `postman/` folder.
2. Ensure the Flask server is running.
3. Use the endpoints in the collection to test functionalities such as:
   - **Fetching Show Listings**
   - **Booking Tickets**
   - **Booking Foods**
   - **Admin Operations: Adding Theaters, Screens, Movies**
   - **Cancellation of bookings**

---

## 🔗 Connect with Me

* 💼 LinkedIn: [aakarsh-kumar-158ab1222](https://www.linkedin.com/in/aakarsh-kumar-158ab1222/)
* 💻 GitHub: [Aakarsh-Kumar](https://github.com/Aakarsh-Kumar)
* 📱 Instagram: [@aakarsh_kumar25](https://www.instagram.com/aakarsh_kumar25/)

---

## 🌟 Acknowledgments

Special thanks to my seniors @Networking Nexus SRM, peers, and all those who made this project possible. Your support and guidance have been invaluable!

## <div align="center"> Made with ❤️ to enhance your theatrical experience </div>
