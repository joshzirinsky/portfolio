from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)



@app.route('/')
def my_home():
	return render_template('index.html')


@app.route('/<string:variable>')
def f(variable):
	return render_template(variable)



# def write_to_file(data):
# 	with open('database.txt', mode="a") as database:
# 		email = data["email"]
# 		subject = data["subject"]
# 		message = data["message"]
# 		file = database.write(f"\n{email}, {subject}, {message}")


def write_to_file(data):
 	with open('database.csv', mode="a", newline='') as database:
 		databasewriter = csv.writer(database)
 		email = data["email"]
 		subject = data["subject"]
 		message = data["message"]
 		databasewriter.writerow([email, subject, message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
    	data = request.form.to_dict()
    	write_to_file(data)
    	return redirect("/thank_you.html")
    else:
    	return "something went wrong. Try again."



# @app.route('/index.html')
# def index():
# 	return render_template('index.html')
	

# @app.route('/works.html')
# def works():
# 	return render_template('works.html')


# @app.route('/about.html')
# def about():
# 	return render_template('about.html')


# @app.route('/contact.html')
# def contact():
# 	return render_template('contact.html')
