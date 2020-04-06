from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.exc

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/corona'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://NishantTheProgra:mypassword@NishantTheProgrammer.mysql.pythonanywhere-services.com/NishantTheProgra$Corona'
db = SQLAlchemy(app)

class User(db.Model):
    phone = db.Column(db.String(20), primary_key=True)

@app.route("/", methods = ['GET', 'POST'])
def index():

    if(request.method == 'POST'):
        """
            Add Entry to database
        """
        try:
            phone = request.form.get('phone')
            entry = User(phone = phone)
            db.session.add(entry)
            db.session.commit()
        except(Exception):
            db.session.rollback()


    return render_template('index.html')


@app.route("/countries")
def countries():
    from Data import get
    return render_template('countries.html', countries = get())
    # return render_template('countries.html', countries = [])


app.run(debug=True)