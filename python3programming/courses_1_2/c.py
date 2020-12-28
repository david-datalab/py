rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rm = rainfall_mi.split(",")
#print(rm)
lst = list()
for i in rm:
	#print(int(i))
	flt_val = float(i)
	#print(flt_val)
	if flt_val >= 3.0:
		#print(flt_val)
		lst.append(flt_val)

num_rainy_months = len(lst)
print(num_rainy_months)