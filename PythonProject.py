#Name: Issah, Jamal Ahmed
#Index: 00713844
#Python Project

import os
import random
from tkinter import *
from tkinter import filedialog, messagebox, simpledialog

# a class for the GUI
class GUI:
    # constructor for GUI class
    def __init__(self, master):
        self.master = master
        master.title("UNH Scripting w/Python")
        master.geometry("650x400")

        # colors for GUI window and buttons
        self.bg_color = "white"
        self.button_color = "purple"
        self.button_fg_color = "white"

        self.current_file = StringVar(value="No file selected.")
        self.data = []

        master.config(bg=self.bg_color)

        # labels and buttons for GUI
        Label(master, textvariable=self.current_file, font=("Times New Roman", 10), bg="grey", fg="#3E5D6E").grid(row=2,column=1,pady=20)

        Button(master, text="Select/Create File", command=self.select_file,
               fg=self.button_fg_color, bg=self.button_color, padx=20, pady=10,
               relief="raised", borderwidth=3).grid(row=3, column=0, padx=5, pady=5)

        Button(master, text="Display All", command=self.display_all,
               fg=self.button_fg_color, bg=self.button_color, padx=20, pady=10,
               relief="raised", borderwidth=3).grid(row=3, column=1, padx=5, pady=5)

        Button(master, text="Sort", command=self.sort,
               fg=self.button_fg_color, bg=self.button_color, padx=20, pady=10,
               relief="raised", borderwidth=3).grid(row=3, column=2, padx=5, pady=5)

        Button(master, text="Search/Occurs", command=self.search_occurs,
               fg=self.button_fg_color, bg=self.button_color, padx=20, pady=10,
               relief="raised", borderwidth=3).grid(row=4, column=0, padx=5, pady=5)

        Button(master, text="Largest", command=self.display_largest,
               fg=self.button_fg_color, bg=self.button_color, padx=20, pady=10,
               relief="raised", borderwidth=3).grid(row=4, column=1, padx=5, pady=5)

        Button(master, text="Append Number", command=self.append_number,
               fg=self.button_fg_color, bg=self.button_color, padx=20, pady=10,
               relief="raised", borderwidth=3).grid(row=4, column=2, padx=5, pady=5)

        Button(master, text="Encrypt", command=self.encrypt,
               fg=self.button_fg_color, bg=self.button_color, padx=20, pady=10,
               relief="raised", borderwidth=3).grid(row=5, column=0, padx=5, pady=5)

        Button(master, text="Decrypt", command=self.decrypt,
               fg=self.button_fg_color, bg=self.button_color, padx=20, pady=10,
               relief="raised", borderwidth=3).grid(row=5, column=1, padx=5, pady=5)

        Button(master, text="Exit", command=master.destroy,
               fg=self.button_fg_color, bg=self.button_color, padx=20, pady=10,
               relief="raised", borderwidth=3).grid(row=5, column=2, padx=5, pady=5)


    # function to select file
    def select_file(self):
        file_path = filedialog.askopenfilename(initialdir="./", title="Select file",
                                               filetypes=(("Text files", ".txt"), ("All files", ".")))
        if file_path:
            self.current_file.set("Current file: " + file_path)
            self.data = self.read_file(file_path)
        else:
            new_file_path = filedialog.asksaveasfilename(initialdir="./", title="Create new file",
                                                         filetypes=(("Text files", ".txt"), ("All files", ".")))
            if new_file_path:
                self.current_file.set("New file created: " + new_file_path + ".txt")
                with open(new_file_path + ".txt", 'w') as file:
                    file.write('')

    # function to read data from file
    def read_file(self, fileName):
        try:
            with open(fileName, "r") as inFile:
                numbers = [float(line.strip()) for line in inFile.readlines()]
        except FileNotFoundError:
            numbers = []
        return numbers

    #write numbers to the file
    def write_file(self, fileName, data):
        inFile = open(fileName, 'a')
        
        for number in data:
            inFile.write(str(number) + "\n")

    # display numbers from the file
    def display_all(self):
        if self.data:
            total = sum(self.data)
            average = float(total / len(self.data))
            message = "Numbers: {}\nTotal: {}\nAverage: {:.2f}".format(self.data, total, average)
            messagebox.showinfo("Display All", message)
        else:
            messagebox.showerror("Error", "No data file selected.")

    # sort numbers in the file
    def sort(self):
        if self.data:
            self.data.sort()
            message = "Sorted numbers: {}".format(self.data)
            messagebox.showinfo("Sort", message)
        else:
            messagebox.showerror("Error", "No data file selected.")

    # search for a number in the file
    def search_occurs(self):
        if self.data:
            search_value = simpledialog.askfloat("Search/Occurs", "Enter a number to search for:")
            if search_value is not None:
                count = self.data.count(search_value)
                message = "Number of occurrences of {}: {}".format(search_value, count)
                messagebox.showinfo("Search/Occurs", message)
        else:
            messagebox.showerror("Error", "No data file selected.")

    # display the largest number in the file
    def display_largest(self):
        if self.data:
            largest = max(self.data)
            message = "Largest number: {}".format(largest)
            messagebox.showinfo("Largest", message)
        else:
            messagebox.showerror("Error", "No data file selected.")

    # add a random number to the file
    def append_number(self):
        if self.current_file.get() != "No file selected.":
            new_number = random.uniform(1, 100)
            self.data.append(new_number)
            self.write_file(self.current_file.get().replace("Current file: ", ""), self.data)
            messagebox.showinfo("Append Number", "Number {} appended to the file.".format(new_number))
        else:
            messagebox.showerror("Error", "No data file selected.")

    # encrypt file
    def encrypt(self):
        if self.data:
            encrypted_data = [number * 2001 for number in self.data]
            self.write_file(self.current_file.get().replace("Current file: ", ""), encrypted_data)
            messagebox.showinfo("Encrypt", "File encrypted.\n\nEncrypted data:\n{}".format(encrypted_data))
        else:
            messagebox.showerror("Error", "No data file selected.")

    # decrypt file
    def decrypt(self):
        if self.data:
            decrypted_data = [number / 2001 for number in self.data]
            self.write_file(self.current_file.get().replace("Current file: ", ""), decrypted_data)
            messagebox.showinfo("Decrypt", "File decrypted.\n\nDecrypted data:\n{}".format(decrypted_data))
        else:
            messagebox.showerror("Error", "No data file selected.")

# main function
def main():
    main_window = Tk()
    app = GUI(main_window)
    main_window.mainloop()

if __name__ == "__main__":
    main()
