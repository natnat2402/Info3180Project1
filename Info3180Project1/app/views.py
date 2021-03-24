"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, flash, Flask, send_from_directory, send_file
from app.forms import CreatePropertyForm
from app import db
from app.models import PropertyInformation
from werkzeug.utils import secure_filename
import psycopg2
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Properties in Jamaica")


#define fuction for connecting to database
def connect_db():
    return psycopg2.connect(host="localhost",database="project1", user="project1", password="project1")

@app.route('/Property/', methods=['GET','POST'])
def Property():
    form = CreatePropertyForm()
    if request.method == 'POST' and form.validate():
        #grab filename from form to be saved in database
        uploaded_file = request.files['photo'] 
        filename = secure_filename(uploaded_file.filename)
        #save copy of image
        uploaded_file.save(os.path.join( app.config['UPLOAD_FOLDER'], filename))
        #connect to database and insert new information
        db = connect_db()
        cur = db.cursor()
        cur.execute('insert into "Property_Information" ("Title","Number_of_Bedrooms","Number_of_Bathrooms","Location","Price","Property_type","Description","Photo")values(%s,%s,%s,%s,%s,%s,%s,%s)',(request.form['propertyname'], request.form['numroom'],request.form['numbathroom'],request.form['address'],request.form['price'],request.form['proptype'],request.form['descrip'],filename))

        db.commit()
        flash('Property Successfully Added')
        #database migration
        os.system('python manage.py db migrate')
        os.system('python manage.py db upgrade')
        return redirect(url_for('properties'))
    return render_template('property.html',form=form)


#Helper funtion to return image from local folder
#Images fail to render
@app.route('/uploads/<filename>')
def get_images(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.route('/Property/<Property_id>', methods=['GET','POST'])
def propertyview(Property_id):
    db = connect_db()
    cur = db.cursor()
    if request.method=="GET":
        #unable to retrieve value from form the below keeps displaying none
        Property_id = request.form.get("Property_id")
        Property_id2 = request.args.get("Property_id")
        Property_id3 = request.values.get("Property_id")

        print("TEESSSTING!!!", Property_id, Property_id2,Property_id3)

        cur.execute('select * from "Property_Information" where "Property_id"="Property_id"')
        propinfo = cur.fetchall()
        db.commit()
        cur.execute('select "Photo" from "Property_Information" where "Property_id"="Property_id"')
        image = cur.fetchone()
    
        return render_template('propertyview.html', propinfo=propinfo, image=image)
    flash('Error accsessing page')
    return render_template('home.html')

@app.route('/properties/')
def properties():
    db = connect_db()
    cur = db.cursor()
    cur.execute('select * from "Property_Information"')
    propertyinfo = cur.fetchall()
    db.commit()
    #get list oof image names from uploads folder
    imagenames = os.listdir(app.config['UPLOAD_FOLDER'])
    print(imagenames)
    
    return render_template('properties.html', propertyinfo=propertyinfo, imagenames=imagenames)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
