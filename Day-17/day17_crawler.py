import asyncio
from crawl4ai import AsyncWebCrawler , CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy

async def main():
    #Configure the 2-level deep crawl
    config = CrawlerRunConfig(
        deep_crawl_strategy = BFSDeepCrawlStrategy(max_depth=1 , include_external=False , max_pages=150),
        scraping_strategy = LXMLWebScrapingStrategy(),
        verbose=True
    )

    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun("https://www.wikipedia.org", config=config)
        print(f"Crawled {len(results)} pages in total")
        for result in results[:5]:
            print(f"URL: {result.url}")
            print(f"Depth: {result.metadata.get('depth',0)}")

if __name__ == "__main__":
    asyncio.run(main())

##OUTPUT : 
# PS C:\Users\Admin\Desktop\GeekForGeeks\Projects\Day-17> python day17_crawler.py
# [INIT].... → Crawl4AI 0.7.4 
# [FETCH]... ↓ https://www.wikipedia.org                                                                            | ✓ | ⏱: 1.60s 
# [SCRAPE].. ◆ https://www.wikipedia.org                                                                            | ✓ | ⏱: 0.27s 
# [COMPLETE] ● https://www.wikipedia.org                                                                            | ✓ | ⏱: 1.88s 
# [FETCH]... ↓ https://bg.wikipedia.org                                                                             | ✓ | ⏱: 1.97s 
# [SCRAPE].. ◆ https://bg.wikipedia.org                                                                             | ✓ | ⏱: 0.55s 
# [COMPLETE] ● https://bg.wikipedia.org                                                                             | ✓ | ⏱: 2.54s 
# [FETCH]... ↓ https://ba.wikipedia.org                                                                             | ✓ | ⏱: 9.76s 
# [SCRAPE].. ◆ https://ba.wikipedia.org                                                                             | ✓ | ⏱: 0.51s 
# [COMPLETE] ● https://ba.wikipedia.org                                                                             | ✓ | ⏱: 10.28s 
# [FETCH]... ↓ https://ace.wikipedia.org                                                                            | ✓ | ⏱: 10.61s 
# [SCRAPE].. ◆ https://ace.wikipedia.org                                                                            | ✓ | ⏱: 0.75s 
# [COMPLETE] ● https://ace.wikipedia.org                                                                            | ✓ | ⏱: 11.37s 
# [FETCH]... ↓ https://an.wikipedia.org                                                                             | ✓ | ⏱: 12.01s 
# [SCRAPE].. ◆ https://an.wikipedia.org                                                                             | ✓ | ⏱: 0.74s 
# [COMPLETE] ● https://an.wikipedia.org                                                                             | ✓ | ⏱: 12.76s 
# [FETCH]... ↓ https://bpy.wikipedia.org                                                                            | ✓ | ⏱: 2.26s 
# [SCRAPE].. ◆ https://bpy.wikipedia.org                                                                            | ✓ | ⏱: 0.47s 
# [COMPLETE] ● https://bpy.wikipedia.org                                                                            | ✓ | ⏱: 2.77s 
# [FETCH]... ↓ https://br.wikipedia.org                                                                             | ✓ | ⏱: 2.56s 
# [SCRAPE].. ◆ https://br.wikipedia.org                                                                             | ✓ | ⏱: 0.41s 
# [COMPLETE] ● https://br.wikipedia.org                                                                             | ✓ | ⏱: 2.98s 
# [FETCH]... ↓ https://bs.wikipedia.org                                                                             | ✓ | ⏱: 1.66s 
# [SCRAPE].. ◆ https://bs.wikipedia.org                                                                             | ✓ | ⏱: 0.22s 
# [COMPLETE] ● https://bs.wikipedia.org                                                                             | ✓ | ⏱: 1.89s 
# [FETCH]... ↓ https://am.wikipedia.org                                                                             | ✓ | ⏱: 16.13s 
# [SCRAPE].. ◆ https://am.wikipedia.org                                                                             | ✓ | ⏱: 0.40s 
# [COMPLETE] ● https://am.wikipedia.org                                                                             | ✓ | ⏱: 16.54s 
# [FETCH]... ↓ https://af.wikipedia.org                                                                             | ✓ | ⏱: 16.64s 
# [SCRAPE].. ◆ https://af.wikipedia.org                                                                             | ✓ | ⏱: 0.33s 
# [COMPLETE] ● https://af.wikipedia.org                                                                             | ✓ | ⏱: 16.98s 
# [FETCH]... ↓ https://ar.wikipedia.org                                                                             | ✓ | ⏱: 16.98s 
# [SCRAPE].. ◆ https://ar.wikipedia.org                                                                             | ✓ | ⏱: 0.27s 
# [COMPLETE] ● https://ar.wikipedia.org                                                                             | ✓ | ⏱: 17.26s 
# [FETCH]... ↓ https://bjn.wikipedia.org                                                                            | ✓ | ⏱: 14.70s 
# [SCRAPE].. ◆ https://bjn.wikipedia.org                                                                            | ✓ | ⏱: 0.74s 
# [COMPLETE] ● https://bjn.wikipedia.org                                                                            | ✓ | ⏱: 15.46s 
# [FETCH]... ↓ https://bar.wikipedia.org                                                                            | ✓ | ⏱: 18.55s 
# [SCRAPE].. ◆ https://bar.wikipedia.org                                                                            | ✓ | ⏱: 0.23s 
# [COMPLETE] ● https://bar.wikipedia.org                                                                            | ✓ | ⏱: 18.80s 
# [FETCH]... ↓ https://ast.wikipedia.org                                                                            | ✓ | ⏱: 18.88s 
# [SCRAPE].. ◆ https://ast.wikipedia.org                                                                            | ✓ | ⏱: 0.58s 
# [COMPLETE] ● https://ast.wikipedia.org                                                                            | ✓ | ⏱: 19.48s 
# [FETCH]... ↓ https://ban.wikipedia.org                                                                            | ✓ | ⏱: 19.53s 
# [SCRAPE].. ◆ https://ban.wikipedia.org                                                                            | ✓ | ⏱: 1.02s 
# [COMPLETE] ● https://ban.wikipedia.org                                                                            | ✓ | ⏱: 20.57s 
# [FETCH]... ↓ https://be-tarask.wikipedia.org                                                                      | ✓ | ⏱: 21.42s 
# [SCRAPE].. ◆ https://be-tarask.wikipedia.org                                                                      | ✓ | ⏱: 0.48s 
# [COMPLETE] ● https://be-tarask.wikipedia.org                                                                      | ✓ | ⏱: 21.93s 
# [FETCH]... ↓ https://bn.wikipedia.org                                                                             | ✓ | ⏱: 12.03s 
# [SCRAPE].. ◆ https://bn.wikipedia.org                                                                             | ✓ | ⏱: 0.65s 
# [COMPLETE] ● https://bn.wikipedia.org                                                                             | ✓ | ⏱: 12.70s 
# [FETCH]... ↓ https://as.wikipedia.org                                                                             | ✓ | ⏱: 23.33s 
# [SCRAPE].. ◆ https://as.wikipedia.org                                                                             | ✓ | ⏱: 1.11s 
# [COMPLETE] ● https://as.wikipedia.org                                                                             | ✓ | ⏱: 24.45s 
# [FETCH]... ↓ https://azb.wikipedia.org                                                                            | ✓ | ⏱: 24.88s 
# [SCRAPE].. ◆ https://azb.wikipedia.org                                                                            | ✓ | ⏱: 0.60s 
# [COMPLETE] ● https://azb.wikipedia.org                                                                            | ✓ | ⏱: 25.50s 
# [FETCH]... ↓ https://avk.wikipedia.org                                                                            | ✓ | ⏱: 26.09s 
# [SCRAPE].. ◆ https://avk.wikipedia.org                                                                            | ✓ | ⏱: 1.07s 
# [COMPLETE] ● https://avk.wikipedia.org                                                                            | ✓ | ⏱: 27.19s 
# [FETCH]... ↓ https://arz.wikipedia.org                                                                            | ✓ | ⏱: 27.54s 
# [SCRAPE].. ◆ https://arz.wikipedia.org                                                                            | ✓ | ⏱: 0.80s 
# [COMPLETE] ● https://arz.wikipedia.org                                                                            | ✓ | ⏱: 28.35s 
# [FETCH]... ↓ https://be.wikipedia.org                                                                             | ✓ | ⏱: 28.41s 
# [SCRAPE].. ◆ https://be.wikipedia.org                                                                             | ✓ | ⏱: 0.33s 
# [COMPLETE] ● https://be.wikipedia.org                                                                             | ✓ | ⏱: 28.75s 
# [FETCH]... ↓ https://az.wikipedia.org                                                                             | ✓ | ⏱: 28.82s 
# [SCRAPE].. ◆ https://az.wikipedia.org                                                                             | ✓ | ⏱: 0.72s 
# [COMPLETE] ● https://az.wikipedia.org                                                                             | ✓ | ⏱: 29.55s 
# [FETCH]... ↓ https://bcl.wikipedia.org                                                                            | ✓ | ⏱: 29.71s 
# [SCRAPE].. ◆ https://bcl.wikipedia.org                                                                            | ✓ | ⏱: 0.34s 
# [COMPLETE] ● https://bcl.wikipedia.org                                                                            | ✓ | ⏱: 30.06s 
# [FETCH]... ↓ https://als.wikipedia.org                                                                            | ✓ | ⏱: 30.58s 
# [SCRAPE].. ◆ https://als.wikipedia.org                                                                            | ✓ | ⏱: 0.15s 
# [COMPLETE] ● https://als.wikipedia.org                                                                            | ✓ | ⏱: 30.75s 
# [FETCH]... ↓ https://ary.wikipedia.org                                                                            | ✓ | ⏱: 30.71s 
# [SCRAPE].. ◆ https://ary.wikipedia.org                                                                            | ✓ | ⏱: 0.32s 
# [COMPLETE] ● https://ary.wikipedia.org                                                                            | ✓ | ⏱: 31.04s 
# [FETCH]... ↓ https://ff.wikipedia.org                                                                             | ✓ | ⏱: 1.80s 
# [SCRAPE].. ◆ https://ff.wikipedia.org                                                                             | ✓ | ⏱: 0.38s 
# [COMPLETE] ● https://ff.wikipedia.org                                                                             | ✓ | ⏱: 2.19s 
# [FETCH]... ↓ https://da.wikipedia.org                                                                             | ✓ | ⏱: 5.19s 
# [SCRAPE].. ◆ https://da.wikipedia.org                                                                             | ✓ | ⏱: 0.37s 
# [COMPLETE] ● https://da.wikipedia.org                                                                             | ✓ | ⏱: 5.57s 
# [FETCH]... ↓ https://cy.wikipedia.org                                                                             | ✓ | ⏱: 6.12s 
# [SCRAPE].. ◆ https://cy.wikipedia.org                                                                             | ✓ | ⏱: 0.39s 
# [COMPLETE] ● https://cy.wikipedia.org                                                                             | ✓ | ⏱: 6.52s 
# [FETCH]... ↓ https://cdo.wikipedia.org                                                                            | ✓ | ⏱: 7.07s 
# [SCRAPE].. ◆ https://cdo.wikipedia.org                                                                            | ✓ | ⏱: 0.24s 
# [COMPLETE] ● https://cdo.wikipedia.org                                                                            | ✓ | ⏱: 7.32s 
# [FETCH]... ↓ https://cs.wikipedia.org                                                                             | ✓ | ⏱: 7.56s 
# [SCRAPE].. ◆ https://cs.wikipedia.org                                                                             | ✓ | ⏱: 0.35s 
# [COMPLETE] ● https://cs.wikipedia.org                                                                             | ✓ | ⏱: 7.92s 
# [FETCH]... ↓ https://fi.wikipedia.org                                                                             | ✓ | ⏱: 5.93s 
# [SCRAPE].. ◆ https://fi.wikipedia.org                                                                             | ✓ | ⏱: 0.31s 
# [COMPLETE] ● https://fi.wikipedia.org                                                                             | ✓ | ⏱: 6.24s 
# [FETCH]... ↓ https://fo.wikipedia.org                                                                             | ✓ | ⏱: 2.93s
# [SCRAPE].. ◆ https://fo.wikipedia.org                                                                             | ✓ | ⏱: 0.39s 
# [COMPLETE] ● https://fo.wikipedia.org                                                                             | ✓ | ⏱: 3.32s 
# [FETCH]... ↓ https://cv.wikipedia.org                                                                             | ✓ | ⏱: 9.18s 
# [SCRAPE].. ◆ https://cv.wikipedia.org                                                                             | ✓ | ⏱: 0.19s 
# [COMPLETE] ● https://cv.wikipedia.org                                                                             | ✓ | ⏱: 9.38s 
# [FETCH]... ↓ https://en.wikipedia.org                                                                             | ✓ | ⏱: 9.40s 
# [SCRAPE].. ◆ https://en.wikipedia.org                                                                             | ✓ | ⏱: 0.35s 
# [COMPLETE] ● https://en.wikipedia.org                                                                             | ✓ | ⏱: 9.76s 
# [FETCH]... ↓ https://ckb.wikipedia.org                                                                            | ✓ | ⏱: 9.83s
# [SCRAPE].. ◆ https://ckb.wikipedia.org                                                                            | ✓ | ⏱: 0.37s 
# [COMPLETE] ● https://ckb.wikipedia.org                                                                            | ✓ | ⏱: 10.21s 
# [FETCH]... ↓ https://ceb.wikipedia.org                                                                            | ✓ | ⏱: 10.23s
# [SCRAPE].. ◆ https://ceb.wikipedia.org                                                                            | ✓ | ⏱: 0.14s 
# [COMPLETE] ● https://ceb.wikipedia.org                                                                            | ✓ | ⏱: 10.38s 
# [FETCH]... ↓ https://fa.wikipedia.org                                                                             | ✓ | ⏱: 10.39s 
# [SCRAPE].. ◆ https://fa.wikipedia.org                                                                             | ✓ | ⏱: 0.29s 
# [COMPLETE] ● https://fa.wikipedia.org                                                                             | ✓ | ⏱: 10.69s 
# [FETCH]... ↓ https://eml.wikipedia.org                                                                            | ✓ | ⏱: 10.73s
# [SCRAPE].. ◆ https://eml.wikipedia.org                                                                            | ✓ | ⏱: 0.31s 
# [COMPLETE] ● https://eml.wikipedia.org                                                                            | ✓ | ⏱: 11.05s 
# [FETCH]... ↓ https://ce.wikipedia.org                                                                             | ✓ | ⏱: 11.13s
# [SCRAPE].. ◆ https://ce.wikipedia.org                                                                             | ✓ | ⏱: 0.19s 
# [COMPLETE] ● https://ce.wikipedia.org                                                                             | ✓ | ⏱: 11.33s 
# [FETCH]... ↓ https://el.wikipedia.org                                                                             | ✓ | ⏱: 11.26s
# [SCRAPE].. ◆ https://el.wikipedia.org                                                                             | ✓ | ⏱: 0.30s 
# [COMPLETE] ● https://el.wikipedia.org                                                                             | ✓ | ⏱: 11.57s 
# [FETCH]... ↓ https://es.wikipedia.org                                                                             | ✓ | ⏱: 11.80s 
# [SCRAPE].. ◆ https://es.wikipedia.org                                                                             | ✓ | ⏱: 0.22s 
# [COMPLETE] ● https://es.wikipedia.org                                                                             | ✓ | ⏱: 12.03s 
# [FETCH]... ↓ https://dag.wikipedia.org                                                                            | ✓ | ⏱: 12.09s 
# [SCRAPE].. ◆ https://dag.wikipedia.org                                                                            | ✓ | ⏱: 0.31s 
# [COMPLETE] ● https://dag.wikipedia.org                                                                            | ✓ | ⏱: 12.41s 
# [FETCH]... ↓ https://de.wikipedia.org                                                                             | ✓ | ⏱: 12.46s 
# [SCRAPE].. ◆ https://de.wikipedia.org                                                                             | ✓ | ⏱: 0.15s 
# [COMPLETE] ● https://de.wikipedia.org                                                                             | ✓ | ⏱: 12.62s 
# [FETCH]... ↓ https://et.wikipedia.org                                                                             | ✓ | ⏱: 12.65s 
# [SCRAPE].. ◆ https://et.wikipedia.org                                                                             | ✓ | ⏱: 0.34s 
# [COMPLETE] ● https://et.wikipedia.org                                                                             | ✓ | ⏱: 12.99s 
# [FETCH]... ↓ https://eu.wikipedia.org                                                                             | ✓ | ⏱: 13.07s 
# [SCRAPE].. ◆ https://eu.wikipedia.org                                                                             | ✓ | ⏱: 0.36s 
# [COMPLETE] ● https://eu.wikipedia.org                                                                             | ✓ | ⏱: 13.44s 
# [FETCH]... ↓ https://eo.wikipedia.org                                                                             | ✓ | ⏱: 13.46s
# [SCRAPE].. ◆ https://eo.wikipedia.org                                                                             | ✓ | ⏱: 0.41s 
# [COMPLETE] ● https://eo.wikipedia.org                                                                             | ✓ | ⏱: 13.88s 
# [FETCH]... ↓ https://ca.wikipedia.org                                                                             | ✓ | ⏱: 14.01s 
# [SCRAPE].. ◆ https://ca.wikipedia.org                                                                             | ✓ | ⏱: 0.42s 
# [COMPLETE] ● https://ca.wikipedia.org                                                                             | ✓ | ⏱: 14.45s 
# [FETCH]... ↓ https://fr.wikipedia.org                                                                             | ✓ | ⏱: 8.10s 
# [SCRAPE].. ◆ https://fr.wikipedia.org                                                                             | ✓ | ⏱: 0.39s 
# [COMPLETE] ● https://fr.wikipedia.org                                                                             | ✓ | ⏱: 8.49s 
# [FETCH]... ↓ https://ia.wikipedia.org                                                                             | ✓ | ⏱: 1.77s 
# [SCRAPE].. ◆ https://ia.wikipedia.org                                                                             | ✓ | ⏱: 0.36s 
# [COMPLETE] ● https://ia.wikipedia.org                                                                             | ✓ | ⏱: 2.15s 
# [FETCH]... ↓ https://id.wikipedia.org                                                                             | ✓ | ⏱: 7.87s 
# [SCRAPE].. ◆ https://id.wikipedia.org                                                                             | ✓ | ⏱: 0.84s 
# [COMPLETE] ● https://id.wikipedia.org                                                                             | ✓ | ⏱: 8.73s 
# [FETCH]... ↓ https://frr.wikipedia.org                                                                            | ✓ | ⏱: 12.88s 
# [SCRAPE].. ◆ https://frr.wikipedia.org                                                                            | ✓ | ⏱: 1.01s 
# [COMPLETE] ● https://frr.wikipedia.org                                                                            | ✓ | ⏱: 13.91s 
# [FETCH]... ↓ https://hyw.wikipedia.org                                                                            | ✓ | ⏱: 21.81s 
# [SCRAPE].. ◆ https://hyw.wikipedia.org                                                                            | ✓ | ⏱: 1.74s 
# [COMPLETE] ● https://hyw.wikipedia.org                                                                            | ✓ | ⏱: 23.56s 
# [FETCH]... ↓ https://gu.wikipedia.org                                                                             | ✓ | ⏱: 30.98s 
# [SCRAPE].. ◆ https://gu.wikipedia.org                                                                             | ✓ | ⏱: 1.38s 
# [COMPLETE] ● https://gu.wikipedia.org                                                                             | ✓ | ⏱: 32.42s 
# [FETCH]... ↓ https://ig.wikipedia.org                                                                             | ✓ | ⏱: 20.64s 
# [SCRAPE].. ◆ https://ig.wikipedia.org                                                                             | ✓ | ⏱: 1.44s 
# [COMPLETE] ● https://ig.wikipedia.org                                                                             | ✓ | ⏱: 22.14s 
# [FETCH]... ↓ https://io.wikipedia.org                                                                             | ✓ | ⏱: 4.34s 
# [SCRAPE].. ◆ https://io.wikipedia.org                                                                             | ✓ | ⏱: 2.19s 
# [COMPLETE] ● https://io.wikipedia.org                                                                             | ✓ | ⏱: 6.61s 
# [FETCH]... ↓ https://ilo.wikipedia.org                                                                            | ✓ | ⏱: 15.59s 
# [SCRAPE].. ◆ https://ilo.wikipedia.org                                                                            | ✓ | ⏱: 0.47s 
# [COMPLETE] ● https://ilo.wikipedia.org                                                                            | ✓ | ⏱: 16.18s 
# [FETCH]... ↓ https://hak.wikipedia.org                                                                            | ✓ | ⏱: 43.40s 
# [SCRAPE].. ◆ https://hak.wikipedia.org                                                                            | ✓ | ⏱: 0.92s 
# [COMPLETE] ● https://hak.wikipedia.org                                                                            | ✓ | ⏱: 44.34s 
# [FETCH]... ↓ https://gl.wikipedia.org                                                                             | ✓ | ⏱: 44.47s 
# [SCRAPE].. ◆ https://gl.wikipedia.org                                                                             | ✓ | ⏱: 0.44s 
# [COMPLETE] ● https://gl.wikipedia.org                                                                             | ✓ | ⏱: 44.95s 
# [FETCH]... ↓ https://hif.wikipedia.org                                                                            | ✓ | ⏱: 45.01s 
# [SCRAPE].. ◆ https://hif.wikipedia.org                                                                            | ✓ | ⏱: 1.00s 
# [COMPLETE] ● https://hif.wikipedia.org                                                                            | ✓ | ⏱: 46.02s 
# [FETCH]... ↓ https://hu.wikipedia.org                                                                             | ✓ | ⏱: 46.09s 
# [SCRAPE].. ◆ https://hu.wikipedia.org                                                                             | ✓ | ⏱: 1.10s 
# [COMPLETE] ● https://hu.wikipedia.org                                                                             | ✓ | ⏱: 47.35s 
# [FETCH]... ↓ https://hsb.wikipedia.org                                                                            | ✓ | ⏱: 48.13s 
# [SCRAPE].. ◆ https://hsb.wikipedia.org                                                                            | ✓ | ⏱: 0.67s 
# [COMPLETE] ● https://hsb.wikipedia.org                                                                            | ✓ | ⏱: 48.91s 
# [FETCH]... ↓ https://ga.wikipedia.org                                                                             | ✓ | ⏱: 49.67s 
# [SCRAPE].. ◆ https://ga.wikipedia.org                                                                             | ✓ | ⏱: 1.67s 
# [COMPLETE] ● https://ga.wikipedia.org                                                                             | ✓ | ⏱: 51.39s 
# [FETCH]... ↓ https://glk.wikipedia.org                                                                            | ✓ | ⏱: 52.04s 
# [SCRAPE].. ◆ https://glk.wikipedia.org                                                                            | ✓ | ⏱: 1.90s 
# [COMPLETE] ● https://glk.wikipedia.org                                                                            | ✓ | ⏱: 53.96s 
# [FETCH]... ↓ https://gd.wikipedia.org                                                                             | ✓ | ⏱: 57.36s 
# [SCRAPE].. ◆ https://gd.wikipedia.org                                                                             | ✓ | ⏱: 1.22s 
# [COMPLETE] ● https://gd.wikipedia.org                                                                             | ✓ | ⏱: 58.64s 
# [FETCH]... ↓ https://hy.wikipedia.org                                                                             | ✓ | ⏱: 59.76s 
# [SCRAPE].. ◆ https://hy.wikipedia.org                                                                             | ✓ | ⏱: 0.91s 
# [COMPLETE] ● https://hy.wikipedia.org                                                                             | ✓ | ⏱: 60.68s 
# [FETCH]... ↓ https://hr.wikipedia.org                                                                             | ✓ | ⏱: 61.13s 
# [SCRAPE].. ◆ https://hr.wikipedia.org                                                                             | ✓ | ⏱: 0.99s 
# [COMPLETE] ● https://hr.wikipedia.org                                                                             | ✓ | ⏱: 62.14s 
# [FETCH]... ↓ https://gor.wikipedia.org                                                                            | ✓ | ⏱: 62.20s 
# [SCRAPE].. ◆ https://gor.wikipedia.org                                                                            | ✓ | ⏱: 0.90s 
# [COMPLETE] ● https://gor.wikipedia.org                                                                            | ✓ | ⏱: 63.14s 
# [FETCH]... ↓ https://ie.wikipedia.org                                                                             | ✓ | ⏱: 53.47s 
# [SCRAPE].. ◆ https://ie.wikipedia.org                                                                             | ✓ | ⏱: 1.62s 
# [COMPLETE] ● https://ie.wikipedia.org                                                                             | ✓ | ⏱: 55.12s 
# [FETCH]... ↓ https://hi.wikipedia.org                                                                             | ✓ | ⏱: 67.15s 
# [SCRAPE].. ◆ https://hi.wikipedia.org                                                                             | ✓ | ⏱: 1.90s 
# [COMPLETE] ● https://hi.wikipedia.org                                                                             | ✓ | ⏱: 69.10s 
# [FETCH]... ↓ https://ht.wikipedia.org                                                                             | ✓ | ⏱: 70.61s 
# [SCRAPE].. ◆ https://ht.wikipedia.org                                                                             | ✓ | ⏱: 1.05s 
# [COMPLETE] ● https://ht.wikipedia.org                                                                             | ✓ | ⏱: 71.69s 
# [FETCH]... ↓ https://fy.wikipedia.org                                                                             | ✓ | ⏱: 71.81s 
# [SCRAPE].. ◆ https://fy.wikipedia.org                                                                             | ✓ | ⏱: 1.01s 
# [COMPLETE] ● https://fy.wikipedia.org                                                                             | ✓ | ⏱: 72.83s 
# [FETCH]... ↓ https://ha.wikipedia.org                                                                             | ✓ | ⏱: 73.07s 
# [SCRAPE].. ◆ https://ha.wikipedia.org                                                                             | ✓ | ⏱: 2.79s 
# [COMPLETE] ● https://ha.wikipedia.org                                                                             | ✓ | ⏱: 76.01s 
# [ERROR]... × https://he.wikipedia.org                           | Error: Unexpected error in _crawl_web at line 696 in _crawl_web 
# (..\..\..\..\AppData\Local\Programs\Python\Python313\Lib\site-packages\crawl4ai\async_crawler_strategy.py):
# Error: Failed on navigating ACS-GOTO:
# Page.goto: Timeout 60000ms exceeded.
# Call log:
#   - navigating to "https://he.wikipedia.org/", waiting until "domcontentloaded"


