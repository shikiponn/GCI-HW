import networkx as nx
import mysql.connector
import matplotlib.pyplot as plt


G = nx.MultiGraph()

# #データベース設定
connect = mysql.connector.connect(
    database="rcdata",
    user="root",
    password="yukikaze",
)
dbc = connect.cursor(buffered=True)   
 
 
# レストランの種類
dbc.execute('SELECT Rcuisine, count(*) FROM usercuisine GROUP BY Rcuisine')
row = dbc.fetchall()
    # 出力
cuisines = []
for i in row:
        G.add_node(i[0], type = i[0])
        
print(cuisines)
G.add_nodes_from(cuisines)

#予算
budget = []
dbc.execute('SELECT budget, count(*) FROM userprofile GROUP BY budget')
row = dbc.fetchall()
for i in row:
        G.add_node(i[0], budget = i[0])
print(budget)


#エッジ
dbc.execute('SELECT Rcuisine, budget, count(*) FROM usercuisine INNER JOIN userprofile ON userprofile.userID = usercuisine.userID  GROUP BY Rcuisine, budget;')
row = dbc.fetchall()
for i in row:
        G.add_edge(i[0], i[1], weight=i[2])
    
# グラフを描く
nx.draw(G)
# グラフを表示する
plt.show()
nx.write_gexf(G,"kadai.gexf")
connect.close()
