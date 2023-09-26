# creating an algorithm that converts different currencies to another based on their rates 

# stage 1:
#prompt user to make a choice on which universal currency to select 

# stage 2:
# recieve amount of money in the seleted universal currency  

# stage  3:
# make a choice between various currency which you want to be converted to 

# stage 4:    
# conversion of the recieved amount in the selected universal currency to the desired currency 

# stage6:
# run and test
# from usd_exch_rates import offline_rates

from api_key import usd_exch_rates

# amount = int(input("how much do you want to convert"))

# def excange_func(amount_usd , universal_currency ):
#     converted_amount = amount_usd * usd_exch_rates["usd_kwd"]
#     result = round(converted_amount, 3)
#     print("KWD "+str(result))
    
# excange_func(amount, "dollar");




start_decision = input(str("Are you ready to begin currency conversion using my algoraithm (Yes/No)  "))
while start_decision == "yes":
    if start_decision == "Yes" or start_decision == "yes" or start_decision == "YES" :
        print("lets begin to exchange")     
        Universal_currency = input(str("""pick a currency you would take as your standard currency to perform your exchanges. Notice!! indicate your choice of input with the numbers provided
            Dollar USD (1)
            Pound  PND (2)
            Euro   EUR (3)
            Franc  CHF (4)  
            Dirham AED (5) 
            Cedi   GHS (6)
            Naira  NGN (7)
            Dinar  KWD (8)
    """))
        # def exchange_func():
            
        if Universal_currency == "USD" or Universal_currency == "1":
            Amount_Usd = float(input("How much dollar would you want to convert  "))
            print(""" 
                (KWD) kuwaiti dinar 
                (GBP) British pound sterling 
                (EUR) Euro  
                (CHF) Swiss Franc
                (AED) Uae dirham   
                (GHS) Ghanian cedi 
                (NGN) Nigerian naira
                """)
            new_currency = str(input("what currency would you want to convert your dollar to.(Notice!!! represent it with the given abreviation to avoid error.) "))
            if new_currency == "KWD" or new_currency == "kwd":
                converted_amount = Amount_Usd * usd_exch_rates["usd_kwd"]
                result = round(converted_amount, 3)
                print("KWD "+str(result))
                
            elif new_currency =="GBP" or new_currency =="gbp":
                converted_amount = Amount_Usd * usd_exch_rates["usd_gbp"]
                result = round(converted_amount, 3)
                print("GBP "+str(result))
                
            elif new_currency =="EUR" or new_currency =="eur":
                result = round(converted_amount, 3)
                print("EUR "+str(result))
                
            elif new_currency =="CHF" or new_currency =="chf":
                converted_amount = Amount_Usd * usd_exch_rates["usd_chf"]
                result = round(converted_amount, 3)
                print("CHF "+str(result))
                
            elif new_currency =="AED" or new_currency =="aed":
                converted_amount = Amount_Usd * usd_exch_rates["usd_aed"]
                result = round(converted_amount, 3)
                print("AED "+str(result))
                
            elif new_currency =="GHS" or new_currency =="ghs":
                converted_amount = Amount_Usd * usd_exch_rates[ "usd_cedi"]
                result = round(converted_amount, 3)
                print("GHS "+str(result))
                
            elif new_currency =="NGN" or new_currency =="ngn":
                converted_amount = Amount_Usd * usd_exch_rates["usd_ngn" ]
                result = round(converted_amount, 3)
                print("NGN "+str(result))
            else:
                print("Wrong input!! please check your value.");    
            start_decision = input(str("Do you want to do more conversion (Yes/No)  "))
