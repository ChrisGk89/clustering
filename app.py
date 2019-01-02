from flask import Flask, render_template
from flask_restful import Api

from hierarchical import hierarchicalcluster, drawdendrogram, showResults
from kmeans import kmeanscluster
from readfile import readfile

app = Flask(__name__)
api = Api(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/kmeans')
def kmeans():
    nr_of_clusters = 5
    blognames,words,data= readfile()
    kclust= kmeanscluster(data,k=5, max_iter=5)
    centroid_0 = []
    centroid_1 = []
    centroid_2 = []
    centroid_3 = []
    centroid_4 = []
    centroids = [];
    for r in kclust[0]:
        centroid_0.append(blognames[r])
    for i in kclust[1]:
         centroid_1.append(blognames[i])
    for j in kclust[2]:
         centroid_2.append(blognames[j])
    for k in kclust[3]:
        centroid_3.append(blognames[k])
    for l in kclust[4]:
            centroid_4.append(blognames[l])
    centroids = ((centroid_0, len(centroid_0)), (centroid_1, len(centroid_1)), (centroid_2, len(centroid_2)), (centroid_3, len(centroid_3)), (centroid_4, len(centroid_4)));
    #print centorids
    return render_template('kmeans.html', kclust = centroids, noc = nr_of_clusters)


@app.route('/hierarchical')
def hierarchical():
    blognames, words, data=readfile()
    cluster = hierarchicalcluster(data)
    resultItems = showResults(cluster, labels=blognames)
    #resultItems = drawdendrogram(clust, blognames, jpeg='blogclust.jpg')
    return render_template('hierarchical.html', itemresult = resultItems)


if __name__ == '__main__':
    app.run(debug=True)