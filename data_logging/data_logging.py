import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename
import serial
from datetime import datetime

##open serial port COM and Baudrate depend on arduino
##ser1 = serial.Serial('COM4', 9600)

class App(tk.Tk):
  logFile = ""
  timeval = 10
  
  def __init__(self):
    super().__init__()

    # configure the root window
    self.title('Data_logging')
    self.geometry('500x300')

    # label
    self.label = ttk.Label(self, text='start')
    self.label.pack()

    # button
    self.button = ttk.Button(self, text='Click Me')
    self.button['command'] = lambda:[self.retrieve_input(), self.file_open()]
    self.button.pack()

    #time_textbox
    self.runtime = tk.Text(self, height = 2, width = 4, font=('Arial', 18))
    self.runtime.pack(padx = 10, pady = 10)

  def set_time(self):
    retrieve_input()
    file_open()

  ##retrieve input inside text box for motor run time
  def retrieve_input(self):
    App.timeval = self.runtime.get("1.0", "end-1c") ##1.0 means read from line on char one, end-1c read until end and remove \n

    ##print(timeval)
    
  def file_open(self):
    logFile = askopenfilename() ##ask to select excel file
    while logFile.endswith(".xlsx")==False: ##continue ask to select file until excel is selected
      showinfo(title='Information', message='please select excel')
      App.logFile = askopenfilename()
    print("correct file selected")
    print(App.timeval)
    print(App.logFile)

  
'''
  def button_clicked(self):
    #for i in range()
    showinfo(title='Information', message='Hello, Tkinter!')
'''
  ##ask to select excel file to write to

      


''' 
  def pwm_2_serial(self):
    while i<100:
      
      time = datetime.now()
'''      

if __name__ == "__main__":
  app = App()
  app.mainloop()
