# 生成新的json文件
import json
from download import get_all_url, load_data

icon = load_data()
all_urls = get_all_url(icon)
# print(all_urls)

for category in all_urls.keys():
    for url in all_urls[category]:
        print(url)
        new_url = f'https://emoji.vccv.cc/emoji/{category}/{url.split("/")[-1]}'
        print(new_url)
        for emoji in icon[category]['container']:
            print(emoji)
            if url in emoji['icon']:
                emoji['icon'] = '<img src="' + new_url + '">'
                print(emoji)
                print('------------------')

with open('json/emoji.json', 'w', encoding='utf-8') as f:
    json.dump(icon, f, ensure_ascii=False)
