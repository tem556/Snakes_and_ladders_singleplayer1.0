# day_5_calc.py
# Temoor Tanveer
# 2020-07-13
# Used this website to learn about import datetime : https://www.w3schools.com/python/python_datetime.asp
from datetime import datetime
file =open("calc_logs.txt", "a")


class Calculator :

    def __init__(self):
        self.result = 0
        file.write(""+str(datetime.now())+": The user has initiated a new calculator\n")

    def Add (self,x):
        self.result+=x
        file.write(""+str(datetime.now())+": add: the user has added "+str(x)+" to the result\n")

    def substract (self,a):
        self.result-=a
        file.write(""+str(datetime.now())+": add: the user has subtracted " + str(a) + " to the result\n")

    def get_result (self):
        file.write(""+str(datetime.now())+": get_result: the user has returned the result variable which is equal to "+str(self.result)+"\n")
        return self.result
a=Calculator()
a.substract(55)
a.Add(121)
print (a.get_result())
b =Calculator()
b.Add(44)
b.Add(2)
b.substract(55)
print (b.get_result())





