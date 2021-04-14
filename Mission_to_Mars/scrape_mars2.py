
# Import dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
  
 # MAC: Set Executable Path & Initialize Chrome Browser
def scrape():   
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

   
    mars={}

    #-----------NASA MARS NEWS---------------
    url = "https://redplanetscience.com/"
    browser.visit(url)
    # Parse Results HTML with BeautifulSoup>
    
    html = browser.html
    news_soup = BeautifulSoup(html, "html.parser")
    
    #News
    news_title=news_soup.find("div", class_="content_title").text
    news_p=news_soup.find("div", class_="article_teaser_body").text
    mars["news_titles"]=news_title
    mars["news_p"]=news_p

    #-------------JPL MARS SPACE IMAGES - FEATURED IMAGE-------------
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    browser.find_by_tag("button")[1].click()
    html = browser.html
    jplimage = BeautifulSoup(html, "html.parser")
    image=jplimage.find('img',class_="fancybox-image").get('src')
    image
    featimgurl="https://spaceimages-mars.com/"+image
    featimgurl
    mars["featured_image_url"]=featimgurl


    #-------------- MARS FACTS---------------
    url = "https://galaxyfacts-mars.com/"
    df=pd.read_html(url)
    df=df[0]
    df
    df.columns=["Description","Mars","Earth"]
    df.set_index("Description",inplace=True)
    df
    df_html=df.to_html()
    df_html
    mars["facts"]=df_html

    #----------- MARS HEMISPHERES---------------
    url = "https://marshemispheres.com/"
    browser.visit(url)
    links = [url + item.find(class_="description").a["href"] for item in soup.find_all("div", class_="item")]
    
    hemisphere_image_url=[]
    
    for url in links:
        
        # from url to soup
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extract data
        title = soup.find("div", class_="content").find("h2", class_="title").text.replace(" Enhanced", "")
        img_url = url + soup.find("img", class_="wide-image")["src"]
        
        # Store in list
        hemisphere_image_url.append({"title": title, "img_url": img_url})

    # close the browser
    browser.quit()

    
    # Return one python dictionary containing all of the scraped data
    mars = {'news_title':news_title}
    mars ['news_p']=news_p
    mars ['featured_image_url']=featimgurl
    mars['facts']=df_html
    mars['hemispheres']=hemisphere_image_url

   


    return mars