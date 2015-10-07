#coding:utf-8
import csv
import mysql.connector
import os
from builtins import range
import config

"""
#データ読み込み
"""
path = "/Users/shiki/Dropbox/2015年度/GCI/RCdata/geoplaces2.csv"

#ファイル名取得＋ファイル開く
f = open(path, 'r', encoding='utf-8')
filename = os.path.basename(path)
name , ext = os.path.splitext(filename)
print("filename is" + name)
dataReader = csv.reader(f)

#csvの列数と各列のラベルを取得しrow_numとcol_nameに代入
row_num = 0
col_name = []
for row in dataReader:
        #col_name = [row[0], row[1]]
        print("csvの列数：", len(row))
        row_num = len(row)
        for i in range(row_num):
            col_name.append(row[i])
        break
print(col_name)

cols = {}

# csvの列の数だけディクショナリにリストを追加 e.g. col+n
for i in range(row_num):
    print(i)
    key_name = "col" + str(i)
    cols.update({key_name : []})
print('Labels :  ')
print(cols)
    


#ラベル以外残りの行をlistに入れていく
for row in dataReader:
    for j in range(row_num):
        label = "col" + str(j)
        cols[label].append(row[j])
        #cols["col0"].append(row[0])
        #cols["col1"].append(row[1])       

ncol = 0 #行数を取得
#格納されたかプリントして確認
for j in range(row_num):
    label = "col" + str(j)
    print("row" + str(j) + "is :")
    print(cols[label])
    ncol = len(cols[label])
    print(ncol)




"""
#データベース設定
"""
connect = mysql.connector.connect(
    database=config.db,
    user=config.user,
    password=config.pw,
)
       
dbc = connect.cursor(buffered=True)    
# DBの指定テーブルを表示
#print(dbc.execute('SELECT * FROM chefmozaccepts'))

"""
#テーブル作成
"""

data_list = 'id int(11) UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT'
for j in range(row_num):
    #カンマを付ける
    data_list = data_list + ", "
    
    print(col_name[j])
    label = "col" + str(j)
    
#各列に格納されているデータの最大文字数を取得しその二倍を最大文字数とする
    max_len = 0
    for i in cols[label]:
        if max_len < len(i):
            max_len = len(i)
    max_len = max_len * 2
    print("double of max_len of this col is　" + str(max_len))
        
    #結合
    data_list = data_list + col_name[j] + " VARCHAR(" + str(max_len) + ")" 
#    data_list.append(col_name[j] + " " + "VARCHAR(25)") 

print(data_list) 
print('CREATE TABLE IF NOT EXISTS rcdata.{0}( {1} )'.format(name, data_list))
print(dbc.execute('CREATE TABLE IF NOT EXISTS rcdata.{0}( {1} )'.format(name, data_list)))


"""
#データinsert
"""

#DBのカラム名を結合
db_vals = ''
j=0
for i in col_name:
    db_vals = db_vals + i
    if j != len(col_name)-1:
        db_vals = db_vals + ", "
    j += 1

#Insert する　VALを展開
vals = ""
for i in range(ncol):
    vals = vals + "( "
    for j in range(row_num):
        label = "col" + str(j)
        vals = vals + '"'+cols[label][i] +'"'
        if j != row_num - 1 :
            vals = vals + ", "
    vals = vals + " )"
    if i != ncol-1:
        vals = vals + ", "
print(vals)




# SQL作成　実行
insert = 'insert into ' + name + " (" + db_vals + ') values ' + vals 
print(insert)
dbc.execute(insert)
connect.commit() #do not forget    
    
#CLOSE処理    

dbc.close()
connect.close()
f.close()
