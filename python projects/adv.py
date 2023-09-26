
# making a prototype 
from api_key import usd_exch_rates

def excange_func(usd):
    converted_amount = usd * usd_exch_rates["usd_kwd"]
    result = round(converted_amount, 3)
    print("KWD "+str(result))
    
excange_func(5)