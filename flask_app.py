import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# api_key = 'c36156a3b014b5e2b6e0655ec8154691'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mypassword@localhost/sit331'
# Host=localhost;Username=postgres;Password=mypassword;Database=sit331
db = SQLAlchemy(app)


migrate = Migrate(app, db)

class weather_table(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), primary_key=True)
    temp = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)  # renamed from 'desc' to 'description'
    
@app.route('/', methods=['GET','POST'])
def index():
    weather_data = {}
    city = 'Chandigarh',
    city = 'Delhi'
    if request.method == 'POST':
        city = request.form['city']
    try:
        weathers = weather_table.query.filter_by(city=city).first()
        if weathers:
            weather_data['temp'] = weathers.temp
            weather_data['description'] = weathers.description
        else:
            return render_template('index.html', weather_data=weather_data, error="No weather data found for the city: {}".format(city))
    except Exception as e:
        return render_template('index.html', weather_data=weather_data, error="Error fetching weather data: {}".format(e))
      
    return render_template('index.html', weather_data=weather_data, error=None)



if __name__ == '__main__':
    with app.app_context():
     db.create_all()
    app.run(debug=True)