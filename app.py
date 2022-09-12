import os
from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_required, current_user, login_user, logout_user
from flask_bcrypt import Bcrypt
import sqlite3
import config


app = Flask(__name__ ,template_folder='templates')
app.secret_key = 'super secret string' 
db = SQLAlchemy(app)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = config.database_url
app.config['UPLOAD_FOLDER'] = config.upload_folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username



######test db
# db.session.execute("INSERT INTO users(id,name,email,password,role) VALUES('5','ed','ert','123456','ewsd';")




@login_manager.user_loader
def load_user(email):
    user = User()
    user.id = email
    return user


#index
@app.route("/")
def index():
    return render_template('index.html')

# @app.route("/me")
# def me():
#     return render_template('me.html')

@app.route('/resume')
def resume():
    return redirect("https://resume.io/r/jav1DVI6t")


@app.route('/github')
def github():
    return redirect("https://github.com/FatemeZamanian")


@app.route('/insta')
def insta():
    return redirect("https://instagram.com/python.with.fateme?igshid=YmMyMTA2M2Y=")

@app.route('/linkedin')
def linkedin():
    return redirect("https://www.linkedin.com/in/fatemezamanian")

@app.route('/youtube')
def youtube():
    return redirect("https://youtube.com/channel/UCfI5V_TExc9ntvGSdUNjJ4Q")


@app.route('/admin/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('admin/login.html')
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = db.session.execute(f"SELECT * FROM users WHERE email='{email}'").fetchone()
        if result is not None and bcrypt.check_password_hash(result["password"], password):
            user = User()
            user.id = email
            login_user(user)
            return redirect("/admin/dashboard")
        else:
            return redirect("/admin/login")

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/blog')
@login_required
def admin_blog():
    posts = db.session.execute(f"SELECT * FROM posts ORDER BY create_time DESC")
    return render_template('admin/blog.html', posts=posts)

@app.route('/admin/blog/add', methods=['POST', 'GET'])
@login_required
def admin_blog_add():
    if request.method == 'GET':
        return render_template('admin/add_post.html')
    
    if request.method == 'POST':
        if 'image' not in request.files or not request.files['image']:
            image_path = ""
        else:
            image_file = request.files['image']
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], "images/posts/", image_file.filename)
            image_file.save(image_path)
        
        title = request.form['title']
        body = request.form['body']
        body = body.replace("'","''")
        db.session.execute(f"INSERT INTO posts(title, body, image,category_id,create_time) VALUES('{title}', '{body}', '{image_path}','{2}','{datetime.now()}')")
        db.session.commit()
        return redirect("/admin/blog")

