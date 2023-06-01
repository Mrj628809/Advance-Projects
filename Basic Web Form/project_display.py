#!/usr/bin/python3
import pymysql
import re 

print("Content-Type: text/html \n")

def read_data():
      
    try:    
        conn = pymysql.connect(
        host='localhost',
        db='judson',
        user='judson',
        password='judson'
        )
     
        cursor = conn.cursor()
     
        sql  = "SELECT fname, lname, address, grade_level, major FROM college_students ORDER BY id" 

        cursor.execute(sql);
        
        print('<table border="1">')
        print('<tr><th>First Name</th><th>Last Name</th><th>Address</th><th>Grade Level</th><th>Major</th></tr>')
     
        for row in cursor.fetchall():
            print('<tr>')
            for col in row:
                print('<td>{}</td>'.format(col))
            print('</tr>')

        print('</table>')
    
    except pymysql.Error as e:
        errorNum = e.args[0]
        errorMsg = e.args[1]
        error = 'Database Error - ' + str(errorNum) + errorMsg
        print(error)
        return   

read_data();
