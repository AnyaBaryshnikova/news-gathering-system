from datetime import datetime, timedelta
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import data
import pandas as pd


def recomends():
    events = createDataSet()
    ds = pd.DataFrame(events)

    tf = TfidfVectorizer(encoding= 'utf8', strip_accents= 'unicode', analyzer='word', ngram_range=(1, 3), min_df=0)
    tfidf_matrix = tf.fit_transform(ds['name'])

    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    results = {}

    for idx, row in ds.iterrows():
        similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
        similar_items = [(cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices]

        results[row['id']] = similar_items[1:]
    return results

def returnRecommendations(itemID):
    results = recomends()
    recs = results[itemID][:3]


def createDataSet():
    connection = data.getConnection()
    now = datetime.now()
    last = now + timedelta(weeks = 2)
    now = now.strftime("%Y-%m-%d")
    last = last.strftime("%Y-%m-%d")

    try:
        cursor = connection.cursor()
        sql = "SELECT id, name FROM events WHERE DATE(startsat) BETWEEN '" + str(now) + "' AND '" + str(last) +"'"
        cursor.execute(sql)
        events = cursor.fetchall()
    finally:
        connection.close()
    return events


def createRandEvents():
    connection = data.getConnection()
    now = datetime.now()
    last = now + timedelta(weeks=2)
    now = now.strftime("%Y-%m-%d")
    last = last.strftime("%Y-%m-%d")

    try:
        cursor = connection.cursor()
        sql = "SELECT id, name FROM events WHERE DATE(startsat) BETWEEN '" + str(now) + "' AND '" + str(last) + "' ORDER BY RAND() LIMIT 30"
        cursor.execute(sql)
        randEvents = cursor.fetchall()
    finally:
        connection.close()
    return randEvents