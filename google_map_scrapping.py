import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

maps = "https://www.google.com/maps/"

options = webdriver.ChromeOptions()
options.headless = False  # Set to True if you want to run in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

record = []
le = 0

def start_browser():
    driver.maximize_window()
    driver.get(maps)

def search_place(placename):
    searchBox = driver.find_element(by=By.ID, value='searchboxinput')
    searchBox.click()
    searchBox.send_keys(placename)
    searchButton = driver.find_element(by=By.ID,value="searchbox-searchbutton")
    searchButton.click()
    time.sleep(2)
    searchButton.click()
    time.sleep(2)

def scroll_and_collect_links():
    links = []
    le = 0

    while True:
        # Collect links on the current page
        links_on_page = driver.find_elements(By.CLASS_NAME, "lcr4fd.S9kvJb")
        for link_element in links_on_page:
            link_href = link_element.get_attribute("href")
            if link_href not in links:
                links.append(link_href)
                print(link_href)

        # Check for the presence of the "HlvSq" element at the end of the page
        if driver.find_elements(By.CLASS_NAME, "HlvSq"):
            print("end of page")
            break
        
        # Scroll down to load more results
        middle_index = len(links_on_page) //2
        scroll_origin = ScrollOrigin.from_element(links_on_page[middle_index])
        action = webdriver.ActionChains(driver)
        action.scroll_from_origin(scroll_origin, 0,100000).perform()
        time.sleep(2) 

        new_links_on_page = driver.find_elements(By.CLASS_NAME, "lcr4fd.S9kvJb")
        if len(new_links_on_page) == len(links_on_page): 
            le += 1
            if le > 20:
                break
        else:
            le = 0

    return links

def save_to_csv(data,filename):
    df = pd.DataFrame(data, columns=['Links'])
    df.to_csv(filename, index=False, encoding='utf-8')

start_browser()
search_place("software company in Bangalore")
links = scroll_and_collect_links()
save_to_csv(links,filename="companies.csv")
driver.quit()
