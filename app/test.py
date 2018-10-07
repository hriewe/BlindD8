#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver


class GoogleTests():
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path='chromedriver',
									   service_args=['--verbose', '--log-path=chromedriverTest.log'])
		self.driver.get("https://google.com")

	def test_google_test(self):
		print 'Test passed'

	def tearDown(self):
		self.driver.close()
		time.sleep(5)
		self.driver.quit()

if __name__ == "__main__":
	options = webdriver.ChromeOptions()
	options.add_argument("--headless")
	driver = webdriver.Chrome(chrome_options=options, executable_path='chromedriver',
									   service_args=['--headless', '--verbose', '--log-path=chromedriverTest.log'])
	driver.set_window_size(1286, 889)
	driver.get("http://127.0.0.1:5000/")
	driver.find_element_by_css_selector("tinderforbananas-item.item.item--top > picture").click()

	time.sleep(.3)
	driver.save_screenshot('screen.png')
	driver.close()
