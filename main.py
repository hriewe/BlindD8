import requests
import base64
import shutil
import random
import json
import os

REQUEST_TEMPLATE = "request_template.json"

try:
	API_KEY = open("API_KEY.txt").read().strip()
except:
	API_KEY = raw_input("API Key: ")

def download_image(url, saveas=None):
	file_extension = url[::-1].partition(".")[0][::-1]
	if saveas == None:
		saveas = ''.join([str(random.randint(1,9)) for i in range(9)]) + '.{}'.format(file_extension)
	response = requests.get(url, stream=True)
	with open(saveas, 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response
	return saveas

def base64_encode(filename):
	with open(filename, "rb") as image_file:
		return base64.b64encode(image_file.read())

def get_image_details(url):
	image_file = download_image(url)
	# This is the local file name of the image
	base64_image = base64_encode(image_file)
	request_info = json.load(open(REQUEST_TEMPLATE))
	request_info['requests'][0]['image']['content'] = base64_image
	f = open("request.json", "w")
	f.write(json.dumps(request_info))
	f.close()
	os.system("""curl --silent -s -H "Content-Type: application/json" \
	https://vision.googleapis.com/v1/images:annotate?key={} \
	--data-binary @request.json -o temp""".format(API_KEY))
	return json.load(open("temp"))



if __name__ == '__main__':
	print get_image_details("https://images-ssl.gotinder.com/596bce36608f375f5e31c6e4/640x640_e7d31153-8522-4ea6-824c-a2f41f373f50.jpg")
