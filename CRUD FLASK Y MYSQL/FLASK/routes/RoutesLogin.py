from flask import render_template, request, flash, redirect, url_for
from config import db
from flask import Blueprint
from models.entities.User import User
from classes.User import User as ModelUser
from flask_login import LoginManager, login_user, logout_user, login_required


app = db.app
mysql = db.mysql
app_login = Blueprint('routes_login',__name__)


login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app_login.route('/')
def index():
    return redirect(url_for('routes_login.login'))

@app_login.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form["username"], request.form["password"])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('routes_login.home'))
            else:
                flash("Contraseña invalida")
                return render_template('index.html')    
        else:
            flash("El usuario no existe")
            return render_template('index.html')
    else:
        return render_template('index.html')

@app_login.route('/home')
def home():
    return render_template('home.html')

@app_login.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('routes_login.index'))

@app_login.route('/protected')
@login_required
def protected():
    return "Holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa "

def status_401(error):
    return redirect(url_for('routes_login.index'))

def status_404(error):
    return "<h1> Pagina no  encontrada </h1>"

