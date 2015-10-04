#coding:utf-8
import feedparser
from datetime import datetime
from time import mktime


feed = feedparser.parse("http://headlines.yahoo.co.jp/rss/san-bus.xml")
print("RSSソース：", feed.feed.title)
for entry in range(len(feed.entries)):
    title = feed.entries[entry].title
    link = feed.entries[entry].link
    #更新日をdatetimeとして取得
    tmp = feed.entries[entry].published_parsed
    published_datetime = datetime.fromtimestamp(mktime(tmp))
    print("")
    print(title)
    print(link)
    print("更新日：", published_datetime)
    