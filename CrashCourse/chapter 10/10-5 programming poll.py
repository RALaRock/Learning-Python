"""
10-5. Programming Poll: 
Write a while loop that asks people why they like programming. Each time 
someone enters a reason, add their reason to a file that stores all the 
responses.
"""
filename = "programming_poll.txt"

while True:
    answer = input("Why do you like programming (enter 'q' to quit): ")
    if answer == 'q':
        break
    elif not answer:
        continue

    with open(filename, 'a') as file_object:
        file_object.write(answer + '\n')
