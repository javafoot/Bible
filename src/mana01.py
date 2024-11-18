# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from datetime import datetime
import requests

# 获取当前日期
today = datetime.today()

# 格式化日期为年月日格式，注意链接中的日期格式通常是两位数表示月份和日，所以使用zfill前面的0
formatted_date = today.strftime('%Y年%m月%d日')
date_number = today.strftime('%y%m%d')

# 构建链接
text_link = f"https://pyhtm.azureedge.net/htm/html/mw/mw{date_number}.html"
audio_link = f"https://aud.ltlt.uk/mw/mw{date_number}.mp3"
# 发送HTTP请求获取网页内容
response = requests.get(text_link)
response.encoding = 'utf-8'  # Set encoding before accessing .text
content_type = response.headers.get('content-type')
if content_type == 'text/html':
    # 使用BeautifulSoup解析网页
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.findAll('p')[1].get_text(strip=True)
    print(f"\n旷野吗哪-{formatted_date}  {title}\n")
    print(f"文字链接(如果打不开，就只能浏览器里打开)：\n{text_link}\n")
else:
    print(f"\n旷野吗哪-{formatted_date}\n")
    print(f"文字链接目前打不开：\n{text_link}\n")
print(f"音频(可能会有1分钟左右的缓冲)：\n{audio_link}")


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
mp3_url = "http://example.com/song.mp3"
downloaded_file = download_mp3(audio_link)
print(f"\n\nMP3文件已下载至: {downloaded_file}")

