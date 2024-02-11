import tkinter as tk
#Creates the window of the app:
window = tk.Tk()
#Set the title of the window:
window.title("Calculator")
#Window size is a string in pixels width x height
window.geometry("300x300")

# Set global variable
calc_number=""


# Define the label globally
label = tk.Label(window, text=calc_number)
label.grid(row=0, column=1)

# Function to update lagel
def updateLabel(number):
  global calc_number
  calc_number = f"{calc_number}{number}"
  # Update the existing label instead of creating a new one
  label.config(text=calc_number)

# Function to perform calculation
def calc():
  global calc_number
  # Try to safely evaluate the calculation
  try:
      result = eval(calc_number)
  except Exception as e:
      result = "Error"
  label.config(text=f"= {result}")

#Function to clear label
def clear():
  global calc_number
  calc_number = ""
  # Update the existing label instead of creating a new one
  label.config(text=calc_number)

#Start with a empty label
clear()

#Buttons
One = tk.Button( text= "1", command = lambda: updateLabel("1"))
One.grid(row=1, column=0)
Two = tk.Button( text= "2", command = lambda: updateLabel("2"))
Two.grid(row=1, column=1)
Three = tk.Button( text= "3", command = lambda: updateLabel("3")).grid(row=1, column=2)
Four = tk.Button( text= "4", command = lambda: updateLabel("4")).grid(row=2, column=0)
Five = tk.Button( text= "5", command = lambda: updateLabel("5")).grid(row=2, column=1)
Six = tk.Button( text= "6", command = lambda: updateLabel("6")).grid(row=2, column=2)
Seven = tk.Button( text= "7", command = lambda: updateLabel("7")).grid(row=3, column=0)
Eight = tk.Button( text= "8", command = lambda: updateLabel("8")).grid(row=3, column=1)
Nine = tk.Button( text= "9", command = lambda: updateLabel("9")).grid(row=3, column=2)
Zero = tk.Button( text= "0", command = lambda: updateLabel("0")).grid(row=4, column=1)


Plus = tk.Button( text= "+", command = lambda: updateLabel("+")).grid(row=2, column=3)
One = tk.Button( text= "-", command = lambda: updateLabel("-")).grid(row=2, column=4)
Multiply = tk.Button( text= "*", command = lambda: updateLabel("*")).grid(row=3, column=3)
Divide = tk.Button( text= "/", command = lambda: updateLabel("/")).grid(row=3, column=4)
Equal = tk.Button( text= "=", command = calc).grid(row=4, column=3)
Clear = tk.Button( text= "Clear", command = clear).grid(row=4, column=4)
#One.pack()



# Starts the app
tk.mainloop()
