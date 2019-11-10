#part of main submission
#________________________________________________________
import masterData as MD        
import getDays as D
#________________________________________________________
def NewOrder(client, product, amount):
    """
    creates New order
    """
    client.addOrder(product, amount)

def finished1Day(totalRequired, remDays):
    """
    gets data about daily productivity
    and performs computations based on the input
    """
    produce = int(input("How was productivity today? "))
    totalRequired = totalRequired - produce
    remDays -= 1
    return totalRequired, remDays, produce

def idealCalculations(clientorder, days):
    orderAmount = clientorder.getAmount()
    # total hours required to fulfill the order
    totalRequired = orderAmount*clientorder.getOrderName().getTime()
    idealRate = (totalRequired)/days
    newTotal, newdays, produce = finished1Day(totalRequired, days)
    newAmount = newTotal/clientorder.getOrderName().getTime()
    return idealRate, newAmount, newdays, produce

def suggestions(idealRate):
    suggestedWorkers = round(int(idealRate)/8)
    print("The suggested worker allocation for this order is %d" % suggestedWorkers)


