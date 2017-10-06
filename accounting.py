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

MELON_COST = 1.00


customer1_expected = customer1_melons * melon_cost
if customer1_expected != customer1_paid:
    print customer1_name, "paid {:.2f}, expected {:.2f}".format(
        customer1_paid, customer1_expected)


def verify_customer_payment(text_file):
    """takes text file, returns info about customers who paid incorrectly"""
    
    data = open(text_file)

    for line in data:
        line = line.rstrip()
        customer_data_list = line.split('|')
        customer_id, customer_name, num_melons, customer_paid = customer_data_list
        customer_first_name = customer_name.split()[0]
        num_melons = float(num_melons)
        customer_paid = float(customer_paid)

        customer_expected = MELON_COST * num_melons
        # print customer_expected, "customer expected"
        # print customer_paid, "customer paid"
        if customer_expected < customer_paid:
            print customer_first_name, "overpaid. Should have paid {:.2f}, but paid {:.2f}".format(customer_expected, customer_paid)

        elif customer_expected > customer_paid:
            print customer_first_name, "underpaid. Should have paid {:.2f}, but paid {:.2f}".format(customer_expected, customer_paid)
    data.close()

        #     print customer_name, "paid {:.2f}, expected {:.2f}".format(customer_paid, customer_expected)


# # def check_customer_paid_correctly(customer_name, quantity_purchased, amount_paid):
# #     """if customer paid wrong amount of money, tells what they should ahve paid"""

# #         for line in data:
# #             line = line.rstrip()
# #             words = line.split('|')

# #         melon = words[0]
# #         count = words[1]
# #         amount = words[2]
#         pass

verify_customer_payment("customer-orders.txt")


