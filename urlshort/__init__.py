from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'jkdshfjkasdfhsadkmad;lsam' #allows information to be securely passed to the html

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app