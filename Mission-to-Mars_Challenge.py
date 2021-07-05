#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Splinter and Beautiful Soup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


#Set executable path
executable_path= {'executable_path': ChromeDriverManager().install()}
browser= Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[3]:


#Visit the mars nasa news site
url= 'https://redplanetscience.com'
browser.visit(url)
#Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


#Set up HTML parser
html= browser.html
news_soup= soup(html, 'html.parser')
#Set parent element
slide_elem= news_soup.select_one('div.list_text')


# In[5]:


#Find most recent article title
slide_elem.find('div', class_='content_title')


# In[6]:


#Use parent element to find the first 'a' tag and save it as 'news_title'
news_title= slide_elem.find('div', class_= 'content_title').get_text()
news_title


# In[7]:


#Use the parent element to find the paragraph text
news_p= slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[8]:


#Visit URL
url= 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


#Parse the resulting html with soup
html= browser.html
img_soup= soup(html, 'html.parser')


# In[11]:


#Find the relative image url
img_url_rel= img_soup.find('img', class_= 'fancybox-image').get('src')
img_url_rel


# In[12]:


#Use the base URL to create an absolute URL
img_url= f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ###  Mars Facts

# In[13]:


df= pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns= ['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[14]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
links= browser.find_by_css('a.product-item img')
for link in range(len(links)):
    dict={}
    browser.find_by_css('a.product-item img')[link].click()
    #full_image = links.click()
    full_image_url= browser.links.find_by_text('Sample').first
    dict["image_url"]=full_image_url["href"]
    dict["title"]= browser.find_by_css('h2.title').text
    #img_url= f’https://marshemispheres.com/{full_image_url}’
    hemisphere_image_urls.append(dict)
    browser.back()

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

browser.quit()





