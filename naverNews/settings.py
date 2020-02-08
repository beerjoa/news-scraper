# -*- coding: utf-8 -*-

# Scrapy settings for naverNews project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import logging

BOT_NAME = 'naverNews'

SPIDER_MODULES = ['naverNews.spiders']
NEWSPIDER_MODULE = 'naverNews.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'naverNews (+http://www.yourdomain.com)'

ROBOTSTXT_OBEY = False
LOG_LEVEL = logging.WARNING
FEED_EXPORT_ENCODING = 'utf-8'



COOKIES_ENABLED = True
# COOKIES_DEBUG = True
