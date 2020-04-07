from flask import Flask, request, render_template, redirect
from twilio.twiml.messaging_response import MessagingResponse
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.exc

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/corona'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://NishantTheProgra:mypassword@NishantTheProgrammer.mysql.pythonanywhere-services.com/NishantTheProgra$Corona'
db = SQLAlchemy(app)

class User(db.Model):
    phone = db.Column(db.String(20), primary_key=True)

class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20))
    country = db.Column(db.Integer)



@app.route("/", methods = ['GET', 'POST'])
def index():



    return render_template('index.html')


@app.route("/countries", methods = ['GET', 'POST'])
def countries():
    if(request.method == 'POST'):
        try:
            try:
                phone = request.form.get('phone')
                entry = User(phone = phone)
                db.session.add(entry)
                db.session.commit()
            except(Exception):
                db.session.rollback()


            selected = Countries.query.filter_by(phone = phone).all()
            from Data import get
            return render_template('countries.html', countries = get(), phone = phone, selected = selected)
            # return render_template('countries.html', countries = [])
        except(Exception):
            return '<h1>Server in heavy load'

    else:
        return redirect("/", code=302)

@app.route("/thanks", methods = ['GET', 'POST'])
def thanks():
    if(request.method == 'POST'):
        items = request.form.get('selected').split()
        phone = request.form.get('phone')
        try:
            delete = Countries.query.filter_by(phone = phone).all()
            for item in delete:
                db.session.delete(item)
                db.session.commit()
        except(Exception):
            pass
        
        for item in items:
            entry = Countries(phone = phone, country=item)
            db.session.add(entry)
            db.session.commit()
        
        return render_template('thanks.html')

    else:
        # return redirect("/", code=302)
        return render_template('thanks.html')

if __name__ == "__main__":
    app.run(debug=True)