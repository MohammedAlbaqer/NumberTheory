#gui envaiormant for 
from tkinter import *
import phifunc
	

class App(Frame):
	def __init__(self,master  = None):
		Frame.__init__(self,master)
		self.grid()
		self.createWidge()

	def createWidge(self):
		#Radiobutton 
		self.a = StringVar()
		self.a.set(0) 
		k = [('IsPrime',0),('Factrolize',1),('Phifounction',2),]
		s=1
		for i,j in k:
			self.rad = Radiobutton(variable=self.a,value =j,text = i )
			self.rad.grid(row =s,sticky = W)
			s +=1


		self.ent1 = Entry()
		self.ent1.grid(row = 0,column = 1)

		self.v = StringVar()
		self.labe = Entry(bg = 'blue',textvariable = self.v)
		self.labe.grid(row = 1,column =1)

		self.quitButton = Button(self,command =self.butt1,text = 'Calculate')
		self.quitButton.grid(row = 2,column = 0)
				
	def butt1(self):
		if self.a.get() == '0':
			if phifunc.is_prime(int(self.ent1.get())):
				self.v.set('Yes')
			else:
				self.v.set('No')
		if self.a.get() == '1':self.v.set(phifunc.sfac(int(self.ent1.get())))
		if self.a.get() == '2':self.v.set(phifunc.phi(int(self.ent1.get())))
		
app =App()
app.master.title('phi func')
app.mainloop()
