import os
import platform
from fastapi import FastAPI
from playwright.async_api import async_playwright

app = FastAPI()
# Check if we're running on Render or a server-like environment

# Load environment variables
USER_AGENT = os.getenv("SCRAPER_USER_AGENT", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

async def scrape_data():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True, 
            args=["--no-sandbox", "--disable-setuid-sandbox"]
        )
        page = await browser.new_page()

        # Set the User-Agent dynamically from environment variables
        await page.set_extra_http_headers({"User-Agent": USER_AGENT})

        await page.goto("https://socolivesq.com/", timeout=120000)
        await page.wait_for_selector(".hot-content.all-content li", timeout=25000)

        scraped_data = await page.evaluate('''
            () => {
                let data = [];
                document.querySelectorAll('.hot-content.all-content li').forEach(item => {
                    let matchLink = item.querySelector('a')?.href || '';
                    let imageUrl = item.querySelector('img.fm.live-cover')?.getAttribute('data-src') || '';
                    let streamerName = item.querySelector('.bottom-title .name')?.innerText.trim() || 'Unknown';
                    let viewerCount = item.querySelector('.bottom-title .num span')?.innerText.trim() || '0';
                    let matchTitle = item.querySelector('h4.ellipsis')?.innerText.trim() || 'No Title';

                    data.push({ matchLink, imageUrl, streamerName, viewerCount, matchTitle });
                });
                return data;
            }
        ''')

        await browser.close()
        return scraped_data

@app.get("/scrape")
async def get_scraped_data():
    try:
        data = await scrape_data()
        return {"data": data}
    except Exception as e:
        return {"error": "Scraping failed", "details": str(e)}
