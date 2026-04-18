# EXPENSE TRACKER PROGRAM (FINAL VERSION WITH STRIP)

categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]

examples = [
    "[e.g. Lunch, snacks, coffee]",
    "[e.g. Bus, jeepney, ride-share]",
    "[e.g. Load, data plan, WiFi top-up]",
    "[e.g. Notebook, pen, bond paper]",
    "[e.g. Games, movies, hangout]"
]

# -----------------------------
# GET STUDENT NAME
# -----------------------------
while True:
    name = input("Enter student name: ")

    if name == "":
        print("Name cannot be empty. Try again.")
    else:
        valid_name = True

        for ch in name:
            if not (ch == " " or (ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z")):
                valid_name = False

        if valid_name == True:
            break
        else:
            print("Invalid name. Letters only. Try again.")

# -----------------------------
# GET WEEKLY BUDGET (WITH STRIP)
# -----------------------------
while True:
    budget_input = input("Enter weekly budget: ").strip()

    if budget_input == "":
        print("Budget cannot be empty. Try again.")
    else:
        valid_budget = True
        dot_count = 0

        i = 0
        while i < len(budget_input):
            ch = budget_input[i]

            if ch == ".":
                dot_count = dot_count + 1
                if dot_count > 1:
                    valid_budget = False

            elif not (ch >= "0" and ch <= "9"):
                valid_budget = False

            i = i + 1

        if valid_budget == True:
            budget = float(budget_input)
            break
        else:
            print("Invalid budget. Numbers only (spaces auto-fixed).")

# -----------------------------
# SHOW CATEGORIES
# -----------------------------
print("\nEXPENSE CATEGORIES:")

for i in range(5):
    print(str(i + 1) + ". " + categories[i] + " " + examples[i])

print("0. Skip entry")

# -----------------------------
# EXPENSE INPUTS
# -----------------------------
expenses = []
entry_count = 0

while entry_count < 4:

    while True:
        cat_input = input("\nChoose category (0-5): ")

        if cat_input == "":
            print("Invalid input.")
        else:
            valid_cat = True

            for ch in cat_input:
                if not (ch >= "0" and ch <= "9"):
                    valid_cat = False

            if valid_cat == True:
                cat_num = int(cat_input)

                if cat_num >= 0 and cat_num <= 5:
                    break
                else:
                    print("Invalid range.")
            else:
                print("Numbers only.")

    if cat_num == 0:
        entry_count = entry_count + 1
    else:
        description = input("Enter description: ")

        while True:
            amount_input = input("Enter amount spent: ")

            if amount_input == "":
                print("Invalid input.")
            else:
                valid_amt = True
                dot_count = 0

                for ch in amount_input:
                    if ch == ".":
                        dot_count = dot_count + 1
                        if dot_count > 1:
                            valid_amt = False
                    elif not (ch >= "0" and ch <= "9"):
                        valid_amt = False

                if valid_amt == True:
                    amount = float(amount_input)
                    break
                else:
                    print("Invalid amount.")

        alert = ""

        if amount > (0.25 * budget):
            alert = "! High Expense Alert!"

        expenses.append([categories[cat_num - 1], description, amount, alert])

        entry_count = entry_count + 1
        