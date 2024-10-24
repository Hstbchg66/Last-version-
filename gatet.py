import requests
import time
def GateTele(cx):
	cc = cx.split("|")[0]
	mes = cx.split("|")[1]
	ano = cx.split("|")[2]
	cvv = cx.split("|")[3]
	if "20" in ano:
		ano = ano.split("20")[1]
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3Mjk4NzQ1MjUsImp0aSI6ImM3ODRhZjBiLTk1MzUtNGE3My1hNmY1LTVmNDZmMmYxYjY5ZSIsInN1YiI6ImJxY3h0bjZ4eWZycWJzd3ciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImJxY3h0bjZ4eWZycWJzd3ciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.2b3JS8B6_KfI2fmH77UfRu7D57-iK2ThifBnCVLo0b5xcT-lbOheRtmA-TCW11IPZEy9auqojfn6Ae98QxveLg',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'e97ac3a9-51ae-44f9-a4f0-2dfb74cd46ea',
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

	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/json',
	    'origin': 'https://www.cytoplan.co.uk',
	    'referer': 'https://www.cytoplan.co.uk/checkout/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'amount': '14.40',
	    'additionalInfo': {
	        'billingLine1': 'Flat 2, 14A',
	        'billingLine2': 'London Road',
	        'billingCity': 'Brighton',
	        'billingPostalCode': 'BN1 4JA',
	        'billingCountryCode': 'GB',
	        'billingPhoneNumber': '+445165554433',
	        'billingGivenName': '\\u0068\\u0072\\u0068\\u0072\\u0068\\u0064',
	        'billingSurname': '\\u0068\\u0068\\u0064\\u0068\\u0064\\u0068\\u0064',
	    },
	    'challengeRequested': True,
	    'bin': '424242',
	    'dfReferenceId': '0_545090e6-8fe4-495b-be8a-ce406f660d49',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.94.0',
	        'cardinalDeviceDataCollectionTimeElapsed': 13,
	        'issuerDeviceDataCollectionTimeElapsed': 2931,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3Mjk4NzQ1MjUsImp0aSI6ImM3ODRhZjBiLTk1MzUtNGE3My1hNmY1LTVmNDZmMmYxYjY5ZSIsInN1YiI6ImJxY3h0bjZ4eWZycWJzd3ciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImJxY3h0bjZ4eWZycWJzd3ciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.2b3JS8B6_KfI2fmH77UfRu7D57-iK2ThifBnCVLo0b5xcT-lbOheRtmA-TCW11IPZEy9auqojfn6Ae98QxveLg',
	    'braintreeLibraryVersion': 'braintree/web/3.94.0',
	    '_meta': {
	        'merchantAppId': 'www.cytoplan.co.uk',
	        'platform': 'web',
	        'sdkVersion': '3.94.0',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': 'e97ac3a9-51ae-44f9-a4f0-2dfb74cd46ea',
	    },
	}
	
	req0 = requests.post(
	    f'https://api.braintreegateway.com/merchants/bqcxtn6xyfrqbsww/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	if 'authenticate_successful' in req0:
		return '3DS Authenticate Successful ✅ '
	elif 'challenge_required' in req0:
		return '3DS Challenge Required ❌'
	elif 'authenticate_attempt_successful' in req0:
	       return '3DS Authenticate Attempt Successful ✅'
	elif 'authenticate_rejected' in req0:
	       return '3DS Authenticate Rejected ❌'
	elif 'authenticate_frictionless_failed' in req0:
	       return '3DS Authenticate Frictionless Failed ❌'
	elif 'lookup_card_error' in req0:
	       return 'lookup_card_error ⚠️'
	elif 'lookup_error' in req0:
	       return 'lookup Error ⚠️'
	else:
		try:
			code = req0.json()['error']
			return code
		except:
			try:
				return req0.json()['error']
			except:
				return req0.text
	