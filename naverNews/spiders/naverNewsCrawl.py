# -*- coding: utf-8 -*-
import scrapy
import datetime
from naverNews.items import NavernewsItem
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta
import urllib.parse
from urllib.parse import quote
import re

def daterange(date1, date2):
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + timedelta(n)

class NavernewscrawlSpider(scrapy.Spider):
    name = 'naverNewsCrawl'
    start_urls = []

    def __init__(self, chkNewsOffice=None, keyword=None, dates=None, newsListDic=None, *pargs, **kwargs) :
        self.chkNewsOffice = chkNewsOffice
        self.keyword = keyword
        self.dates = dates
        self.newsListDic = newsListDic
        super(NavernewscrawlSpider, self).__init__(*pargs, **kwargs)

    def start_requests(self):

        chked = ",".join(self.chkNewsOffice)
        fromDate, toDate = list(
            map(lambda x: datetime.datetime.strptime(x, "%Y%m%d"), self.dates))

        dateList = [dt.strftime("%Y.%m.%d")
                    for dt in daterange(fromDate, toDate)]
        keywordList = [quote(self.keyword)]
        self.start_urls = ["https://search.naver.com/search.naver?where=news&query={}&sort=1&photo=0&field=0&reporter_article=&pd=3&ds={}&de={}&docid=&nso=so%3Add%2Cp%3Afrom{}to{}%2Ca%3Aall&mynews=1&refresh_start=0&related=0".format(keyword, date, date, date.replace(".", ""), date.replace(".", "")) for keyword in keywordList for date in dateList]
        for url in self.start_urls:
            yield scrapy.Request(url=url,
                                 cookies = {
                                    'news_office_checked': chked
                                 },
                                 headers={
                                     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
                                 },
                                 callback=self.parse)

    def parse(self, response):
        for i in response.css('div.news ul.type01 li'):
            naver_href = i.css('dd.txt_inline a::attr(href)').get()
            yield response.follow(naver_href, self.naver_news)

        # next page
        next_page = response.css('div.paging a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def naver_news(self, response):
        item = NavernewsItem()
        item['href'] = response.url
        dateRegex = re.compile(r"([0-9]{4}\.[0-9]{2}\.[0-9]{2})")
        keys = ['title', 'date', 'content', 'newsfrom']
        for k in keys:
            item.setdefault(k,False)

        if response.status != 200:
            yield item

        try:
            # entertain form
            if "entertain" in response.url:
                newsOffice = response.css('div.press_logo a img::attr(alt)').get()
                title = response.css('h2.end_tit::text').get()
                time = response.css('div.article_info span.author em::text').get()
                bodyText = response.css('div#articeBody *::text').getall()
                bodyText = [t.strip() for t in bodyText[3:-2]]

                item['newsfrom'] = newsOffice
                item['title'] = title.strip()
                item['date'] = dateRegex.search(time)[0]
                item['content'] = " ".join(bodyText)



            # sports form
            elif "sports" in response.url:
                if response.css('div.column_logo a::text').get() == "칼럼":
                    newsOffice = response.css('div.column_info p.info_spec span.spec_writer::text').get()
                    newsOffice += " 칼럼"
                    title = response.css('div.column_info div.default_h h3::text').get()
                    time = response.css('div.column_info div.default_h span::text').get()
                else:
                    newsOffice = response.css('span.logo a img::attr(alt)').get()
                    title = response.css('div.news_headline h4.title::text').get()
                    time = response.css('div.news_headline div.info span::text').get()
                bodyText = response.css('div#newsEndContents *::text').getall()
                bodyText = [t.strip() for t in bodyText[:-3]]

                item['newsfrom'] = newsOffice
                item['title'] = title.strip()
                item['date'] = dateRegex.search(time)[0]
                item['content'] = " ".join(bodyText)


            # news form
            else:
                newsOffice = response.css('div.press_logo a img::attr(title)').get()
                title = response.css('div.article_info>h3::text').get()
                time = response.css('div.sponsor span.t11::text').get()
                bodyText = response.css('div.article_body div#articleBodyContents *::text').getall()
                bodyText = [t.strip() for t in bodyText[5:-4]]

                item['newsfrom'] = newsOffice
                item['title'] = title.strip()
                item['date'] = dateRegex.search(time)[0]
                item['content'] = " ".join(bodyText)


            yield item

        except:
            yield item
