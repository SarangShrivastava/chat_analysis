#!/usr/bin/python

'''
Chat-analysis gui
'''
try:
  from Tkinter import *             # Python 2
  import ttk
except ImportError:
  from tkinter import *             # Python 3
  import tkinter.ttk as ttk

from glob import glob
import tkMessageBox
import tkFileDialog
import os

class App(Frame):
	def __init__(self):
			Frame.__init__(self)
			self.master.title('Imposter Detector')

			self.master.rowconfigure(0, weight=1)
			self.master.columnconfigure(0, weight=1)
			self.master.configure(height=200, width=200)
			self.grid(sticky = W+E+N+S)

			# variables
			self.Datasetfile = StringVar()
			self.status = StringVar()
			self.selectedAlgo = StringVar()
			self.message = StringVar()
			self.samplefiles = ['--User your own dataset--']
			self.algoList = ['algo1', 'algo2', 'algo3']
			
			os.chdir('../chat_analysis/package')
			for fn in glob('chat*.txt'):
			    print self.samplefiles.append(fn)


			#filepath
			self.file_entry = Entry(self,textvariable=self.Datasetfile)
			self.file_entry.grid( row=0, column=0, columnspan = 4, padx=5, pady=2 , sticky = W+E+N+S )
			self.file_entry.focus()
			# self.file_entry.bind('<Return>', self.doNothing)

			# browse button
			self.browseBtn = Button( self, text = "Browse", command=self.browse_file )
			self.browseBtn.grid( row = 0, column = 4, sticky = W+E )

			# Algorigthm dropdown list
			self.Algobox = ttk.Combobox(self, textvariable=self.selectedAlgo)
			self.Algobox.bind("<<ComboboxSelected>>", self.doNothing)
			self.Algobox.configure(value=self.algoList)
			self.Algobox.grid(row=1, column=0,columnspan=2, sticky=(W,E))

			# Dataset dropdown list
			self.selectedDataset = StringVar()
			self.Databox = ttk.Combobox(self, textvariable=self.selectedDataset)
			# self.Databox.configure(value=['--User your own dataset--','pehala Dataset','dusra Dataset'])
			self.Databox.configure(value=self.samplefiles)
			self.Databox.bind("<<ComboboxSelected>>", self.on_data_select)
			self.Databox.grid(row=1, column=3,columnspan=2, sticky=(W,E))

			# Train button
			self.trainBtn = ttk.Button(self, text="Train", command=self.train_cmd)
			self.trainBtn.grid(column=0, row=2, sticky=W+E)

			# Status Label
			self.status.set("untrained")
			self.statusLbl = ttk.Label(self, textvariable=self.status, width=10)
			self.statusLbl.grid(column=2, row=2,sticky=E+W)

			# Kill button
			self.killBtn = ttk.Button(self, text="Kill/Reset", command=self.kill_cmd)
			self.killBtn.grid(row=2, column=4)

			# legitimate Label
			self.legLbl = ttk.Label(self, text="legitimate").grid(row=3, column=0, sticky=W)

			# imposter label
			self.impLbl = ttk.Label(self, text="imposter").grid(row=3, column=4, sticky=E)

			# Detection Bar
			self.DetectBar = ttk.Progressbar(self, orient='horizontal', mode='determinate')
			self.DetectBar.grid(row=4, column=0, columnspan=5, padx=5, pady=5, sticky=W+E)

			# Message input entry
			self.msgInput_entry = ttk.Entry(self, textvariable=self.message)
			self.msgInput_entry.grid(row=5, column=0, columnspan=5, sticky=(W,E), pady=5, padx=5)
			self.msgInput_entry.focus()
			self.msgInput_entry.bind('<Return>', self.on_msg_input)


			self.rowconfigure(1, weight=1)
			self.columnconfigure(1, weight=1)

	def doNothing(self, *args):
		# tkMessageBox.showinfo("Kuch bhi","hi "+self.message.get())
		pass

	def browse_file(self):
		selected_file = tkFileDialog.askopenfile(parent=self,mode='rb',title='Select a file')
		if selected_file != None:
			self.Datasetfile.set(selected_file.name)
		selected_file.close()
	
	def on_data_select(self, event):
		if(self.Databox.current()!=0):
			self.Datasetfile.set(os.getcwd() + '/' + self.Databox.get())
		else:
			self.Datasetfile.set('')

	def on_msg_input(self, *args):
		# tkMessageBox.showinfo("Kuch bhi","hi "+self.message.get())
		self.message.set('')

	def train_cmd(self):
		self.status.set('tain')

	def kill_cmd(self):
		self.status.set('untrained')
		self.Datasetfile.set('')
		self.Databox.set(self.samplefiles[0])

	def run(self):
		self.DetectBar.start(60)
		self.mainloop()


if __name__ == '__main__':
	App().run()

# os.chdir('../chat_analysis/package')
# for fn in glob('chat*.txt'):
#     print fn
