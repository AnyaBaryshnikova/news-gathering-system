import csv

def ReadFile(filename):
    file = open (filename)
    data = csv.reader (file)
    mentions = dict()
    for line in data:
        user = line[0]
        event = line[1]
        rating = float(line[2])
        if not user in mentions:
            mentions[user] = dict()
        mentions[user][event] = rating
    file.close()
    return mentions


