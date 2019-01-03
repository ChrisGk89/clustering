from Pearson import pearson


class branches:
    def __init__(self, vec, left=None, right=None, distance=0.0, id=None):
        self.left = left
        self.right = right
        self.vec = vec
        self.id = id
        self.distance = distance


def hierarchicalcluster(rows, distance=pearson):
    distances = {}
    currentclustid = -1
    cluster = []
    merge = []

    # Clusters are initially rows
    for i in range(len(rows)):
        cluster.append(branches(rows[i], id=i))

    # Iterate till only on cluster left
    while len(cluster) > 1:
        # Find the two closest nodes
        closestpair = (0, 1)
        closest = distance(cluster[0].vec, cluster[1].vec)

        # loop through every pair looking for the smallest distance
        for i in range(len(cluster)):
            for j in range(i + 1, len(cluster)):
                ClusterA = cluster[i]
                ClusterB = cluster[j]

                # Store the correlation results for each pair to
                # save time,since they will have to be calculated
                # again and again until one of the items in the pair
                # is merged into another cluster.
                if (ClusterA.id, ClusterB.id) not in distances:
                    distances[(ClusterA.id, ClusterB.id)] = distance(ClusterA.vec, ClusterB.vec)
                smallestdistance = distances[(ClusterA.id, ClusterB.id)]

                # From the calculated distances we find the closest
                # New set of closest nodes found
                if smallestdistance < closest:
                    closest = smallestdistance
                    closestpair = (i, j)

        # Merge the two clusters
        merge = [(cluster[closestpair[0]].vec[i] + cluster[closestpair[1]].vec[i]) / 2.0
                 for i in range(len(cluster[0].vec))]

        # Add the new cluster
        newcluster = branches(merge, left=cluster[closestpair[0]],
                              right=cluster[closestpair[1]],
                              distance=closest, id=currentclustid)

        # final_clusters = merge (closestpair, closest, currentclustid)

        # cluster ids that weren't in the original set are negative
        currentclustid -= 1
        del cluster[closestpair[1]]
        del cluster[closestpair[0]]
        cluster.append(newcluster)
        # cluster[currentclustid] = final_clusters
        # Return the final cluster of the merged clusters
        # return final_clusters[0]
    return cluster[0]


''' 
def merge(clusters, distance, id):

    countWordA = cluster[closestpair[0].vec[i]]
    countWordB = cluster[closestpair[1].vec[i]]
    newCluster = []

    for i in range (len(A.vec)):

      count = (wordA + wordB) / 2.0
      newCluster.append(count)


    newcluster = branches(newCluster, left=A,right=B, distance=closest, id=currentclustid)

    return newcluster'''


def showTree(cluster, labels=None, n=0):
    # indent to make a hierarchy layout
    for i in range(n):
        print' ',
    if cluster.id < 0:
        # negative id means that this is branch
        print '--'
    else:
        # positive id means that this is an endpoint
        if labels == None:
            print cluster.id
        else:
            print labels[cluster.id]
    # now print the right and left branches
    if cluster.left != None: showTree(cluster.left, labels=labels, n=n + 1)
    if cluster.right != None: showTree(cluster.right, labels=labels, n=n + 1)

