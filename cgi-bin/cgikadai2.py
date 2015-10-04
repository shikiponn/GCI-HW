import urllib.request
import json
import sys
import codecs
import MeCab

def extractKeyword(text):
    #extを形態素解析して、名詞のみのリストを返す"""
    tagger = MeCab.Tagger()
    encoded_text = text.encode('utf-8')
    tagger.parse('')    #python3のバグ回避用　cf http://www.trifields.jp/how-to-use-mecab-in-ubuntu-14-04-and-python-3-1196
    node = tagger.parseToNode(text)
    wordCount = {}
    keywords = []
    while node:
        hinshi = node.feature.split(",")[0]
#         print(hinshi)
        if hinshi  == "動詞" or hinshi == "名詞" or hinshi == "形容詞" or hinshi == "形容動詞":
            keywords.append(node.surface)
            wordCount.setdefault(node.surface,0)
            wordCount[node.surface]+=1
        node = node.next
    return keywords, wordCount


"""
API部分
"""
def analysenico(query):
#     query = '初音ミク'  
    data = json.dumps({'query': query, 'service': ['video'], 'search': ['title', 'description', 'tags'],'join': [ 'title', 'view_counter'], 'issuer': 'nico_api',
                       "filters": [{
          "type": "range",
          "field": "view_counter",
          "from": "50000",
          
        }], "from":0,  "size": 100, "sort_by":"view_counter"  })
    
    req = urllib.request.Request('http://api.search.nicovideo.jp/api/snapshot/')
    req.add_header('content-type', 'application/json')
    
    response = urllib.request.urlopen(req, data.encode('utf-8'))
    response = response.readall().decode('utf-8')
    response = response.split("\n")
    obj = json.loads(response[0])
    
    #統合文字列　
    titles = ""
    
    for i in obj["values"]:
        titles = "".join([titles, i["title"]])
    titles = titles.replace(query, "").replace("　", "").replace(" ", "")
    d = extractKeyword(titles)[1]
    word=[]
    count=[]
    for k, v in sorted(d.items(), key=lambda x:x[1]):
        word.append(k)
        count.append(v)
    count = count[::-1]
    word = word[::-1]
    return word, count
