from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import sys
import time
from selenium import webdriver
import threading

try:
	image_url = sys.argv[1]
	name = sys.argv[2].title()
	age = sys.argv[3]
	bio = sys.argv[4]
	job = sys.argv[5].title()
	distance = sys.argv[6]
except:
	pass

a = open("static/app_template.js").read()
new_data = "{"
new_data += '''
		id: 0,
	  name: '{}',
	  age: {},
	  job: '{}',
	  images: ["static/images/image.jpg"],
	  distance: {},
	  description: '{}'
	'''.format(name, age, job, distance, bio)
new_data += "}"
a = a.replace("TEMPLATE_FILE", new_data)
e = open("static/app.js", "w")
e.write(a)
e.close()
def thread_webAPP():
	app = Flask(__name__, static_url_path='/static')
	@app.route('/', methods=['GET'])
	def index():
		return render_template("index.html")
	app.run(host='127.0.0.1', port=5000)

if __name__ == '__main__':
	t_webApp = threading.Thread(name='Web App', target=thread_webAPP)
	t_webApp.setDaemon(True)
	t_webApp.start()

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
	exit(0)

