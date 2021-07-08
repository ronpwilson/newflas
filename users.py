from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:iamronzappan@localhost:5432/injuries'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Allinjuries(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    playername = db.Column(db.String(100))
    injury = db.Column(db.String(2000))


@app.route('/')
def index():
    result = Allinjuries.query.all()
    return render_template('index.html',result=result)

@app.route('/process',methods =['POST'])
def process():
    playername = request.form['playername']
    injury = request.form['injury']
    injurydata = Allinjuries(playername=playername,injury=injury)
    db.session.add(injurydata)
    db.session.commit()
    
    return redirect(url_for('index'))
