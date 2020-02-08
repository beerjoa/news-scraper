# -*- coding: utf-8 -*-

import sys
import requests
import re
import base64
import json
import logging
import os
import scrapy
import json
import datetime
import timeit
from scrapy.crawler import CrawlerProcess
from naverNews.spiders.naverNewsCrawl import NavernewscrawlSpider
from scrapy.utils.project import get_project_settings

BASE_DIR = os.getcwd()

with open(BASE_DIR + "/newsList.json") as newsList:
    newsListDic = json.load(newsList)

argvList = [False] * 5

def printUsage():
    for k, v in newsListDic.items():
        print("- {}".format(k))
        for kk, kv in v.items():
            print("     {}: {}".format(kk, kv))

    print("\n    -og: newsOfficeGroup")
    print("    -o: newsOffice")
    print("    -from: from date (YYYYMMDD)")
    print("    -to: to date (YYYYMMDD)")
    print("    -k: news keyword")
    print("  ex: ")
    print('  python news-scraper.py -og=방송/통신 -o=1109,1079 -from=20200202 -to=20200205 -k="야구"')
    print('  python news-scraper.py -o=1109,1079 -o=1109,1079 -from=201901102 -to=20200205 -k="날씨 | 미세먼지"')
    print('  python news-scraper.py -og=경제/IT -o=1109,1079 -from=20130101 -to=20200205 -k="금리 인상"')


def setArgv():
    for a in sys.argv[1:]:
        try:
            k, v = a.split("=")
        except:
            print("incorrent argv")
            sys.exit(1)

        if v == "":
            continue

        if k == "-og":
            argvList[0] =  [i for i in v.split(",") if i in newsListDic.keys()]
            argvList[1] = True
        elif k == "-o":
            for i in v.split(","):
                if i.strip() not in ([kk for k, v in newsListDic.items() for kk, vv in v.items()]):
                    print("entered wrong office code")
                    sys.exit(1)
            if  argvList[0] == False:
                argvList[0] = True
            argvList[1] = v
        elif k == "-from":
            argvList[2] = v
        elif k == "-to":
            argvList[3] = v
        elif k == "-k":
            argvList[4] = v

    if False in argvList:
        print("argv error")
        print("")
        printUsage()
        sys.exit(1)


def main():
    setArgv()
    chkNewsOffice = []
    if argvList[0] not in [True,False]:
        chkNewsOffice = [ i for k in argvList[0] for i in newsListDic[k].keys() ]
    if argvList[1] not in [True,False]:
        chkNewsOffice.extend(argvList[1].split(","))
    keyword = argvList[-1]
    dates = argvList[2:-1]
    s = get_project_settings()
    s.update({
        'FEED_FORMAT':'json',
        'FEED_URI': 'outputNews/{}.json'.format("-".join(argvList[2:])),
    })
    process = CrawlerProcess(s)
    process.crawl(NavernewscrawlSpider, chkNewsOffice=chkNewsOffice, keyword=keyword, dates=dates, newsListDic=newsListDic)
    process.start()
    #


if __name__ == '__main__':
    start = timeit.default_timer()

    main()

    stop = timeit.default_timer()
    print("소요 시간: {}분 {}초".format(int(stop - start) // 60, int(stop - start) % 60))
