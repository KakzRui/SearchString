import json
from googleapiclient.discovery import build


def search_string(search_key):
    api_key = 'AIzaSyCySWKZOWuHhxF6Wb1HG_Lo95vZthWIJt4'
    cse = '013985332573525868405:ytdwjm685jw'
    # TODO: Need to save the data in proper path.
    file_name = 'C:\\tmp\\search_results.json'
    results = google_search(search_key, api_key, cse)
    results = json.dumps(results, sort_keys=True, indent=4)
    with open(file_name, 'w', encoding='utf-8') as outfile:
        json.dump(results, outfile)


def google_search(search_term, api_key, cse, **kwargs):
    service = build('customsearch', 'v1', developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse, num=5, **kwargs).execute()
    return res
