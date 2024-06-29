import requests
import json


def shortToLong(shortUrl):
    url = 'http://api.dwzjh.com/api/reduction?url={}'.format(shortUrl)
    res = requests.get(url).text
    res_dict = json.loads(res)
    longUrl = res_dict['longurl']  # 获取app长链接
    print(longUrl)
    noteUrl = longUrl.split('?')[0]
    print(noteUrl)


if __name__ == '__main__':
    shortToLong('http://xhslink.com/do9xGe')
