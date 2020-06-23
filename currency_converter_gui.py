from tkinter import *
import requests
import simplejson as json

root = Tk()

Variable1 = StringVar(root)
Variable2 = StringVar(root)

Variable1.set('currency')
Variable2.set('currency')

def realtimecurrencyConverter():
    from_currency = Variable1.get()
    to_currency = Variable2.get()
    api_key = "Your API KEY"
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
  
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key

    req_ob = requests.get(main_url)
    result = req_ob.json()
    exchange_rate = float(result['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    amount = float(Amount1_field.get())
    new_amount = round(amount * exchange_rate, 3)

    Amount2_field.insert(0, str(new_amount))

def clear_all():
    Amount1_field.delete(0, END)
    Amount2_field.delete(0, END)

if __name__ == "__main__":
    root.configure(background = "light green")

    root.geometry('550x400')
    image1 = PhotoImage(file = "D:\\PYTHON PROGRAMS\\currency_converter\\currency.png")
    label_for_image = Label(root , image=image1)
    label_for_image.place(x=0,y=0, relwidth=1, relheight=1)
    headlabel = Label(root, text="Welcome to currency converter", font = 'cursive', bg = 'light blue', fg = 'black')
    label1 = Label(root, text = "Amount :", fg = 'black', bg = 'light pink') 
      
    label2 = Label(root, text = "From Currency",  
                   fg = 'black', bg = 'light pink')  
    
    label3 = Label(root, text = "To Currency :",  
                   fg = 'black', bg = 'light pink') 
  
    label4 = Label(root, text = "Converted Amount :",  
                   fg = 'black', bg = 'light pink')

    headlabel.grid(row = 0, column = 1)  
    label1.grid(row = 1, column = 0)  
    label2.grid(row = 2, column = 0) 
    label3.grid(row = 3, column = 0) 
    label4.grid(row = 5, column = 0, ipadx = '15')

    Amount1_field = Entry(root)  
    Amount2_field = Entry(root) 
    Amount1_field.grid(row = 1, column = 1, ipadx ="25")  
    Amount2_field.grid(row = 5, column = 1, ipadx ="25") 
    
    CurrenyCode_list = ['AFN', 'ALL', 'DZD', 'USD', 'EUR', 'AOA', 'XCD', 'ARS', 'AMD', 'AWG', 'AUD', 'AZN', 'BSD', 'BHD', 'BDT', 'BBD', 'BYN', 'BZD', 'XOF', 'BMD', 'BTN', 'INR', 'BOB', 'BOV', 'BAM', 'BWP', 'NOK', 'BRL', 'BND', 'BGN', 'BIF', 'CVE', 'KHR', 
'XAF', 'CAD', 'KYD', 'CLF', 'CLP', 'CNY', 'COP', 'COU', 'KMF', 'CDF', 'NZD', 'CRC', 'HRK', 'CUC', 'CUP', 'ANG', 'CZK', 'DKK', 'DJF', 'DOP', 'EGP', 'SVC', 'ERN', 'ETB', 'FKP', 'FJD', 'XPF', 'GMD', 'GEL', 'GHS', 'GIP', 'GTQ', 'GBP','KPW', 'KRW', 'KWD', 'KGS', 'LAK', 'LBP', 'LSL', 'ZAR', 'LRD', 'LYD', 'CHF', 'MOP', 'MGA', 'MWK', 'MYR', 'MVR', 'MRU', 'MUR', 'XUA', 'MXN', 'MXV', 'MDL', 'MNT', 'MAD', 'MZN', 'MMK', 'NAD', 'NPR', 'NIO', 'NGN', 'OMR', 'PKR', 'PAB', 'PGK', 'PYG', 'PEN', 'PHP', 'PLN', 'QAR', 'MKD', 'RON', 'RUB', 'RWF', 'SHP', 'WST', 'STN', 'SAR', 'RSD', 'SCR', 'SLL', 'SGD', 'XSU', 'SBD', 'SOS', 'SSP', 'LKR', 'SDG', 'SRD', 'SZL', 'SEK', 'CHE', 'CHW', 'SYP', 'TWD', 'TJS', 'TZS', 
'THB', 'TOP', 'TTD', 'TND', 'TRY', 'TMT', 'UGX', 'UAH', 'AED', 'USN', 'UYI', 'UYU', 'UZS', 'VUV', 'VEF', 'VND', 'YER', 'ZMW', 'ZWL']
    FromCurrency_option = OptionMenu(root, Variable1, *CurrenyCode_list) 
    ToCurrency_option = OptionMenu(root, Variable2, *CurrenyCode_list) 

    FromCurrency_option.grid(row = 2, column = 1, ipadx = 10) 
    ToCurrency_option.grid(row = 3, column = 1, ipadx = 10) 
      
    button1 = Button(root, text = "Convert", bg = "red", fg = "black", 
                                command = realtimecurrencyConverter) 
      
    button1.grid(row = 4, column = 1) 
  
    button2 = Button(root, text = "Clear", bg = "red",  
                     fg = "black", command = clear_all) 
    button2.grid(row = 6, column = 1) 
    
    root.mainloop()  
