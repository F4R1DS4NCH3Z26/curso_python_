from . import auth
from app.form import LoginForm

@auth.route('/login')

def login():
    context = {
        "login_form" : LoginForm()
    }
    return ""