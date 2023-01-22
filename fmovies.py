from __future__ import unicode_literals
import sys
import urllib
import requests
import shutil
import time
import json
import youtube_dl
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def seleniumInit():
    # init Chrome driver (Selenium)
    options = Options()
    options.add_experimental_option('w3c', False) ### added this line
    options.headless = True
    cap = DesiredCapabilities.CHROME
    cap["loggingPrefs"] = {"performance": "ALL"}

    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options, desired_capabilities=cap)
    return drive

def downloadMovie(driver):
    if len(sys.argv) == 1:
        return print("Please provide a movie")

    movie = sys.argv[1])
    driver.get(movie)
    # kinda iffy, running into some errors ocassionally here
    driver.find_element(By.ID, "play-now").click()
    time.sleep(3)
    video = driver.find_element(By.TAG_NAME, "iframe").get_attribute('src')
    print("Found video...")
    driver.get(video)
    time.sleep(3)
    log = driver.get_log("performance")
    driver.quit()

    blob = ""
    for i in log:
        res = str(i)
        if "master.m3u8" in res:
            logDict = json.loads(i["message"])
            headers = logDict["message"]["params"]["headers"]
            blob = "https://" + headers[":authority"] + headers[":path"]
            print("Video source: {blob}".format(blob=blob))
            break

    print("Starting video download...")
    ydl_opts = {"nocheckcertificate": True, "format": "mp4", "outtmpl": "./movies/movie.mp4"}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([blob])

if __name__ == "__main__":
    driver = seleniumInit()
    downloadMovie(driver)
