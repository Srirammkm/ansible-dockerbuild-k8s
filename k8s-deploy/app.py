import os
import mysql.connector
from flask import Flask, render_template, request
app = Flask(__name__)
mydb = mysql.connector.connect(
  #host in which DB is running. In this case IKS cluste.
  host="169.57.56.131",
  port=30002,
  user="root",
  password="root",
  database="MyDB"
)
mycursor = mydb.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        val = [(firstName, lastName)]
        sql = "INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)"
        mycursor.executemany(sql, val)
        mydb.commit()
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    res = ''
    if request.method == "POST":
        details = request.form
        fname = details["fname"]
        sql = "SELECT * FROM MyUsers WHERE firstName =  %s"
        name = (fname,)
        mycursor.execute(sql,name)
        res = mycursor.fetchall()
    return render_template('search.html', res = res)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
