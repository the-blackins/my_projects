import requests
import json 
  
# construct the request url with the desired endpoint and  your API 
base_url = "https://v6.exchangerate-api.com/v6/"
api_key = "1a6ec61b5882bd0d9fff3c63"
endpoint = "latest/USD"
file_path = "exchange_rates.json"
request_url = f"{base_url}{api_key}/{endpoint}"

#  send the request 
response = requests.get(request_url)
    
# handle the response
if response.status_code == 200:
    data = response.json()
    rates = data['conversion_rates']
    # print(rates)    
    with open("rates.json" , 'w') as file:
        json.dump(rates, file) 
    print("exchamge rates successful")
else:
    # error message 
    print("internet connection required")
    # print(f"request failed with status code: { response.status_code}")

       


# gpb_exch_rates = {
#         "gbp_ng":  (1/["usd_gbp"])*462.03126,
#        "gbp_cedi": (1/["usd_gbp"])*11.295342,
#         "gbp_aed": (1/["usd_gbp"])*3.673,
#         "gbp_btc": (1/["usd_gbp"])*0.00003876,
#         "gbp_eur": (1/["usd_gbp"])*0.92993,
#         "gbp_usd": (1/["usd_gbp"])*1.257071,
#         "gbp_kwd": (1/["usd_gbp"])*0.306776
       
#     }
# print(gpb_exch_rates["gbp_ng"])
    
# list of currency and their rates to pounds sterling
# """ 
#     (KWD)kuwaiti dinar  = 0.386147
#     (USD) united states dollar = 1.25705
#     (EUR)Euro  = 1.168968
#     (BTC)Bitcoin = 0.0000487
#     (AED)Uae dirham = 4.617
#     (GHS)Ghanian cedi = 14.198809
#     (NGN)Nigerian naira = 580.796399"""