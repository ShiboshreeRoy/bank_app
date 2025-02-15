import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# Stores all accounts (key: account number, value: account details)
accounts = {}

# Color scheme inspired by iOS
COLOR_BACKGROUND = "#F5F5F7"  # Light gray background
COLOR_BUTTON = "#007AFF"      # iOS blue
COLOR_TEXT = "#1C1C1E"        # Dark gray text
COLOR_ACCENT = "#34C759"      # Green for positive actions
COLOR_WARNING = "#FF3B30"     # Red for warnings

# Fonts
FONT_HEADER = ("Helvetica", 16, "bold")
FONT_BODY = ("Helvetica", 12)
FONT_BUTTON = ("Helvetica", 14, "bold")

def create_account():
    name = simpledialog.askstring("Create Account", "Enter your name:")
    if name:
        account_number = len(accounts) + 1  # Simple auto-generated account number
        accounts[account_number] = {
            "name": name,
            "balance": 0,
            "transactions": []
        }
        messagebox.showinfo("Account Created", f"Account created successfully! Your account number is: {account_number}")

def deposit(account_number):
    amount = simpledialog.askfloat("Deposit", "Enter the amount to deposit:")
    if amount is None or amount <= 0:
        messagebox.showerror("Invalid Amount", "Please enter a positive value.")
        return

    accounts[account_number]["balance"] += amount
    accounts[account_number]["transactions"].append({
        "type": "deposit",
        "amount": amount,
        "balance_after": accounts[account_number]["balance"]
    })
    messagebox.showinfo("Deposit Successful", f"Deposited ${amount:.2f}. New balance: ${accounts[account_number]['balance']:.2f}")

def withdraw(account_number):
    amount = simpledialog.askfloat("Withdraw", "Enter the amount to withdraw:")
    if amount is None or amount <= 0:
        messagebox.showerror("Invalid Amount", "Please enter a positive value.")
        return

    if amount > accounts[account_number]["balance"]:
        messagebox.showerror("Insufficient Funds", "You do not have enough balance.")
        return

    accounts[account_number]["balance"] -= amount
    accounts[account_number]["transactions"].append({
        "type": "withdraw",
        "amount": amount,
        "balance_after": accounts[account_number]["balance"]
    })
    messagebox.showinfo("Withdrawal Successful", f"Withdrew ${amount:.2f}. New balance: ${accounts[account_number]['balance']:.2f}")

def check_balance(account_number):
    balance = accounts[account_number]["balance"]
    messagebox.showinfo("Account Balance", f"Your current balance is: ${balance:.2f}")

def view_transactions(account_number):
    transactions = accounts[account_number]["transactions"]
    if not transactions:
        messagebox.showinfo("Transaction History", "No transactions found.")
        return

    transaction_history = "\nTransaction History:\n"
    for transaction in transactions:
        transaction_history += f"{transaction['type'].capitalize()}: ${transaction['amount']:.2f} | Balance after: ${transaction['balance_after']:.2f}\n"
    messagebox.showinfo("Transaction History", transaction_history)

def main_menu():
    def create_account_gui():
        create_account()

    def deposit_gui():
        account_number = simpledialog.askinteger("Deposit", "Enter your account number:")
        if account_number in accounts:
            deposit(account_number)
        else:
            messagebox.showerror("Account Not Found", "Invalid account number.")

    def withdraw_gui():
        account_number = simpledialog.askinteger("Withdraw", "Enter your account number:")
        if account_number in accounts:
            withdraw(account_number)
        else:
            messagebox.showerror("Account Not Found", "Invalid account number.")

    def check_balance_gui():
        account_number = simpledialog.askinteger("Check Balance", "Enter your account number:")
        if account_number in accounts:
            check_balance(account_number)
        else:
            messagebox.showerror("Account Not Found", "Invalid account number.")

    def view_transactions_gui():
        account_number = simpledialog.askinteger("View Transactions", "Enter your account number:")
        if account_number in accounts:
            view_transactions(account_number)
        else:
            messagebox.showerror("Account Not Found", "Invalid account number.")

    # Create the main window
    root = tk.Tk()
    root.title("Banking App")
    root.geometry("400x500")
    root.configure(bg=COLOR_BACKGROUND)

    # Header
    header = tk.Label(root, text="Banking App", font=FONT_HEADER, fg=COLOR_TEXT, bg=COLOR_BACKGROUND)
    header.pack(pady=20)

    # Buttons
    button_style = {
        "font": FONT_BUTTON,
        "bg": COLOR_BUTTON,
        "fg": "white",
        "activebackground": COLOR_ACCENT,
        "borderwidth": 0,
        "padx": 20,
        "pady": 10,
        "width": 20
    }

    tk.Button(root, text="Create Account", command=create_account_gui, **button_style).pack(pady=10)
    tk.Button(root, text="Deposit Money", command=deposit_gui, **button_style).pack(pady=10)
    tk.Button(root, text="Withdraw Money", command=withdraw_gui, **button_style).pack(pady=10)
    tk.Button(root, text="Check Balance", command=check_balance_gui, **button_style).pack(pady=10)
    tk.Button(root, text="View Transactions", command=view_transactions_gui, **button_style).pack(pady=10)

    # Exit button with a different color
    tk.Button(root, text="Exit", command=root.quit, bg=COLOR_WARNING, fg="white", font=FONT_BUTTON, borderwidth=0, padx=20, pady=10, width=20).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_menu()