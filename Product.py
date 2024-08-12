from playwright.async_api import async_playwright
import asyncio

class product:
    def __init__(self,baseUrl):
        self.url = "https://www.drmartens.com.au/"+str(baseUrl)+".html"
        print(self.url)
        
    def getUrl(self):
        return self.url

    def getStock(self):
        asyncio.run(self.getSampleCodes()) 

    async def getSampleCodes(self):
        #tf = tempfile.NamedTemporaryFile(suffix='.png')
        
        async with async_playwright() as p:
            for browser_type in [p.webkit]:
                browser = await browser_type.launch()

                page = await browser.new_page()
                await page.goto('https://www.drmartens.com.au/kids-junior-1460-softy-t-15382001-blk.html#93=4702')
                #content = await page.content()
                await page.screenshot(path="screenshot.png")
                await browser.close()

                return "epic"
        
        #async with async_playwright() as p:
        #    for browser_type in [p.webkit]:
        #        browser = await browser_type.launch()

        #        page = await browser.new_page()
        #        await page.goto(self.url)
        #        content = await page.content()
        #        await page.screenshot()

        #        await browser.close()