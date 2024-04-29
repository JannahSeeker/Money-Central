from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Numeric, Float
# from decimal import Decimal
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    type = db.Column(db.String(50))  # Added type field to distinguish between deposit and withdraw
    bank_account_id = db.Column(db.Integer, db.ForeignKey('bank_account.id'))

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class BankAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float)  # Numeric type with precision 10 and scale 2
    type = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    transactions = db.relationship('Transaction', backref='bank_account', lazy=True)

    def deposit(self, amount):
        # Convert the amount to Decimal before performing the operation
        amount_decimal = int(amount)
        print(type(amount_decimal))
        print(type(self.balance))
        print("Hello")
        self.balance = self.balance + amount_decimal
        print(self.balance)
        self._add_transaction(amount_decimal, 'deposit')

    def withdraw(self, amount):
        # Convert the amount to Decimal before performing the operation
        amount_decimal =  int(amount)
        print(type(amount_decimal))
        print(type(self.balance))
        if self.balance >= amount_decimal:
            self.balance -= amount_decimal
            self._add_transaction(amount_decimal, 'withdraw')
        else:
            raise ValueError("Insufficient funds")

    def _add_transaction(self, amount, type):
        transaction = Transaction(amount=amount, type=type, bank_account_id=self.id)
        db.session.add(transaction)
        db.session.commit()

    def get_transaction_history(self):
        return self.transactions.order_by(Transaction.date.desc()).all()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.Integer)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    bankaccounts = db.relationship('BankAccount')

