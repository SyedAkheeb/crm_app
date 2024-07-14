# CRM Application

## Description
This is a Customer Relationship Management (CRM) application with functionalities for generating, preprocessing, and entering data into an SQLite3 database. It also includes features for querying, updating leads, syncing changes, performing qualitative analysis using Pie Charts, and calculating payouts based on conversions.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/akheeb/CRM_App.git
   Navigate to the project directory:

cd CRM_App
(Optional) Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the dependencies:
pip install -r requirements.txt
Usage
Run the application:
python main.py
File Descriptions
main.py: Contains the business logic of the CRM application.
init.py: Initialization script for setting up the database and any initial configurations.
database.db: The SQLite3 database file.
data/leads.csv: Example CSV data file.
data/report.html: Example HTML report.
requirements.txt: List of dependencies required for the project.
README.md: Project documentation.
Dependencies
Python 3.x
SQLite3
(Other dependencies listed in requirements.txt)
Author Syed Akheebuddin