
<img src="https://github.com/user-attachments/assets/5f4fd81b-bb63-47de-92d8-919334920957" alt="dump_tool" width="498.5" height="390.5">

# Tkinter MySQL Database Manager

This is a simple desktop application built with Python's Tkinter library for managing contact information stored in a MySQL database. It allows you to add, view, update, and delete records with a user-friendly graphical interface.

---

## Features

* **Add Records:** Easily input Name, Date of Birth, Email, and Phone number to add new entries to the database.
* **View Records:** Displays all stored records in a clear, organized table (Treeview).
* **Select Records:** Click on any record in the table to populate the input fields, making it easy to view and prepare for updates or deletions.
* **Update Records:** Modify existing records after selecting them from the table.
* **Delete Records:** Remove individual records.
* **Delete All Records:** Clear all entries from the database with a confirmation prompt.
* **Refresh Database:** Manually refresh the displayed data from the database.
* **Input Validation:** (Basic) Phone numbers are expected to be unique.
* **Connection Handling:** Handles database connection errors gracefully.

---

## Requirements

To run this application, you need:

* Python 3.x
* `tkinter` (usually comes pre-installed with Python)
* `mysql-connector-python` library
* An active MySQL database connection (specifically, this application is configured for `sql6.freesqldatabase.com` with a specific user and database name).

---

## Setup

1.  **Clone the repository (or save the code):**
    Save the provided Python code as a `.py` file (e.g., `db_app.py`).

2.  **Install necessary libraries:**
    Open your terminal or command prompt and run:

    ```bash
    pip install mysql-connector-python
    ```

3.  **Database Configuration:**
    This application is pre-configured to connect to a specific free MySQL database. You'll be prompted to enter the password for the database when you run the application.
    * **Host:** `sql6.freesqldatabase.com`
    * **User:** `sql6511664`
    * **Database Name:** `sql6511664`

    **Important:** Before running, ensure you have a table named `DEPARTMENT` in your `sql6511664` database with the following schema:

    ```sql
    CREATE TABLE DEPARTMENT (
        Name VARCHAR(255),
        DOB VARCHAR(255), -- Storing as VARCHAR to accommodate 'year-month-day' format
        Email VARCHAR(255),
        Phone BIGINT PRIMARY KEY UNIQUE
    );
    ```

    If you're using a different database or credentials, you'll need to modify the `mysql.connector.connect` line in the Python code.

---

## How to Run

1.  Open your terminal or command prompt.
2.  Navigate to the directory where you saved `db_app.py`.
3.  Run the application using:

    ```bash
    python db_app.py
    ```

4.  A small dialog box will appear asking for the database password. Enter the password and click "OK".
5.  If the connection is successful, the main application window will appear.

---

## Usage

* **Adding a Record:**
    1.  Enter the **Name**, **D-O-B** (in `year-month-day` format), **Email**, and **Phone** in the respective input fields.
    2.  Click the **"ADD"** button.
* **Selecting a Record:**
    1.  Click on any row in the table (the Treeview widget) to select it.
    2.  Click the **"SELECT\_RECORD"** button to populate the input fields with the selected record's data.
* **Updating a Record:**
    1.  First, **select the record** you wish to update using the "SELECT\_RECORD" button.
    2.  Modify the data in the input fields.
    3.  Click the **"UPDATE"** button.
    *Note: The update uses the original Phone number of the selected record as a unique identifier.*
* **Deleting a Record:**
    1.  First, **select the record** you wish to delete using the "SELECT\_RECORD" button.
    2.  Click the **"DELETE"** button.
* **Deleting All Records:**
    1.  Click the **"DELETE ALL"** button.
    2.  Confirm your decision in the pop-up warning.
* **Refreshing Data:**
    1.  Click the **"REFRESH\_DATABASE"** button to reload all records from the database and update the table display.

---

## Developed By

Mithlesh BCA
* **LinkedIn/Instagram:** `@mithlesh1144`
