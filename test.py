import random

##tesla stock data
def stock_tesla_data_check():
    import urllib.request, json
    resp = urllib.request.urlopen('https://query2.finance.yahoo.com/v10/finance/quoteSummary/tsla?modules=price')
    data = json.loads(resp.read())
    price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
    print(price)

def iki_bilinmeyenli_denklem():
     
    print("2.Dereceden Bir Denklemin Kökünü Bulma")
    #y=ax^2+bx+c
 
    a=int(input("a : "))
    b=int(input("b : "))
    c=int(input("c : "))
 
    delta=b**2-4*a*c
 
    x1=(-b-delta**0.5)/(2*a)
    x2=(-b+delta**0.5)/(2*a)
 
    print("Birinci Kök : {}\nİkinci Kök : {}".format(x1,x2))

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nÖzyineleme örnek sonuçlar")
tri_recursion(5)