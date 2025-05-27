"""
To open files, use the built-in function open().
open()
file: the name of the file to open.
modes:
r read-only
w write-only (creates a new file if it does not exist)
"""

# This opens the file (in writing mode).
file = open("example.txt", "w") # This returns a file class object.

# File uses a method (file.write()) to write to the file.
file.write("This is an example of writing to a file.\n")

# This method closes the file. Finishes the work.
file.close()

"""
"With" statement helps with automatically closing files and writing to them.
"""

with open("example.txt", "w") as file:
    file.write("Name, Description\n")
    file.write("This is another example of writing to a file.\n")



