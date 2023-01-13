import os
import re
from multiprocessing import Pool
import requests
import json


# 加载数据
def load_data():
    with open('json/new_emoji.json', 'r') as f:
        icon = json.load(f)
    return icon


# 存储所有的url
def get_all_url(icon):
    all_url = {}
    print('开始下载表情包')
    _categories = icon.keys()
    print(f'共有{len(icon)}个表情包\n分别是：{_categories}')
    for _category in _categories:
        icons = icon[_category]
        containers = icons['container']
        _urls = []
        for container in containers:
            # print(container['icon'])
            _url = re.findall(r"src=('|\")(.*?)('|\")", container['icon'])[0][1]
            _urls.append(_url)
        all_url[_category] = _urls
    return all_url


def download(icon_category, icon_url):
    print(f'正在下载{icon_category}/{icon_url.split("/")[-1]}')
    if not os.path.exists('emoji'):
        os.mkdir('emoji')
    if not os.path.exists(f'./emoji/{icon_category}'):
        os.mkdir(f'./emoji/{icon_category}')
    with open(f'emoji/{icon_category}/{icon_url.split("/")[-1]}', 'wb') as f:
        f.write(requests.get(icon_url).content)
        if not os.path.exists(f'./emoji/{icon_category}'):
            os.mkdir(f'./emoji/{icon_category}')
        with open(f'emoji/{icon_category}/{icon_url.split("/")[-1]}', 'wb') as f:
            f.write(requests.get(icon_url).content)


if __name__ == '__main__':
    # 加载数据
    icon = load_data()

    # 获取所有的url
    all_url = get_all_url()

    # 开始下载
    for icon_category in all_url.keys():
        category_url = all_url[icon_category]
        print(f'开始下载{icon_category}表情包')
        pool = Pool(10)
        for icon_url in category_url:
            pool.apply_async(download, args=(icon_category, icon_url))
        pool.close()
        pool.join()
        print(f'{icon_category}表情包下载完成')
