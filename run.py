# If __init__ is in urlshort folder
# from urlshort.__init__ import create_app

from urlshort.__init__ import create_app
from flask import Flask

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)