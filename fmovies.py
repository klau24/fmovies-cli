from __future__ import unicode_literals
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

# init Chrome driver (Selenium)
options = Options()
options.add_experimental_option('w3c', False) ### added this line
options.headless = True
cap = DesiredCapabilities.CHROME
cap["loggingPrefs"] = {"performance": "ALL"}

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",
                              options=options,
                              desired_capabilities=cap)



driver.get("https://ww3.fmovies.co/film/interstellar-1655/")
# kinda iff, running into some errors ocassionally here
driver.find_element(By.ID, "playit").click()
time.sleep(3)
video = driver.find_element(By.TAG_NAME, "iframe").get_attribute('src')
print("Found video...")
driver.get(video)
time.sleep(3)
print("Still working...")

log = driver.get_log("performance")
driver.quit()

blob = ""
for i in log:
    res = str(i)
    if "master.m3u8" in res:
        logDict = json.loads(i["message"])
        headers = logDict["message"]["params"]["headers"]
        blob = "https://" + headers[":authority"] + headers[":path"]
        print(blob)
        break

print("Starting video download...")
ydl_opts = {"nocheckcertificate": True, "format": "mp4", "outtmpl": "./interstellar.mp4"}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([blob])
