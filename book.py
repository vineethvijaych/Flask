from flask import Flask,request,send_from_directory
from flask import render_template
from werkzeug.utils import secure_filename
import os
import sqlite3 as sql

app = Flask(__name__)

BOOK_FOLDER = './BOOK_FOLDER'
app.config['BOOK_FOLDER'] = BOOK_FOLDER


@app.route('/')
def home():
      return render_template('home.html')


@app.route('/bform',methods=['POST','GET'])
def bform():
      if request.method == 'POST':
            
            nm= request.form['name']
            p= request.form['author']

            f= request.files['file']
            filename=secure_filename(f.filename)
            f.save(os.path.join(app.config['BOOK_FOLDER'],filename))

            con = sql.connect("database3.db")
            cur = con.cursor()
            cur.execute("INSERT INTO book(name,author,pdf) VALUES (?,?,?)",(nm,p,filename))
            con.commit()

            return render_template('resultb.html')
      return render_template('bform.html')

@app.route('/uploader',methods=['POST','GET'])
def uploader():
      if request.method== 'POST':
            f= request.files['file']
            filename= secure_filename(f.filename)
            f.save(os.path.join(app.config['BOOK_FOLDER'],filename))
            return render_template('uploader.html',x=filename)
      

@app.route('/up/<f>')
def uploaded_file(f):
      return send_from_directory(app.config['BOOK_FOLDER'],f)

@app.route('/booklist')
def booklist():
      con = sql.connect("database3.db")
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("select * from book")
      rows = cur.fetchall()
      return render_template('booklist.html',rows=rows)

if __name__=='__main__':
      app.run()
      
