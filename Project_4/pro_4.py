# Add user
# Display
# Deposit
# Withdraw
# Transfer
# Quit
import sqlite3

conn = sqlite3.connect("pro_4.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS accounts( 
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    balance REAL NOT NULL
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY,
    from_account_id INTEGER,
    to_account_id INTEGER,
    amount REAL NOT NULL,
    FOREIGN KEY (from_account_id) REFERENCES accounts(id),
    FOREIGN KEY (to_account_id) REFERENCES accounts(id)
);
""")

# 1. Add user
def add_user():
    print('\n--- Add new user ---')
    name = input('User\'s name: ').upper()
    start_balance = float(input("Starter Balance: "))
    cur.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, start_balance))
    print("User added successfully")
    conn.commit()

# 2. Display
def display():
    print('\n--- Here is the users list ---') 
    cur.execute("""SELECT * FROM accounts""")
    users = cur.fetchall()
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Balance: {user[2]}")

# 3. Deposit
def deposit():
    print('\n / ---- Deposit ---- / ')
    account_id = int(input("Enter your ID: "))
    amount = float(input("Amount: "))
    cur.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, account_id))
    print("Deposit completed successfully!")
    conn.commit()

# 4. Withdraw
def withdraw():
    print('\n / ---- Withdraw ---- / ')
    withdraw_account_id = int(input("Enter your ID: "))
    withdraw_amount = float(input("Amount: "))
    cur.execute('UPDATE accounts SET balance = balance - ? WHERE id = ?', (withdraw_amount, withdraw_account_id))
    print("Withdrawal completed successfully!")
    conn.commit()

# 5. Transfer
def transfer():
    print('\n / ---- Transfer ---- / ')
    transfer_from_id = int(input("From who(ID): "))
    transfer_to_id = int(input("To who(ID): "))
    transfer_amount = float(input("Transfer amount: "))
    cur.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (transfer_amount, transfer_from_id))
    cur.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (transfer_amount, transfer_to_id))
    print("Transfer completed successfully!")
    conn.commit()

# Quit
def quit_program():
    print('The program is closed. Goodbye!')
    conn.close()
    exit()

while True:
    print('\n / -- Main Menu -- / ')
    print(' 1. Add user')
    print(' 2. Display users')
    print(' 3. Deposit')
    print(' 4. Withdraw')
    print(' 5. Transfer')
    print(' 6. Quit')

    choice = int(input("\nChoose the action: "))

    if choice == 1:
        add_user()
    elif choice == 2:
        display()
    elif choice == 3:
        deposit()
    elif choice == 4:
        withdraw()
    elif choice == 5:
        transfer()
    elif choice == 6:
        quit_program()
    else:
        print('Invalid choice. Please try again.')