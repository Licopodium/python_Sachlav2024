users = []
print()
# Step 2: Add 'kevin', 'bob', and 'alice' to the list without reassigning
users.append('kevin')
users.append('bob')
users.append('alice')

# Step 3: Remove 'bob' from the list without reassigning
users.remove('bob')

# Step 4: Reverse the users list and assign it to 'rev_users'
rev_users = list(reversed(users))

# Step 5: Add 'melody' where 'bob' used to be
users.insert(1, 'melody')

# Step 6: Add 'andy', 'wanda', and 'jim' using a single command
users.extend(['andy', 'wanda', 'jim'])

# Step 7: Slice the users list to get the 3rd and 4th items and assign to 'center_users'
center_users = users[2:4]

# Output the final results
print("users:", users)
print("rev_users:", rev_users)
print("center_users:", center_users)
