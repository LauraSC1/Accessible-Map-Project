from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Set up the connection string for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:YourStrong!Passw0rd@localhost:1433/AccessibleMapDB?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Define the database model (table structure)
class AccessibleLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<AccessibleLocation {self.name}>"

# Route to render the index.html page (map page)
@app.route('/')
def home():
    # You can fetch data from the database here if needed
    locations = AccessibleLocation.query.all()  # Example of fetching all locations
    return render_template('index.html', locations=locations)  # Pass data to the template

# Route to add a new location to the database
@app.route('/add_location')
def add_location():
    # Example: Add a sample location to the database
    new_location = AccessibleLocation(name="Kennesaw State University", description="A university with accessible facilities")
    db.session.add(new_location)
    db.session.commit()
    return f"Added location: {new_location.name}"

if __name__ == "__main__":
    app.run(debug=True)
