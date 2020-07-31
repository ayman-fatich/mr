from flask import Flask, render_template, url_for, request, session, redirect, send_file, send_from_directory, safe_join, abort
import mysql.connector
import datetime
from io import BytesIO
from werkzeug.security import generate_password_hash, check_password_hash
import os

#take time
x = datetime.datetime.now()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/files'

#i know i should  from github it but who cares
app.secret_key = b'_5#y2L"F4Q8z@##HG]/'

#i should not publish that neither lol :)
mydb = mysql.connector.connect(user="bbcfca50b39d8b", password='04b37381', host="us-cdbr-east-06.cleardb.net",port="3306", database="heroku_b11ddfefff9990e")
crsr = mydb.cursor()

#well let's get some fun boys eyyy ! 😁

#the home page function
@app.route('/')
def home():
    if 'user_name' in session:
    
        return render_template('index.htm', uname=session['user_name'])
    
    else:
        return render_template('index.htm')



#well i will not tell you what function everytime is neither, you can read it yourself
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        #it takes user's email and check if he/she is in the db or not
        crsr.execute("SELECT * FROM users WHERE email =  '%s';" %
                     request.form['email'])
        user = crsr.fetchall()
        if user:
            user = user[0]
            valid = check_password_hash(user[2], request.form['pwd'])
            if valid:
                #we found it yeey
                session['user_name'] = user[0]
                session['statue'] = user[3]
                session['field'] = user[4]
                return redirect(url_for('home'))
            else:
                # :(
                error = "Mot de pass incorrect"
                return render_template('login.htm', error=error)
        else:
            error = "utilisateur introuvable"
            return render_template('login.htm', error=error)
    
    else:
        return render_template('login.htm', error=error)

#i'm tired from commenting it

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/singup', methods=['GET', 'POST'])
def singup():
    if request.method == 'POST':
        error = None
        crsr.execute("SELECT * FROM users WHERE email =  '%s';" %
                     request.form['email'])
        user = crsr.fetchall()
        if user:
            error = "l'utilisateur existe deja"
            return render_template('login.htm', error=error)
        else:
            cmd = "INSERT INTO `users` VALUES (name, email, password, statue, field) VALUES (%s, %s, %s, %s, %s);"
            password = generate_password_hash(request.form['password'])
            nuser = (request.form['user_name'], request.form['email'],password, request.form['statue'], request.form['field'])
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
        if 'statue' in session:
            subject = request.form["subject"]
            field = session['field']
            crsr.execute(
                "SELECT * FROM posts WHERE subject =  '{}' and field LIKE '%{}%'; ".format(subject, field))
            courses = crsr.fetchall()
        else:
            subject = request.form["subject"]
            field = request.form["field"]
            crsr.execute(
                "SELECT * FROM posts WHERE subject =  '{}' and field LIKE '%{}%'; ".format(subject, field))
            courses = crsr.fetchall()

        return render_template('courses.htm', courses=courses)
    return render_template('courses.htm')


@app.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == 'POST':

        file = request.files['upFile']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        dir = file.filename

        cmd = "INSERT INTO posts (title, author, file, date, subject, field ) VALUES (%s, %s, %s, %s, %s, %s);"
        post = (request.form["title"], session["user_name"], str(dir), x, str(
            request.form["subject"]), str(request.form.getlist("field[]")))
        crsr.execute(cmd, post)
        mydb.commit()

        return redirect(url_for('upload'))
    else:
        return render_template('upload.htm')


app.config["CLIENT_IMAGES"] = "/home/ayman/dev/mr/static/files"


@app.route('/download/<filename>')
def download(filename):
    try:
        return send_from_directory(app.config["CLIENT_IMAGES"], filename=filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(port="5000")
