import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()

    page = await browser.newPage()

    await page.goto("youtube.com")

    await page.reload()
    await page.screenshot({'path': "screenshot.png"})

    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())