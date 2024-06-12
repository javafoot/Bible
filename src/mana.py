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

# 使用BeautifulSoup解析网页
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.findAll('p')[1].get_text(strip=True)

print(f"旷野吗哪-{formatted_date}  {title}\n")
print(f"文字链接(如果打不开，就只能浏览器里打开)：\n{text_link}\n")
print(f"音频(可能会有1分钟左右的缓冲)：\n{audio_link}")

