def get_valid_cost(prompt):
    while True:
        try:
            cost = float(input(prompt))
            if cost >= 0:  
                return cost
            else:
                print("Please enter a valid positive number.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

venue_cost = get_valid_cost("Enter the estimated cost for the venue: ")
catering_cost = get_valid_cost("Enter the estimated cost for catering: ")
decorations_cost = get_valid_cost("Enter the estimated cost for decorations: ")
entertainment_cost = get_valid_cost("Enter the estimated cost for entertainment: ")
miscellaneous_cost = get_valid_cost("Enter the estimated cost for miscellaneous expenses: ")

total_cost = 0
total_cost += venue_cost
total_cost += catering_cost
total_cost += decorations_cost
total_cost += entertainment_cost
total_cost += miscellaneous_cost

predefined_budget = 1000.0  

print("\n--- Expense Summary ---")
print(f"Total Estimated Cost: ${total_cost:.2f}")
if total_cost <= predefined_budget:
    print("The total estimated cost is within the predefined budget.")
else:
    print("The total estimated cost exceeds the predefined budget.")