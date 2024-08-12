import asyncio
from playwright.async_api import async_playwright
import re
from Product import product as PRODUCT

class catalog:
    def __init__(self):
        #webdata = self.main()
        self.products = self.buildCatalog()

    def stockEnquiry(self,id):
        if (id in self.products):
            return self.products[id].getStock()
        else:
            return None

    def getLink(self,code):
        if str(code) in self.products:
            page = "https://www.drmartens.com.au/" + str(self.products[code]) + ".html"
        else:
            page = None
        return page
    
    async def main(self):
        async with async_playwright() as p:
            for browser_type in [p.webkit]:
                browser = await browser_type.launch()

                page = await browser.new_page()
                await page.goto('https://www.drmartens.com.au/media/sitemap_docau.xml')
                content = await page.content()

                await browser.close()
                return content

    def buildCatalog(self):
        catalog = []
        disc = {}

        with open('catalog.html','r') as file: 
            for line in file:     
                for link in line.split("https://www.drmartens.com.au"):    
                    for htmlPage in link.split(".html"):
                        if (len(htmlPage) < 100):
                            product = htmlPage.split("/")
                            catalog.append(product[len(product) - 1])

        for validProduct in catalog:
            product = validProduct.split("-")
            if (len(product[len(product) - 2]) == 8):
                disc[product[len(product) - 2]] = PRODUCT(validProduct)

        return disc

cat = catalog()
cat.stockEnquiry("22695001")