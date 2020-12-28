inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for item in inventory:
	item = item.split(",")
	goods = "the store has{quant} {goods}, each for{price} {cur}".format(quant = item[1], goods = item[0], price = item[2], cur = "USD.")
	print(goods)
