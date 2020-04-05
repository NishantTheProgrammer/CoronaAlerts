from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/corona'
db = SQLAlchemy(app)

class User(db.Model):
    phone = db.Column(db.String(20), primary_key=True)

@app.route("/", methods = ['GET', 'POST'])
def hello():

    if(request.method == 'POST'):
        """
            Add Entry to database
        """
        phone = request.form.get('phone')
        entry = User(phone = phone)
        db.session.add(entry)
        db.session.commit()


    return render_template('index.html')

app.run(debug=True)