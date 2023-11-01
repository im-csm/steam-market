"""
--- Description ---

Creator: Chance M.
Date: 10/18/23
"""

from bs4 import BeautifulSoup as SOUP
import requests as r
import sys

from filters import weapon, collection

def buildURL(itemSet = 'any', player = 'any', stickerCapsule = 'any', teamName = 'any', weapon = 'any'):
  URL = searchURL = f'https://steamcommunity.com/market/search?q=\
                      &category_730_ItemSet%5B%5D=any\
                      &category_730_ProPlayer%5B%5D=any\
                      &category_730_StickerCapsule%5B%5D=any\
                      &category_730_TournamentTeam%5B%5D=any\
                      &category_730_Weapon%5B%5D=tag_weapon_{weapon["AK47"]}\
                      &appid=730'
  return URL

# For each collection
# For each page:
  # Grab listing (Name, Price, Float val)
    # Insert into database

page = r.get('https://steamcommunity.com/market/search?appid=730') 
soup = SOUP(page.text, 'html.parser')




###############################################################################
# print(soup.find(id='resultlink_0').prettify())

#find all <a> class=market_listing_row_link

# for i in range(0, 10):
#   print(f'Listing {i+1}')
#   print('----------------------------------------')
#   print(soup.find(id=f'resultlink_{i}').prettify())


# Results display in <div id="searchResultRows"> </div>
# NO RESULTS: There were no items matching your search. Try again with different keywords.
# FOUND RESULTS: <a id="resultlink{n}"/>