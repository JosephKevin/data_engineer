README

Using the following tables:

customers (customer_id INT, name VARCHAR)
1 COMPANY_A
2 COMPANY_B

orders(order_id INT, quantity INT, order_date
DATETIME[YYYY-MM-DD], customer_id INT)
1002 12 2015-01-01 2
1003 8 2015-01-01 1
1003 9 2015-01-02 1
1003 62 2015-01-02 3


1. Write a query to select the name of each customer and his or her latest order date, eg
	COMPANY_A 2016-01-02
	COMPANY_B 2016-01-06
2. We want to find out which customers have changed their behaviour the most from one
   order to the next. Write a query using a window function that shows, for each customer,
   the largest absolute change in quantity (positive or negative) between orders. Caveats:
	a. If two orders for a customer occur on the same day, consider them one order with
		the sum as the quantity.
	b. Days when a customer has not ordered anything should not be considered at all,
		as opposed to considering them 0 quantity.
	c. Ignore the theoretical increase between the time they were not a customer and
		their first order, as well as customers that may only have one order.
	
	COMPANY_A 2016-01-03 -23
	COMPANY_B 2016-01-02 15