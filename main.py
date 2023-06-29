import tkinter as tk 
import ttkbootstrap as ttk 
from grades import Grade

def calculations():
    percentage = float(coursePercent.get())
    weight = int(courseWeight.get())
    code = courseCode.get()
    letterGrade = ""
    gradePoints = 0

    coursePercent.set("")
    courseWeight.set("")
    courseCode.set("")

    if percentage >= 90 and percentage <= 100: 
        letterGrade = "A+"
        gradePoints = 4.33
    
    elif percentage >= 85 and percentage <= 89:
        letterGrade = "A"
        gradePoints = 4.00

    elif percentage >= 80 and percentage <= 84:
        letterGrade = "A-"
        gradePoints = 3.67
    
    elif percentage >= 77 and percentage <= 79: 
        letterGrade = "B+"
        gradePoints = 3.33
    
    elif percentage >= 73 and percentage <= 76: 
        letterGrade = "B"
        gradePoints = 3.00
    
    elif percentage >= 70 and percentage <= 72:
        letterGrade = "B-"
        gradePoints = 2.67

    elif percentage >= 67 and percentage <= 69: 
        letterGrade = "C+"
        gradePoints = 2.33
    
    elif percentage >= 63 and percentage <= 66:
        letterGrade = "C"
        gradePoints = 2.00
    
    elif percentage >= 60 and percentage <= 62: 
        letterGrade = "C-"
        gradePoints = 1.67

    elif percentage >= 57 and percentage <= 59:
        letterGrade = "D+"
        gradePoints = 1.33

    elif percentage >= 53 and percentage <= 56: 
        letterGrade = "D"
        gradePoints = 1.00

    elif percentage >= 50 and percentage <= 52:
        letterGrade = "D-"
        gradePoints = 0.67

    elif percentage >= 0 and percentage <= 49: 
        letterGrade = "F"
        gradePoints = 0.00

    grades.append(Grade(gradePoints, letterGrade, weight, code))
    getCGPA()

def getCGPA():
    savetxt = ""
    textbox.delete("1.0", tk.END)
    totalgradepoint = 0
    totalWeight = 0
    for i in grades:
        outputmsg = f"Course Code: {i.getCourseCode()}: {i.getLetterGrade()} | Grade Point: {i.getGradePoint()} | Weight: {i.getWeight()}\n"
        savetxt += outputmsg
        textbox.insert(tk.END, outputmsg)
        totalgradepoint += i.getGradePoint()
        totalWeight += i.getWeight()

    culmGPA.set("CGPA: " + str(totalgradepoint/totalWeight))
    
def exportToTXT():

    calculations()

    print(savetxt)
    file = open("cgpasavefile.txt", "w")
    file.write(savetxt)
    file.close()

# window 
window = ttk.Window(themename = "darkly")
window.title("CGPA Calculator")
window.geometry("500x450")
window.resizable(False,False)

# variables
culmGPA = tk.StringVar()
coursePercent = tk.StringVar()
courseWeight = tk.StringVar()
courseCode = tk.StringVar()
outputText = tk.StringVar()
grades = []
savetxt = ""

# title
title = ttk.Label(
    master = window,
    text = "CGPA Calculator",
    font = "Calibri 24 bold"
)
title.pack(pady = 10)

# frame 
frame = ttk.Frame(
    master = window
)
frame.pack()

# labels
label1 = ttk.Label(
    master = frame,
    text = "Course Code: ",
    font = "Calibri 12"
)
label1.grid(column = 1, row = 1, pady = 5)

label2 = ttk.Label(
    master = frame,
    text = "Grade Percentage: ",
    font = "Calibri 12"
)
label2.grid(column = 1, row = 2, pady = 5)

label3 = ttk.Label(
    master = frame,
    text = "Course Weight: ",
    font = "Calibri 12"
)
label3.grid(column = 1, row = 3, pady = 5)

# entry fields 
entry1 = ttk.Entry(
    master = frame, 
    textvariable = courseCode
)
entry1.grid(column = 2, row = 1, pady = 5)

entry2 = ttk.Entry(
    master = frame, 
    textvariable = coursePercent
)
entry2.grid(column = 2, row = 2, pady = 5)

entry3 = ttk.Entry(
    master = frame, 
    textvariable = courseWeight
)
entry3.grid(column = 2, row = 3, pady = 5)

# output label
outputlabel = ttk.Label(
    master = frame,
    textvariable =  culmGPA,
    font = "Calibri 15 bold"
)
outputlabel.grid(column = 1, row = 4, pady = 2)

# calculate button 
calculatebutton = ttk.Button(
    master = frame,
    text = "Calculate",
    command = calculations
)
calculatebutton.grid(column = 2, row = 4)

# output window 
textbox = ttk.Text(
    master = window,
    height = 10
)
textbox.pack(pady = 10)

# frame2
frame2 = ttk.Frame(
    master = window
)
frame2.pack()

# import button
importbutton = ttk.Button(
    master = frame2,
    text = "Import from .txt"
)
importbutton.grid(column = 1, row = 1, padx = 10)

# export button
importbutton = ttk.Button(
    master = frame2,
    text = "Export to .txt",
    command = exportToTXT
)
importbutton.grid(column = 2, row = 1, padx = 10)

# run
window.mainloop()