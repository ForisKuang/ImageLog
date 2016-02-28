import json

def main():
	condition = False
	var tries = 1
	while not condtion or tries <= 3:
		read = ReadImage()
		user_id = read.get_user_id()
		json_data = read.get_json_data()
		compare = FireBase(user_id)
		condition = compareTo(json_data)
		tries += 1
	if condition:
		Access(json_data)

if __name__ == "__main__": main()
