"""
========================================
FILE HANDLING IN PYTHON
========================================

Definition:
-----------
File handling allows Python programs
to read data from files and write data
into files permanently.
"""

# ==================================================
# WHY FILE HANDLING IS IMPORTANT
# ==================================================

"""
✔ Store data permanently
✔ Read large data efficiently
✔ Used in logs, reports, databases
✔ Required in real-world applications
"""

# ==================================================
# FILE MODES
# ==================================================

"""
Mode | Meaning
----------------
r    | Read (default)
w    | Write (overwrite)
a    | Append
x    | Create new file
rb   | Read binary
wb   | Write binary
"""

# ==================================================
# OPENING AND CLOSING FILE
# ==================================================

"""
open(filename, mode)
close() is used to free resources
"""

# f = open("data.txt", "w")
# f.write("Hello Python")
# f.close()

# ==================================================
# READING FROM FILE
# ==================================================

# f = open("data.txt", "r")
# print(f.read())
# f.close()

# ==================================================
# READ METHODS
# ==================================================

"""
✔ read()       → Reads entire file
✔ readline()   → Reads one line
✔ readlines()  → Reads all lines as list
"""

# f = open("data.txt", "r")
# print(f.readline())
# print(f.readlines())
# f.close()

# ==================================================
# WRITING TO FILE
# ==================================================

# f = open("data.txt", "w")
# f.write("Python File Handling\n")
# f.write("Second line")
# f.close()

# ==================================================
# APPENDING DATA
# ==================================================

# f = open("data.txt", "a")
# f.write("\nAppended line")
# f.close()

# ==================================================
# PROGRAM LOGIC
# ==================================================

"""
1. Open file in required mode
2. Perform read/write operation
3. Close file to release memory
"""

# ==================================================
# USING with STATEMENT (BEST PRACTICE)
# ==================================================

"""
with automatically closes file
"""

# with open("data.txt", "r") as f:
#     print(f.read())

# ==================================================
# FILE NOT FOUND ERROR HANDLING
# ==================================================

# try:
#     with open("missing.txt", "r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File does not exist")

# ==================================================
# WORKING WITH CSV FILE (BASIC)
# ==================================================

# import csv
#
# with open("data.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Name", "Age"])
#     writer.writerow(["Rohit", 25])

# with open("data.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# ==================================================
# WORKING WITH JSON FILE (BASIC)
# ==================================================

import json

# data = {"name": "Rohit", "age": 25}

# with open("data.json", "w") as f:
#     json.dump(data, f)

# with open("data.json", "r") as f:
#     print(json.load(f))

# ==================================================
# IMPORTANT POINTS
# ==================================================

"""
✔ Always close files
✔ Use with statement
✔ Handle file exceptions
✔ Use correct file mode
"""

# ==================================================
# QUICK SUMMARY (EXAM READY)
# ==================================================

"""
File Handling:
--------------
open() → open file
read/write → file operations
close() → free resources
with → safest method
"""
