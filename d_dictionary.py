import Tkinter as tk 
import tkMessageBox
import requests 
from bs4 import BeautifulSoup

try:
    import httplib
except:
    import http.client as httplib

def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

class meaning:
    def __init__(self,parent):
        self.myParent = parent 
        WORD = word_entry.get()
        parent.resizable(height=True,width=True)
        parent.title("Meaning of " + WORD)
        parent.minsize(800,200)
        #parent.geometry("+400+100")
        
        
        l1 = tk.Label(parent,text=WORD.capitalize(),justify="left",font="ubuntu 20")
        s = soup.findAll(class_="css-1o58fj8 e1hk9ate4")
        
        self.meanings = tk.Label(parent,text="")
        self.meanings.configure(font="monospace 12",wraplength="700",justify="left")
        
        
    
        l1.pack()
        self.meanings.pack(expand=True)
        parent.after(1000,self.resize)
        
    def resize(self):
        s = soup.findAll(class_="css-1o58fj8 e1hk9ate4")
        self.meanings.configure(text=(s[0].text).capitalize())

class myApp:
    def __init__(self,parent):
        self.myParent = parent 
        parent.title("D DICTIONARY")
        parent.geometry("420x100+300+200")
        parent.maxsize(420,100)
        word_label = tk.Label(text="WORD")
        word_label.configure(font="20")
        
        global word_entry
        word_entry = tk.Entry()
        word_entry.focus_set()
        word_entry.configure(width="35",font="20")
        
        word_button = tk.Button(text="  GO  ",command=self.get)
        #word_button.bind('<a>',lambda e:self.get_a)
        
        word_label.place(x=15,y=11)
        word_entry.place(x=85,y=10)
        word_button.place(x=175,y=60)
    
    def get(self):
        global word_entry   
        global soup 
        
        WORD = word_entry.get()
        WORD.replace('','+')
        WORD.replace('\'','%27')
        
        if(have_internet()):
        
            url = "https://www.dictionary.com/browse/" + WORD + "?s=t"
            response = requests.get(url)
            if(response.status_code == 200):
                soup = BeautifulSoup(response.text,"html.parser")
                r1 = tk.Tk()
                meaning(r1)
                r1.mainloop()
            
            elif(response.status_code == 404):
                tkMessageBox.showerror("UH OH","Word not found")
        else:
            tkMessageBox.showerror("ERROR","No internet connection!.Try again later")
        
    def getKEY(self, event):
        print("HELLO WORLD")
    
if __name__ == "__main__":
    root = tk.Tk()
    myApp(root)
    root.mainloop()
