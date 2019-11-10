# date
# deadline
# how many days; how many weekends; total weekdays; each worker works 9 hours per day; 9-6
# e.g. 50 workers; client requires 1000 specific products; each product needs 2 hours; total time needed 2000 hours
# 2000/(50*9)

# need ideal rate
# need real time rate calculator function for each day

# we have:
# - from class product; time to build one specific product unit; we have product name; dictionaary;

# create a function which takes in the current date and the specified deadline; outputs total weekdays available;
def weekdays(currentDate, deadline):
 	# input parameters are in string format: YYYY-MM-DD
 	# assume the company takes orders every monday
 	# assume 30 days in a month

 	CDateList = currentDate.split('-')
 	DDateList = deadline.split('-')
 	yearDiff = int(DDateList[0]) - int(CDateList[0])
 	monthDiff = int(DDateList[1]) - int(CDateList[1])

 	totalMonths = 0 
 	if monthDiff!=0:
 		for i in range(yearDiff+1):
 			if i == 0:
 				# current month int
 				totalMonths = totalMonths + 12 - int(CDateList[1].lstrip('0'))
 			elif i == yearDiff:
 				totalMonths = totalMonths + int(DDateList[1].lstrip('0'))
 			else:
 				totalMonths += 12

 	if int(CDateList[2].lstrip('0')) == int(DDateList[2].lstrip('0')):
 		totalDays = totalMonths*30
 	elif int(CDateList[2].lstrip('0')) < int(DDateList[2].lstrip('0')):
 		totalDays = totalMonths*30 + int(DDateList[2].lstrip('0')) - int(CDateList[2].lstrip('0'))
 	else:
 		totalDays = (totalMonths-1)*30 + 30 + int(DDateList[2].lstrip('0')) - int(CDateList[2].lstrip('0'))

 	try:
 		totalWeeks = totalDays//7
 		daysRemaining = totalDays % 7
 		weekends = totalWeeks*2
 	except ZeroDivisionError:
 		pass
 	finally:
 		if daysRemaining>5:
 			weekends += daysRemaining - 5

 		weekdays = totalDays - weekends
 		return weekdays

## input daily production in terms of hours koto ghonta kaaj hoise akdine 
# have total order amount, 
# inputs : (at the start of the day) the total no. of products left to be built, days remaining
# take input for # hours worked during the day
# we know: the numbers of hours required to build each product
"""
def finished1Day(remProducts, remDays, prodReq):
	# Number of hours worked during the day, workers should provide this input
	n =int(input('How many hours of work were done today? '))
	# Assume there is global variable named prodReq which represents the specific number of hours necessary to build each product
	remProducts = remProducts - n/prodReq
	remDays-=1
	return remProducts, remDays
"""

if __name__ == '__main__':
	print(weekdays('2019-12-09', '2020-01-05'))


