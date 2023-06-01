#!/usr/bin/env python3

import pymysql
import cgi
import cgitb

cgitb.enable()

def validate_data(fname, lname, address, grade_level, major):
    errors = []
    if not fname:
        errors.append("First name is required.")
    if not lname:
        errors.append("Last name is required.")
    if not address:
        errors.append("Address is required.")
    if not grade_level:
        errors.append("Grade level is required.")
    if not major:
        errors.append("Major is required.")
    return errors

try:
    db = pymysql.connect(
        host="localhost",
        user="judson",
        password="judson",
        database="judson"
    )
except pymysql.Error as error:
    print("Failed to connect to database: {}".format(error))
    exit(1)

form = cgi.FieldStorage()
fname = form.getvalue('fname')
lname = form.getvalue('lname')
address = form.getvalue('address')
grade_level = form.getvalue('grade_level')
major = form.getvalue('major')

errors = validate_data(fname, lname, address, grade_level, major)

if not errors:
    cursor = db.cursor()
    sql = f"""INSERT INTO college_students (id, fname, lname, address, grade_level, major) 
              VALUES (0, '{fname}', '{lname}', '{address}', '{grade_level}', '{major}')"""
    cursor.execute(sql)
    db.commit()

    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>Success</title>")
    print("</head>")
    print("<body>")
    print("<h1>Form submitted successfully</h1>")
    print("</body>")
    print("</html>")

else:
    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>Error</title>")
    print("</head>")
    print("<body>")
    print("<h1>Please correct the following errors:</h1>")
    print("<ul>")
    for error in errors:
        print(f"<li>{error}</li>")
    print("</ul>")
    print("</body>")
    print("</html>")
