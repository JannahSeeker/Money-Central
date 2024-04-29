from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, BankAccount, Transaction
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home(): 
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("frontend/home_page.html", user=current_user)

@views.route('/settings', methods=['GET', 'POST'])
@login_required
def settings(): 
     return render_template("frontend/settings.html", user=current_user)


@views.route('/homeview', methods=['GET', 'POST'])
@login_required
def homeview(): 
    if request.method == 'POST': 
        account = request.form.get('selection')#Gets the note from the HTML 
        if account:
            new_account = BankAccount(balance = 0.00, type=account, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_account) #adding the note to the database 
            db.session.commit()
    return render_template("frontend/home.html", user=current_user)


@views.route('/account', methods=['GET', 'POST'])
@login_required
def account(): 

    return render_template("frontend/Account.html", user=current_user)


@views.route('/account/<int:bank_account_id>')
@login_required
def view_bank_account(bank_account_id):
    # Execute a SQL query to retrieve the bank account by ID
    bank_account = db.session.query(BankAccount).filter_by(id=bank_account_id).first()

    if bank_account is None:
        # Redirect the user to a previous page or a specific route
        return redirect(url_for('views.homeview'))

    return render_template('frontend/Account.html', user=bank_account)

@views.route('/account/<int:bank_account_id>/deposit', methods=['POST'])
@login_required
def deposit(bank_account_id):
    # Execute a SQL query to retrieve the bank account by ID
    bank_account = db.session.query(BankAccount).filter_by(id=bank_account_id).first()

    if bank_account is None:
        # Redirect the user to a previous page or a specific route
        return redirect(url_for('views.homeview'))

    if request.method == 'POST':
        amount = float(request.form['amount'])
        bank_account.deposit(amount)
        return redirect(url_for('views.view_bank_account', bank_account_id=bank_account_id))

    return render_template('frontend/Account.html', user=bank_account)


@views.route('/account/<int:bank_account_id>/withdraw', methods=['POST'])
@login_required
def withdraw(bank_account_id):
    # Execute a SQL query to retrieve the bank account by ID
    bank_account = db.session.query(BankAccount).filter_by(id=bank_account_id).first()

    if bank_account is None:
        # Redirect the user to a previous page or a specific route
        return redirect(url_for('views.homeview'))

    if request.method == 'POST':
        amount = float(request.form['amount'])
        bank_account.withdraw(amount)
        return redirect(url_for('views.view_bank_account', bank_account_id=bank_account_id))

    return render_template('frontend/Account.html', user=bank_account)

@views.route('/account/<int:bank_account_id>/delete', methods=['GET','POST'])
@login_required
def delete_account(bank_account_id):
    # Execute a SQL query to retrieve the bank account by ID
    bank_account = db.session.query(BankAccount).filter_by(id=bank_account_id).first()

    if bank_account is None:
        # Redirect the user to a previous page or a specific route
        return redirect(url_for('views.homeview'))

    if bank_account:
       
            db.session.delete(bank_account)
            db.session.commit()
            return render_template('frontend/home.html', user=current_user)


    return render_template('frontend/home.html', user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
