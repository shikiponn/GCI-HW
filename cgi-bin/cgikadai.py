#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#URL http://localhost:8000/cgi-bin/cgikadai.py    
# 鯖起動　python -m CGIHTTPServer

import datetime
import cgi
import MeCab
import cgikadai2

print('Content-type: text/html\n')
print(  """
<!DOCTYPE html>
<html>
<head>
    <title>CGI Script</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" >
    <script>
    function clearContents(element) {
        element.value = '';
    }
    </script>
</head>
<body>
<h3>CGI Script</h3>
<form method="post" action="cgikadai.py">
    <textarea onfocus="clearContents(this);" name="message">文章を入力してください</textarea>
    <input type="submit" name="submit" value="SEND">
</form>
""")
form = cgi.FieldStorage()
message = form.getvalue('message', '')
result = cgikadai2.analysenico(message)
print("""
<p>
<strong>検索キーワード:</strong><br>
<br>%s<br>
</p>
<h3>人気動画TOP100のタイトルに使われている名詞,動詞、形容詞、形容動詞トップ20:</h3>
""" %(message))
for i in range(1,20):
     print('<span>'+result[0][i]+'</span>：'+str(result[1][i]) +"<br>")
print('</body></html>')
