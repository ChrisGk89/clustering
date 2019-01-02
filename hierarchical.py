from PIL import Image, ImageDraw
from Pearson import pearson


class mergedclusters:
    # Left Subtree
    # Right Subtree
    # Blog id
    # Distance
    # Vector
    def __init__(self, vec, left=None, right=None, distance=0.0, id=None):
        self.left = left
        self.right = right
        self.vec = vec
        self.id = id
        self.distance = distance


def hierarchicalcluster(rows, distance=pearson):
    cluster = {}
    closestClusters = []

    for i in range(len(rows)):
        cluster[i] = mergedclusters(rows[i], id=i)
    # Find two closest nodes
    while len(cluster) > 1:
        closestClusters = (0, 1)
        closest = distance(cluster[0].vec, cluster[1].vec)

        # loop through every pair looking for the smallest distance
        for i in range(len(cluster)):
            for j in range(i + 1, len(cluster)):
                A = cluster[i]
                B = cluster[j]

                distances = {}
                # distances is the cache of distance calculations
                if (A.id, B.id) not in distances:
                    distances[(A.id, B.id)] = distance(A.vec, B.vec)
                d = distances[(A.id, B.id)]

                # New set of closest nodes found
                if d < closest:
                    closest = d
                    closestClusters = (i, j)

        # Merging the closest clusters
        currentclustid = -1
        currentclustid -= 1
        merged_clusters = merge(closestClusters, closest, currentclustid)

        # Closest clusters merged so we delete the old ones.
        del cluster[closestClusters[1].id]
        del cluster[closestClusters[0].id]
        #  Add new cluster
        cluster[currentclustid] = merged_clusters

    # Return the final cluster of all clusters
    return list(cluster.values())[0]

# calculate the average of the two clusters
# mergevec = [
#   (cluster[closestpair[0]].vec[i] + cluster[closestpair[1]].vec[i]) / 2.0
#  for i in range(len(cluster[0].vec))]

# create the new cluster
# newcluster = mergedclusters(mergevec, left=cluster[closestpair[0]],
#                           right=cluster[closestpair[1]],
#                          distance=closest, id=currentclustid)


# Merge two clusters A and B
def merge(clusters, distance, id):
    # Create new cluster
    A = clusters[0]
    B = clusters[1]
    newCluster = []

    # Merge blog data by averaging word counts for each word
    for i in range(len(A.vec)):
        countWordA = A.vec[i]
        countWordB = B.vec[i]
        merge_count = countWordA + countWordB / 2.0
        # Set blog to new cluster
        newCluster.append(merge_count)

    merged_clusters = mergedclusters(newCluster, left=A, right=B, id=id, distance=distance)

    return merged_clusters


def showResults(cluster, labels=None, n=0):
    # indent to make a hierarchy layout
    for i in range(n):
        print ' ',
    if cluster.id < 0:
        # negative id means that this is branch
        print '-'
    else:
        # positive id means that this is an endpoint
        if labels == None:
            print cluster.id
        else:
            print labels[cluster.id]

    # now print the right and left branches
    if cluster.left != None: showResults(cluster.left, labels=labels, n=n + 1)
    if cluster.right != None: showResults(cluster.right, labels=labels, n=n + 1)

