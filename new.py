import tkinter as tk
#Creates the window of the app:
window = tk.Tk()
#Set the title of the window:
window.title("Calculator")
#Window size is a string in pixels width x height
window.geometry("300x300")


calc_number=0

def updateLabel(number):
  global calc_number
  calc_number = f"{calc_number}{number}"
  label = tk.Label(window, text=calc_number)
  label.grid(row=0, column=1)








#Label
hello = tk.Label(text = "")  # Creates an entry widget in the 'window'
hello.grid(row=0, column=1)  # Places the entry widget in row 0, column 0 of the grid layout


#Buttons
One = tk.Button( text= "1", command = lambda: updateLabel("1"))
One.grid(row=1, column=0)
Two = tk.Button( text= "2", command = lambda: updateLabel("2"))
Two.grid(row=1, column=1)
Three = tk.Button( text= "3").grid(row=1, column=2)
Four = tk.Button( text= "4").grid(row=2, column=0)
Five = tk.Button( text= "5").grid(row=2, column=1)
Six = tk.Button( text= "5").grid(row=2, column=2)
Seven = tk.Button( text= "7").grid(row=3, column=0)
Eight = tk.Button( text= "8").grid(row=3, column=1)
Nine = tk.Button( text= "9").grid(row=3, column=2)
Zero = tk.Button( text= "0").grid(row=4, column=1)


Plus = tk.Button( text= "+").grid(row=2, column=3)
One = tk.Button( text= "-").grid(row=2, column=4)
Multiply = tk.Button( text= "*").grid(row=3, column=3)
Divide = tk.Button( text= "/").grid(row=3, column=4)
Equal = tk.Button( text= "=").grid(row=4, column=3)

#One.pack()



# Starts the app
tk.mainloop()