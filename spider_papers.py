import os
import requests
import re
import shelve
import random
from lxml import etree


class wp_stats():
    def __init__(self):
        self.page = 0
        self.number = 0
        self.n = 0


def get_url(index, headers, params):
    '''通过url获得原图地址'''
    url = 'https://openreview.net/group?id=NeurIPS.cc/2022/Conference'
    res = requests.get(url, headers=headers, params=params)
    content = res.content
    html = etree.HTML(content)
    result = html.xpath('//li/a/@href')
    return result


def get_bmp(result, headers, params):
    result_p = []
    for key in result:
        asm = key.replace('.htm', '-1920x1080.htm')
        asm = 'http://www.netbian.com/' + asm
        fes = requests.get(asm, headers=headers,  params=params)
        content = fes.content
        html = etree.HTML(content)
        key_f = html.xpath('//td/a/img/@src')
        for m in key_f:
            result_p.append(m)
    return result_p


def download_p(result_p, i):
    if not os.path.exists('image'):
        os.makedirs('image')

    for key in result_p:
        try:
            # 超时异常判断 10秒超时
            pic = requests.get(key, timeout=10)
        except requests.exceptions.ConnectionError:
            print('当前图片无法下载')
            continue

        file_name = "image\\" + str(i) + ".jpg"  # 拼接图片名
        print(file_name)

        fp = open(file_name, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
    return i


def wallpaper(stats):

    if not os.path.exists('data'):
        os.makedirs('data')

    shelfFile = shelve.open('.\\data\\cord')
    stats.page = shelfFile['page']
    stats.number = shelfFile['number']
    shelfFile.close()

    print('Began_page: %d' % stats.page)
    print('Began_number: %d' % stats.number)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'

    }
    paramslist = ['210.5.10.87:53281', '183.236.232.160:8080']

    stats.n = stats.page + 5
    while True:
        if (stats.page < stats.n):
            httpindex = random.randint(0, len(paramslist)-1)
            params = {
                'HTTP': paramslist[httpindex]
            }
            result = get_url(stats.page, headers, params)
            result_p = get_bmp(result, headers, params)
            stats.number = download_p(result_p, stats.number)
            stats.page += 1

            shelfFile = shelve.open('.\\data\\cord')
            shelfFile['page'] = stats.page
            shelfFile['number'] = stats.number
            shelfFile.close()

            print('End_page: %d' % (stats.page - 1))
            print('End_number: %d' % stats.number)


def main():
    stats = wp_stats()
    wallpaper(stats)


if __name__ == '__main__':
    main()
