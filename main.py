from tkinter import *
def converter1() :  
   user_in = input.get()
   result["text"] = round(int(user_in)*1.609344,2)  
window = Tk()
window.configure(bg="white")
window.title("km to miles converter".capitalize())
window.minsize(width=300 ,height=120)
window.configure(padx=75)
miletokm_output = Label(text="", font=("Arial", 24, "bold")) 
miletokm_output.grid(row=0,column=0)
miletokm_output.configure(bg='white')
input = Entry(width=7,justify="center")
input.grid(column=2, row=0)
input.insert(END, '0')
convert = Button(text="convert".capitalize(),command=converter1)
convert.grid(column=2, row=2)
miletokm_output = Label(justify="center",text="=", font=("Arial", 24, "bold")) 
miletokm_output.grid(row=1,column=1)
miletokm_output.configure(bg='white')
miles = Label(text="miles".title()) 
miles.grid(row=0,column=3)
miles.configure(bg='white')
km = Label(text="km".title()) 
km.grid(row=1,column=3)
km.configure(bg='white')
result = Label(text="1.609344") 
result.configure(bg='white')
result.grid(row=1,column=2)

















window.mainloop()