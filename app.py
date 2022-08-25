import logging

from flask import Flask, send_from_directory
from loader.loader_views import loader_blueprint
from main.main_views import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)
logging.basicConfig(level=logging.INFO)
# filename='basic.log',

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
