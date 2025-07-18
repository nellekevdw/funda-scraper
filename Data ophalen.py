# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 20:52:43 2025

@author: Nelleke
"""

import pandas as pd
from fundascraper import FundaScraper

columns = ["url", "house_id", "city", "house_type",	"building_type", 
           "price", "price_m2", "room", "bedroom", "bathroom", "living_area",
           "energy_label",	"zip", "address", "year_built",	"construction_period", "house_age", "description"]

data = pd.DataFrame(columns=columns)

steden = ["velp-ge", "dieren", "rheden"]


if __name__ == '__main__':
    for stad in steden:
        scraper = FundaScraper(
            area= stad, 
            want_to="buy", 
            find_past=False, 
            page_start=1, 
            n_pages=1000,
            max_price=550000
        )
        df = scraper.run(raw_data=False, save=False)
        data = pd.concat([data, df], ignore_index=True)



data.to_csv('C:/Users/Nelleke/Documents/Funda/funda-scraper-tofix/funda-scraper/data/velp_dieren_rheden.csv', sep=";")