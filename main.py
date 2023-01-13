import json
import re

import requests

with open('emoji.json', 'r') as f:
    emoji = json.load(f)

emoji_category = emoji.keys()
select_category = ['Heo', 'Cat', '阿鲁', '小鲨鱼', 'Yurui-Neko']

# 新的emoji字典
new_emoji = {}

# 选择需要的表情包 最后生成的json文件只包含这些表情包
for category in emoji_category:
    if category in select_category:
        print(category)
        new_emoji[category] = emoji[category]

# 保存到json文件
with open('new_emoji.json', 'w') as f:
    json.dump(new_emoji, f)

# print(new_emoji)
# 下载表情包
for category in new_emoji.keys():
    for emoji in new_emoji[category]['container']:
        # <img src='https://twikoo-magic.oss-cn-hangzhou.aliyuncs.com/Yurui-Neko/039.png'>
        url = re.findall(r"src='(.*?)'", emoji['icon'])
        if url:
            url = url[0]
            print(url)
            r = requests.get(url)
            with open(f'./emoji/{url.split("/")[-1]}', 'wb') as f:
                f.write(r.content)
        else:
            print(emoji['text'])
            raise Exception('url not found')
        name = emoji['text']
