#have y days, hours = y * 8
#have z workers, work time = yz * 8
#1 unit of product production takes say x hours
#l amount of units take = l * x hours
#________________________________________________________
import masterData as MD        
import getDays as D
#________________________________________________________
def NewOrder(client, product, amount):
    client.addOrder(product, amount)

def finished1Day(totalRequired, remDays):
    produce = int(input("How was productivity today? "))
    totalRequired = totalRequired - produce
    remDays -= 1
    return totalRequired, remDays

def idealCalculations(clientorder, days):
    orderAmount = clientorder.getAmount()
    # total hours required to fulfill the order
    totalRequired = orderAmount*clientorder.getOrderName().getTime()
    idealRate = (totalRequired)/days
    newTotal, newdays = finished1Day(totalRequired, days)
    newAmount = newTotal/clientorder.getOrderName().getTime()
    return idealRate, newAmount, newdays

def suggestions(idealRate):
    suggestedWorkers = round(int(idealRate)/8)
    print("The suggested worker allocation for this order is %d" % suggestedWorkers)

