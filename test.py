


class Motor :

	def setMotorName(self,name):

		self.motorName = name


	def driveBy(self,human):
		self.driver =human
		print self.motorName+" Motor drived by "+self.driver.driverName+"."
		human.say("That is awesome")

	

class Human:

	def setHumanName(self,hName):

		self.driverName =hName
	
	def say(self,strs):
		print "human say: "+strs+"."









if __name__ =='__main__':

	motor=Motor()
	motor.setMotorName("kawasaki")

	human=Human()
	human.setHumanName("Backman")

	motor.driveBy(human)





