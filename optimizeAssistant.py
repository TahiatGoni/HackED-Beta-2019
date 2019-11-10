import multiTrack
import singleHandle
import projectclasses
import calculations
import getDays
orderBase = {}
print("welcome!")
client = multiTrack.setClient()
while True:
    print("current ", str(client))
    print("You can:\n1-add new order\n2-update order")
    print("3-set client\n4-set order number")
    activity = input("What would you like to do today? ")
    if activity == "1":
        totalDays, orderNumber, orderAmount = singleHandle.getOrder(client)
        key = str(client) + str(orderNumber)
        orderBase[key] = [totalDays, orderNumber, orderAmount]
        print(orderBase.keys())
    if activity ==     