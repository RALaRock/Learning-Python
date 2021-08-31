"""
10-6. Addition: 
One common problem when prompting for numerical input occurs when people 
provide text instead of numbers. When you try to convert the input to an int, 
you’ll get a ValueError. Write a program that prompts for two numbers. Add 
them together and print the result. Catch the ValueError if either input value 
is not a number, and print a friendly error message. Test your program by 
entering two numbers and then by entering some text instead of a number.
"""

while True:
    print("Add two numbers. Enter two numbers or press Enter to quit.")
    try:
        first_num = input("Enter a number: ")
        if not first_num:
            break
        first_num = int(first_num)

        second_num = input("Enter another number: ")
        if not second_num:
            break
        second_num = int(second_num)

    except ValueError:
        print("You must enter only integers.")

    else:
        total = first_num + second_num
        print(f"The total of {first_num} + {second_num} is {total}.")
