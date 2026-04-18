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
