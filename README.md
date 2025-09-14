# DishDiscover
A simple and easy-to-use Django-based web app where users can share their favorite recipes and cooking experiences with others. Perfect for food lovers who want to explore and contribute delicious dishes.

# Motivation 
Many food enthusiasts struggle to find a platform where they can share personal recipes and cooking experiences in an organized, interactive way. DishDiscover solves this by letting users post, comment, and explore recipes easily.

# Features 
 User registration & login system : Django session Based authentication.
 <img width="787" height="863" alt="Register" src="https://github.com/user-attachments/assets/d0533683-f7c5-42a3-b4b5-48c8ddb23213" />

 Create, read, update, and delete (CRUD) recipes
 Upload images of your dishes
 Browse recipes shared by other users
 Comment and share cooking experiences
 Responsive UI using Tailwind CSS 

# Tech Stack
Backend: Django (Python)
Frontend: HTML, CSS (Tailwind)
Database: SQLite (default)
Auth: Django built-in authentication system

# Getting Started
1) Clone the Repository :
git clone (https://github.com/Lakde-Maheshwari/DishDiscover.git)
cd dishdiscover


2) Create Virtual Environment :
python -m venv venv
on linux or mac: source venv/bin/activate
On Windows: venv\Scripts\activate


4) Install Dependencies :
pip install -r requirements.txt


5) Apply Migrations :
python manage.py makemigrations
python manage.py migrate

6) Run the Server :
python manage.py runserver
Open and go to the browswer http://127.0.0.1:8000/

