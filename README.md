# Late Show Dashboard

## Description
This project is a web application for tracking episodes, guests, and appearances on a late show. It uses **Flask**, **SQLAlchemy**, and **SQLite** for the backend, and a simple **HTML/JavaScript** frontend to interact with the API.

## Features
- View all episodes
- View all guests
- Add guest appearances with ratings
- Delete episodes
- JSON API for integration

## Backend
- Built with Flask
- Database managed with SQLAlchemy and Flask-Migrate
- CORS enabled for frontend integration

## Frontend
- Simple HTML, CSS, and JavaScript
- Fetches data from the backend API
- Displays episodes, guests, and server responses
- Form to create new appearances

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <your-repo-url
   cd late-show

## Create and activate virtual environment:

pipenv install
pipenv shell


## Initialize database:

export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial"
flask db upgrade


Seed the database:

python server/seed.py


Run the Flask server:

flask run


Open the frontend:

client/index.html


(Open in your browser)

## Author

Sharon Njoroge
Email: waithirasharon@gmail.com