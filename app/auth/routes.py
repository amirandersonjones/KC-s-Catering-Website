#initial auth system setup stuff:
    #we need to connect this system to our larger flask app so we define it as a blueprint
from flask import Blueprint, render_template, request, redirect, url_for, flash

#define blueprint/instantiate
auth= Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')

#import forms
from .authforms import SignInForm, RegisterForm

#import user and login stuff:
from app.models import Customer, db
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user,logout_user, login_required


#make my first route in the auth blueprint
@auth.route('/', methods=['GET','POST'])
def signin():
    siform = SignInForm()
    if request.method == 'POST':  #user submitted the form
        if siform.validate_on_submit(): #ok the user gave us proper form info   
            #actually go about signing the user in
               #check if the username actually exists in the database/have to query our database
            customer = Customer.query.filter_by(username=siform.username.data).first()
             #if it does, check if the password matches
             #this function returns true if these two match and false if they dont
            if customer and check_password_hash(customer.password, siform.password.data):
                login_user(customer)
                print(current_user, current_user.__dict__)
                #successful sign-in:redirect user to homepage-THIS COULD CHANGE DEPENDING ON HOW I SET UP KELLIE'S PAGE
                flash(f'Welcome back, {current_user.first_name}!')
                return redirect(url_for('home'))   
                #if either username doesn't exist or password doesnt match-reject
                #everthing looks food sign the user in through our login manager
        #they did not give proper info  
        flash('Login failed, incorrect username or password!', category='info')
        return redirect(url_for('auth.signin')) #redirect to url for sign in page
    return render_template('signin.html', siform=siform)

@auth.route('/register', methods=['GET','POST'])
def register():
    rform = RegisterForm()
    if request.method == 'POST':  #user submitted the form
        if rform.validate_on_submit(): #ok the user gave us proper form info
            #actually go about signing the user in
            newcustomer = Customer(rform.username.data, rform.phone.data, rform.email.data, rform.address.data, rform.password.data, rform.first_name.data, rform.last_name.data)  
            try: #will produce an error if the username or password is taken
                db.session.add(newcustomer)
                db.session.commit()
            except:
                flash(f'That username or email is taken. Please try a different one.', category='danger') 
                return redirect(url_for('auth.register')) #redirect to url for sign in page
            login_user(newcustomer)   
            flash(f'Successfully registered! Welcome, {rform.first_name.data}!', category='success')
            return redirect(url_for('home')) #successful registration-in:redirect user to homepage-THIS COULD CHANGE DEPENDING ON HOW I SET UP KELLIE'S PAGE
        else: #they did not give proper info
            flash('Your passwords did not match or you provided an improper email/username.Try again!', category='danger')
            return redirect(url_for('auth.register'))
    return render_template('register.html', rform=rform)

@auth.route('/logout')
@login_required
def signout():
    logout_user()
    flash('You have been signed out.', category='info')
    return redirect(url_for('auth.signin'))