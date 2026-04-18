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
