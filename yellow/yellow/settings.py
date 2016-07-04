# -*- coding: utf-8 -*-

# Scrapy settings for yellow project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'yellow'

SPIDER_MODULES = ['yellow.spiders']
NEWSPIDER_MODULE = 'yellow.spiders'


ITEM_PIPELINES = ['yellow.pipelines.YellowPipeline']

MONGODB_SERVER = "192.168.15.252"
MONGODB_PORT = 27017
MONGODB_DB = "seccion_amarilla"
MONGODB_COLLECTION = "contacts"

MX_STATES = [
	'aguascalientes',
	'baja-california',
	'baja-california-sur',
	'campeche',
	'chiapas',
	'chihuahua',
	'coahuila',
	'colima',
	'distrito-federal',
	'durango',
	'guerrero',
	'guanajuato',
	'hidalgo',
	'jalisco',
	'mexico',
	'michoacan',
	'morelos',
	'nayarit',
	'nuevo-leon',
	'oaxaca',
	'puebla',
	'quintana-roo',
	'queretaro',
	'sinaloa',
	'san-luis-potosi',
	'sonora',
	'tabasco',
	'tamaulipas',
	'tlaxcala',
	'veracruz',
	'yucatan',
	'zacatecas'
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'yellow (+http://www.yourdomain.com)'
