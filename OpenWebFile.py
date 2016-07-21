# default host: localhost
# default port = 5000

import Person
import PersonToDatabase
import mysql.connector as mc


# Allows webpage to be read
from flask import * #Flask, render_template

# for connecting to database
con = PersonToDatabase.getConnection("root", "password", "localhost", "myFirstDB")


app = Flask (__name__)

# localhost:5000/home in URL will run show_page()
@app.route("/home")
def show_page():
	allPer = PersonToDatabase.selectAllPersons(con)
	return render_template("SampleWebpage.html", all_persons = allPer)

# @app.route("/home/signup")
# def show_register():
# 	return render.template("")


@app.route("/home/register", methods=['POST'])
def register():
	first_name = request.form["FirstName"]
	last_name = request.form["LastName"]

	person1 = Person.Person(first_name, last_name)
	successAddPerson = PersonToDatabase.addPerson(person1, con)
	
	if successAddPerson:
		# call show_page when success add user info
		return redirect(url_for('show_page'))
	else:
		print("ERROR. Person not added.")

# runs flask; allows python-html connection
if __name__ == '__main__':
	app.run(debug = True)

