# Nutri-Scan: Ingredient Safety Checker

Nutri-Scan is a lightweight app that scans or searches product ingredients to identify harmful substances. It considers the user’s health profile (like allergies) and provides risk insights, reasons for concern, and safer alternatives. Past searches are stored for user reference.

## Project Structure

Nutri-Scan/
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
├── backend/
│ ├── app.py
│ ├── analyzer.py
│ ├── barcode_parser.py
│ ├── history_manager.py
│ ├── profile_manager.py
│ ├── ingredient_datas.csv
│ ├── product_alternatives.csv
│ └── user_data.json
├── requirements.txt
└── README.md


## Key Features

- Scan barcode or search product manually
- Analyze ingredients and highlight risks
- Personalize results using health profile
- Show safer alternative products
- Store and access past scans/searches

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- Data: CSV, JSON
- Version Control: Git & GitHub

# NutriScan Frontend

## Features
- Responsive and accessible login and signup forms
- Large, bold, and engaging input fields and buttons for better user experience
- Toggle between login and signup forms without page reload
- Aesthetic header image and clean UI design
- Uses localStorage for simple user state management (demo purposes)

## How to Run
1. Clone this repo.
2. Open `login.html` in a modern web browser.
3. Enter credentials and test login/signup functionality.
4. Upon login/signup, user is redirected to `index.html`.

### Tech stack
- Plain HTML, CSS, and JavaScript — no frameworks

### Notes
- No backend yet — just frontend for now
- User info is saved locally in your browser’s storage for demo purposes only.