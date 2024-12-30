from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # 'Income' or 'Expense'
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

# Home Route
@app.route('/')
def index():
    transactions = Transaction.query.order_by(Transaction.date.desc()).all()
    total_income = sum(t.amount for t in transactions if t.type == "Income")
    total_expenses = sum(t.amount for t in transactions if t.type == "Expense")
    balance = total_income - total_expenses
    return render_template(
        'index.html',
        transactions=transactions,
        total_income=total_income,
        total_expenses=total_expenses,
        balance=balance
    )

# Add Transaction Route
@app.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        description = request.form['description']
        transaction_type = request.form['type']
        amount = float(request.form['amount'])
        
        new_transaction = Transaction(
            description=description, 
            type=transaction_type, 
            amount=amount
        )
        db.session.add(new_transaction)
        db.session.commit()
        return redirect('/')
    
    return render_template('add_transaction.html')

# Delete Transaction Route (Handling with Form)
@app.route('/delete_transaction/<int:transaction_id>', methods=['POST'])
def delete_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    db.session.delete(transaction)
    db.session.commit()
    return redirect('/')

# Run the App
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensures the database is created
    app.run(debug=True)
