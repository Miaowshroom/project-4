import scrapy
from scrapy.selector import Selector
import os
from selenium import webdriver
from time import sleep
from datajob.items import DatajobItem

class DatajobSpider(scrapy.Spider):
    name = "datajob"
    allowed_domains = ["mycareersfuture.sg"]
    start_urls = [
        "https://www.mycareersfuture.sg/search?search=data&sortBy=new_posting_date&page=0"
    ]


    def __init__(self):
        self.masterpage = "https://www.mycareersfuture.sg"
        chromedriver = "D:\GA\project_submission\project-4\chromedriver\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(executable_path="D:\GA\project_submission\project-4\chromedriver\chromedriver.exe")
        self.search_url_base = "https://www.mycareersfuture.sg/search?search=data&sortBy=new_posting_date&page="

    def parse(self, response):
        items = []
        page_current = 0
        stop = False
        while ((not stop) | (page_current<3)) :
            
            self.driver.get(self.search_url_base + str(page_current))
            sleep(4)
            links = Selector(text=self.driver.page_source).xpath('//div[contains(@id, "job-card-")]/div/a/@href').extract()
            if len(links)==0:
            	stop = True
            	break

            for page in links:
                self.driver.get(self.masterpage+page)
                sleep(4)
                item = DatajobItem()
                try:
                    item['job_link'] = self.masterpage+page
                    item['company_name'] = Selector(text=self.driver.page_source).xpath('//p[@name="company"]/text()').extract()
                    item['job_title'] = Selector(text=self.driver.page_source).xpath('//*[@id="job_title"]/text()').extract()
                    item['job_location'] = Selector(text=self.driver.page_source).xpath('//p[@id="address"]/a/text()').extract()
                    item['job_type'] = Selector(text=self.driver.page_source).xpath('//p[@id="employment_type"]/text()').extract()
                    item['job_level'] = Selector(text=self.driver.page_source).xpath('//p[@id="seniority"]/text()').extract()
                    item['job_experience'] = Selector(text=self.driver.page_source).xpath('//p[@id="min_experience"]/text()').extract()
                    item['job_categories'] = Selector(text=self.driver.page_source).xpath('//p[@id="job-categories"]/text()').extract()
                    item['job_salaries_min'] = Selector(text=self.driver.page_source).xpath('//span[@class="dib"]/text()').extract()[0]
                    item['job_salaries_max'] = Selector(text=self.driver.page_source).xpath('//span[@class="dib"]/text()').extract()[1]
                    item['job_salaries_type'] = Selector(text=self.driver.page_source).xpath('//span[contains(@class,"salary_type")]/text()').extract()[0]
                    job_role_resp = Selector(text=self.driver.page_source).xpath('//div[@id="description-content"]//text()').extract()
                    item['job_role_resp'] = [ele.strip() for ele in job_role_resp if ele.strip() !='']
                    job_requirement = Selector(text=self.driver.page_source).xpath('//div[@id="requirements-content"]//text()').extract()
                    item['job_requirement'] = [ele.strip() for ele in job_requirement if ele.strip() !='']
                    item['job_skills'] = Selector(text=self.driver.page_source).xpath('//label[contains(@class, "br-pill")]/text()').extract()
                    items.append(item)

                except:
                    pass

            page_current +=1

        return items
