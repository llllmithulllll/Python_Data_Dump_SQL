# Tkinter MySQL Database Manager

This is a simple desktop application built with Python's Tkinter library for managing contact information stored in a MySQL database. It allows you to add, view, update, and delete records with a user-friendly graphical interface.


## Features

Add Records: Easily input Name, Date of Birth, Email, and Phone number to add new entries to the database.

View Records: Displays all stored records in a clear, organized table (Treeview).

Select Records: Click on any record in the table to populate the input fields, making it easy to view and prepare for updates or deletions.

Update Records: Modify existing records after selecting them from the table.

Delete Records: Remove individual records.

Delete All Records: Clear all entries from the database with a confirmation prompt.

Refresh Database: Manually refresh the displayed data from the database.

Input Validation: (Basic) Phone numbers are expected to be unique.

Connection Handling: Handles database connection errors gracefully.

## Requirements
To run this application, you need:

Python 3.x

tkinter (usually comes pre-installed with Python)

mysql-connector-python library

An active MySQL database connection (specifically, this application is configured for sql6.freesqldatabase.com with a specific user and database name).

## Setup
Clone the repository (or save the code):
Save the provided Python code as a .py file (e.g., db_app.py).

Install necessary libraries:
Open your terminal or command prompt and run:

pip install mysql-connector-python

Database Configuration:
This application is pre-configured to connect to a specific free MySQL database. You'll be prompted to enter the password for the database when you run the application.

Host: sql6.freesqldatabase.com

User: sql6511664

Database Name: sql6511664

Important: Before running, ensure you have a table named DEPARTMENT in your sql6511664 database with the following schema:

CREATE TABLE DEPARTMENT (
    Name VARCHAR(255),
    DOB VARCHAR(255), -- Storing as VARCHAR to accommodate 'year-month-day' format
    Email VARCHAR(255),
    Phone BIGINT PRIMARY KEY UNIQUE
);

If you're using a different database or credentials, you'll need to modify the mysql.connector.connect line in the Python code.

## How to Run
Open your terminal or command prompt.

Navigate to the directory where you saved db_app.py.

Run the application using:

python db_app.py

A small dialog box will appear asking for the database password. Enter the password and click "OK".

If the connection is successful, the main application window will appear.

Usage
Adding a Record:

Enter the Name, D-O-B (in year-month-day format), Email, and Phone in the respective input fields.

Click the "ADD" button.

Selecting a Record:

Click on any row in the table (the Treeview widget) to select it.

Click the "SELECT_RECORD" button to populate the input fields with the selected record's data.

Updating a Record:

First, select the record you wish to update using the "SELECT_RECORD" button.

Modify the data in the input fields.

Click the "UPDATE" button.
Note: The update uses the original Phone number of the selected record as a unique identifier.

Deleting a Record:

First, select the record you wish to delete using the "SELECT_RECORD" button.

Click the "DELETE" button.

Deleting All Records:

Click the "DELETE ALL" button.

Confirm your decision in the pop-up warning.

Refreshing Data:

Click the "REFRESH_DATABASE" button to reload all records from the database and update the table display.

Developed By
Mithlesh BCA

LinkedIn/Instagram: @mithlesh1144
