# Expense Tracker

#### Video Demo: [<URL HERE>](<URL HERE>)

### Description:

This is an **Expense Tracker** web application built as part of the CS50 course requirements. The goal of this project is to help users manage their personal finances by tracking income, expenses, and their overall balance.

### Features:
- **Add Transaction**: Allows users to add income or expense transactions.
- **View Summary**: Displays total income, total expenses, and balance.
- **View Transactions**: Lists all transactions with options to delete specific entries.
- **Responsive Design**: Designed to work across devices, ensuring an optimized experience for both desktop and mobile users.
- **User-Friendly Interface**: Clear, well-organized interface with simple navigation.

### Technologies Used:
- **HTML**: Structuring the content and layout of the page.
- **CSS**: Styling the user interface to make it visually appealing.
- **Flask (Python Framework)**: Backend handling for the dynamic generation of content, including data from the server.

### Setup Instructions:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/amanmauryas/expense_tracker.git
   cd expense_tracker
2. **Install Dependencies**:
   You may need to install the required libraries, particularly Flask:
   ```bash
   pip install Flask==2.3.3 Flask-SQLAlchemy==3.0.4 SQLAlchemy==2.0.20 Flask-WTF==1.0.1 Flask-Migrate==3.1.0 Flask-Login==0.6.3
  
3. **Run the Flask Application**: Start the server:
     ```bash
     python app.py

4. **Visit the Web App**: Navigate to http://localhost:5000 in your browser.

### Project Structure:
- **index.html**: Main page displaying the expense tracker UI, with options for viewing and adding transactions.
- **style.css**: Styling for the layout, tables, and buttons.
- **app.py**: The main backend file to run the server, handle routes, and process transactions.
- **models.py**: File containing the Transaction model (this is typically where SQLAlchemy models will be defined).
- **templates/**: Folder for HTML templates (if using Jinja2 templates for dynamic content).
### Contributing:
If you want to contribute to this project, feel free to fork the repository, make changes, and submit pull requests.

### License:
This project is open-source, and you can freely use, modify, and distribute it under the terms of the MIT License.

### How to Use:
The app is completely web-based and user friendly. Also You can follow video tutorial to use the web app






