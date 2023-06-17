import scrapy
import csv


class RimSpider(scrapy.Spider):
    name = "rim"
    allowed_domains = ["rim.org.ru"]
    start_urls = ["https://rim.org.ru/catalog/tyunery-t2/"]

    def parse(self, response):
        # Парсинг категорий
        categories = response.css('ul.navbar-nav > li > a::attr(href)').getall()
        for category_url in categories:
            yield response.follow(category_url, callback=self.parse_category)

    def parse_category(self, response):
        products = response.css('div.product-thumb')
        for product in products:
            # Извлечение данных о товаре внутри категории
            name = product.css('.product-thumb .caption > a::text').get()
            category = product.css('.nav > li ul li a::text').get()
            price = product.css('.product-thumb .price::text').get()
            link = response.urljoin(product.css('.product-thumb .caption > a::attr(href)').get())
            if price is None:
                price = 'Нет цены'

            yield {
                'Название': name,
                'Категория': category,
                'Цена': price,
                'Ссылка': link
            }

        # Переход к следующей странице категории, если есть
        next_page = response.css('ul.pagination li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_category)

    def closed(self, reason):
        # Сохранение данных в CSV-файл
        items = self.crawler.stats.get_value('item_scraped_count')
        if items:
            filename = "products.csv"
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['Название', 'Категория', 'Цена', 'Ссылка'])
                writer.writeheader()
                writer.writerows(self.items)
            self.logger.info(f"Сбор данных завершен. Результат сохранен в {filename}.")
