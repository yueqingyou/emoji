"""
{
    "Takagi": {
        "type": "image",
        "container": [{
            "icon": "<img src=\"https://emoji.vccv.cc/emoji/Takagi/在干嘛.png\">",
            "text": "takagi-在干嘛"
        }, {
            "icon": "<img src=\"https://emoji.vccv.cc/emoji/Takagi/如何.png\">",
            "text": "takagi-怎么样"
        }, {
            "icon": "<img src=\"https://emoji.vccv.cc/emoji/Takagi/拜拜.png\">",
            "text": "takagi-拜拜"
        }, {
            "icon": "<img src=\"https://emoji.vccv.cc/emoji/Takagi/没事儿.png\">",
            "text": "takagi-没事儿"
        }]
    }
}
"""
import json
import os

emoji_dir = 'emoji/'
emoji_json = {}
url_prefix = 'https://emoji.vccv.cc/'
# 各表情包
all_emojis = []
g = os.walk(emoji_dir)
for path, dir_list, file_list in g:
    for dir_name in dir_list:
        all_emojis.append(os.path.join(path, dir_name))
# print(all_emojis)


# 处理每一个表情包
def emoji_fix(_emoji_dir):
    _container = []
    # Url
    _g = os.walk(_emoji_dir)
    for _path, _dir_list, _file_list in _g:
        for file_name in _file_list:
            if file_name != '.DS_Store':
                url = url_prefix + os.path.join(_path, file_name)
                # print(url)
                # Details
                _details = {
                    'icon': f'<img src=\"{url}\">',
                    'text': ''.join(file_name.split('.')[:-1])
                }
                # Container
                _container.append(_details)
    # 最内层
    _emoji = {'type': 'image',
              'container': _container
              }
    # 第一层
    emoji_json[_emoji_dir.split('/')[1]] = _emoji


if __name__ == '__main__':
    for emoji in all_emojis:
        emoji_fix(emoji)
    print(emoji_json)
    with open('json/emoji.json', 'w', encoding='utf-8') as f:
        json.dump(emoji_json, f, ensure_ascii=False)
