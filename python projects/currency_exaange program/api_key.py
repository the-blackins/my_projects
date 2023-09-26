# 1a6ec61b5882bd0d9fff3c63

import json
file_path = "exchange_rates.json"


with open("rates.json", "r") as file:
    rates = json.load(file)
    
# print(rates)
# print(rates)
usd_ngn = rates['NGN']
usd_cedi = rates['GHS']
usd_aed = rates['AED']
usd_eur = rates['EUR']
usd_chf = rates['CHF']
usd_gbp = rates['GBP']
usd_kwd = rates['KWD']


# usd_rates: {
# 		"USD": 1,
# 		"AUD": 1.4817,
# 		"BGN": 1.7741,
# 		"CAD": 1.3168,
# 		"CHF": 0.9774,
# 		"CNY": 6.9454,
# 		"EGP": 15.7361,
# 		"EUR": 0.9013,
# 		"GBP": 0.7679,
# }
# print(usd_exch_rates])
kwd = usd_kwd
gbp = usd_gbp
chf = usd_chf
eur = usd_eur
aed = usd_aed
cedi = usd_cedi
ngn = usd_ngn
usd = 1 



# for rates in usd_exch_rates[vars]:
    
    # print(rates)
# version update my netxt stage of my program update 

""" 
stage 1:
create a class of object that carries properties of currencies in the list 
such as the the rates, currency id(name), index

stage 2:
recieve inputs from user such as the base_currency, selected_currency and the amount which is to be exchanged 
for each currency which is selected 
 iv been able to achieve these funtions and upgraded my algorithm 
 the next upgrade 


"""
        
usd_exch_rates = {
        "0": "USD",
        "usd_gbp":  gbp,
        "usd_eur":  eur,
        "3":  "AED",
        "4":  "CHF",
        "5": "CEDI",
        "usd_ngn":  ngn,
        "7":  "KWD"
        
    }


# # using a classes and object
# class currency_class:
#     def __init__(self, currency_id, currency_rates):
#         currency_id.self = currency_id
#         currency_rates.self = currency_rates
    
# class  pair:
#     def __init__(self, obj1):
#         self.obj1 = obj1

# exchange_class = currency_class
# # let assume the currency in  the list can be represented in dictionary
# # dict_currencies = {
# #     "usd" : currency[4],
# #       "name": currency_class.currency_id
# # }
# # print(rates.keys())
# currency_list = []
# for currency in rates:
#     # append the keys in the rates dictionary into the currency list
#     currency_list.append(currency)
    
# # Create a list of formatted strings
# formatted_list = [f"I: {index}, {value}" for index, value in enumerate(currency_list)]
# print(formatted_list)



# Print the list of formatted strings as a single string
 

    
    
usd_exch_rates = []
currency = [] 
 
for key in rates:
     usd_exch_rates.append(key)
for key, value in rates.items():
         key = value
         currency.append(key)
print(currency)
print(rates)

    
# print(usd_exch_rates)
# print(usd_exch_rates[9 ])
# for rates in currency :
#     print(rates)
# print(currency)
# print(""" 
#             Dollar USD (0)
#             Pound  PND (1)
#             Euro   EUR (2)
#             Franc  CHF (3)  
#             Dirham AED (4) 
#             Cedi   GHS (5)
#             Naira  NGN (6)
#             Dinar  KWD (7)
#         """)

start_decision = int(input("Are you ready to begin exchange with m program( 1 / 0) "))




# if base_currency == True :0
#     currency.remove(base_currency)

while start_decision == 1:
        base_currency = int(input("select a base currency you would want to trade with "))
        if base_currency <= len(currency):
            amount_usd = int(input(f"how much {usd_exch_rates[base_currency]} do you want to convert "))
            selected_currency = int(input("input a number to signify your choice of currency "))
            if selected_currency <= len(currency):
                print(len(currency))
                def excange_func(amount_usd , selected_currency, base_currency ):
                        if base_currency == 0 :
                            # currency.remove(usd) #removes the base currency which was selected 
                            # print(currency) 2
                            # print(usd_exch_rates)
                            
                            # this code suits when usd is used as the base currency 
                            converted_amount = amount_usd   *  currency[selected_currency]
                            result = round(converted_amount, 3)
                            print(usd_exch_rates[selected_currency], " " , str(result)) 
                            start_decision = int(input("Do you want to continue the exchange using my program( 1 / 0) "))
                            
                        elif base_currency== selected_currency:
                            converted_amount = amount_usd
                            result = round(converted_amount, 3)
                            print( usd_exch_rates[selected_currency] ,"", str(result))   
                            start_decision = int(input("Do you want to continue the exchange using my program( 1 / 0) "))
                        else:
                            # usd_exch_rates.remove(base)
                            # print(usd_exch_rates)
                            # this code condition is met when the currency used is not equal to usd 
                            converted_amount = (1/base_currency) * currency[selected_currency]
                            converted_amount = amount_usd * converted_amount
                            result = round(converted_amount, 3)
                            print( usd_exch_rates[selected_currency] ,"", str(result))   
                            start_decision = int(input("Do you want to continue the exchange using my program( 1 / 0) "))
                excange_func(  amount_usd , selected_currency, base_currency );
            else:
                print("this is a wrong value")    
                start_decision = int(input("Do you want to continue the exchange using my program( 1 / 0) "))         
        else:
            print("this is a wrong value")            
            start_decision = int(input("Do you want to continue the exchange using my program( 1 / 0)"))
if start_decision  != 1:
    print("this is a wrong input of value")
    start_decision = int(input("Do you want to continue the exchange using my program( 1 / 0) "))
    
    


# if number == True:
#     print(currency[number])
    
# else:
#     print ("this is a negative integer  ")
    