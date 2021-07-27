names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
# Create a variable total_cost and initialize it to 0
total_cost = 0

# Iterate through actual_insurance_costs to get the total cost
j = 0
while j < len(actual_insurance_costs):
  total_cost += actual_insurance_costs[j]
  j += 1

# Calculate the average cost for the actual_insurance_costs
average_cost = total_cost / len(actual_insurance_costs)

# A print statement to display the Average Insurance Cost in an informative way
print("Average Insurance Cost: " + str(average_cost) + " dollars.")

# Display a new line
print("\n")

# Using Range in Loops
for i in range(0, len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  difference = actual_insurance_costs[i] - average_cost
  print("\nThe insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")
  if insurance_cost > average_cost:
    print("The insurance cost for " +
     name + " is above average")
    print("The insurance cost for " + name + " is " + str(difference) + " dollars" + " higher than the average cost")
  elif insurance_cost < average_cost:
    print("The insurance cost for " + name + " is bellow average")
  else:
    print("The insurance cost for " + name + " equal to the average.")

# Create a new list updated_estimated_costs
updated_estimated_costs = [(cost * (11/10)) for cost in estimated_insurance_costs]

# Display a new line
print("\n")

# Display estimated_insurance_costs
print(estimated_insurance_costs)