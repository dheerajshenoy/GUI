import pyqrcode as qr
from pyqrcode import QRCode 
from PyQt4 import QtGui,QtCore 
import sys 
import png 

class mainWindow(QtGui.QWidget):
	
	def __init__(self):
		super(mainWindow,self).__init__()
		
		self.ui()
		
	def ui(self):
		self.form = ".jpg"
		self.setGeometry(100,100,400,5)
		layout = QtGui.QFormLayout()
		
		code_label = QtGui.QLabel(self,text="Text:")
		global code_box 
		code_box = QtGui.QLineEdit(self)
		
		fcolor_label = QtGui.QLabel(self,text="Foreground Color:")
		global fcolor_btn 
		fcolor_btn = QtGui.QPushButton(self,text="Choose Color")
		fcolor_btn.clicked.connect(self.getfgcolor)
		
		
		bgcolor_label = QtGui.QLabel(self,text="Background Color:")
		global bgcolor_btn
		bgcolor_btn = QtGui.QPushButton(self,text="Choose Color")
		bgcolor_btn.clicked.connect(self.getbgcolor)
		
		fileName_label = QtGui.QLabel(self,text="File Name:")
		
		global fileName_box
		fileName_box = QtGui.QLineEdit(self)
		
		saveFile_label = QtGui.QLabel(self,text="Save File Directory:")
		global saveFile_box 
		saveFile_box = QtGui.QLineEdit(self)
		
		orLabel = QtGui.QLabel(self,text="")
		
		global chooseDirBtn
		chooseDirBtn = QtGui.QPushButton(self,text="Choose Directory")
		chooseDirBtn.clicked.connect(self.getDir)
		
		formatChoose_label = QtGui.QLabel(self,text="Save File Format:") 
		
		global formatChoose 
		formatChoose = QtGui.QComboBox(self)
		formatChoose.addItems([".jpg",".png",".svg"])
		formatChoose.activated.connect(self.getFormat)
		
		btn = QtGui.QPushButton(self,text="GENERATE")
		btn.clicked.connect(self.generate)
		
		
		layout.addRow(code_label,code_box)
		layout.addRow(fcolor_label,fcolor_btn)
		layout.addRow(bgcolor_label,bgcolor_btn)
		layout.addRow(saveFile_label,saveFile_box)
		layout.addRow(orLabel,chooseDirBtn)
		layout.addRow(fileName_label,fileName_box)
		layout.addRow(formatChoose_label,formatChoose)
		layout.addRow(btn)
		
		self.setLayout(layout)
		
		self.show()

	def getDir(self):
		fileDialog = QtGui.QFileDialog.getExistingDirectory(self,"Select Directory")
		chooseDirBtn.setText(fileDialog)
	
	def getfgcolor(self):
		global fg 
		fg = QtGui.QColorDialog.getColor()
		fcolor_btn.setText(fg.name())
		fcolor_btn.setStyleSheet("background-color:" + fg.name())


		
	def getbgcolor(self):
		global bg 
		bg = QtGui.QColorDialog.getColor()
		bgcolor_btn.setText(bg.name())
		bgcolor_btn.setStyleSheet("background-color:" + bg.name())


	def getFormat(self):
		hold = formatChoose.currentIndex()
		if(hold == 0):
			self.form = ".jpg"
		elif(hold == 1):
			self.form = ".png"
		else:
			self.form = ".svg"
		
	
	def generate(self):

		string = code_box.text()
		x = QRCode(str(string))
		print(str(fg.name()),str(bg.name()))
		if(self.form == ".jpg"):
			x.svg(fileName_box.text()+".jpg",module_color=str(fg.name()),background=str(bg.name()),scale=8)
		elif(self.form == ".png"):
			x.svg(fileName_box.text()+".png",module_color=str(fg.name()),background=str(bg.name()),scale=8)
		else:
			x.svg(fileName_box.text()+".svg",module_color=str(fg.name()),background=str(bg.name()),scale=8)
		
		
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	win = mainWindow()
	sys.exit(app.exec_())
		