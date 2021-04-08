from flask import Flask, render_template, jsonify
import data
from flask_restful import reqparse, abort, Api, Resource
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app)

# @app.route('/', methods=['POST', 'GET'])
# def index():
#     connection = data.getConnection()
#     try:
#         cursor = connection.cursor()
#         sql = "SELECT name FROM events"
#         cursor.execute(sql)
#         events = cursor.fetchall()
#     finally:
#         connection.close()
#     return render_template("index.html", events = events)
#
# @app.route('/getrecomendations')        #передача параметров как для timepad
# def recomendations():
#     return render_template("recomendations.html")


class Categories(Resource):
    def get(self, category):
        connection = data.getConnection()
        try:
            cursor = connection.cursor()
            idsql = "SELECT id FROM categories WHERE name='" + category + "'"
            cursor.execute(idsql)
            id = cursor.fetchall()
            id = id[0]['id']
            sql = "SELECT name FROM events WHERE categoryid = " + str(id)

            cursor.execute(sql)
            categoryEvents = cursor.fetchall()
        finally:
            connection.close()
        # categoryEvents = json.dumps(categoryEvents, ensure_ascii=False).encode('utf8')
        return categoryEvents

api.add_resource(Categories, '/cats/<category>')
if __name__ == "__main__":
    app.run(debug = True)



