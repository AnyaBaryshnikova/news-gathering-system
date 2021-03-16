import math

def makeRecommendation (userID, userRates):

    simUsers = [(u, cosDistance(userRates[userID], userRates[u])) for u in userRates if u != userID]
    #sortedSimilarities = simUsers.sort(reverse = True)

    userSimilarity = dict()
    sim_all = sum([x[1] for x in simUsers])
    sortedSimilarities = dict([x for x in simUsers if x[1] > 0.0])
    for relatedUser in sortedSimilarities:
        for event in userRates[relatedUser]:
            if not event in userRates[userID]:
                if not event in userSimilarity:
                    userSimilarity[event] = 0.0
                userSimilarity[event] += userRates[relatedUser][event] * sortedSimilarities[relatedUser]
    for event in userSimilarity:
        userSimilarity[event] /= sim_all




def cosDistance (vectorA, vectorB):

    return scalarProduct(vectorA, vectorB) / (math.sqrt(scalarProduct(vectorA, vectorA)) * math.sqrt(scalarProduct(vectorB, vectorB)))

def scalarProduct(vectorA, vectorB):
    res = 0.0
    for temp in vectorA:
        if temp in vectorB:
            res+= vectorA[temp] * vectorB[temp]
    return res