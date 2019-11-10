import calculations
import getDays
import masterData
import projectclasses
#'2019-11-11'
#'2019-11-29'
startDate = input("Enter order Date (YYYY-MM-DD): ")
endDate = input("Enter delivery Date (YYYY-MM-DD): ")
totalDays = getDays.weekdays(startDate, endDate)
calculations.NewOrder(masterData.clienta, masterData.producta, 1000)
print("initialize with 0")
rate, amount, totalDays = calculations.idealCalculations(masterData.clienta.pullOrders(1), totalDays)

initialWorkers = calculations.suggestions(rate)
amount = masterData.clienta.pullOrders(1).getAmount()
while amount>0:
    rate, amount, totalDays = calculations.idealCalculations(masterData.clienta.pullOrders(1), totalDays)
    print(rate)
    print(calculations.suggestions(rate))
    masterData.clienta.pullOrders(1).updateAmount(amount)

print("order complete!")