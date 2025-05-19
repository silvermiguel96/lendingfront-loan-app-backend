from flask import Flask
from flasgger import Swagger
from interfaces.routes import bp
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

swagger = Swagger(app)

app.register_blueprint(bp, url_prefix='/api/v1')

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
