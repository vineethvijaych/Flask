from flask import Flask
from flask import render_template
from flask import request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
      return render_template('home.html')

@app.route('/page1')
def page1():
      d="kevin"
      return render_template('page1.html',n=d)


@app.route('/page2')
def page2():
      x=[1,2,3,4]
      y={'name':'arun','age':'24','place':'kochi'}

    
      return render_template('page2.html',n=x,s=y)


@app.route('/form1',methods=['POST','GET'])
def form1():
      if request.method == 'POST':
            try:
                  nm = request.form['name']
                  p = request.form['physics']
                  c = request.form['chemistry']
                  con = sql.connect("data3.db")
                  cur = con.cursor()
                  cur.execute("INSERT INTO student(name,physics,chemistry) VALUES (?,?,?)",(nm,p,c))
                  con.commit()
                  msg="record success"
            except:
                  con.rollback()
                  msg="error"
            finally:
                  return render_template('result1.html',msg=msg)
      return render_template('form1.html')
@app.route('/list')
def list():
      con = sql.connect("data3.db")
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("select * from student")
      row = cur.fetchall()
      return render_template('list.html',rows=row)

              

if __name__ =='__main__':
        app.run()