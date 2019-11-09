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
        string = "Product: " + self.__name
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

    def updateAmount(self, produced):
        self.__amount = self.__amount - produced
    def __str__(self):
        string = "Product: " + self.__prodType + "Order Amount: " + self.__amount
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
    def getOrders(self):
        for element in self.__clientOrder:
            print(element)
    def __str__(self):
        string = "client: " + self.__client
        return string

        