import os
from collections import Counter
import urllib.request
from xml.etree import ElementTree as etree

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

with open(tempfile) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    root = etree.fromstring(content)
    categories = [c.text for c in root.iterfind('channel/item/category')]
    c = Counter(categories)
    return c.most_common(n)