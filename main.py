import recomendations
import data



if __name__ == '__main__':
    #recomendations.makeRecommendation('Ivan', data.ReadFile('data/ratings.csv'))
    event = data.getEventsFromServer()
    event = data.getorders()



