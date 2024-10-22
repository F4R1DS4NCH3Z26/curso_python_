from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'CLAVE SEGURA'
items = ["item 1", "item 2", "item 3"]

class LoginForm(FlaskForm):
    username = StringField("Nombre de usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Iniciar Sesión", validators=[DataRequired()])

@app.errorhandler(404)
def not_found_page(error):
    return render_template('404.html', error=error)

@app.route("/index")
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect("/show_information_address"))
    session['user_ip_information'] = user_ip_information
    
    return response

@app.route("/show_information_address", methods=['GET', 'POST'])
def show_information():
    user_ip = session.get("user_ip_information")
    login_form = LoginForm()
    context = {
        "user_ip":user_ip, 
        "items": items,
        "login_form":login_form, 
        }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username
        return make_response(redirect("/index"))
    return render_template("ip_information.html", **context)

app.run(host="0.0.0.0", port=3000, debug=True )

