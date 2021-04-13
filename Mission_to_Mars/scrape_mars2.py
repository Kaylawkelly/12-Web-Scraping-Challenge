#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dependencies and Setup
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager
import nbconvert


# In[ ]:


# MAC: Set Executable Path & Initialize Chrome Browser
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


mars={}


# In[ ]:


#NASA Mars News Site
url = "https://redplanetscience.com/"
browser.visit(url)


# In[ ]:


# Parse Results HTML with BeautifulSoup>

html = browser.html
news_soup = BeautifulSoup(html, "html.parser")


# In[ ]:


#News
news_title=news_soup.find("div", class_="content_title").text


# In[ ]:


news_p=news_soup.find("div", class_="article_teaser_body").text


# In[ ]:


mars["news_titles"]=news_title
mars["news_p"]=news_p


# In[ ]:


#JPL Mars Space Image
url = "https://spaceimages-mars.com/"
browser.visit(url)
browser.find_by_tag("button")[1].click()


# In[ ]:


html = browser.html
jplimage = BeautifulSoup(html, "html.parser")


# In[ ]:


image=jplimage.find('img',class_="fancybox-image").get('src')


# In[ ]:


image


# In[ ]:


featimgurl="https://spaceimages-mars.com/"+image


# In[ ]:


featimgurl


# In[ ]:


mars["featured_image_url"]=featimgurl


# In[ ]:


#Facts
url = "https://galaxyfacts-mars.com/"
df=pd.read_html(url)
df=df[0]
df


# In[ ]:


df.columns=["Description","Mars","Earth"]
df.set_index("Description",inplace=True)
df


# In[ ]:


df_html=df.to_html()
df_html


# In[ ]:


mars["facts"]=df_html


# In[ ]:


#hemispheres
url = "https://marshemispheres.com/"
browser.visit(url)
result=browser.find_by_css("a.product-item img")

hemisphere_image_url=[]

for i in range(len(result)):
    hemisphere={}
    browser.find_by_css("a.product-item img")[i].click()
    element = browser.links.find_by_text('Sample').first
    img_url= element["href"]
    hemisphere["img_url"]=img_url
    hemisphere["title"]=browser.find_by_css("h2.title").text
    hemisphere_image_url.append(hemisphere)
    browser.back()


# In[ ]:


hemisphere_image_url


# In[ ]:


mars["hemispheres"]=hemisphere_image_url


# In[ ]:


mars


# In[ ]:


#convert to notebook to python script

#delete some lines (cells, ie run blah)
#grab to app.py (Day 3)
#index.html use same variables


# In[ ]:





# In[ ]:




