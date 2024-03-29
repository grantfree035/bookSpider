# -*- coding: utf-8 -*-

# Scrapy settings for bookBNTC project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bookBNTC'

SPIDER_MODULES = ['bookBNTC.spiders']
NEWSPIDER_MODULE = 'bookBNTC.spiders'
ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE = '\image_dump'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bookBNTC (+http://www.yourdomain.com)'
