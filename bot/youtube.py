# -*- coding: utf-8 -*-

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data.config import PATH


options = Options()
options.headless = True
driver = webdriver.Chrome(PATH, chrome_options=options)


class YouTube(object):
    """Parser"""

    def __init__(self):
        pass

    def search_videos(self, user_text):
        self.user_text = user_text
        main_url = "https://www.youtube.com/results?search_query=" + user_text
        driver.get(main_url)
        sleep(1)
        videos = driver.find_elements_by_id("video-title")
        url = []
        for i in range(len(videos)):
            url.append(videos[i].get_attribute('href'))
            if i == 10:
                return url
                break

    def search_videos_from_channel(self, user_url):
        self.user_url = user_url
        driver.get(user_url + "/videos")
        videos = driver.find_elements_by_id("video-title")
        url = []
        for i in range(len(videos)):
            url.append(videos[i].get_attribute('href'))
            if i == 10:
                return url
                break

    def search_name_channel(self, user_url):
        self.user_url = user_url
        driver.get(user_url)
        channel_name = driver.find_element_by_id("channel-name")
        return channel_name.text

    def search_youtube_trends(self):
        url = "https://www.youtube.com/feed/trending/"
        driver.get(url)
        videos = driver.find_elements_by_id("thumbnail")
        url = []
        for i in range(len(videos)):
            url.append(videos[i].get_attribute('href'))
            if i == 10:
                return url
                break
