from UpdateCatalog import catalog
from DownloadWebsite import GetProductSizeCode
from AnotherTestCurl import CheckAvalibility

ProductDB = catalog()

code = input("Provide product code: ")
size = input("Provide shoe size: ")

ProductSiteCode = ProductDB.getLink(code)
print(ProductSiteCode)

def ShowCompleteStock():
    StockEnquiry = ""
    Store = "Shop 10.18 World Square Shopping Centre, 644 George St"

    for x in range(3,13):
        for y in range(len(SizeProductCodes) - 1):
            if (len(SizeProductCodes[y]['products'])==0):
                StockEnquiry = StockEnquiry + SizeProductCodes[y]['label'] + str(" uk: 0 qty, ")
            else:
                APIrequest = CheckAvalibility(SizeProductCodes[y]['products'][0])
                
                for NewKey in APIrequest['data']:
                    storeSubject = str(NewKey['collectplace']['address'])
                    if (storeSubject == Store):
                        StockEnquiry = str(StockEnquiry) + str(SizeProductCodes[y]['label']) + str(" uk: ") + str(NewKey['collectplace']['freestock'] + str(" qty, "))
                        break


    print(StockEnquiry)


def SingleItemCheck():
    if (SizeProductCodes == None):
        print("Product isn't a shoe or doesn't exist")

    for x in range(len(SizeProductCodes) - 1):

        if (SizeProductCodes[x]['label'] == size):
            if (len(SizeProductCodes[x]['products'])>0):
                
                OutputText = CheckAvalibility(SizeProductCodes[x]['products'][0])

                print("\n")
                for key in OutputText:
                    for NewKey in OutputText[key]:
                        print(NewKey['collectplace']['address'] + " Stock: " + str(NewKey['collectplace']['freestock']))
                    break

                break
            else:
                print("Size " + size + " uk is out of stock.")
            
#ShowCompleteStock()
#SingleItemCheck()