from flask import request, make_response, redirect, render_template, session, url_for, flash
from app.form import LoginForm
import unittest
from app import create_app
app = create_app()
items = ["item 1", "item 2", "item 3"]

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found_page(error):
    return render_template('404.html', error=error)

@app.route("/index")
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect("/show_information_address"))
    session['user_ip_information'] = user_ip_information
    
    return response

@app.route("/show_information_address")
def show_information():
    user_ip = session.get("user_ip_information")
    username = session.get("username")
    context = {
        "user_ip":user_ip, 
        "items": items,
        "username":username, 
        }
    return render_template("ip_information.html", **context)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True )

