#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install nbconvert


# In[2]:


# Dependencies and Setup
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager
import nbconvert


# In[3]:


# MAC: Set Executable Path & Initialize Chrome Browser
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


mars={}


# In[5]:


#NASA Mars News Site
url = "https://redplanetscience.com/"
browser.visit(url)


# In[6]:


# Parse Results HTML with BeautifulSoup>

html = browser.html
news_soup = BeautifulSoup(html, "html.parser")


# In[7]:


#News
news_title=news_soup.find("div", class_="content_title").text


# In[8]:


news_p=news_soup.find("div", class_="article_teaser_body").text


# In[9]:


mars["news_titles"]=news_title
mars["news_p"]=news_p


# In[10]:


#JPL Mars Space Image
url = "https://spaceimages-mars.com/"
browser.visit(url)
browser.find_by_tag("button")[1].click()


# In[11]:


html = browser.html
jplimage = BeautifulSoup(html, "html.parser")


# In[12]:


image=jplimage.find('img',class_="fancybox-image").get('src')


# In[13]:


image


# In[14]:


featimgurl="https://spaceimages-mars.com/"+image


# In[15]:


featimgurl


# In[16]:


mars["featured_image_url"]=featimgurl


# In[17]:


#Facts
url = "https://galaxyfacts-mars.com/"
df=pd.read_html(url)
df=df[0]
df


# In[18]:


df.columns=["Description","Mars","Earth"]
df.set_index("Description",inplace=True)
df


# In[19]:


df_html=df.to_html()
df_html


# In[20]:


mars["facts"]=df_html


# In[21]:


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


# In[22]:


hemisphere_image_url


# In[23]:


mars["hemispheres"]=hemisphere_image_url


# In[24]:





# In[25]:


#convert to notebook to python script

#delete some lines (cells, ie run blah)
#grab to app.py (Day 3)
#index.html use same variables


# In[ ]:





# In[ ]:




