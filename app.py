from flask import Flask

app = Flask(__name__)

# the app is not much unless it displays some information on the webpage
# To do that, we need to create a route
# a route tells the app what to serve when a particular address is visited
@app.route('/') # '/' is for the base URL
def index():
    return 'Hello FLASK!'

@app.route('/about') # 'about' is for the URL/about
def about(): # the function name doesn't have to match the name of the route
    return 'this is a URL shortener'

@app.route('/home')
def home(): 
    return 'this is a URL shortener home page'

@app.route('/contact')
def contact():
    return 'this is a URL shortener contact page'

@app.route('/sign')
def sign():
    return 'this is a URL shortener sign up page'

if __name__ == '__main__':
    app.run(debug=True)

    