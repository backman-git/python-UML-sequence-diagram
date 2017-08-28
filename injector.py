

import re


class Injector:

	def __init__(self,f):
		self.f=f
		self.cName=""
		print >>self.f, "SD = open(\"./SD\",\"w\")"

	def write(self,line):
		print >>self.f, line
	def injectNameMethod(self,cName,nTab):
		self.cName=cName
		for i in range(nTab):
			print>>self.f, '\t',
		print >>self.f, "\tdef name(self,n):"
		for i in range(nTab):
			print>>self.f, '\t',
		print >>self.f, "\t\tself.name=n"

	def injectToast(self,m,nTab):
		for i in range(nTab):
			print>>self.f, '\t',
		print>>self.f, "\tprint>>SD, \""+ "->\"+str(self.name)+\""+":"+str(m)+ "\""

	def injectCallerToast(self,nTab,flag):
		for i in range(nTab):
			print>>self.f, '\t',
		if flag is False:
			print>>self.f, "print>>SD, str(self.name), "
		else:
			print>>self.f, "print>>SD, \'main\',"


	def injectNewNameToast(self,obj,nTab):
		for i in range(nTab):
			print>>self.f, '\t',
		print>>self.f, str(obj)+".name(\""+str(obj)+"\""+")"











source = open("./test.py","r")
output = open("./sourceInject.py","w")

injector=Injector(output)

classAry=[]

runTimeStack=["main"]



def countTab(line):
	count=0
	for obj in line:
		if obj =='\t':
			count+=1
	return count



#only for class
#search for class 

flag =False
for line in source:
	
	
	classObj=re.match(r'\t*class (.*):',line)
	methodObj=re.match(r'\t*def (.*)\((.*)\):',line)

	newObj = re.match(r'\t*(.*)\s?=\s?(.*)\(\)',line)
	callObj=re.match(r'\t*(.*)\.(.*)\((.*)\)',line)

	mainObj= re.match(r"if __name__ ==\'__main__\':",line)	
	if mainObj:
		flag=True
		




	if classObj:
		n=countTab(line)
		className=classObj.group(1)
		
		classAry.append(className)
		# inject Name method
		injector.write(line)
		injector.injectNameMethod(className,n)

	elif methodObj:
		n=countTab(line)
		methodName = methodObj.group(1)
		initMethod=re.match(r"__init__(.*)",methodName)
		if not initMethod:
			injector.write(line)
			injector.injectToast(methodName,n)

	elif callObj:
		n=countTab(line)
		injector.injectCallerToast(n,flag)
		injector.write(line)
		runTimeStack.append(callObj.group(1))
		pass
	elif newObj:
		n=countTab(line)
		objName=newObj.group(1)
		injector.write(line)
		injector.injectNewNameToast(objName,n)
		
	
	else:
		injector.write(line)


	

