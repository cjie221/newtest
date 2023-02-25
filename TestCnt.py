# -*-coding:GBK -*- 
from tkinter import *

st = 0
counter = 5
def start():
	global st
	st=1
	print("st="+str(st))
	print("counter="+str(counter))
	counting()

def counting():
	global counter
	global st
	if(counter>0 and st==1 ):
		counter -= 1
		digit.config(text=str(counter))
		digit.after(1000,counting)
		print("counter="+str(counter))
	elif(counter==0):
		digit.config(text="时间到!")
		counter = 5
		st=0
		digit.after(1000,counting)
		print("counter="+str(counter))
	else:
		digit.config(text="是否再试？")
#	digit.after(1000,counting)
#	print("counter="+str(counter))

#def run_counter(digit):
#	counting()

root = Tk()
root.title("but")
root.geometry("300x200")

digit=Label(root,bg="snow",fg="darkblue",width=10,
			font="Helvetic 20")
digit.pack()
#while(st==1):
#	if(counter>0):
#		digit.config(text=str(counter))
#	elif(counter==0):
#		digit.config(text="时间到!")
#	root.update()
#	root.after(1000)
#	counter -= 1
#	print("counter="+str(counter))

exitbtn = Button(root,text="Exit",command=root.destroy)
startbtn = Button(root,text="Start",command=start)

exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
startbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

root.mainloop()
