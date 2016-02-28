import json
import Firebase
import ReadImage

nubmer_of_tries = 3

def main():
	condition = False
	tries = 1
	while not condtion or tries <= number_of_tries:
		user_id = ReadImage.get_user_id()
		json_data = ReadImage.get_json_data()
		condition = Firebase.compareTo(json_data)
		tries += 1
	if condition:
		Access(json_data)

if __name__ == "__main__": main()