from flask import Flask, render_template, redirect, url_for, request
import os
from status import main

app = Flask(__name__)

userData = {}

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/school')
def school():
	return render_template("school.html")

@app.route('/user-data-berkeley')
def userB():
	return render_template("userDataBerkeley.html")

@app.route('/user-data-davis')
def userD():
	return render_template("userDataDavis.html")

@app.route('/user-data-irvine')
def userI():
	return render_template("userDataIrvine.html")

@app.route('/user-data-losangeles')
def userLA():
	return render_template("userDataLosAngeles.html")

@app.route('/user-data-merced')
def userM():
	return render_template("userDataMerced.html")

@app.route('/user-data-riverside')
def userR():
	return render_template("userDataRiverside.html")

@app.route('/user-data-sandiego')
def userSD():
	return render_template("userDataSanDiego.html")

@app.route('/user-data-santabarbara')
def userSB():
	return render_template("userDataSantaBarbara.html")

@app.route('/user-data-santacruz')
def userSC():
	return render_template("userDataSantaCruz.html")

@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
	userData['url'] = "https://bcsweb.is.berkeley.edu/psc/bcsprd_pub/EMPLOYEE/HRMS/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL"
	userData['term'] = request.form['term']
	userData['career'] = request.form['car']
	userData['classNum'] = request.form['classNum']
	userData['mailTo'] = request.form['emailName']
	userData['textTo'] = request.form['phoneNumber']
	userData['service'] = request.form['service']
	return render_template("confirm.html")

@app.route('/done')
def run():
	main(userData['url'], userData['term'], userData['career'], userData['classNum'], userData['mailTo'], userData['textTo'], userData['service'])
	return render_template("done.html")


if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)
