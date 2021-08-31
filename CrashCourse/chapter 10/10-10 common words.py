"""10-10. Common Words: 

Visit Project Gutenberg (https://gutenberg.org/) and find a few texts you’d 
like to analyze. Download the text files for these works, or copy the raw text 
from your browser into a text file on your computer. You can use the count() 
method to find out how many times a word or phrase appears in a string. For 
example, the following code counts the number of times 'row' appears in a 
string: 

>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3 

Notice that converting the string to lowercase using lower() catches all 
appearances of the word you’re looking for, regardless of how it’s formatted. 
Write a program that reads the files you found at Project Gutenberg and 
determines how many times the word 'the' appears in each text. This will 
be an approximation because it will also count words such as 'then' and 
'there'. Try counting 'the ', with a space in the string, and see how much 
lower your count is.
"""

filenames = [
    "text_files/dracula.txt",
    "text_files/frankenstein.txt",
    "file that does not exist.txt",
    "text_files/metamorphosis.txt",
    "text_files/sherlock holmes.txt",
]

searchstr = "the "
# searchstr = "the"

for filename in filenames:
    print(f"Attempting to open: {filename}")

    try:
        with open(filename, encoding="utf-8") as file_obj:
            contents = file_obj.read()
            count = contents.lower().count(searchstr)
            print(f"\t'{searchstr}' occurs {count} times in the file.")

    except FileNotFoundError:
        print(f"\tCannot find file.")

    print()
