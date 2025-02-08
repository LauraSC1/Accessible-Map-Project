# Import necessary libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
# Flask is a web framework used to build web applications in Python
app = Flask(__name__)

# Set up the connection string for SQLAlchemy
# The URI (Uniform Resource Identifier) defines how to connect to your database
# In this case, it's connecting to a Microsoft SQL Server using the pyodbc driver
# The format is: mssql+pyodbc://<username>:<password>@<server>/<database>?driver=<driver_name>
# Replace 'YourStrong!Passw0rd' with your actual password and 'AccessibleMapDB' with your database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:YourStrong!Passw0rd@localhost:1433/AccessibleMapDB?driver=ODBC+Driver+17+for+SQL+Server'

# This configuration option tells SQLAlchemy not to track modifications of objects (which saves memory)
# It's optional, but recommended for performance reasons
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
# SQLAlchemy is the ORM (Object Relational Mapper) that allows Python code to interact with the database
db = SQLAlchemy(app)

# Define the database model (table structure)
# Here we create a model called AccessibleLocation, which represents a table in the database
# It has three columns: id, name, and description
class AccessibleLocation(db.Model):
    # Define the 'id' column as an integer and set it as the primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Define the 'name' column, which holds a string value and cannot be empty (nullable=False)
    name = db.Column(db.String(100), nullable=False)
    
    # Define the 'description' column, which holds a string value and cannot be empty (nullable=False)
    description = db.Column(db.String(200), nullable=False)

    # This method returns a readable string representation of the object when printed
    def __repr__(self):
        return f"<AccessibleLocation {self.name}>"

# Define the routes (URLs) of the web application
@app.route('/')  # This is the home route, which means when you visit the root URL (e.g., http://localhost:5000/)
def home():
    # When the user visits the home route, the string 'Hello, World!' will be displayed
    return 'Hello, World!'

@app.route('/add_location')  # This is a route to add a new location to the database
def add_location():
    # Create a new AccessibleLocation object with sample data (name and description)
    new_location = AccessibleLocation(name="Park", description="A beautiful park with ramps")
    
    # Add the new location to the database session (but don't commit yet)
    db.session.add(new_location)
    
    # Commit the transaction to save the new location to the database
    db.session.commit()
    
    # Return a message indicating the new location was added
    return f"Added location: {new_location.name}"

# Check if the script is being run directly (rather than being imported as a module)
if __name__ == '__main__':
    # Run the Flask application in debug mode (which helps catch errors and automatically restarts the app)
    app.run(debug=True)
