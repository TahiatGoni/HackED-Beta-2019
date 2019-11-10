#used for trial and error and experimentation
import calculations
import getDays
import masterData
import projectclasses
import matplotlib.pyplot as plt
rateList = []
dailyProduce = []
#'2019-11-11'
#'2019-11-29'
global total
global ideal
total = []
ideal = []
def getOrder():
    startDate = input("Enter order Date (YYYY-MM-DD): ")
    endDate = input("Enter delivery Date (YYYY-MM-DD): ")
    orderAmount = int(input("Enter order amount: "))
    totalDays = getDays.weekdays(startDate, endDate)
    calculations.NewOrder(masterData.clienta, masterData.producta, orderAmount)
    orderNumber = masterData.clienta.getLen()
    return totalDays, orderNumber, orderAmount
    

def handleData(totalDays, orderNumber):
    rate, amount, totalDays, produce = calculations.idealCalculations(masterData.clienta.pullOrders(orderNumber), totalDays)
    x = produce/masterData.clienta.pullOrders(orderNumber).getOrderName().getTime()
    total.append(x)
    dailyProduce.append(sum(total))
    ideal.append(rate/masterData.clienta.pullOrders(orderNumber).getOrderName().getTime())
    rateList.append(sum(ideal))
    calculations.suggestions(rate)
    masterData.clienta.pullOrders(orderNumber).updateAmount(amount)
    return amount, totalDays

if __name__ == '__main__':
    days, Number, amount = getOrder()
    while amount>0:
        amount, days = handleData(days, Number)
        plt.ion()
        plt.plot(rateList, '--ro')
        plt.plot(dailyProduce, '--bo')
        plt.draw()
        plt.pause(0.001)
    print("order complete")    

