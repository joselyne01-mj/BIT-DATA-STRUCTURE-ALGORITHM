import array

# Step 1: Integers
mentorship_values = [85, 90, 78, 92, 88, 79, 95]

# Compute total, average, minimum, and maximum values
total = sum(mentorship_values)
average = total / len(mentorship_values)
min_value = min(mentorship_values)
max_value = max(mentorship_values)

# Step 2: Strings (Formatted report using f-strings)
report = f"""
Mentorship Pairing Log Summary:
--------------------------------
Total: {total}
Average: {average:.2f}
Minimum: {min_value}
Maximum: {max_value}
"""

# Step 3: Booleans (Threshold condition check)
threshold = 85
if average > threshold:
    status_message = "Above Standard"
else:
    status_message = "Below Standard"

# Step 4: Lists (Maintain list, add, remove, sort)
mentorship_list = ['John', 'Alice', 'Bob', 'Charlie', 'David']

# Add a new mentor
mentorship_list.append('Eve')

# Remove a mentor based on a condition (remove 'Bob')
if 'Bob' in mentorship_list:
    mentorship_list.remove('Bob')

# Sort and display the list before and after modification
print("List before modifications:")
print(['John', 'Alice', 'Bob', 'Charlie', 'David'])
print("\nList after modifications:")
print(mentorship_list)

# Step 5: Arrays (Using the array module)
mentorship_array = array.array('i', [85, 90, 78, 92, 88, 79, 95])

# Compute sum of the array
array_sum = sum(mentorship_array)

# Compare sum with list sum
list_sum = sum(mentorship_values)

# Step 6: Dictionaries (List of dictionaries)
mentorship_dicts = [
    {'id': 1, 'name': 'John', 'value': 85},
    {'id': 2, 'name': 'Alice', 'value': 90},
    {'id': 3, 'name': 'Bob', 'value': 78},
    {'id': 4, 'name': 'Charlie', 'value': 92},
    {'id': 5, 'name': 'David', 'value': 88}
]

# Update one record (change 'value' for 'John' to 95)
for mentor in mentorship_dicts:
    if mentor['name'] == 'John':
        mentor['value'] = 95

# Delete another record (remove 'Bob')
mentorship_dicts = [mentor for mentor in mentorship_dicts if mentor['name'] != 'Bob']

# Compute total of 'value' field
value_total = sum(mentor['value'] for mentor in mentorship_dicts)

# Output the final results
print("\nMentorship Log Report:")
print(report)
print(f"Status: {status_message}")
print(f"Array Sum: {array_sum}, List Sum: {list_sum}")
print(f"Updated mentorship records (total value sum): {value_total}")
print("\nUpdated mentorship records:")
for mentor in mentorship_dicts:
    print(mentor)
