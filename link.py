from PyQt4 import QtGui,QtCore 
import sys 
import time 
import os 


def isTime(arg1,arg2):
	if(time.localtime().tm_hour == arg1 and time.localtime().tm_min == arg2):
			rem_box = QtGui.QMessageBox(self)
			rem_box.setText(remind_msg_box.text())
	else:
		isTime(arg1,arg2)
	
	
	
global mainWindow
class mainWindow(QtGui.QWidget):
	def __init__(self):
		super(mainWindow,self).__init__()
		self.ui()
	
	def ui(self):
		
		
		menubar = QtGui.QMenuBar(self)

		layout = QtGui.QFormLayout()
		layout.setMargin(40)
		layout.setSpacing(10)
				
		fileMenu = menubar.addMenu("File")
		fileMenu.addAction("New Window")
		fileMenu.addAction("Exit")
		
		Added = menubar.addMenu("Added")
		Added.addAction("Programs")
		Added.addAction("Reminders")
		Added.addAction("Message")
		Added.addAction("URL")
		Added.addAction("Shutdown")

		
		date_label = QtGui.QLabel(self,text="Date:")
		
		global date_box 
		date_box = QtGui.QLineEdit(self)
		
		time_label = QtGui.QLabel(self,text='Time:')
		
		global time_box
		time_box = QtGui.QLineEdit(self)
	
		time_box.setToolTip("FORMAT: dd/mm/yyyy (Leave blank if today)<SPACE>hr/min/second")
			
		global am_pm_box
		
		am_pm_label = QtGui.QLabel(self,text="AM/PM:")
		am_pm_box = QtGui.QLineEdit(self)
		
		
		wtd_label = QtGui.QLabel(self,text='What to do :')
		
		global wtd_chooser 
		
		wtd_chooser = QtGui.QComboBox(self)
		wtd_chooser.addItems(["Test It Out","Open Program","Remind something","Message Prompt","URL","Shutdown"])
		
		ok_btn = QtGui.QPushButton(self,text="OK")
		ok_btn.clicked.connect(self.getInfo)
		
			
		
		layout.addRow(date_label,date_box)
		layout.addRow(time_label,time_box)
		layout.addRow(am_pm_label,am_pm_box)
		layout.addRow(wtd_label,wtd_chooser)
		layout.addRow(ok_btn)
		
		remind_layout = QtGui.QFormLayout()
		
		
		
		self.setLayout(layout)
		
		self.show()
	
	def getInfo(self):
		x = wtd_chooser.currentIndex()
		
		if(x == 0):
			pass 
	
		elif(x == 1):
			pass 
		
		elif(x == 2):
			global win
			win = QtGui.QDialog(self)
			
			win.setGeometry(150,150,400,200)
			remind_layout = QtGui.QFormLayout(win)
			
			remind_msg_label = QtGui.QLabel(win,text="Reminder Message:")

			global remind_msg_box 
			remind_msg_box = QtGui.QPlainTextEdit(win)	
			
			
			remind_ok_btn = QtGui.QPushButton(win,text="Create Reminder")
			remind_ok_btn.clicked.connect(self.remind_ok)
			
			remind_cancel_btn = QtGui.QPushButton(win,text="Cancel")
			
			remind_layout.addRow(remind_msg_label,remind_msg_box)	
			remind_layout.addRow(remind_cancel_btn,remind_ok_btn)
			
			win.show()
			
	def remind_ok(self):
		if(date_box.text() == ""):
			
			remind_date = time.localtime().tm_mday
			remind_month = time.localtime().tm_mon
			remind_year = time.localtime().tm_year 
			
		hold = str(time_box.text())
		remind_time_hr,remind_time_min = hold.split(':')
		
		self.remind_start_ticking(remind_time_hr,remind_time_min)
		
	def remind_start_ticking(self,remind_time_hr,remind_time_min):
		win.close()
		self.setWindowState(QtCore.Qt.WindowMinimized)
		
	
		
		else:
			
						
			
			
			
			
			
			
			
			
		
		
		
		
		
			
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = mainWindow()
	sys.exit(app.exec_())