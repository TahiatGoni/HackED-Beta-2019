import calculations
import getDays
import masterData
import projectclasses
import matplotlib.pyplot as plt
#'2019-11-11'
#'2019-11-29'
rateList = []
ratePlot = []
dailyproduce = []
productPlot = []
def getOrder(client):
    """
    Gets order
    """

    startDate = input("Enter order Date (YYYY-MM-DD): ")
    endDate = input("Enter delivery Date (YYYY-MM-DD): ")
    """
    clientName = input("Enter client Name: ")
    global client
    if clientName == "a":
        client = masterData.clienta
    elif clientName == "b":
        client = masterData.clientb
    """
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
    

def handleData(totalDays, orderNumber, client):
    """
    adjusts order information at the end of the day for a particular order
    """
    rate, amount, totalDays, produce = calculations.idealCalculations(client.pullOrders(orderNumber), totalDays)
    rateList.append(rate)
    dailyproduce.append(produce)
    calculations.suggestions(rate)
    client.pullOrders(orderNumber).updateAmount(amount)
    return amount, totalDays

def createPlot():
    ratePlot.append(sum(rateList))
    productPlot.append(sum(dailyproduce))
    plt.plot(ratePlot, '--ro')
    plt.plot(productPlot, '--bo')
    plt.draw()
    plt.pause(0.001)


if __name__ == '__main__':
    days, Number, amount = getOrder()
    while amount>0:
        amount, days = handleData(days, Number)
        createPlot()
    print("order complete")    

