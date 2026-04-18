# Expense Tracker Program

# Ask for student details
name = input("Student name: ")
budget = float(input("Weekly budget: "))

# Expense categories
categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]

examples = [
    "Lunch, snacks, coffee",
    "Bus, jeepney, ride-share",
    "Load, data plan, WiFi",
    "Notebook, pen, paper",
    "Games, movies, hangout"
]
# Show categories using loop
print("\n==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")

for i in range(len(categories)):
    print(f" {i+1}. {categories[i]:20} (e.g. {examples[i]})")

print("==========================================")

expenses = []

# Allow exactly 4 entries
for i in range(4):
    print(f"\n--- EXPENSE {i+1} ---")
    cat = int(input("Category (0–5): "))

    if cat == 0:
        continue

    if 1 <= cat <= 5:
        desc = input("Description: ")
        amount = float(input("Amount spent: "))

        # Check high expense (25% of budget)
        if amount > 0.25 * budget:
            alert = "! High Expense Alert!"
        else:
            alert = ""

        expenses.append([cat, desc, amount, alert])
    else:
        print("Invalid category. Skipping entry.")

# Compute totals
total = 0
for e in expenses:
    total += e[2]

remaining = budget - total

if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."

# Display report
print("\n======================================================")
print(f"Student name: {name}")
print(f"Weekly budget: {budget:.0f}\n")

for i, e in enumerate(expenses, start=1):
    cat_name = categories[e[0] - 1]
    print(f"{i}. {cat_name} | {e[1]} | {e[2]:.0f} {e[3]}")
print("\n------------------------------------------------------")
print(f"Total spent: {total:.0f}")
print(f"Remaining balance: {remaining:.0f}")
print(f"Status: {status}")
print("======================================================")