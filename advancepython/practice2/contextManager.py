## Write a context manager using @contextmanager that prints "Entering" and "Exiting" around a block.
from contextlib import contextmanager

# @contextmanager
# def my_context():
#     print("entering")
#     try:
#         yield
#     finally:
#         print("Exiting")
# with my_context():
#     print("inside the block")

## Create a context manager that temporarily changes the current working directory and restores it on exit.
import os
# @contextmanager
# def change_dir(path):
#     prev_dir = os.getcwd()
#     try:
#         os.chdir(path)
#         yield
#     finally:
#         os.chdir(prev_dir)
    
# print("Before: ", os.getcwd())
# with change_dir("/advancepython"):
#     print(f"inside: {os.getcwd()}")
# print(f"after: {os.getcwd()}")
