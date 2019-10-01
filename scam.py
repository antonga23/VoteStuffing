import requests
import names

url = 'https://woobox.com/kyx98p'

v_email = "mandydingo95@gmail.com"
v_custom_8 = "on"
v_prsoptin = "on"
v_custom_4 = "300 Park Ave"
v_custom_5 = "New York"
v_custom_6 = "NY"
v_custom_7 = "10003"

for x in range(100000):

	first_name = names.get_first_name()
	last_name = names.get_last_name()
##

	response = requests.post(url, allow_redirects=False, data={
		'email': v_email,
		'custom_8': v_custom_8,
		'prsoptin': v_prsoptin,
		'custom_3_first': first_name,
		'custom_3_last': last_name,
		'custom_4': v_custom_4,
		'custom_5': v_custom_5,
		'custom_6': v_custom_6,
		'custom_7': v_custom_7
	})
	if response.status_code == 200:
		print('Success!')
	elif response.status_code == 404:
		print('Not Found.')