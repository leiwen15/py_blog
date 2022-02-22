# from elasticsearch import Elasticsearch
# es = Elasticsearch('http://localhost:9200')

# es.index(index='my_index', id=1, body={'text': 'this is a test'})
#
# print(es.search(index='my_index', body={'query':{'match': {'text': 'this is text'}}}))
#
# es.indices.delete('my_index')

from app.search import add_to_index, remove_from_index, query_index
