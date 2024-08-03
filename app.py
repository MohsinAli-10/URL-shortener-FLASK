from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# the app is not much unless it displays some information on the webpage
# To do that, we need to create a route
# a route tells the app what to serve when a particular address is visited
@app.route('/') # '/' is for the base URL
def home():
    return render_template('home.html') # function to return the template
# This templating functionality is derived from jinja (template engine)

@app.route('/your_url', methods=['GET', 'POST']) 
def your_url():
    if request.method == 'POST':
        urls = {} # empty dictionary
        urls[request.form['code']] = {'url': request.form['url']} # key value pair of code and url passed through the POST request
        with open('urls.json', 'w') as url_file: #only proceed if the json file can be opened
            json.dump(urls, url_file) # dump the key-value pair into the json file
        return render_template('your_url.html', code=request.form['code'])
        # when working with post requests we use request.form instead of request.args 
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

# we pass the url path to the route function
# the function name doesn't have to match the name of the route
# in a GET request, all the information passed gets displayed in the URL
# a POST request does not display the passed information explicitly in the URL
# the form tag in an html defaults to GET, but the method can be set to POST
# by default, FLASK resticts the routes to the GET method only. 
# For other methods we have to specify them in the route argument methods = 'sa;dn;aklsd'