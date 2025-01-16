import random as rd
import pandas as pd
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

colour1 = "#020f12"
colour2 = '#05d7ff'
colour3 = '#65e7ff'
colour4 = 'BLACK'

PLAYER_NAMES = ["Emma", "Olivia", "Ava", "Isabella", "Sophia", "Emilia", "Charlotte", "Amanda", "Harper", "Evelyn"]
PLAYER_COUNT = 10
BET_AMOUNT = 100


class Lottery:

    def __init__(self):
        self.net_worth = 500
        self.net_worth_history = []

    def lottery_draw(self):
        draws = []
        for i in range(PLAYER_COUNT):
            draws.append(rd.randint(1000, 9999))
        players_draws = pd.Series(PLAYER_NAMES, draws)
        return players_draws, draws

    def lucky_number(self, draws):
        lucky_num = rd.choice(draws)
        return lucky_num

    def is_Emma_Winner(self, players_draws, lucky_num):
        return True if players_draws[players_draws == 'Emma'].index[0] == lucky_num else False

    def one_lottery_iteration(self):
        players_draws, draws = self.lottery_draw()
        lucky_num = self.lucky_number(draws)
        if self.is_Emma_Winner(players_draws, lucky_num):
            self.net_worth += BET_AMOUNT * (PLAYER_COUNT - 2)
        else:
            self.net_worth -= BET_AMOUNT
        self.net_worth_history.append(self.net_worth)

    def lottery_over_a_period(self, no_of_days):
        self.net_worth_history.append(0)
        for _ in range(no_of_days):
            self.one_lottery_iteration()
        # print(self.net_worth_history)

class plotter:

    def plot_net_worth(self,net_worth_history):
        plt.plot(range(len(net_worth_history)), net_worth_history)
        plt.xlabel('Day')
        plt.ylabel('Net Worth')
        plt.title('Net Worth Over Time')
        plt.grid(True)
        plt.show()

    def show_one_month_graph(self):
        lottery = Lottery()
        lottery.lottery_over_a_period(30)
        self.plot_net_worth(lottery.net_worth_history)

    def show_five_year_graph(self):
        lottery = Lottery()
        lottery.lottery_over_a_period(365*5)
        self.plot_net_worth(lottery.net_worth_history)

    def show_one_year_graph(self):
        lottery = Lottery()
        lottery.lottery_over_a_period(365)
        self.plot_net_worth(lottery.net_worth_history)

    def update_net_worth_label(self,days):
        lottery = Lottery()
        lottery.lottery_over_a_period(365*5)
        last_net_worth = lottery.net_worth_history[-1]  # Access the last element of net_worth_history
        return last_net_worth

# def update_label(label):
#     label.config(text="Net Worth: {}".format(update_net_worth_label(days)))

def main():
    p = plotter()
    root = tk.Tk()
    root.geometry('400x400')

    root.title("Long Term Profitability in Lottery")
    root.configure(background=colour1)

    # Create labels
    label1 = tk.ttk.Label(root, text="'Emma' is gambling", background=colour1, foreground=colour2, font=("Arial", 20, "bold"))
    label1.grid(row=2, column=2, padx=75, pady=40)

    label2 = tk.ttk.Label(root, text="Price per ticket: {} ".format(BET_AMOUNT), background=colour1, foreground=colour2, font=("Arial", 12, "bold"))
    label2.grid(row=3, column=2)

    # Create buttons using the custom style
    button1 = tk.Button(root, text="One Month", command=p.show_one_month_graph,
                font=("arial",11,"bold"),
                background=colour2,
                foreground=colour4,
                activebackground=colour3,
                activeforeground=colour4,
                highlightthickness=2,
                highlightbackground=colour2,
                highlightcolor='WHITE',
                width=10,
                height=2,
                border=0,
                cursor='hand1',)
    button1.grid(row=5, column=2, pady=20)

    button2 = tk.Button(root, text="One Year", command=p.show_one_year_graph,
                font=("arial",11,"bold"), 
                background=colour2,
                foreground=colour4,
                activebackground=colour3,
                activeforeground=colour4,
                highlightthickness=2,
                highlightbackground=colour2,
                highlightcolor='WHITE',
                width=10,
                height=2,
                border=0,
                cursor='hand1',)
    button2.grid(row=6, column=2, pady=20)

    button3 = tk.Button(root, text="Five Year", command=p.show_five_year_graph, 
                font=("arial",11,"bold"),
                background=colour2,
                foreground=colour4,
                activebackground=colour3,
                activeforeground=colour4,
                highlightthickness=2,
                highlightbackground=colour2,
                highlightcolor='WHITE',
                width=10,
                height=2,
                border=0,
                cursor='hand1',)
    button3.grid(row=7, column=2, pady=20)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == '__main__':
    main()
