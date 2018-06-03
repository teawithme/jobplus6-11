# -*- coding: utf-8 -*-

import scrapy

class JobsSpider(scrapy.Spider):
    name = 'jobs'

    start_urls = ['https://segmentfault.com/jobs']

    def parse(self, response):
        for job in response.css('div.job-list-item-block')[0:10]:
            yield {
                'title': job.xpath('.//a[@class="job-name nowrap"]/text()').extract_first().strip(),
                'location': job.xpath('.//span[@class="text-muted job-list-item-block-city"]/text()').extract_first().strip(),
                'experience': job.xpath('.//div[@class="text-muted job-require"]').extract_first().split('/')[2].strip(),
                'salary': job.xpath('.//div[@class="text-muted job-require"]/strong/text()').extract_first().strip()
            }
