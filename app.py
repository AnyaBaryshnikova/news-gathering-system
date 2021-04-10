import flask
from flask import Flask, render_template, jsonify
import data
from flask_restful import reqparse, abort, Api, Resource
import json
from datetime import datetime

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app)

@app.route('/')
def index():
    connection = data.getConnection()
    try:
        cursor = connection.cursor()
        sql = "SELECT name FROM categories"
        cursor.execute(sql)
        categories = cursor.fetchall()
    finally:
        connection.close()
    return render_template("index.html", categories = categories)


class Categories(Resource):
    def get(self, category):
        category = category.replace('%20', ' ')
        connection = data.getConnection()
        now = datetime.now()
        now = now.strftime("%Y-%m-%d")
        try:
            cursor = connection.cursor()
            idsql = "SELECT id FROM categories WHERE name='" + category + "'"
            cursor.execute(idsql)
            id = cursor.fetchall()
            id = id[0]['id']
            sql = "SELECT name FROM events WHERE categoryid = " + str(id) + " AND startsat >= " + str(now)
            cursor.execute(sql)
            categoryEvents = cursor.fetchall()
        finally:
            connection.close()
        listedevents = []
        for event in categoryEvents:
             listedevents.append(event['name'])


        listedevents = flask.jsonify(listedevents)
        return listedevents

class CategoriesWithDates(Resource):
    def get(self, category, date):
        category = category.replace('%20', ' ')
        connection = data.getConnection()
        try:
            cursor = connection.cursor()
            idsql = "SELECT id FROM categories WHERE name='" + category + "'"
            cursor.execute(idsql)
            id = cursor.fetchall()
            id = id[0]['id']
            sql = "SELECT name FROM events WHERE categoryid = " + str(id) + " AND startsat >= " + str(date)
            cursor.execute(sql)
            categoryEvents = cursor.fetchall()
        finally:
            connection.close()
        listedevents = []
        for event in categoryEvents:
            listedevents.append(event['name'])

        listedevents = flask.jsonify(listedevents)
        return listedevents


class Events(Resource):
    def get(self):
        connection = data.getConnection()
        now = datetime.now()
        now = now.strftime("%Y-%m-%d")
        try:
            cursor = connection.cursor()
            sql = "SELECT name FROM events WHERE startsat >= " + str(now)
            cursor.execute(sql)
            categoryEvents = cursor.fetchall()
        finally:
            connection.close()
        listedevents = []
        for event in categoryEvents:
            listedevents.append(event['name'])

        listedevents = flask.jsonify(listedevents)
        return listedevents


class EventsWithDates(Resource):
    def get(self, date):
        connection = data.getConnection()
        try:
            cursor = connection.cursor()
            sql = "SELECT name FROM events WHERE startsat >= " + str(date)
            cursor.execute(sql)
            categoryEvents = cursor.fetchall()
        finally:
            connection.close()
        listedevents = []
        for event in categoryEvents:
            listedevents.append(event['name'])

        listedevents = flask.jsonify(listedevents)
        return listedevents


api.add_resource(Categories, '/cats/<category>')
api.add_resource(CategoriesWithDates, '/cats/<category>/<date>')
api.add_resource(Events, '/events')
api.add_resource(EventsWithDates, '/events/<date>')
if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run(debug = True)



