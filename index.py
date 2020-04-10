from flask import Flask, render_template, url_for, request, session, redirect, send_file
import mysql.connector
import datetime
from io import BytesIO
import os
x = datetime.datetime.now()
UPLOAD_FOLDER = '/home/ayman/dev/mr/static/files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.secret_key = b'_5#y2L"F4Q8z@##HG]/'


mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "AYfaof26..@",
	database = "moulay_rachid",
)
crsr = mydb.cursor()

@app.route('/')
def home():
    if 'user_name' in  session:
        session['user_name'] = session['user_name']
        session['user_name'] = session['user_name']
        session['field'] = request.form.getlist("field[]")
        session['statue'] = session['statue']
        return render_template('index.htm', uname=session['user_name'])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        crsr.execute("SELECT * FROM users WHERE email =  '%s'" %request.form['email'])
        user = crsr.fetchall()
        if user:
            user = user[0]
            valid = valid_log(user[2], request.form['pwd'])
            if valid:
                session['user_name'] = user[0]
                session['statue'] = user[3]
                session['field'] = user[4]
                return redirect(url_for('home'))
            else:
                error = "Mot de pass incorrect"
                return render_template('login.htm', error= error)
        else:
            error = "utilisateur introuvable"
            return render_template('login.htm', error= error)

    else:
        return render_template('login.htm', error= error)

@app.route('/logout')
def logout():
   session.clear()
   return redirect(url_for('login'))

def valid_log(pwd, pwd1):
    if pwd==pwd1 :
        return True
    else:
        return  False

@app.route('/singup', methods=['GET', 'POST'])
def singup():
    if request.method =='POST':
        error = None
        crsr.execute("SELECT * FROM users WHERE email =  '%s'" %request.form['email'])
        user = crsr.fetchall()
        if user:
            error = "l'utilisateur existe deja"
            return render_template('login.htm', error=error)
        else:
            cmd = "INSERT INTO users (name, email, password, statue, field) VALUES (%s, %s, %s, %s, %s)"
            nuser = (request.form['user_name'], request.form['email'], request.form['password'], request.form['statue'], request.form['field'])
            crsr.execute(cmd, nuser)
            mydb.commit()
            session['user_name'] = request.form['user_name']
            session['statue'] = request.form['statue']
            session['field'] = request.form['field']
            return redirect(url_for('home'))

    else:    
        return render_template('login.htm')

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    if request.method == 'POST':
        subject = request.form["subject"]
        crsr.execute("SELECT * FROM posts WHERE subject =  '%s'" %subject )
        courses = crsr.fetchall()
        
        return render_template('courses.htm', courses = courses)
    return render_template('courses.htm')

@app.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == 'POST':

        file = request.files['upFile']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        dir = app.config['UPLOAD_FOLDER']+ file.filename

        cmd  = "INSERT INTO posts (title, author, file, date, subject, field ) VALUES (%s, %s, %s, %s, %s, %s)"
        post = (request.form["title"], session["user_name"], str(dir), x, str(request.form["subject"]), str(request.form.getlist("field[]")))
        crsr.execute(cmd, post)
        mydb.commit()

        return redirect(url_for('upload'))
    else:
        return render_template('upload.htm')

if __name__ == '__main__':
    app.run(debug=True)    