#    a = int(rowww.get())
#    b = int(guyss.get())
#    c = int(zaddd.get())

def frst_fun(c):
	d = 4 #кол-во вариантов
	p = c//d #кол-во заданий на вариант
	k = 0
	l = " "
	g = " "
	import shutil
	import random

	for i in range(1,d + 1):
		while k != p + 1 :
			e = random.randint(1,c) #переменная для рандомности
			g = str(e)
			if l.find(g) == -1 or ((l.find(g) == -1 or l.find(g) == 1) and e > 9 ) or ((l.find(g) == -1 or l.find(g) == 1 or l.find(g) == 2) and e > 100):
				k = k + 1 #Кол-во заданий на вариант в данный момент
				l = str(l) + " " + str(g)
				input = open(str(e) + ".txt", "r")
				v = input.read()
				with open("var" + str(i) + ".txt", 'a') as file: 
					file.write(v + "\n")
				input.close()
				g = "sadsad"
			else:
				g = "sadsad"
		k = 0
		l = " "
		g = "sadasd"