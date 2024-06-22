import json
import os

# 定义表情包目录和URL前缀
emoji_dir = 'emoji/'
url_prefix = 'https://emoji.vccv.cc/'

# 初始化存储表情包信息的字典
emoji_json = {}

# 获取所有表情包目录
all_emojis = [os.path.join(path, dir_name) for path, dir_list, file_list in os.walk(emoji_dir) for dir_name in dir_list]

# 处理每一个表情包
def emoji_fix(_emoji_dir):
    _container = []
    # 遍历表情包目录中的文件
    for _path, _dir_list, _file_list in os.walk(_emoji_dir):
        for file_name in _file_list:
            if file_name != '.DS_Store':
                # 构建文件URL
                url = url_prefix + os.path.join(_path, file_name).replace('\\', '/')
                # 构建表情包详情
                _details = {
                    'icon': f'<img src="{url}">',
                    'text': '-'.join(file_name.split('.')[:-1])
                }
                # 添加到容器
                _container.append(_details)
    # 构建最内层结构
    _emoji = {
        'type': 'image',
        'container': _container
    }
    # 构建第一层结构
    emoji_json[_emoji_dir.split(os.sep)[1]] = _emoji

if __name__ == '__main__':
    # 处理所有表情包
    for emoji in all_emojis:
        emoji_fix(emoji)
    # 打印结果
    print(json.dumps(emoji_json, ensure_ascii=False, indent=4))
    # 保存结果到文件
    with open('json/emoji.json', 'w', encoding='utf-8') as f:
        json.dump(emoji_json, f, ensure_ascii=False, indent=4)
