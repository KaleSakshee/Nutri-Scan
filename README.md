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


