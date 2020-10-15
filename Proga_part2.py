#    a = int(rowww.get())
#    b = int(guyss.get())
#    c = int(zaddd.get())

def scnd_fun(a,b):
	z = b // a #Кол-во парт(рядов)
	pr = " "
	if a % 2 == 0 or a == 0:
		for i in range(z):
			if i % 2 == 0 or i == 0:
				for x in range(a):
					if x % 4 == 0:
						pr = str(pr) + "1" + " "
					elif x % 4 == 1:
						pr = str(pr) + "2" + " "
					elif x % 4 == 2:
						pr = str(pr) + "3" + " "
					elif x % 4 == 3:
						pr = str(pr) + "4" + " "
			else:
				for x in range(a):
					if x % 4 == 0:
						pr = str(pr) + "4" + " "
					elif x % 4 == 1:
						pr = str(pr) + "3" + " "
					elif x % 4 == 2:
						pr = str(pr) + "2" + " "
					elif x % 4 == 3:
						pr = str(pr) + "1" + " "
			print(str(pr))
			pr = " "
		gr=b - a*z
		if (gr > 0) and (z % 2 == 0):
			for x in range(gr):
				if x % 4 == 0:
					pr = str(pr) + "1" + " "
				elif x % 4 == 1:
					pr = str(pr) + "2" + " "
				elif x % 4 == 2:
					pr = str(pr) + "3" + " "
				elif x % 4 == 3:
					pr = str(pr) + "4" + " "
			print(pr)
		elif (gr > 0) and (z % 2 == 1):
			for x in range(gr):
				if x % 4 == 0:
					pr = str(pr) + "4" + " "
				elif x % 4 == 1:
					pr = str(pr) + "3" + " "
				elif x % 4 == 2:
					pr = str(pr) + "2" + " "
				elif x % 4 == 3:
					pr = str(pr) + "1" + " "
			print(str(pr))








	if a % 2 == 1 or a == 0:
		for i in range(z):
			if i % 2 == 0 or i == 0:
				for x in range(a):
					if x % 4 == 0:
						pr = str(pr) + "1" + " "
					elif x % 4 == 1:
						pr = str(pr) + "2" + " "
					elif x % 4 == 2:
						pr = str(pr) + "3" + " "
					elif x % 4 == 3:
						pr = str(pr) + "4" + " "
			else:
				for x in range(a):
					if x % 4 == 0:
						pr = str(pr) + "4" + " "
					elif x % 4 == 1:
						pr = str(pr) + "1" + " "
					elif x % 4 == 2:
						pr = str(pr) + "2" + " "
					elif x % 4 == 3:
						pr = str(pr) + "3" + " "
			print(str(pr))
			pr = " "
		gr=b - a*z
		if (gr > 0) and (z % 2 == 0):
			for x in range(gr):
				if x % 4 == 0:
					pr = str(pr) + "1" + " "
				elif x % 4 == 1:
					pr = str(pr) + "2" + " "
				elif x % 4 == 2:
					pr = str(pr) + "3" + " "
				elif x % 4 == 3:
					pr = str(pr) + "4" + " "
			print(pr)
		elif (gr > 0) and (z % 2 == 1):
			for x in range(gr):
				if x % 4 == 0:
					pr = str(pr) + "4" + " "
				elif x % 4 == 1:
					pr = str(pr) + "1" + " "
				elif x % 4 == 2:
					pr = str(pr) + "2" + " "
				elif x % 4 == 3:
					pr = str(pr) + "3" + " "
			print(str(pr))

