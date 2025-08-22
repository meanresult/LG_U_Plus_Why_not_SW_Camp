import meilisearch

client = meilisearch.Client('http://127.0.0.1:7700', 'R49yUQJ4Vqm8AoWC7DXkguPv0buBAMQoRFd6ZskKk8c')


def stock_search(query):
    return client.index('nasdaq').search(query)
