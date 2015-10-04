#coding:utf-8
import time
import numpy as np
import matplotlib.pyplot as pylab
from sklearn.cluster import KMeans


start = time.time()


#平均
mu1 = [-5,-5]
mu2 = [60,64]
mu3 = [-40,-74]
mu4 = [-50,24]
#共分散
cov = [[35,4],[4,20]] #分散共分散行列
cov2 = [[65,10],[10,60]] #分散共分散行列
cov3 = [[55,15],[15,60]] #分散共分散行列    
cov4 = [[85,55],[55,120]] #分散共分散行列    

#500はデータ数
x1,y1 = np.random.multivariate_normal(mu1,cov,500).T
x2,y2 = np.random.multivariate_normal(mu2,cov,500).T
x3,y3 = np.random.multivariate_normal(mu3,cov3,500).T
x4,y4 = np.random.multivariate_normal(mu4,cov4,500).T



#グラフ描画
#背景を白にする
pylab.figure(facecolor="w")

#散布図をプロットする
pylab.scatter(x1,y1,color='r',marker='x',label="$K_1,mu_1$")
pylab.scatter(x2,y2,color='b',marker='x',label="$K_2,mu_2$")
pylab.scatter(x3,y3,color='g',marker='x',label="$K_3,mu_3$")
pylab.scatter(x4,y4,color='y',marker='x',label="$K_3,mu_3$")
#ついでにグラフの中に文字を入れてみる
# pylab.figtext(0.8,0.6,"$R_1$",size=20)
# pylab.figtext(0.2,0.3,"$R_2$",size=20)

#ラベル
pylab.xlabel('$x$',size=20)
pylab.ylabel('$y$',size=20)

#軸
pylab.axis([-100.0,100.0,-100.0,100.0],size=20)
pylab.grid(True)
pylab.legend()

#描画
pylab.show()

elapsed_time = time.time() - start
print("サンプリングに要した時間: ", elapsed_time)


"""
Kmeans
"""

# print(np.c_[x1, y1])
m1 = np.c_[x1, y1]
m2 = np.c_[x2, y2]
m3 = np.c_[x3, y3]
m4 = np.c_[x4, y4]
mx = np.r_[m1, m2, m3, m4]
print(mx)
print(mx.shape)

# K-means クラスタリングをおこなう
# この例では 4 つのグループに分割、 1 回のランダマイズをおこなう
kmeans_model = KMeans(n_clusters=4, random_state=2).fit(mx)
labels = kmeans_model.labels_
# ラベル (班) 、成績、三科目の合計得点を表示する
for label, feature in zip(labels, mx):
    print(label, feature, feature.sum())

end_time = time.time() - elapsed_time

print("クラスタリングに要した時間: ", end_time )
print(kmeans_model)