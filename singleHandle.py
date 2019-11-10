import calculations
import getDays
import masterData
import projectclasses
#'2019-11-11'
#'2019-11-29'
def getOrder():
    startDate = input("Enter order Date (YYYY-MM-DD): ")
    endDate = input("Enter delivery Date (YYYY-MM-DD): ")
    clientName = input("Enter client Name: ")
    if clientName == "a":
        global client
        client = masterData.clienta
    productName = input("Enter order Name: ")
    if productName == "a":
        product = masterData.producta
    elif productName == "b":
        product = masterData.productb
    elif productName == "c":
        product = masterData.productc
    orderAmount = int(input("Enter order amount: "))
    totalDays = getDays.weekdays(startDate, endDate)
    calculations.NewOrder(client, product, orderAmount)
    orderNumber = client.getLen()
    return totalDays, orderNumber, orderAmount
    

def handleData(totalDays, orderNumber):
    rate, amount, totalDays, produce = calculations.idealCalculations(client.pullOrders(orderNumber), totalDays)
    calculations.suggestions(rate)
    client.pullOrders(orderNumber).updateAmount(amount)
    return amount, totalDays

if __name__ == '__main__':
    days, Number, amount = getOrder()
    while amount>0:
        amount, days = handleData(days, Number)
    print("order complete")    

