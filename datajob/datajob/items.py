# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DatajobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_link = scrapy.Field()
    company_name = scrapy.Field()
    job_title = scrapy.Field()
    job_location = scrapy.Field()
    job_type = scrapy.Field()
    job_level = scrapy.Field()
    job_experience = scrapy.Field()
    job_categories = scrapy.Field()
    job_salaries_min = scrapy.Field()
    job_salaries_max = scrapy.Field()
    job_salaries_type = scrapy.Field()
    job_role_resp = scrapy.Field()
    job_requirement = scrapy.Field()
    job_skills = scrapy.Field()