# Code context:
#  691                               tag="GOTO",
#  692                               params={"url": url},
#  693                           )
#  694                           response = None
#  695                       else:
#  696 →                         raise RuntimeError(f"Failed on navigating ACS-GOTO:\n{str(e)}")
#  697
#  698                   await self.execute_hook(
#  699                       "after_goto", page, context=context, url=url, response=response, config=config
#  700                   )
#  701
# [FETCH]... ↓ https://it.wikipedia.org                                                                             | ✓ | ⏱: 38.32s 
# [SCRAPE].. ◆ https://it.wikipedia.org                                                                             | ✓ | ⏱: 0.98s 
# [COMPLETE] ● https://it.wikipedia.org                                                                             | ✓ | ⏱: 39.42s 
# [FETCH]... ↓ https://is.wikipedia.org                                                                             | ✓ | ⏱: 42.56s 
# [SCRAPE].. ◆ https://is.wikipedia.org                                                                             | ✓ | ⏱: 1.87s 
# [COMPLETE] ● https://is.wikipedia.org                                                                             | ✓ | ⏱: 44.47s 
# [FETCH]... ↓ https://map-bms.wikipedia.org                                                                        | ✓ | ⏱: 3.25s 
# [SCRAPE].. ◆ https://map-bms.wikipedia.org                                                                        | ✓ | ⏱: 1.38s 
# [COMPLETE] ● https://map-bms.wikipedia.org                                                                        | ✓ | ⏱: 4.66s 
# [FETCH]... ↓ https://mg.wikipedia.org                                                                             | ✓ | ⏱: 3.48s 
# [SCRAPE].. ◆ https://mg.wikipedia.org                                                                             | ✓ | ⏱: 1.84s 
# [COMPLETE] ● https://mg.wikipedia.org                                                                             | ✓ | ⏱: 5.36s 
# [FETCH]... ↓ https://ja.wikipedia.org                                                                             | ✓ | ⏱: 24.91s 
# [SCRAPE].. ◆ https://ja.wikipedia.org                                                                             | ✓ | ⏱: 1.09s 
# [COMPLETE] ● https://ja.wikipedia.org                                                                             | ✓ | ⏱: 26.07s 
# [FETCH]... ↓ https://mhr.wikipedia.org                                                                            | ✓ | ⏱: 19.79s 
# [SCRAPE].. ◆ https://mhr.wikipedia.org                                                                            | ✓ | ⏱: 2.06s 
# [COMPLETE] ● https://mhr.wikipedia.org                                                                            | ✓ | ⏱: 21.94s 
# [FETCH]... ↓ https://ku.wikipedia.org                                                                             | ✓ | ⏱: 34.56s 
# [SCRAPE].. ◆ https://ku.wikipedia.org                                                                             | ✓ | ⏱: 0.66s 
# [COMPLETE] ● https://ku.wikipedia.org                                                                             | ✓ | ⏱: 35.26s 
# [FETCH]... ↓ https://mai.wikipedia.org                                                                            | ✓ | ⏱: 35.84s 
# [SCRAPE].. ◆ https://mai.wikipedia.org                                                                            | ✓ | ⏱: 2.23s 
# [COMPLETE] ● https://mai.wikipedia.org                                                                            | ✓ | ⏱: 38.11s 
# [FETCH]... ↓ https://ky.wikipedia.org                                                                             | ✓ | ⏱: 38.88s 
# [SCRAPE].. ◆ https://ky.wikipedia.org                                                                             | ✓ | ⏱: 1.19s 
# [COMPLETE] ● https://ky.wikipedia.org                                                                             | ✓ | ⏱: 40.19s 
# [FETCH]... ↓ https://ko.wikipedia.org                                                                             | ✓ | ⏱: 40.37s 
# [SCRAPE].. ◆ https://ko.wikipedia.org                                                                             | ✓ | ⏱: 0.59s 
# [COMPLETE] ● https://ko.wikipedia.org                                                                             | ✓ | ⏱: 40.98s 
# [FETCH]... ↓ https://la.wikipedia.org                                                                             | ✓ | ⏱: 53.73s 
# [SCRAPE].. ◆ https://la.wikipedia.org                                                                             | ✓ | ⏱: 1.32s 
# [COMPLETE] ● https://la.wikipedia.org                                                                             | ✓ | ⏱: 55.07s 
# [DEBUG]... ⋯ Body visibility info: True 
# [FETCH]... ↓ https://kn.wikipedia.org                                                                             | ✓ | ⏱: 56.60s 
# [SCRAPE].. ◆ https://kn.wikipedia.org                                                                             | ✓ | ⏱: 1.44s 
# [COMPLETE] ● https://kn.wikipedia.org                                                                             | ✓ | ⏱: 58.06s 
# [FETCH]... ↓ https://lb.wikipedia.org                                                                             | ✓ | ⏱: 58.11s 
# [SCRAPE].. ◆ https://lb.wikipedia.org                                                                             | ✓ | ⏱: 0.99s 
# [COMPLETE] ● https://lb.wikipedia.org                                                                             | ✓ | ⏱: 59.14s 
# [DEBUG]... ⋯ Body visibility info: True 
# [FETCH]... ↓ https://li.wikipedia.org                                                                             | ✓ | ⏱: 59.51s 
# [SCRAPE].. ◆ https://li.wikipedia.org                                                                             | ✓ | ⏱: 2.25s 
# [COMPLETE] ● https://li.wikipedia.org                                                                             | ✓ | ⏱: 61.77s 
# [FETCH]... ↓ https://lld.wikipedia.org                                                                            | ✓ | ⏱: 62.07s 
# [SCRAPE].. ◆ https://lld.wikipedia.org                                                                            | ✓ | ⏱: 1.49s 
# [COMPLETE] ● https://lld.wikipedia.org                                                                            | ✓ | ⏱: 63.57s 
# [DEBUG]... ⋯ Body visibility info: True 
# [ERROR]... × https://kk.wikipedia.org                           | Error: Unexpected error in _crawl_web at line 696 in _crawl_web 
# (..\..\..\..\AppData\Local\Programs\Python\Python313\Lib\site-packages\crawl4ai\async_crawler_strategy.py):
# Error: Failed on navigating ACS-GOTO:
# Page.goto: Timeout 60000ms exceeded.
# Call log:
#   - navigating to "https://kk.wikipedia.org/", waiting until "domcontentloaded"


