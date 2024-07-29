import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 4,
    "B": 6,
    "C": 8,
    "D": 10
}

symbol_value = {
    "A": 40,
    "B": 20,
    "C": 10,
    "D": 5
}


def check_winnings(columns, lines, bet, values):
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

    return winnings


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for i in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for i in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("Minkä summan haluaisit tallettaa? €")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("Summan tulee olla suurempi kuin 0.")
        else:
            print("Syötä numero kiitos.")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Syötä pelattavien rivien määrä (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Syötä kelpaava määrä rivejä.")
        else:
            print("Syötä numero kiitos.")
    return lines


def get_bet():
    while True:
        amount = input("Minkä summan haluaisit pelata joka riville? €")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Summan tulee olla välillä {MIN_BET}€ - {MAX_BET}€")
        else:
            print("Syötä numero kiitos.")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Sinulla ei ole tarpeeksi varoja talletettuna tälle panokselle. Tämänhetkiset varasi ovat: {balance} ")
        else:
            break

    print(f"Olet pelaamassa {bet}€, {lines} riville. Kokonaispanos on: {total_bet}€")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings = check_winnings(slots, lines, bet, symbol_value)
    print(f"Voitit {winnings}€")


main()