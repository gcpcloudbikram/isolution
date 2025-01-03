# Import Flask framework
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello():
    # Return a welcome message
    return "Hello, Welcome to iSolution_v02"

# Run the application if this script is executed directly
if __name__ == '__main__':
    # Start the Flask app on all available network interfaces at port 5000
    app.run(host='0.0.0.0', port=5000)
