import multiTrack
import singleHandle
import projectclasses
import calculations
import getDays
import matplotlib.pyplot as plt
orderBase = {}
print("welcome!")
client = multiTrack.setClient()
amount = 0
while True:
    print("\n\n")
    print("current ", str(client))
    print("\n")
    print("You can:\n1-add new order\n2-update order")
    print("3-set client\n4-Show data\n5-exit")
    activity = input("What would you like to do today? ")
    if activity == "1":
        totalDays, orderNumber, orderAmount = singleHandle.getOrder(client)
        key = str(client) + str(orderNumber)
        orderBase[key] = [totalDays, orderNumber, orderAmount]
        print(orderBase.keys())
    if activity == "2":
        key = input("Enter the order detals(client: <name><number>): ")
        amount, totalDays = singleHandle.handleData(orderBase[key][0],orderBase[key][1],client)
        orderBase[key][0] = totalDays
        plt.clf()
        singleHandle.createPlot(client, orderBase[key][1])
        if amount <=0:
            client.removeOrder(orderBase[key][1])
            del orderBase[key]
            print("order complete!")
    if activity == "3":
        client = multiTrack.setClient()
    if activity == "4":
        client.showOrders()
    if activity == "5":
        exit()     