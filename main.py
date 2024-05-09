import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10


ROWS=3
COLS=3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column =[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(columns[row],  end=" | ")
            else:
                print(columns[row], end="")
        print()

def check_win(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
      symbol = columns[0][line]
      for column in columns:
         symbol_to_check = column[line]
         if symbol != symbol_to_check:
           break
         else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def deposit():
    while True:
        amount = input("Deposit amount: ")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                break
        else:
            print("Please enter a positive number")
    return amount

def number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + ")? " )
        if lines.isdigit():
            lines = int(lines)
            if 0 <= lines <= MAX_LINES:
                break
        else:
            print("Enter a valid number of lines")
    return lines

def bet_num():
    while True:
        amount = input("Deposit amount to bet on each line: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
        else:
            print(f"Please enter between {MIN_BET} and {MAX_BET}")
    return amount
def main():
    blnc = deposit()
    lines = number_of_lines()
    while True:
        bet = bet_num()
        total_bet = bet * lines

        if total_bet > blnc:
            print(f"You have not enough money, your total is {blnc}.")
        else:
            break


    print(blnc ,lines)

    print(f"You are betting {blnc} on {lines} lines. Total bet equals {total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print(slots)
    winnings,winning_lines = check_win(slots,lines,bet,symbol_value)
    print(f"You won {winnings}.")


main()
