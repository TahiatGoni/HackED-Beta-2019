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

def idealCalculations(clientorder, days):
    orderAmount = clientorder.getAmount()
    totalRequired = orderAmount*clientorder.getOrderName().getTime()
    idealRate = (totalRequired)/days

    return idealRate

def suggestions(idealRate):
    suggestedWorkers = round(idealRate/8)
    print("The suggested worker allocation for this order is %d" % suggestedWorkers)






