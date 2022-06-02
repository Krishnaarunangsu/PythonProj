# List copy using =
old_list = [1, 2, 3]
new_list = old_list

# Howerver, there is one problem with copying lists in this way. If you modify new_list,
# old_list is also modified.
# It is because the new list is referencing or pointing to the same old_list object.

# add an element to list
new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)
