import json, math

from firebase import firebase

key = 'upxdwaxBxJkPI8dXxTa0rvEKWph98hg2fxaBLF2M'
url = 'https://imagelog.firebaseio.com/'
email = 'kfc369@gmail.com'
number_of_tries = 3

firebase.FirebaseApplication(url, authentication=None)

def init():
	authentication = firebase.Authentication(key, email)
	firebase.authentication = authentication

def compareTo(user_id, image_json):
	result = firebase.get('/user', user_id)

	for x in range(0, number_of_tries):
		if result['description'] == image_json['responses']['labelAnnotations']['description']:
			difference = abs(float(result['score']) - float(image_json['responses']['labelAnnotations']['score']))
			if difference < math.pow(10, -6):
				average_score = (float(result['score']) + float(image_json['responses']['labelAnnotations']['score']))/2
				firebase.post('/users', user_id, {'score': average_score}, result['description'])
				return True
	return False