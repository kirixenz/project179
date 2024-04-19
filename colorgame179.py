from tkinter import *
import random

root = Tk()
root.title("Project 178")
root.geometry("400x300")

label_name = Label(root, font=("Helvetica", 24), bg="white")
label_name.place(relx=0.5, rely=0.3, anchor="center")

label_score = Label(root, text="Score: 0", font=("Helvetica", 16), bg="lightgray")
label_score.place(relx=0.15, rely=0.1, anchor="center")

input_value = Entry(root)
input_value.place(relx=0.5, rely=0.5, anchor="center")


class Game:
    def  __init__(self):
        self.__score = 0

    def updateGame(self):
        self.text = ["BLACK", "PINK", "GREEN", "BLUE", "YELLOW", "RED"]
        self.random_number_for_text = random.randint(0,5)
        self.color = ["black", "pink", "green", "blue", "yellow", "red"]
        self.random_number_for_color = random.randint(0,5)   
        label_name["text"] = self.text[self.random_number_for_text]
        label_name["fg"] = self.color[self.random_number_for_color]

    def __update_score(self, input_value):
        if(input_value == self.color[self.random_number_for_color]):
            self.__score = self.__score + random.randint(0,10)
            label_score["text"] = "Score: " + str(self.__score)

    def get_user_value(self, input_value):
        self.__update_score(input_value)  


def getInput():
    value = input_value.get()
    game_instance.get_user_value(value)
    game_instance.updateGame()
    input_value.delete(0, END)

              

game_instance = Game()

button_start = Button(root, text="Start", command=game_instance.updateGame, bg="lightblue", fg="black", relief=FLAT, padx=10, pady=1, font=("Helvetica", 15))
button_start.place(relx=0.6, rely=0.7, anchor="center")

btn1 = Button(root, text="Check", command=getInput, bg="IndianRed1", fg="white", relief=FLAT, padx=10, pady=1, font=("Helvetica", 15))
btn1.place(relx=0.3, rely=0.7, anchor="center")


root.mainloop()