from flask import Flask, render_template
import data
import pymysql
import pymysql.cursors

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    connection = data.getConnection()

    try:
        cursor = connection.cursor()
        sql = "SELECT name FROM events "
        cursor.execute(sql)
        events = cursor.fetchall()
    finally:
        connection.close()
    return render_template("index.html", events = events)

@app.route('/getrecomendations')        #передача параметров как для timepad
def recomendations():
    return render_template("recomendations.html")


if __name__ == "__main__":
    app.run(debug = True)