# Code context:
#  691                               tag="GOTO",
#  692                               params={"url": url},
#  693                           )
#  694                           response = None
#  695                       else:
#  696 →                         raise RuntimeError(f"Failed on navigating ACS-GOTO:\n{str(e)}")
#  697
#  698                   await self.execute_hook(
#  699                       "after_goto", page, context=context, url=url, response=response, config=config
#  700                   )
#  701
# [FETCH]... ↓ https://kaa.wikipedia.org                                                                            | ✓ | ⏱: 65.05s 
# [SCRAPE].. ◆ https://kaa.wikipedia.org                                                                            | ✓ | ⏱: 1.38s 
# [COMPLETE] ● https://kaa.wikipedia.org                                                                            | ✓ | ⏱: 66.45s 
# [ERROR]... × https://lij.wikipedia.org                          | Error: Unexpected error in _crawl_web at line 696 in _crawl_web 
# (..\..\..\..\AppData\Local\Programs\Python\Python313\Lib\site-packages\crawl4ai\async_crawler_strategy.py):
# Error: Failed on navigating ACS-GOTO:
# Page.goto: Timeout 60000ms exceeded.
# Call log:
#   - navigating to "https://lij.wikipedia.org/", waiting until "domcontentloaded"


# Code context:
#  691                               tag="GOTO",
#  692                               params={"url": url},
#  693                           )
#  694                           response = None
#  695                       else:
#  696 →                         raise RuntimeError(f"Failed on navigating ACS-GOTO:\n{str(e)}")
#  697
#  698                   await self.execute_hook(
#  699                       "after_goto", page, context=context, url=url, response=response, config=config
#  700                   )
#  701
# [FETCH]... ↓ https://ka.wikipedia.org                                                                             | ✓ | ⏱: 66.72s 
# [SCRAPE].. ◆ https://ka.wikipedia.org                                                                             | ✓ | ⏱: 1.33s 
# [COMPLETE] ● https://ka.wikipedia.org                                                                             | ✓ | ⏱: 68.07s 
# [FETCH]... ↓ https://lmo.wikipedia.org                                                                            | ✓ | ⏱: 68.32s 
# [SCRAPE].. ◆ https://lmo.wikipedia.org                                                                            | ✓ | ⏱: 0.72s 
# [COMPLETE] ● https://lmo.wikipedia.org                                                                            | ✓ | ⏱: 69.09s 
# [FETCH]... ↓ https://km.wikipedia.org                                                                             | ✓ | ⏱: 71.16s 
# [SCRAPE].. ◆ https://km.wikipedia.org                                                                             | ✓ | ⏱: 2.11s 
# [COMPLETE] ● https://km.wikipedia.org                                                                             | ✓ | ⏱: 73.34s 
# [FETCH]... ↓ https://jv.wikipedia.org                                                                             | ✓ | ⏱: 74.51s 
# [SCRAPE].. ◆ https://jv.wikipedia.org                                                                             | ✓ | ⏱: 1.62s 
# [COMPLETE] ● https://jv.wikipedia.org                                                                             | ✓ | ⏱: 76.17s 
# [FETCH]... ↓ https://lt.wikipedia.org                                                                             | ✓ | ⏱: 76.98s 
# [SCRAPE].. ◆ https://lt.wikipedia.org                                                                             | ✓ | ⏱: 0.60s 
# [COMPLETE] ● https://lt.wikipedia.org                                                                             | ✓ | ⏱: 77.65s 
# [FETCH]... ↓ https://lv.wikipedia.org                                                                             | ✓ | ⏱: 78.01s 
# [SCRAPE].. ◆ https://lv.wikipedia.org                                                                             | ✓ | ⏱: 0.50s 
# [COMPLETE] ● https://lv.wikipedia.org                                                                             | ✓ | ⏱: 78.53s 
# [FETCH]... ↓ https://os.wikipedia.org                                                                             | ✓ | ⏱: 3.21s 
# [SCRAPE].. ◆ https://os.wikipedia.org                                                                             | ✓ | ⏱: 0.56s 
# [COMPLETE] ● https://os.wikipedia.org                                                                             | ✓ | ⏱: 3.78s 
# [FETCH]... ↓ https://mn.wikipedia.org                                                                             | ✓ | ⏱: 5.56s 
# [SCRAPE].. ◆ https://mn.wikipedia.org                                                                             | ✓ | ⏱: 0.26s 
# [COMPLETE] ● https://mn.wikipedia.org                                                                             | ✓ | ⏱: 5.83s 
# [FETCH]... ↓ https://mk.wikipedia.org                                                                             | ✓ | ⏱: 8.50s 
# [SCRAPE].. ◆ https://mk.wikipedia.org                                                                             | ✓ | ⏱: 0.38s 
# [COMPLETE] ● https://mk.wikipedia.org                                                                             | ✓ | ⏱: 8.88s 
# [FETCH]... ↓ https://nv.wikipedia.org                                                                             | ✓ | ⏱: 8.85s 
# [SCRAPE].. ◆ https://nv.wikipedia.org                                                                             | ✓ | ⏱: 0.15s 
# [COMPLETE] ● https://nv.wikipedia.org                                                                             | ✓ | ⏱: 9.00s 
# [FETCH]... ↓ https://my.wikipedia.org                                                                             | ✓ | ⏱: 9.20s 
# [SCRAPE].. ◆ https://my.wikipedia.org                                                                             | ✓ | ⏱: 0.25s 
# [COMPLETE] ● https://my.wikipedia.org                                                                             | ✓ | ⏱: 9.46s 
# [FETCH]... ↓ https://min.wikipedia.org                                                                            | ✓ | ⏱: 9.69s 
# [SCRAPE].. ◆ https://min.wikipedia.org                                                                            | ✓ | ⏱: 0.34s 
# [COMPLETE] ● https://min.wikipedia.org                                                                            | ✓ | ⏱: 10.04s 
# [FETCH]... ↓ https://pa.wikipedia.org                                                                             | ✓ | ⏱: 6.46s 
# [SCRAPE].. ◆ https://pa.wikipedia.org                                                                             | ✓ | ⏱: 0.36s 
# [COMPLETE] ● https://pa.wikipedia.org                                                                             | ✓ | ⏱: 6.83s 
# [FETCH]... ↓ https://nl.wikipedia.org                                                                             | ✓ | ⏱: 10.73s 
# [SCRAPE].. ◆ https://nl.wikipedia.org                                                                             | ✓ | ⏱: 0.39s 
# [COMPLETE] ● https://nl.wikipedia.org                                                                             | ✓ | ⏱: 11.13s 
# [FETCH]... ↓ https://no.wikipedia.org                                                                             | ✓ | ⏱: 11.14s 
# [SCRAPE].. ◆ https://no.wikipedia.org                                                                             | ✓ | ⏱: 0.32s 
# [COMPLETE] ● https://no.wikipedia.org                                                                             | ✓ | ⏱: 11.46s 
# [FETCH]... ↓ https://ne.wikipedia.org                                                                             | ✓ | ⏱: 11.50s
# [SCRAPE].. ◆ https://ne.wikipedia.org                                                                             | ✓ | ⏱: 0.37s 
# [COMPLETE] ● https://ne.wikipedia.org                                                                             | ✓ | ⏱: 11.88s 
# [FETCH]... ↓ https://oc.wikipedia.org                                                                             | ✓ | ⏱: 12.07s 
# [SCRAPE].. ◆ https://oc.wikipedia.org                                                                             | ✓ | ⏱: 0.36s 
# [COMPLETE] ● https://oc.wikipedia.org                                                                             | ✓ | ⏱: 12.43s 
# [FETCH]... ↓ https://pam.wikipedia.org                                                                            | ✓ | ⏱: 6.79s 
# [SCRAPE].. ◆ https://pam.wikipedia.org                                                                            | ✓ | ⏱: 0.18s 
# [COMPLETE] ● https://pam.wikipedia.org                                                                            | ✓ | ⏱: 6.98s 
# [FETCH]... ↓ https://nds.wikipedia.org                                                                            | ✓ | ⏱: 12.79s 
# [SCRAPE].. ◆ https://nds.wikipedia.org                                                                            | ✓ | ⏱: 0.17s 
# [COMPLETE] ● https://nds.wikipedia.org                                                                            | ✓ | ⏱: 12.97s 
# [FETCH]... ↓ https://mzn.wikipedia.org                                                                            | ✓ | ⏱: 13.14s 
# [SCRAPE].. ◆ https://mzn.wikipedia.org                                                                            | ✓ | ⏱: 0.16s 
# [COMPLETE] ● https://mzn.wikipedia.org                                                                            | ✓ | ⏱: 13.32s 
# [FETCH]... ↓ https://nap.wikipedia.org                                                                            | ✓ | ⏱: 13.39s 
# [SCRAPE].. ◆ https://nap.wikipedia.org                                                                            | ✓ | ⏱: 0.37s 
# [COMPLETE] ● https://nap.wikipedia.org                                                                            | ✓ | ⏱: 13.77s 
# [FETCH]... ↓ https://or.wikipedia.org                                                                             | ✓ | ⏱: 13.75s 
# [SCRAPE].. ◆ https://or.wikipedia.org                                                                             | ✓ | ⏱: 0.31s 
# [COMPLETE] ● https://or.wikipedia.org                                                                             | ✓ | ⏱: 14.07s 
# [FETCH]... ↓ https://mrj.wikipedia.org                                                                            | ✓ | ⏱: 14.40s 
# [SCRAPE].. ◆ https://mrj.wikipedia.org                                                                            | ✓ | ⏱: 0.34s 
# [COMPLETE] ● https://mrj.wikipedia.org                                                                            | ✓ | ⏱: 14.75s 
# [FETCH]... ↓ https://new.wikipedia.org                                                                            | ✓ | ⏱: 15.14s 
# [SCRAPE].. ◆ https://new.wikipedia.org                                                                            | ✓ | ⏱: 0.43s 
# [COMPLETE] ● https://new.wikipedia.org                                                                            | ✓ | ⏱: 15.58s 
# [FETCH]... ↓ https://ms.wikipedia.org                                                                             | ✓ | ⏱: 15.68s 
# [SCRAPE].. ◆ https://ms.wikipedia.org                                                                             | ✓ | ⏱: 0.49s 
# [COMPLETE] ● https://ms.wikipedia.org                                                                             | ✓ | ⏱: 16.19s 
# [FETCH]... ↓ https://nn.wikipedia.org                                                                             | ✓ | ⏱: 16.39s 
# [SCRAPE].. ◆ https://nn.wikipedia.org                                                                             | ✓ | ⏱: 0.61s 
# [COMPLETE] ● https://nn.wikipedia.org                                                                             | ✓ | ⏱: 17.03s 
# [FETCH]... ↓ https://pl.wikipedia.org                                                                             | ✓ | ⏱: 8.70s 
# [SCRAPE].. ◆ https://pl.wikipedia.org                                                                             | ✓ | ⏱: 0.20s 
# [COMPLETE] ● https://pl.wikipedia.org                                                                             | ✓ | ⏱: 8.93s 
# [FETCH]... ↓ https://pms.wikipedia.org                                                                            | ✓ | ⏱: 8.67s
# [SCRAPE].. ◆ https://pms.wikipedia.org                                                                            | ✓ | ⏱: 0.23s 
# [COMPLETE] ● https://pms.wikipedia.org                                                                            | ✓ | ⏱: 8.90s 
# [FETCH]... ↓ https://mr.wikipedia.org                                                                             | ✓ | ⏱: 18.16s 
# [SCRAPE].. ◆ https://mr.wikipedia.org                                                                             | ✓ | ⏱: 1.57s 
# [COMPLETE] ● https://mr.wikipedia.org                                                                             | ✓ | ⏱: 19.81s 
# [FETCH]... ↓ https://tt.wikipedia.org                                                                             | ✓ | ⏱: 2.91s 
# [SCRAPE].. ◆ https://tt.wikipedia.org                                                                             | ✓ | ⏱: 0.72s 
# [COMPLETE] ● https://tt.wikipedia.org                                                                             | ✓ | ⏱: 3.65s 
# [FETCH]... ↓ https://ml.wikipedia.org                                                                             | ✓ | ⏱: 28.87s 
# [SCRAPE].. ◆ https://ml.wikipedia.org                                                                             | ✓ | ⏱: 1.58s 
# [COMPLETE] ● https://ml.wikipedia.org                                                                             | ✓ | ⏱: 30.48s 
# [FETCH]... ↓ https://pt.wikipedia.org                                                                             | ✓ | ⏱: 26.33s 
# [SCRAPE].. ◆ https://pt.wikipedia.org                                                                             | ✓ | ⏱: 1.48s 
# [COMPLETE] ● https://pt.wikipedia.org                                                                             | ✓ | ⏱: 27.83s 
# [FETCH]... ↓ https://ru.wikipedia.org                                                                             | ✓ | ⏱: 27.16s 
# [SCRAPE].. ◆ https://ru.wikipedia.org                                                                             | ✓ | ⏱: 0.60s 
# [COMPLETE] ● https://ru.wikipedia.org                                                                             | ✓ | ⏱: 27.78s 
# [FETCH]... ↓ https://uk.wikipedia.org                                                                             | ✓ | ⏱: 21.45s 
# [SCRAPE].. ◆ https://uk.wikipedia.org                                                                             | ✓ | ⏱: 1.32s 
# [COMPLETE] ● https://uk.wikipedia.org                                                                             | ✓ | ⏱: 23.08s 
# [FETCH]... ↓ https://pnb.wikipedia.org                                                                            | ✓ | ⏱: 37.42s 
# [SCRAPE].. ◆ https://pnb.wikipedia.org                                                                            | ✓ | ⏱: 0.82s 
# [COMPLETE] ● https://pnb.wikipedia.org                                                                            | ✓ | ⏱: 38.26s 
# [FETCH]... ↓ https://ur.wikipedia.org                                                                             | ✓ | ⏱: 17.48s 
# [SCRAPE].. ◆ https://ur.wikipedia.org                                                                             | ✓ | ⏱: 0.39s 
# [COMPLETE] ● https://ur.wikipedia.org                                                                             | ✓ | ⏱: 17.89s 
# [FETCH]... ↓ https://simple.wikipedia.org                                                                         | ✓ | ⏱: 36.14s 
# [SCRAPE].. ◆ https://simple.wikipedia.org                                                                         | ✓ | ⏱: 0.60s 
# [COMPLETE] ● https://simple.wikipedia.org                                                                         | ✓ | ⏱: 36.75s 
# [FETCH]... ↓ https://sh.wikipedia.org                                                                             | ✓ | ⏱: 38.03s 
# [SCRAPE].. ◆ https://sh.wikipedia.org                                                                             | ✓ | ⏱: 0.93s 
# [COMPLETE] ● https://sh.wikipedia.org                                                                             | ✓ | ⏱: 39.03s 
# [FETCH]... ↓ https://ro.wikipedia.org                                                                             | ✓ | ⏱: 39.94s 
# [SCRAPE].. ◆ https://ro.wikipedia.org                                                                             | ✓ | ⏱: 0.65s 
# [COMPLETE] ● https://ro.wikipedia.org                                                                             | ✓ | ⏱: 40.59s 
# [FETCH]... ↓ https://sl.wikipedia.org                                                                             | ✓ | ⏱: 38.77s
# [SCRAPE].. ◆ https://sl.wikipedia.org                                                                             | ✓ | ⏱: 0.49s 
# [COMPLETE] ● https://sl.wikipedia.org                                                                             | ✓ | ⏱: 39.27s 
# [FETCH]... ↓ https://ps.wikipedia.org                                                                             | ✓ | ⏱: 42.58s 
# [SCRAPE].. ◆ https://ps.wikipedia.org                                                                             | ✓ | ⏱: 0.91s 
# [COMPLETE] ● https://ps.wikipedia.org                                                                             | ✓ | ⏱: 43.50s 
# [FETCH]... ↓ https://tr.wikipedia.org                                                                             | ✓ | ⏱: 35.58s 
# [SCRAPE].. ◆ https://tr.wikipedia.org                                                                             | ✓ | ⏱: 0.90s 
# [COMPLETE] ● https://tr.wikipedia.org                                                                             | ✓ | ⏱: 36.49s 
# [FETCH]... ↓ https://sv.wikipedia.org                                                                             | ✓ | ⏱: 40.38s 
# [SCRAPE].. ◆ https://sv.wikipedia.org                                                                             | ✓ | ⏱: 0.86s 
# [COMPLETE] ● https://sv.wikipedia.org                                                                             | ✓ | ⏱: 41.27s 
# [FETCH]... ↓ https://ta.wikipedia.org                                                                             | ✓ | ⏱: 40.48s 
# [SCRAPE].. ◆ https://ta.wikipedia.org                                                                             | ✓ | ⏱: 0.94s 
# [COMPLETE] ● https://ta.wikipedia.org                                                                             | ✓ | ⏱: 41.43s 
# [FETCH]... ↓ https://sw.wikipedia.org                                                                             | ✓ | ⏱: 42.41s 
# [SCRAPE].. ◆ https://sw.wikipedia.org                                                                             | ✓ | ⏱: 0.77s 
# [COMPLETE] ● https://sw.wikipedia.org                                                                             | ✓ | ⏱: 43.20s 
# [FETCH]... ↓ https://tg.wikipedia.org                                                                             | ✓ | ⏱: 41.16s 
# [SCRAPE].. ◆ https://tg.wikipedia.org                                                                             | ✓ | ⏱: 0.38s 
# [COMPLETE] ● https://tg.wikipedia.org                                                                             | ✓ | ⏱: 41.55s 
# [FETCH]... ↓ https://sq.wikipedia.org                                                                             | ✓ | ⏱: 45.99s 
# [SCRAPE].. ◆ https://sq.wikipedia.org                                                                             | ✓ | ⏱: 0.76s 
# [COMPLETE] ● https://sq.wikipedia.org                                                                             | ✓ | ⏱: 46.77s 
# [FETCH]... ↓ https://sr.wikipedia.org                                                                             | ✓ | ⏱: 46.32s
# [SCRAPE].. ◆ https://sr.wikipedia.org                                                                             | ✓ | ⏱: 0.59s 
# [COMPLETE] ● https://sr.wikipedia.org                                                                             | ✓ | ⏱: 46.93s 
# [FETCH]... ↓ https://te.wikipedia.org                                                                             | ✓ | ⏱: 45.16s 
# [SCRAPE].. ◆ https://te.wikipedia.org                                                                             | ✓ | ⏱: 0.81s 
# [COMPLETE] ● https://te.wikipedia.org                                                                             | ✓ | ⏱: 45.99s 
# [FETCH]... ↓ https://th.wikipedia.org                                                                             | ✓ | ⏱: 45.24s 
# [SCRAPE].. ◆ https://th.wikipedia.org                                                                             | ✓ | ⏱: 0.62s 
# [COMPLETE] ● https://th.wikipedia.org                                                                             | ✓ | ⏱: 45.87s 
# [FETCH]... ↓ https://sk.wikipedia.org                                                                             | ✓ | ⏱: 52.13s 
# [SCRAPE].. ◆ https://sk.wikipedia.org                                                                             | ✓ | ⏱: 1.48s 
# [COMPLETE] ● https://sk.wikipedia.org                                                                             | ✓ | ⏱: 53.65s 
# [FETCH]... ↓ https://uz.wikipedia.org                                                                             | ✓ | ⏱: 29.08s 
# [SCRAPE].. ◆ https://uz.wikipedia.org                                                                             | ✓ | ⏱: 0.40s 
# [COMPLETE] ● https://uz.wikipedia.org                                                                             | ✓ | ⏱: 29.52s 
# [FETCH]... ↓ https://war.wikipedia.org                                                                            | ✓ | ⏱: 21.67s 
# [SCRAPE].. ◆ https://war.wikipedia.org                                                                            | ✓ | ⏱: 0.69s 
# [COMPLETE] ● https://war.wikipedia.org                                                                            | ✓ | ⏱: 22.38s 
# [FETCH]... ↓ https://zh.wikipedia.org                                                                             | ✓ | ⏱: 18.16s 
# [SCRAPE].. ◆ https://zh.wikipedia.org                                                                             | ✓ | ⏱: 0.86s 
# [COMPLETE] ● https://zh.wikipedia.org                                                                             | ✓ | ⏱: 19.05s 
# [FETCH]... ↓ https://vi.wikipedia.org                                                                             | ✓ | ⏱: 30.71s 
# [SCRAPE].. ◆ https://vi.wikipedia.org                                                                             | ✓ | ⏱: 0.59s 
# [COMPLETE] ● https://vi.wikipedia.org                                                                             | ✓ | ⏱: 31.32s 
# [FETCH]... ↓ https://zh-yue.wikipedia.org                                                                         | ✓ | ⏱: 21.71s 
# [SCRAPE].. ◆ https://zh-yue.wikipedia.org                                                                         | ✓ | ⏱: 0.45s 
# [COMPLETE] ● https://zh-yue.wikipedia.org                                                                         | ✓ | ⏱: 22.18s 
# [FETCH]... ↓ https://zh-min-nan.wikipedia.org                                                                     | ✓ | ⏱: 23.39s 
# [SCRAPE].. ◆ https://zh-min-nan.wikipedia.org                                                                     | ✓ | ⏱: 0.50s 
# [COMPLETE] ● https://zh-min-nan.wikipedia.org                                                                     | ✓ | ⏱: 23.90s 
# [FETCH]... ↓ https://xmf.wikipedia.org                                                                            | ✓ | ⏱: 24.72s 
# [SCRAPE].. ◆ https://xmf.wikipedia.org                                                                            | ✓ | ⏱: 0.91s 
# [COMPLETE] ● https://xmf.wikipedia.org                                                                            | ✓ | ⏱: 25.66s 
# Crawled 150 pages in total
# URL: https://www.wikipedia.org
# Depth: 0
# URL: https://bg.wikipedia.org
# Depth: 1
# URL: https://ba.wikipedia.org
# Depth: 1
# URL: https://ace.wikipedia.org
# Depth: 1
# URL: https://an.wikipedia.org
# Depth: 1
# PS C:\Users\Admin\Desktop\GeekForGeeks\Projects\Day-17> 