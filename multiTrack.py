import singleHandle as sh

def setClient():
    clientName = input("Enter client Name: ")
    if clientName == "a":
        client = sh.masterData.clienta
    elif clientName == "b":
        client = sh.masterData.clientb
    return client


if __name__ == '__main__':
    global client
    client = setClient()
    days, Number, amount = sh.getOrder(client)
    Number = switchToOrder(client)
    while amount>0:
        amount, days = sh.handleData(days, Number, client)
        sh.createPlot(client, Number)
    print("order complete")            