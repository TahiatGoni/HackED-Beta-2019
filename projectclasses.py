class product:
    """
    product types are stored in this class
    """
    def __init__(self, productName, producingTime):
        """
        set name and production type
        """    
        self.__name = productName
        self.__time = producingTime
    def getName(self):
        return self.__name
    def getTime(self):
        return self.__time
    def __str__(self):
        string = "Product: " + str(self.__name)
        return string

class order:
    """
    the order info is stored in this class
    """
    def __init__(self, orderAmount, ordertype):
        try:
            if (isinstance(ordertype, product)):
                self.__prodType = ordertype
                self.__amount = orderAmount
            else:
                raise Exception("Order match Error")
        except Exception:
            print("%s is not a valid product" % ordertype)
    def getOrderName(self):
        return self.__prodType
    def getAmount(self):        
        return self.__amount
    def updateAmount(self, produced):
        self.__amount = produced
    def __str__(self):
        string = str(self.__prodType) + "\n Order Amount: " + str(self.__amount)
        return string
class client:
    """
    client info is stored in this class
    """
    def __init__(self, Name):
        self.__client = Name
        self.__clientOrder = []
    def addOrder(self, ordername, amount):
        self.__clientOrder.append(order(amount, ordername))
    def showOrders(self):
        i = 1
        for element in self.__clientOrder:
            print(i,"-",str(element))
            i += 1
    def getLen(self):
        return len(self.__clientOrder)
    def pullOrders(self, number):
        return self.__clientOrder[number - 1]
    def removeOrder(self, number):
        self.__clientOrder.pop(number-1)
    def __str__(self):
        string = "client: " + self.__client
        return string

        