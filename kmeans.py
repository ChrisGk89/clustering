import random
from Pearson import pearson


def kmeanscluster(rows, distance=pearson, k=5, max_iter=50):

    # Determine the minimum and maximum values for each point
    ranges = []
    for i in range(len(rows[0])):
            min_value = min([row[i] for row in rows])
            max_value = max([row[i] for row in rows])
            ranges_value = (int(min_value), int(max_value))
            ranges.append(ranges_value)


    newClusters= []
    for j in range(k):
        newClusters.append([random.random() * (ranges[i][1] - ranges[i][0]) + ranges[i][0] for i in range(len(rows[0]))])

    lastmatches = None
    iterations =  0
    bestmatches = [[] for i in range(k)]

    while not shouldStop(lastmatches, bestmatches, iterations, max_iter):

        #temporary assign last match value to best match
        lastmatches = bestmatches

        bestmatches = getBestMatch(rows, k, distance, newClusters)


        # Move the centroids to the average of their members
        for i in range(k):
            avgs = [0.0] * len(rows[0])
            if len(bestmatches[i]) > 0:
                for rowid in bestmatches[i]:
                    for m in range(len(rows[rowid])):
                        avgs[m] += rows[rowid][m]
                for j in range(len(avgs)):
                    avgs[j] /= len(bestmatches[i])
                newClusters[i] = avgs

        print 'Iteration %d' % iterations
        iterations += 1

    return bestmatches


# Function: Should Stop
# -------------
# Returns True or False if k-means is done. K-means terminates either
# because it has run a maximum number of iterations OR the centroids
# stop changing.

def shouldStop(oldCentroids, centroids, iterations, max_iter):
    if iterations > max_iter: return True

    # If the results are the same as last time, this is complete
    return oldCentroids == centroids


# Function: Best Matches
# -------------
#if newDistance is less than best match distance assign new best match

def getBestMatch(rows, k, distance, newClusters):
    bestmatches = [[] for i in range(k)]
    rowno = 0
    while rowno < len(rows):
        row = rows[rowno]
        bestmatch = 0
        for i in range(k):
            newDistance = distance(newClusters[i], row)

            #if newDistance is less than baest match distance assign new best match

            if newDistance < distance(newClusters[bestmatch], row):
                bestmatch = i
        bestmatches[bestmatch].append(rowno)

        rowno += 1
    return bestmatches