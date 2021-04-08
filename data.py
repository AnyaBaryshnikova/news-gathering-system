import requests
from requests.structures import CaseInsensitiveDict
import pymysql
import pymysql.cursors


def writeEventsToDB():
    #events = getData('https://api.timepad.ru/v1/events?limit=100&sort=%2Bid&access_statuses=public&moderation_statuses=featured%2Cshown%2Cnot_moderated&starts_at_min=01.01.2021')
    connection = getConnection()
    cursor = connection.cursor()
    sql = "Insert ignore into events (id, name, categoryid) " + " values (%s, %s, %s) "

    events = getData('https://api.timepad.ru/v1/events?limit=10&skip=10&sort=%2Bid&access_statuses=public&moderation_statuses=featured%2Cshown%2Cnot_moderated')
    total = events['total']
    try:

        for i in range(total // 100 + 1):
            string = 'https://api.timepad.ru/v1/events?limit=100&skip='+ str(i * 100) + '&sort=%2Bid&access_statuses=public&moderation_statuses=featured%2Cshown%2Cnot_moderated'
            events = getData(string)

            for event in events['values']:
                id = event['id']
                name = event['name']
                categoryId = 0
                if len(event['categories']) > 0:
                    categoryId = event['categories'][0]['id']
                cursor.execute(sql, (id, name, categoryId))
            connection.commit()
    finally:
        connection.close()


def writeCategoriesToDB():
    categories = getData('https://api.timepad.ru/v1/dictionary/event_categories.json')
    connection = getConnection()

    try:
        cursor = connection.cursor()

        sql = "Insert into categories (id, name) " + " values (%s, %s) "
        for category in categories['values']:
            id = category['id']
            name = category['name']
            cursor.execute(sql, (id, name))
        connection.commit()
    finally:
        connection.close()


def getData(url):
    headers = CaseInsensitiveDict()
    headers['Authorization'] = 'Bearer 70f2fdf1f1cba3c000e7df087d2484592f277070'

    response = requests.get(url, headers=headers)
    data = response.json()

    return data


def getConnection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='news',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