# pounds exchange
        elif  Universal_currency == "PND" or Universal_currency == "2" :
            Amount_Usd = float(input("How much Pound would you want to convert  "))
            print("""  
                    (USD) United states dollar
                    (KWD) kuwaiti dinar 
                    (EUR) Euro  
                    (CHF) Swiss Franc 
                    (AED) Uae dirham   
                    (GHS) Ghanian cedi 
                    (NGN) Nigerian naira
                    """)
            new_currency = str(input("what currency would you want to convert your pound to.(Notice!!! represent it with the given abreviation to avoid error.) "))
            if new_currency == "KWD" or new_currency == "kwd":
                calc_updated_currency = (1/usd_exch_rates["usd_gbp"]) * usd_exch_rates["usd_kwd"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("KWD "+str(result))
                
            elif new_currency =="USD" or new_currency =="usd":
                calc_updated_currency = (1/usd_exch_rates["usd_gbp"]) 
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("USD "+str(result))
                
            elif new_currency =="EUR" or new_currency =="eur":
                calc_updated_currency = (1/usd_exch_rates["usd_gbp"]) * usd_exch_rates["usd_eur"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("EUR "+str(result))
                
            elif new_currency =="CHF" or new_currency =="chf":
                calc_updated_currency = (1/usd_exch_rates["usd_gbp"]) * usd_exch_rates["usd_chf"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("BTC "+str(result))
            
            elif new_currency =="AED" or new_currency =="aed":
                calc_updated_currency = (1/usd_exch_rates["usd_gbp"]) * usd_exch_rates["usd_aed"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("AED "+str(result))
            
            elif new_currency =="GHS" or new_currency =="ghs":
                calc_updated_currency = (1/usd_exch_rates["usd_gbp"]) * usd_exch_rates["usd_cedi"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("GHS "+str(result))
            
            elif new_currency =="NGN" or new_currency =="ngn":
                calc_updated_currency = (1/usd_exch_rates["usd_gbp"]) * usd_exch_rates["usd_ngn"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("NGN "+str(result))   
            else:
                print("Wrong input!! please check your value.");
            start_decision = input(str("would you want to continue currency conversion using my algorithm (Yes/No)  "))
        
            
# Euro exchange
        elif  Universal_currency == "EUR" or Universal_currency == "3" :
            Amount_Usd = float(input("How much euro would you want to convert  "))
            print(""" 
                    (KWD) kuwaiti dinar 
                    (USD) United states dollar
                    (GBP) British pound sterling  
                    (CHF) Swiss Franc 
                    (AED) Uae dirham   
                    (GHS) Ghanian cedi 
                    (NGN) Nigerian naira
                    """)
            new_currency = str(input("what currency would you want to convert your euro to.(Notice!!! represent it with the given abreviation to avoid error.) "))
            if new_currency == "KWD" or new_currency == "kwd":
                calc_updated_currency = (1/usd_exch_rates["usd_eur"]) * usd_exch_rates["usd_kwd"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("KWD "+str(result))
                
            elif new_currency =="USD" or new_currency =="usd":
                calc_updated_currency = (1/usd_exch_rates["usd_eur"]) 
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("USD "+str(result))
                
            elif new_currency =="GBP" or new_currency =="gbp":
                calc_updated_currency = (1/usd_exch_rates["usd_eur"]) * usd_exch_rates["usd_gbp"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("GBP "+str(result))
                
            elif new_currency =="CHF" or new_currency =="chf":
                calc_updated_currency = (1/usd_exch_rates["usd_eur"]) * usd_exch_rates["usd_chf"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("CHS "+str(result))
                
            elif new_currency =="AED" or new_currency =="aed":
                calc_updated_currency = (1/usd_exch_rates["usd_eur"]) * usd_exch_rates["usd_aed"] 
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("AED "+str(result))
                
            elif new_currency =="GHS" or new_currency =="ghs":
                calc_updated_currency = (1/usd_exch_rates["usd_eur"]) * usd_exch_rates["usd_cedi"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("GHS "+str(result))
                
            elif new_currency =="NGN" or new_currency =="ngn":
                calc_updated_currency = (1/usd_exch_rates["usd_eur"]) * usd_exch_rates["usd_ngn"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("NGN "+str(result))
            else:
                print("Wrong input!! please check your value.");
            start_decision = input(str("would you want to continue currency conversion using my algorithm (Yes/No)  ")) 
        
# swiss franc exchange
        elif  Universal_currency == "CHF" or Universal_currency == "4" :
            Amount_Usd = float(input("How much franc would you want to convert  "))
            print(""" 
                    (KWD) kuwaiti dinar 
                    (USD) United states dollar
                    (GBP) British pound sterling  
                    (EUR) Euro 
                    (AED) Uae dirham   
                    (GHS) Ghanian cedi 
                    (NGN) Nigerian naira
                    """)
            new_currency = str(input("what currency would you want to convert your franc to.(Notice!!! represent it with the given abreviation to avoid error.) "))
            if new_currency == "KWD" or new_currency == "kwd":
                calc_updated_currency = (1/usd_exch_rates["usd_chf"]) * usd_exch_rates["usd_kwd"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("KWD "+str(result))
                
            elif new_currency =="USD" or new_currency =="usd":
                calc_updated_currency = (1/usd_exch_rates["usd_chf"]) 
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("USD "+str(result))
                
            elif new_currency =="GBP" or new_currency =="gbp":
                calc_updated_currency = (1/usd_exch_rates["usd_chf"]) * usd_exch_rates["usd_gbp"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("GBP "+str(result))
                
            elif new_currency =="EUR" or new_currency =="eur":
                calc_updated_currency = (1/usd_exch_rates["usd_chf"]) * usd_exch_rates["usd_eur"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("EUR "+str(result))
                
            elif new_currency =="AED" or new_currency =="aed":
                calc_updated_currency = (1/usd_exch_rates["usd_chf"]) * usd_exch_rates["usd_aed"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("AED "+str(result))
                
            elif new_currency =="GHS" or new_currency =="ghs":
                calc_updated_currency = (1/usd_exch_rates["usd_chf"]) * usd_exch_rates["usd_cedi"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("GHS "+str(result))
                
            elif new_currency =="NGN" or new_currency =="ngn":
                calc_updated_currency = (1/usd_exch_rates["usd_chf"]) * usd_exch_rates["usd_ngn"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("NGN "+str(result))
            else:
                print("Wrong input!! please check your value.");
            start_decision = input(str("would you want to continue currency conversion using my algorithm (Yes/No)  ")) 
        
        elif  Universal_currency == "AED" or Universal_currency == "5" :
            Amount_Usd = float(input("How much dirham would you want to convert  "))
            print(""" 
                    (KWD) kuwaiti dinar 
                    (USD) United states dollar
                    (GBP) British pound sterling  
                    (CHF) Swiss Franc 
                    (EUR) Euro   
                    (GHS) Ghanian cedi 
                    (NGN) Nigerian naira
                    """)
            new_currency = str(input("what currency would you want to convert your dirham to.(Notice!!! represent it with the given abreviation to avoid error.) "))
            if new_currency == "KWD" or new_currency == "kwd":
                calc_updated_currency = (1/usd_exch_rates["usd_aed"]) * usd_exch_rates["usd_kwd"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("KWD "+str(result))
                
            elif new_currency =="USD" or new_currency =="usd":
                calc_updated_currency = (1/usd_exch_rates["usd_aed"]) 
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("USD "+str(result))
                
            elif new_currency =="GBP" or new_currency =="gbp":
                calc_updated_currency = (1/usd_exch_rates["usd_aed"]) * usd_exch_rates["usd_gbp"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("GBP "+str(result))
                
            elif new_currency =="EUR" or new_currency =="eur":
                calc_updated_currency = (1/usd_exch_rates["usd_aed"]) * usd_exch_rates["usd_eur"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("EUR "+str(result))
                
            elif new_currency =="CHF" or new_currency =="chf":
                calc_updated_currency = (1/usd_exch_rates["usd_aed"]) * usd_exch_rates["usd_chf"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("CHF "+str(result))
                
            elif new_currency =="GHS" or new_currency =="ghs":
                calc_updated_currency = (1/usd_exch_rates["usd_aed"]) * usd_exch_rates["usd_cedi"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("GHS "+str(result))
                
            elif new_currency =="NGN" or new_currency =="ngn":
                calc_updated_currency = (1/usd_exch_rates["usd_aed"]) * usd_exch_rates["usd_ngn"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("NGN "+str(result))
            else:
                print("Inorrect input of value");
            start_decision = input(str("Do you want to embark on your  currency conversion using my algorithm (Yes/No)  "))
            
        elif  Universal_currency == "GHS" or Universal_currency == "6" :
            Amount_Usd = float(input("How much cedi would you want to convert  "))
            print(""" 
                    (KWD) kuwaiti dinar 
                    (USD) United states dollar
                    (GBP) British pound sterling  
                    (CHF) Swiss Franc 
                    (AED) Uae dirham   
                    (EUR) Euro 
                    (NGN) Nigerian naira
                    """)
            new_currency = str(input("what currency would you want to convert your cedi to.(Notice!!! represent it with the given abreviation to avoid error.) "))
            if new_currency == "KWD" or new_currency == "kwd":
                calc_updated_currency = (1/usd_exch_rates["usd_cedi"]) * usd_exch_rates["usd_kwd"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("KWD "+str(result))
                
            elif new_currency =="USD" or new_currency =="usd":
                calc_updated_currency = (1/usd_exch_rates["usd_cedi"]) 
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("USD "+str(result))
                
            elif new_currency =="GBP" or new_currency =="gbp":
                calc_updated_currency = (1/usd_exch_rates["usd_cedi"]) * usd_exch_rates["usd_gbp"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("GBP "+str(result))
                
            elif new_currency =="EUR" or new_currency =="eur":
                calc_updated_currency = (1/usd_exch_rates["usd_cedi"]) * usd_exch_rates["usd_eur"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("EUR "+str(result))
                
            elif new_currency =="CHF" or new_currency =="chf":
                calc_updated_currency = (1/usd_exch_rates["usd_cedi"]) * usd_exch_rates["usd_chf"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("CHF "+str(result))
                
            elif new_currency =="AED" or new_currency =="aed":
                calc_updated_currency = (1/usd_exch_rates["usd_cedi"]) * usd_exch_rates["usd_aed"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("AED "+str(result))
                
            elif new_currency =="NGN" or new_currency =="ngn":
                calc_updated_currency = (1/usd_exch_rates["usd_cedi"]) * usd_exch_rates["usd_ngn"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("NGN "+str(result))
            else:
                print("Inorrect input of value");
            start_decision = input(str("Do you want to embark on your  currency conversion using my algorithm (Yes/No)  "))     
            
        elif  Universal_currency == "NGN" or Universal_currency == "7" :
            Amount_Usd = float(input("How much naira would you want to convert  "))
            print(""" 
                    (KWD) kuwaiti dinar 
                    (USD) United states dollar
                    (GBP) British pound sterling  
                    (CHF) Swiss Franc 
                    (AED) Uae dirham   
                    (EUR) Euro 
                    (GHS) Ghanian cedi
                    """)
            new_currency = str(input("what currency would you want to convert your naira to.(Notice!!! represent it with the given abreviation to avoid error.) "))
            if new_currency == "KWD" or new_currency == "kwd":
                calc_updated_currency = (1/usd_exch_rates["usd_ngn"]) * usd_exch_rates["usd_kwd"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("KWD "+str(result))
                
            elif new_currency =="USD" or new_currency =="usd":
                calc_updated_currency = (1/usd_exch_rates["usd_ngn"]) 
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("USD "+str(result))
                
            elif new_currency =="GBP" or new_currency =="gbp":
                calc_updated_currency = (1/usd_exch_rates["usd_ngn"]) * usd_exch_rates["usd_gbp"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("GBP "+str(result))
                
            elif new_currency =="EUR" or new_currency =="eur":
                calc_updated_currency = (1/usd_exch_rates["usd_ngn"]) * usd_exch_rates["usd_eur"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("EUR "+str(result)) 
                
            elif new_currency =="CHF" or new_currency =="chf":
                calc_updated_currency = (1/usd_exch_rates["usd_ngn"]) * usd_exch_rates["usd_chf"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("CHF "+str(result))
                
            elif new_currency =="AED" or new_currency =="aed":
                calc_updated_currency = (1/usd_exch_rates["usd_ngn"]) * usd_exch_rates["usd_aed"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("GHS "+str(result))
                
            elif new_currency =="GHS" or new_currency =="ghs":
                calc_updated_currency = (1/usd_exch_rates["usd_ngn"]) * usd_exch_rates["usd_cedi"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("GHS "+str(result))
            else:
                 print("incorrect input of value ")
            start_decision = input(str("Do you want to embark on your  currency conversion using my algorithm (Yes/No)  "))
        
        elif  Universal_currency == "KWD" or Universal_currency == "8" :
            Amount_Usd = float(input("How much dinar would you want to convert  "))
            print("""  
                    (USD) United states dollar
                    (GBP) British pound sterling  
                    (CHF) Swiss Franc 
                    (AED) Uae dirham   
                    (EUR) Euro 
                    (NGN) Nigerian naira
                    (GHS) Ghanian cedi
                    """)
            new_currency = str(input("what currency would you want to convert your dinar to.(Notice!!! represent it with the given abreviation to avoid error.) "))
            if new_currency == "NGN" or new_currency == "ngn":
                calc_updated_currency = (1/usd_exch_rates["usd_kwd"]) * usd_exch_rates["usd_ngn"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("NGN "+str(result))
                
            elif new_currency =="USD" or new_currency =="usd":
                calc_updated_currency = (1/usd_exch_rates["usd_kwd"]) 
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("USD "+str(result))
                
            elif new_currency =="GBP" or new_currency =="gbp":
                calc_updated_currency = (1/usd_exch_rates["usd_kwd"]) * usd_exch_rates["usd_gbp"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("GBP "+str(result))
                
            elif new_currency =="EUR" or new_currency =="eur":
                calc_updated_currency = (1/usd_exch_rates["usd_kwd"]) * usd_exch_rates["usd_eur"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("EUR "+str(result)) 
                
            elif new_currency =="CHF" or new_currency =="chf":
                calc_updated_currency = (1/usd_exch_rates["usd_kwd"]) * usd_exch_rates["usd_chf"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("CHF "+str(result))
                
            elif new_currency =="AED" or new_currency =="aed":
                calc_updated_currency = (1/usd_exch_rates["usd_kwd"]) * usd_exch_rates["usd_aed"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("AED "+str(result))
                
            elif new_currency =="GHS" or new_currency =="ghs":
                calc_updated_currency = (1/usd_exch_rates["usd_kwd"]) * usd_exch_rates["usd_cedi"]
                converted_amount = Amount_Usd * calc_updated_currency
                result = round(converted_amount, 3)
                print("GHS "+str(result))
            else:
                 print("incorrect input of value ")
            start_decision = input(str("Do you want to embark on your  currency conversion using my algorithm (Yes/No)  "))
        else:
            print("wrong input of value ")
else:
    start_decision="no"
    print("thanks for running my program")