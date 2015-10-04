import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from string import *
from itertools import count
from _ast import Str
from numpy.random import *

seed(100)
a=np.random.random((10,2))+2   #5*10行列
b=np.random.random((10,2))+5
c=np.random.random((10,2))+8
X=np.concatenate((a,b,c))


tX = np.array([[1, 2, 0], [2, 4, 0], [0, 0, 10 ]])


#距離行列を作って返す
def calc(X):
    ncol = X.shape[0]
    #距離行列 distance matrix を作成 0 padded
    mat = np.zeros([ncol, ncol])
    
    #ユークリッド距離行列を作成
    count_i = 0
    for i in X:
        count_j = 0
        
        for j in X:        
            ed = np.linalg.norm(i-j)
#             print(ed)
            mat[count_i][count_j] = ed
            count_j += 1
        count_i += 1
        
    return mat

##最小値を検索
def slm(mat):
    #0以上の最小値を取る
    i,j = np.unravel_index(mat.argmax(), mat.shape)
    max = mat[i,j]
    print(max,i, j)
    min = np.array([max,i, j]) #[ 最小値、行2、列 ]
    
    count_i = 0
    for i in mat:
        count_j = 0
        for j in mat:        
            if mat[count_i][count_j] > 0 and mat[count_i][count_j] < min[0] and count_i != count_j:
                
                min[0] = mat[count_i][count_j]
                min[1] = count_i
                min[2] = count_j
            count_j += 1  
            
        count_i += 1
#     print(min)
    
    return min
    
#ベクトルを単結合する         
def cut_n_comb(X, min, add_vec):
    v1= X.iloc[min[1]]
    v2 = X.iloc[min[2]]
    #新しいベクトル生成
    new_v = np.zeros([1,v1.size])
    for i in range(v1.size):    
        if v1[i] > v2[i]:   
            new_v[0][i] = v2[i]
        elif v2[i] > v1[i]:
            new_v[0][i] = v1[i]
#     for i in v1:
        
    print("合成ベクトル：", new_v)  
    #削除して結合
#     print("更新前サイズ", X.shape)
    min1 = min[1]
    min2 = min[2]
    #列置き換え
#     print("列１前: ", X.ix[:, min1])
#     print("行１前: ", X.ix[min1])
    X.iloc[:, min1] = new_v[0] 
    X.iloc[min1] = new_v[0] 
#     print("post: ", X.ix[:, min1])
#     print("post: ", X.ix[min1])
    
    #該当番号のラベルを取得し更新
    print(X.index[min1])
    print(X.index[min2])
    new_label = str(X.index[min1]) + "+" + str(X.index[min2])
    X = X.rename(index={X.index[min1]: new_label})
    X = X.rename(columns={X.columns[min1]: new_label})
    add_vec.append(new_label)


#削除
    print("col", X.columns)
    print("row", X.index)
    print(X.index[min2])
    print(X.columns[min2])
    X = X.drop(X.index[min2])
    r =X.columns[min2]
    X = X.drop(r, axis = 1)
    print(X)
    print("col", X.columns)
    print("row", X.index)
    ncol = X.shape
    print("更新後サイズ", ncol)
    print(X.index)
    new_X = X
    return new_X, add_vec
        
    
def klst(X):
    history=[] #結合履歴
    clusters = [] #クラスタ管理用配列
    for row in X:
        clusters.append(row)
    print("クラスタ配列", clusters)
    add_vec =[]    
    print("データ行列の大きさ ", X.shape)
    count = X.shape[0]
    dist = calc(X)
    print("距離行列の大きさ", dist.shape)
    print(dist)

    #距離行列の最小値とインデックスを取得
    dist2= dist[dist>0]
    print("最短距離", dist2.min())
    #print(dist.where(dist2.min))
    i,j = np.unravel_index(dist2.argmin(), dist.shape)
    min = dist[i,j]
    print(min)
    print(i,j)
    exit()
    
    
    ind=[x for x in range(0,count)]
    #距離行列の大きさが１より大きい間処理を続ける
    while dist.shape[0] > 1:
        dist = pd.DataFrame(dist, index = ind ,columns = ind)

        p =slm(dist.values)
        print("最短距離ベクトル", p)
    #     print(dist)
        dist, add_vec = cut_n_comb(dist, p, add_vec)
        ind= dist.index
        dist = dist.values
        i,j = np.unravel_index(dist.argmax(), dist.shape)
        max = dist[i,j]
        if max == 0:#の例外処理が必要
            break
        print("合成結果：", add_vec)
        count -= 1
        print(count-1, "残り処理回数")
        print("-----------------------------")




clusters = []
#for count in len(X):
    
klst(tX)
print("元データ：",X)







