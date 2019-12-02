# based on example taken from Miguel Grinberg introduction to Flask

from flask import Flask
from config import Config

# in this case "app" is a variable
app = Flask(__name__)
app.config.from_object(Config)

# here "app" refers to the directory 
# put this here to avoid circular imports
# i.e. because routes requires the use of "app" the variable 
from app import routes 