import time
from bs4 import BeautifulSoup 
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests

def init_browser():
    # Create path to browse by using webdriver manager
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

   # define url
    mars_news_url = "https://redplanetscience.com/"
    browser.visit(mars_news_url)

# Create BeautifulSoup
    html = browser.html
    mars_news_soup = BeautifulSoup(html, 'html.parser')

# Find the news title and paragraph
    news_title = mars_news_soup.body.find('div', class_='content_title').text

    news_paragraph = mars_news_soup.body.find('div', class_='article_teaser_body').text

    print(f"The Title is: \n{news_title}")
    print()
    print(f"The Paragraph is: \n{news_paragraph}")

# url for images
    mars_image_url = 'https://spaceimages-mars.com'
    browser.visit(mars_image_url)
    html_images = browser.html
    browser.links.find_by_partial_text('FULL IMAGE').click()

    html_images = browser.html

    soup = BeautifulSoup(html_images, 'html.parser')

    featured_url = soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url = f'https://spaceimages-mars.com/{featured_url}'


    
    print (featured_image_url) 

#Mars facts
    mars_facts_url = "https://galaxyfacts-mars.com"

# html into panda
    tables = pd.read_html(mars_facts_url)

    tables

    type(tables)
    tables_df = tables[0]
    tables_df.column = ['Mars', 'Earth']

    mars_table=tables_df.to_html()

## Mars Hemisphere

    hemispheres_url= 'https://marshemispheres.com/'

    browser.visit(hemispheres_url)
    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')
    mars_url = soup.find_all('div', class_='item')

    hemisphere_image_urls = []
    titles = []
    for h in mars_url:
        title = h.find('h3').text
        p_img_url = h.find('a', class_='itemLink product-item')['href']
        browser.visit(hemispheres_url + p_img_url)
        p_img_url = browser.html
        soup = BeautifulSoup( p_img_url, 'html.parser')
    
        image_url = hemispheres_url + soup.find('img', class_='thumb')['src']
    
        print(image_url)
        hem_data=dict({'title':title, 'img_url':image_url})
        hemisphere_image_urls.append(hem_data)
        hemisphere_image_urls

    # return hem_data

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image_url": featured_image_url,
        "mars_table": mars_table,
        "hemisphere_image_urls": hemisphere_image_urls




    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data


    













 


    

