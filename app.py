from datetime import date
from urllib import request
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.
studentOrganisationDetails = {'Josh': 'Charlotte Hack', 'Khanna': 'Women Who Code', 'Devon': 'Code 9', 'Josh': 'Charlotte Hack', 'Emily': 'Runtime Terror'}

@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html

    return render_template('index.html', currentDate=datetime.datetime.now().replace(microsecond=0))


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')

import math
@app.route('/result', methods=['POST'])
def checkNumber():
    oddOrEven=''
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']

    # Write your to code here to check whether number is even or odd and render result.html page
    if number == '':
        oddOrEven='No number provided'
    elif not number.isnumeric():
        oddOrEven='Provided input is not an integer!'
    elif len(number) > 4300:
        oddOrEven='Your number is too large! (Flask breaks above this amount!)'
    elif int(number) % 2 == 0:
        oddOrEven=number + ' is even!'
    else: 
        oddOrEven=number + ' is odd!'

    return render_template('result.html', oddOrEven=oddOrEven)



@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    return render_template('studentForm.html')


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    org = request.form['org']

    # Append this value to studentOrganisationDetails
    studentOrganisationDetails[studentName] = org

    # Display studentDetails.html with all students and organisations
    return render_template('studentDetails.html', studentOrganisationDetails=studentOrganisationDetails)