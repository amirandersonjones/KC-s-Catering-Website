#initial auth system setup stuff:
    #we need to connect this system to our larger flask app so we define it as a blueprint
from flask import Blueprint, render_template, request, redirect, url_for, flash

#define blueprint/instantiate
auth= Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')

#import forms
from .authforms import SignInForm, RegisterForm

#make my first route in the auth blueprint
@auth.route('/', methods=['GET','POST'])
def signin():
    siform = SignInForm()
    if request.method == 'POST':  #user submitted the form
        if siform.validate_on_submit(): #ok the user gave us proper form info   
            print(siform.data)
            #actually go about signing the user in
            #successful sign-in:redirect user to homepage-THIS COULD CHANGE DEPENDING ON HOW I SET UP KELLIE'S PAGE
            flash(f'Welcome back, {siform.username.data}!')
            return redirect(url_for('home'))
        else: #they did not give proper info
            flash('Login failed, incorrect username or password!')
            return redirect(url_for('auth.signin')) #redirect to url for sign in page
    return render_template('signin.html', siform=siform)

@auth.route('/register', methods=['GET','POST'])
def register():
    rform = RegisterForm()
    if request.method == 'POST':  #user submitted the form
        if rform.validate_on_submit(): #ok the user gave us proper form info   
            print(rform.data)
            #actually go about signing the user in
            #successful registration-in:redirect user to homepage-THIS COULD CHANGE DEPENDING ON HOW I SET UP KELLIE'S PAGE
            flash(f'Successfully registered! Welcome, {rform.first_name.data}!')
            return redirect(url_for('home'))
        else: #they did not give proper info
            flash('Your passwords did not match or you provided an improper email/username.Try again!')
            return redirect(url_for('auth.register')) #redirect to url for sign in page
    return render_template('register.html', rform=rform)