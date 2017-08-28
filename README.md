# python-UML-sequence-diagram
A python tool for generating sequence diagram schema of plantUML.


This tool is used for generating sequence diagram schema of platUML. 

The more you play, the more fun you have! :>

plantUML SD schema: http://plantuml.com/sequence-diagram

Example Demo code :


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


The tool output :

main ->motor:setMotorName
main ->human:setHumanName
main ->motor:driveBy
motor ->human:say

![image] https://github.com/backman-git/python-UML-sequence-diagram/blob/master/result.png


