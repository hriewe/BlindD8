# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import re

from rake_nltk import Rake
import nltk
import os
import glob
import json

def extract_key_words(profile):
	string = ""
	if 'dog' in str(profile['bio']).lower():
		string += "{} is a dog lover.  ".format(profile['name'])
	if 'lie' in str(profile['bio']).lower() and 'age' in str(profile['bio']).lower():
		for val in re.findall("\d+", str(profile['bio'])):
			if int(val) > 18:
				string += "{} has the wrong age in her profile description.  She is actually {} years old".format(profile['name'], profile['bio'])
	return string

def predict_socioeconomic_status(outputResponse, pictureResponses):
	try:
		tilt = outputResponse[1][0]['faceAnnotations'][0]['tiltAngle']
	except:
		tilt = 0
	return ('blurredlikelihood": "very' in str(outputResponse).lower() and tilt < 15)

def generate_string_response(outputResponse, pictureResponses):
	emotion = None
	try:
		sad_characteristics = []
		happy_characteristics = []
		for val in pictureResponses:
			try:
				sad_keyword = str(val["responses"][0]["faceAnnotations"][0].get('sorrowLikelihood'))
				if sad_keyword != "None":
					sad_characteristics.append(sad_keyword.lower())
				happy_keyword = happy = str(val["responses"][0]["faceAnnotations"][0].get('joyLikelihood'))
				if happy_keyword != "None":
					happy_characteristics.append(happy_keyword.lower())
			except:
				pass
		sad_count = sad_characteristics.count('very_likely') + sad_characteristics.count('highly_likely')
		happy_count = happy_characteristics.count('very_likely') + happy_characteristics.count('highly_likely')
		if sad_count > happy_count:
			emotion = "Sad"
		else:
			emotion = "Happy"
	except Exception as exp:
		print exp
		pass
	string = "Meet "
	string += outputResponse['name']
	string += " she is {} years old".format(outputResponse['age'])
	distanceInKM = int(outputResponse['distance_km'])
	string += " and lives {} kilometers away".format(distanceInKM)
	if emotion != None:
		string += " {} is {} in most of her photos".format(outputResponse['name'], emotion)
	return string

r = Rake()
for folder in glob.glob("5*/"):
	a = json.load(open("{}profile.json".format(folder)))
	b = json.load(open("{}output.json".format(folder)))
	r.extract_keywords_from_text(a['bio'])
	string = generate_string_response(a, b)
	string += " and she mentioned her {} ".format(' '.join(re.findall('\w+', r.get_ranked_phrases()[0]))) + " in her profile.  "
	g = extract_key_words(a)
	print g
	string += g
	if predict_socioeconomic_status(b, a) == True:
		string += "  {} is from a higher socioeconomic status".format(a['bio'])
	print ' '.join(re.findall("\w+", string))
