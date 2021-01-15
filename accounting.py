melon_cost = 1.00

customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00





# define melon_cost globally because it may be used in business's program more than just this specfic function

melon_cost = 1.00
# create a function that takes in a text file of customer orders 
def customer_acccounting(customer_orders):
    """ calculate the amount a customer has either overpaid/underpaid"""
# open a file of customer info -- use pythondocs for help here--- do need to include r or w???
customer_orders= open("customer-orders.txt")
#iterate through each customer order ---name -melons bought- and price paid
for line in customer_orders:
    customer_order = line.split('|')
    customer_name = customer_order[1]
    num_melons = customer_order[2]
    melon_cost = customer_order[3]
    # define what customer is expected to pay by number of melons purchased multiplied by cost of melons
    customer_expected = float(num_melons) * float(melon_cost)
  #implement an if statement that will work for any number of customers/values entered - cutting down on repetition of previous code
  #add in float so that index[3] gets processed from str --> float
    if customer_expected != float(melon_cost): 
        if customer_expected > float(melon_cost):
            #return a statement for Underpaying customers
            print(f"{customer_name} paid ${float(melon_cost):.2f},",
            f"Customer underpaid for melons! ${customer_expected:.2f}")
        else: 
            #return statement if they overpaid
            print(f"{customer_name} paid ${float(melon_cost):.2f},",
            f"Customer overpaid for melons! ${customer_expected:.2f}")
    else: # return statement if they paid correctly
        print(f"{customer_name} paid ${float(melon_cost):.2f},",
        f"Customer paid for melons ${customer_expected:.2f}")
  

