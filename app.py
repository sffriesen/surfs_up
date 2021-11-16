# Import the Flask dependency
from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Routes
# Define the root/starting point
@app.route('/')
# Create a function called hello_world
def hello_world():
    return "Hello world"
