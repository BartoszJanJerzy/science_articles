import pprint
import bs4
import requests
import urllib, urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

from src.utils.get_articles import ArticlesMetadataLoader


url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=2'
results = ArticlesMetadataLoader().load(
    query='abs:cognitive+AND+abs:psychology',
    start=0,
    max_results=2,
    date_min="20200101",
    date_max=None
)

for r in results:
    print()
    print(r.title)
    print(r.abstract)
    print(r.authors)
    print(r.published)
    print()