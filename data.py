import csv
import requests
from requests.structures import CaseInsensitiveDict

TOKEN = '70f2fdf1f1cba3c000e7df087d2484592f277070'


# def ReadFile(filename):
#     file = open (filename)
#     data = csv.reader (file)
#     mentions = dict()
#     for line in data:
#         user = line[0]
#         event = line[1]
#         rating = float(line[2])
#         if not user in mentions:
#             mentions[user] = dict()
#         mentions[user][event] = rating
#     file.close()
#     return mentions

def getEventsFromServer():
    headers = CaseInsensitiveDict()
    url = 'https://api.timepad.ru/v1/events.json'
    headers['Authorization'] = 'Bearer 6c7332a6b69de35d08d4e7b17005a50e82eb0521'

    response = requests.get(url, headers=headers)
    events = response.json()

    return events


def getorders():
    headers = CaseInsensitiveDict()
    url = 'https://api.timepad.ru/v1/events/1589821/orders.json'
    headers['Authorization'] = 'Bearer 6c7332a6b69de35d08d4e7b17005a50e82eb0521'

    response = requests.get(url, headers=headers)
    orders = response.json()

    return orders

def getCategories():
    headers = CaseInsensitiveDict()
    url = 'https://api.timepad.ru/v1/dictionary/event_categories.json'
    headers['Authorization'] = 'Bearer 70f2fdf1f1cba3c000e7df087d2484592f277070'

    response = requests.get(url, headers=headers)
    categories = response.json()
    return categories


# def getCliens():
#     headers = CaseInsensitiveDict()
#     url = 'https://api.timepad.ru/introspect.json'
#     headers['Authorization'] = 'Bearer 70f2fdf1f1cba3c000e7df087d2484592f277070'
#
#     response = requests.get(url, headers=headers)
#     clients = response.json()
#     return clients


