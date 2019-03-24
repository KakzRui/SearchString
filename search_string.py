import json
from googleapiclient.discovery import build


api_key = 'AIzaSyCySWKZOWuHhxF6Wb1HG_Lo95vZthWIJt4'
cse = '013985332573525868405:ytdwjm685jw'
file_name = 'C:\\tmp\\search_results.json'


def google_search(search_term, api_key, cse, **kwargs):
    service = build('custom_search', 'v1', developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse, num=5, **kwargs).execute()
    return res


result = google_search('keystone - Circular reference found role inference', api_key, cse)
result = json.dumps(result, sort_keys=True, indent=4)
with open(file_name, 'w') as outfile:
    json.dump(result, outfile)
