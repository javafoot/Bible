# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from datetime import datetime
import requests

# 获取当前日期并格式化为"yyyymmdd"
noww = datetime.now()
today = noww.strftime("%y%m%d")
# Get the current year
current_year = noww.year

text_link = f"https://r.lyapp2.net/devotionals/devotionals-mw/devotionals-mw-mw{today}"
audio_link = f"https://z.lydt.work/ly/audio/{current_year}/mw/mw{today}.mp3"

# 发送GET请求获取网页内容
response = requests.get(text_link)
response.encoding = 'utf-8'  # Set encoding before accessing .text
content_type = response.headers.get('content-type')
# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')
# 获取标题元素并提取文本
title = soup.find('title').text
print(title)
print(text_link)
print('\n(微信里打不开。请把链接拷贝到浏览器里打开)')

def download_mp3(url, local_filename=None):
    """
    下载MP3文件并保存到本地。
    :param url: MP3文件的URL地址
    :param local_filename: 本地保存的文件名，默认为URL的最后一部分
    :return: 本地文件路径
    """
    if local_filename is None:
        # 如果未指定本地文件名，则从URL中提取
        local_filename = url.split('/')[-1]
    local_filename_path = f'/storage/emulated/0/Download/mn/{local_filename}'
    with requests.get(url, stream=True) as r:
        r.raise_for_status()  # 如果响应状态码不是200，将抛出HTTPError异常
        with open(local_filename_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # 使用分块传输来节省内存并显示进度
                f.write(chunk)
    return local_filename_path

# 示例URL，请替换为实际的MP3文件URL
downloaded_file = download_mp3(audio_link)
print(f"\n\nMP3文件已下载至: {downloaded_file}")



