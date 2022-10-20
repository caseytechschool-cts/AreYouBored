from googlesearch import search
import requests
from youtube_search import YoutubeSearch
import ast
import re


def feel_bored():
    url = 'http://www.boredapi.com/api/activity/'
    response = requests.get(url)
    if response.status_code == 200:
        data = ast.literal_eval(response.content.decode('utf-8'))
        return data['activity']


def web_search(task):
    web_results = {
        'title': [],
        'link': []
    }

    results = search(task, num_results=5)

    for result in results:
        title_txt = result[0:-1] if result[-1] == '/' else result
        title = re.sub('_|-', ' ', title_txt.split('/')[-1])
        web_results['title'].append(title.capitalize())
        web_results['link'].append(result)

    return web_results['title'], web_results['link']


def youtube_search(task):
    youtube_results = {
        'title': [],
        'image': [],
        'url_suffix': []
    }
    results = YoutubeSearch(task, max_results=5).to_dict()
    for result in results:
        youtube_results['title'].append(result['title'])
        youtube_results['image'].append((result['thumbnails'][0]))
        youtube_results['url_suffix'].append(f"https://youtube.com{result['url_suffix']}")
    return youtube_results['title'], youtube_results['url_suffix']

