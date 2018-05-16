from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import csv
import time
import re

#netflix_all: https://reelgood.com/movies/source/netflix?filter-sort=5
#netflix_actionadventure: https://reelgood.com/movies/source/netflix?filter-genre=5&filter-sort=5
#netflix_comedy: https://reelgood.com/movies/source/netflix?filter-genre=9&filter-sort=5
#netflix_documentary: https://reelgood.com/movies/source/netflix?filter-genre=11&filter-sort=5
#netflix_drama: https://reelgood.com/movies/source/netflix?filter-genre=3&filter-sort=5
#netflix_horror: https://reelgood.com/movies/source/netflix?filter-genre=19&filter-sort=5
#netflix_scifi: https://reelgood.com/movies/source/netflix?filter-genre=26&filter-sort=5
#netflix_thriller: https://reelgood.com/movies/source/netflix?filter-genre=32&filter-sort=5
#netflix_family: https://reelgood.com/movies/source/netflix?filter-genre=12&filter-sort=5
#netflix_romance: https://reelgood.com/movies/source/netflix?filter-genre=4&filter-sort=5
#netflix_fantasy: 

#amazon_action: https://reelgood.com/movies/source/amazon?filter-genre=5&filter-sort=5
#amazon_comedy: https://reelgood.com/movies/source/amazon?filter-genre=9&filter-sort=5
#amazon_documentary:https://reelgood.com/movies/source/amazon?filter-genre=11&filter-sort=5
#amazon_drama: https://reelgood.com/movies/source/amazon?filter-genre=3&filter-sort=5
#amazon_horror: https://reelgood.com/movies/source/amazon?filter-genre=19&filter-sort=5
#amazon_scifi: https://reelgood.com/movies/source/amazon?filter-genre=26&filter-sort=5
#amazon_thriller: https://reelgood.com/movies/source/amazon?filter-genre=32&filter-sort=5
#amazon_family: https://reelgood.com/movies/source/amazon?filter-genre=12&filter-sort=5
#amazon_romance: https://reelgood.com/movies/source/amazon?filter-genre=4&filter-sort=5
#amazon_fantasy:https://reelgood.com/movies/source/amazon?filter-genre=13&filter-sort=5

#hulu_action: https://reelgood.com/movies/source/hulu?filter-genre=5&filter-sort=5
#hulu_comedy: https://reelgood.com/movies/source/hulu?filter-genre=9&filter-sort=5
#hulu_documentary: https://reelgood.com/movies/source/hulu?filter-genre=11&filter-sort=5
#hulu_drama: https://reelgood.com/movies/source/hulu?filter-genre=3&filter-sort=5
#hulu_horror: https://reelgood.com/movies/source/hulu?filter-genre=19&filter-sort=5
#hulu_scifi: https://reelgood.com/movies/source/hulu?filter-genre=26&filter-sort=5
#hulu_thriller: https://reelgood.com/movies/source/hulu?filter-genre=32&filter-sort=5
#hulu_family: https://reelgood.com/movies/source/hulu?filter-genre=12&filter-sort=5
#hulu_romance: https://reelgood.com/movies/source/hulu?filter-genre=4&filter-sort=5
#hulu_fantasy: https://reelgood.com/movies/source/hulu?filter-genre=13&filter-sort=5


driver = webdriver.Chrome()
driver.get("https://reelgood.com/movies/source/amazon?filter-genre=5&filter-sort=5")

csv_file = open('rgScrape_amazon_action.csv', 'w')
writer = csv.writer(csv_file)

index = 1

try:
    wait_button = WebDriverWait(driver, 10)
    load_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//a[contains(@href, "/movies/source/amazon?filter")]'))) 

    while True:
        try: 
            load_button.click()
        except:
            print("page load complete...")
            break

    #for i in range(2):
     #   load_button.click()
      #  print("page has been loaded...")            

    wait_film = WebDriverWait(driver, 10)

    films = wait_film.until(EC.presence_of_all_elements_located((By.XPATH,'''//*[@id="app_mountpoint"]/div/main/div[7]/table/tbody//tr''')))
    print(films)
    for film in films:
        try:
            print("Scraping item number: " + str(index))
            films_dict = {}
            position = film.find_element_by_xpath('./td/meta[@itemprop="position"]').get_attribute('content')
            #all_info = film.find_element_by_xpath('')
            title = film.find_element_by_xpath('./td[2]/a').text

            year = film.find_element_by_xpath('./td[4]').text

            imdb = film.find_element_by_xpath('./td[6]').text

            tomato = film.find_element_by_xpath('./td[7]').text.strip("%")
            films_dict['position'] = position
            films_dict['title'] = title
            films_dict['year'] = year
            films_dict['imdb'] = imdb
            films_dict['tomato'] = tomato
            print(films_dict)
            writer.writerow(films_dict.values())
            print("next")
            index += 1
        except:
            index += 1
            break
    
    #time.sleep(2)

except Exception as e:
    print(e)
    csv_file.close()
    driver.close()