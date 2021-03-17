# 4. Create a Time class and initialize it with hours and minutes.
#     Create a method addTime which should take two Time objects and add them. 
#     E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
#     Create another method displayTime which should print the time. 
#     Also create a method displayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.


class Time():
	def __init__(self, hours, mins):
		self.hours = hours
		self.mins = mins

	def addTime(self,t1,t2):
		hr=t1.hours+t2.hours
		mn =t1.mins+t2.mins
		temp=(hr*60)+mn
		t3=Time(0,0)
		while temp>=60:
			temp-=60
			t3.hours+=1
		t3.mins=temp
		return t3

	def displayTime(self):
		print("Time is", self.hours,"hours and", self.mins, "minutes.")

	def displayMinute(self):
		print (self.hours*60)+self.mins
a = Time(2,50)
b = Time(1,20)
ans=addTime(Time(2,50),Time(1,20))
ans.displayTime()
ans.displayMinute()

