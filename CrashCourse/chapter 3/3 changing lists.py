# it's common to build lists by appending items as 
# users provide them
# initialize an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ktm')
# results in the same thing as this:
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ktm']
print(motorcycles)

# add to list
motorcycles.append('ducati')
print(motorcycles)

# insert to anywhere in a list
motorcycles.insert(0, 'bmw') # insert at start of list
print(motorcycles)
motorcycles.insert(-2, 'bmw') # insert two from end of list
print(motorcycles)

# remove from list
print()
print('remove from list')
print(motorcycles)

# does remove() remove all elements with same value?
# NO it only removes the first instance found
motorcycles.remove('bmw')
print(motorcycles)

# if you know the position of the item, use del
del motorcycles[1] # remove second item in list
print(motorcycles)

# remove the last item in a list and work with it 
# using pop method
pop_motorcycles = motorcycles.pop()
print(motorcycles)
print(pop_motorcycles)

# use pop to remove any item from a list with in index
pop_motorcycles = motorcycles.pop(0) # remove first item
print(motorcycles)
print(pop_motorcycles)

# removing a list item by it's value
# if you don't know the item's position
# but do know the item's name
motorcycles.remove('ktm')
print(motorcycles)

# if the item does not exist, returns none
motorcycles.remove('yamaha')
print(motorcycles)

# remove all occurences of an item from a list
def remove_items(test_list, item):
      
    # using list comprehension to perform the task
    res = [i for i in test_list if i != item]
  
    return res

test_list = [1,1,2,3,4,3,5,6,7,1,4,5]
print(remove_items(test_list, 1))
