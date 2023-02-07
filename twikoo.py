import os

import json
from urllib.parse import quote
from download import get_all_url, load_data

icon = load_data()
all_urls = get_all_url(icon)
# print(all_urls)

url_fix = {}
for category in all_urls.keys():
    for url in all_urls[category]:
        url = quote(url, safe=':/')
        # print(url)
        new_url = f'https://emoji.vccv.cc/emoji/{category}/{url.split("/")[-1]}'
        # print(new_url)
        url_fix[url] = new_url
# print(url_fix)

count = 0
with open('twikoo.json', 'r') as f:
    for line in f:
        data = json.loads(line)
        comment = data['comment']
        for url in url_fix.keys():
            if url in comment:
                # print(url)
                count += 1
                comment = comment.replace(url, url_fix[url])
        data['comment'] = comment
        with open('twikoo_new.json', 'a') as f:
            f.write(json.dumps(data, ensure_ascii=False))
            f.write('\n')

print(count)
