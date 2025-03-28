from config import db
from routes.RoutesProfesor import app_profesor
app = db.app

app.register_blueprint(app_profesor)

if __name__ == "__main__":
    app.run(port=3000, debug=True)


# @app.route('/')
# def Index():
#     return render_template("/index.html")

# @app.route('/profesor')
# def get_profesor():
    
#     prof = Profesor(mysql)
#     profesors = prof.get_profesor() 
    
#     return render_template("/Profesor.html", profesor = profesors)

# @app.route('/create_profesor', methods=['POST'])
# def create_profesor():
#     if request.method == 'POST':
#         document = request.form['document'] 
#         name = request.form['name'] 
#         lastname = request.form['lastname'] 
#         second_lastname = request.form['second_lastname'] 
#         city = request.form['city'] 
#         address = request.form['address'] 
#         phone = request.form['phone'] 
#         origin_date = request.form['origin_date'] 
#         sex = request.form['sex'] 
#         state_id = request.form['state_id']

#         data = {
#             "document" : document, 
#             "name" : name, 
#             "lastname" : lastname, 
#             "second_lastname" : second_lastname, 
#             "city" : city, 
#             "address" : address, 
#             "phone" : phone, 
#             "origin_date" : origin_date, 
#             "sex" : sex, 
#             "state_id" : state_id
#         }
#         prof = Profesor(mysql)
#         insert_profesor = prof.create_profesor(data)
    
#         if insert_profesor:
#             flash("Registrado")
#         else:
#             flash("Error")

#         return redirect(url_for("get_profesor"))

# @app.route('/delete_profesor/<string:id>')
# def delete_profesor(id):
    
#     prof = Profesor(mysql)
#     delete_profesor = prof.delete_profesor(id)
    
#     if delete_profesor:
#         flash("Registrado")
#     else:
#         flash("Error")
    
#     return redirect(url_for("get_profesor"))

# @app.route('/edit_profesor/<id>', methods=['POST'])
# def edit_profesor(id):
#     if request.method == 'POST':
#         id = request.form['id'] 
#         document = request.form['document'] 
#         name = request.form['name'] 
#         lastname = request.form['lastname'] 
#         second_lastname = request.form['second_lastname'] 
#         city = request.form['city'] 
#         address = request.form['address'] 
#         phone = request.form['phone'] 
#         origin_date = request.form['origin_date'] 
#         sex = request.form['sex'] 
#         state_id = request.form['state_id']

#         data = {
#             "id" : id,
#             "document" : document, 
#             "name" : name, 
#             "lastname" : lastname, 
#             "second_lastname" : second_lastname, 
#             "city" : city, 
#             "address" : address, 
#             "phone" : phone, 
#             "origin_date" : origin_date, 
#             "sex" : sex, 
#             "state_id" : state_id
#         }
#         prof = Profesor(mysql)
#         edit = prof.edit_profesor(data)
    
#         if edit:
#             flash("Registrado")
#         else:
#             flash("Error")

#         return redirect(url_for("get_profesor"))


# @app.route("/data_edit/<id>")
# def data_edit(id):
#     prof = Profesor(mysql)
#     edit = prof.get_profesor(id)
#     return render_template("/edit_profesor.html", data_edit = edit)


