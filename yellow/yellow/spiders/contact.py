# -*- coding: utf-8 -*-
import scrapy
import urlparse
from yellow.items import ContactItem, AddressItem
import yellow.settings


class ContactSpider(scrapy.Spider):
    name = "contacts"
    allowed_domains = ["seccionamarilla.com.mx"]
    def __init__(self, category='medicos', state=''):
        self.start_urls = []
        for state in yellow.settings.MX_STATES:
            self.start_urls.append('http://www.seccionamarilla.com.mx/resultados/%s/%s/1' % (category, state))

    def parse(self, response):
        for card in response.css('.vcard'):
                
            address = AddressItem()
            str_address = ''.join(card.css('.street-address::text').extract()).strip().split(',');
            for i in range(0, len(str_address)):
                if i == 0:
                    address['street'] = str_address[i].strip()
                elif i == 1:
                    address['neighborhood'] = str_address[i].strip()       
                else:
                    address['municipality'] = str_address[i].strip()
            
            address['postal_code'] = ''.join(card.css('.postal-code::text').extract()).strip()
            address['state'] = ''.join(card.css('.locality').xpath('acronym/@title').extract())

            contact = ContactItem()
            contact['name'] = ''.join(card.css('.org').xpath('a/text()').extract()).strip()
            contact['phone'] = ''.join(card.css('.phone-number').xpath('span/text()').extract())
            contact['category'] = ''.join(card.css('.category::text').extract()).strip()
            contact['web_site'] = ''.join(card.css('.url::text').extract())
            contact['address'] = dict(address)
            
            contact['rating'] = ''.join(card.css('.rating').xpath('@class').extract()).replace('rating star', '')
            contact['votes'] = ''.join(card.css('.votes::text').extract())

            full_info = ''.join(card.css('.mas_info').xpath('@href').extract())
            if (len(full_info) > 0):
                request = scrapy.Request(full_info, callback=self.parse_full_contact)
                request.meta['contact'] = contact
                yield request
            else:
                yield contact

        link = response.css('.icon.next').xpath('@href').extract()[0]
        url = urlparse.urljoin('http://www.seccionamarilla.com.mx', link)
        yield scrapy.Request(url, callback=self.parse)

    def parse_full_contact(self, response):
        contact = response.request.meta['contact']

        contact['email'] = ''.join(response.xpath('//a[contains(@href, "mailto")]/@href').extract()).replace('mailto:', '')
        contact['web_site'] = ''.join(response.css('.super_pagina').xpath('@href').extract())
        contact['services'] = response.css('.servicios').xpath('ul/li/text()').extract()
        
        yield contact

