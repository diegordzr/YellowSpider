# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class AddressItem(Item):
    street = Field()
    neighborhood = Field()
    municipality = Field()
    postal_code = Field()
    state = Field()

class ContactItem(Item):
    key = Field()
    name = Field()
    phone = Field()
    email = Field()
    address = Field()
    services = Field()
    schedules = Field()
    payment_types = Field()
    web_site = Field()
    rating = Field()
    votes = Field()
    category = Field()
    
    
        