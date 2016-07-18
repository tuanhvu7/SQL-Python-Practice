# default host: localhost
# default port = 5000


# Allows webpage to be read
from flask import * #Flask, render_template

app = Flask (__name__)

# localhost:5000/home in URL will run show_page()
@app.route("/home")
def show_page():
	return render_template("SampleWebpage.html")
if __name__ == '__main__':
	app.run(debug = True)





