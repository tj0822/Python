# def printMyAddress():
#     print "Warren Sande"
#     print "123 Main Street"
#     print "Ottawa, Ontario, Canada"
#     print "K2M 2E9"
#     print
#
# printMyAddress()



def calculateTax(price, tax_rate):
    taxTotal = price + (price * tax_rate)
    return taxTotal

my_price = float(raw_input("Enter a price : "))

totalPrice = calculateTax(my_price, 0.06)

print "price = ", my_price, " Total price = ", totalPrice



