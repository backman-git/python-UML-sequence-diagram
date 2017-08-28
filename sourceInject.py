SD = open("./SD","w")






class Motor :

	def name(self,n):
		self.name=n


	def setMotorName(self,name):

		print>>SD, "->"+str(self.name)+":setMotorName"


		self.motorName = name





	def driveBy(self,human):

		print>>SD, "->"+str(self.name)+":driveBy"
		self.driver =human

		print self.motorName+" Motor drived by "+self.driver.driverName+"."

		print>>SD, str(self.name), 
		human.say("That is awesome")



	



class Human:

	def name(self,n):
		self.name=n


	def setHumanName(self,hName):

		print>>SD, "->"+str(self.name)+":setHumanName"


		self.driverName =hName

	

	def say(self,strs):

		print>>SD, "->"+str(self.name)+":say"
		print "human say: "+strs+"."



















if __name__ =='__main__':



	motor=Motor()

	motor.name("motor")
	print>>SD, 'main',
	motor.setMotorName("kawasaki")



	human=Human()

	human.name("human")
	print>>SD, 'main',
	human.setHumanName("Backman")



	print>>SD, 'main',
	motor.driveBy(human)











