from flask import Flask, render_template, request, redirect, url_for, flash, abort
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'jkdshfjkasdfhsadkmad;lsam' #allows information to be securely passed to the html

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
        

        # -------------------------------------------------
        # Ensure that the urls json file exists, otherwise initialize it as an empty dictionary
        urls = {} # empty dictionary

        if os.path.exists('urls.json'):
            with open('urls.json') as url_file:
                try:
                    urls = json.load(url_file)
                except json.JSONDecodeError:
                    urls = {}  # Initialize as empty dictionary if the file is empty
        # ---------------------------------------------------

        if request.form['code'] in urls.keys():
            flash('This shortname is already in use. Please choose a different shortname.')
            return redirect(url_for('home'))
        
        if 'url' in request.form:
            urls[request.form['code']] = {'url': request.form['url']}
            with open('urls.json', 'w') as url_file:
                json.dump(urls, url_file)
            return render_template('your_url.html', code=request.form['code'], url=request.form['url'])

        elif 'file' in request.files:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save('C:/Users/Mohsin/Desktop/Github/URL-shortener-FLASK/static/user_files/' + full_name)
            urls[request.form['code']] = {'file': full_name}
            with open('urls.json', 'w') as url_file:
                json.dump(urls, url_file)
            return render_template('your_url.html', code=request.form['code'], url=full_name)

        else:
            flash('No URL or file provided.')
            return redirect(url_for('home'))
 
    else:
        return redirect(url_for('home'))
    
@app.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as url_file:
            try:
                urls = json.load(url_file)
                if code in urls.keys():
                    if 'url' in urls[code].keys():
                        return redirect(urls[code] ['url'])
                    else:
                        return redirect(url_for('static', filename='user_files/' + urls[code] ['file']))
                else:
                    return abort(404)
                    # flash('Shortname not found.')
                    # return redirect(url_for('home'))
            except json.JSONDecodeError:
                flash('Shortname list is empty. Please post an entry for the list.')
                return redirect(url_for('home'))
                # return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

# we pass the url path to the route function
# the function name doesn't have to match the name of the route
# in a GET request, all the information passed gets displayed in the URL
# a POST request does not display the passed information explicitly in the URL
# the form tag in an html defaults to GET, but the method can be set to POST
# by default, FLASK resticts the routes to the GET method only. 
# For other methods we have to specify them in the route argument methods = 'sa;dn;aklsd'