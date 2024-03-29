from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import Scrape_mars


# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_data")
#conn="mongodb://localhost:27017"
# client=pymongo.MongoClient(conn)
# db= client.marsdb
# collection= db.collection

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mongo.db.marsdb.find_one()

    # Return template and data
    return render_template("index.html", data=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    marsdb=mongo.db.marsdb
    mars_data = Scrape_mars.init_browser()

    # Update the Mongo database using update and upsert=True
    marsdb.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
