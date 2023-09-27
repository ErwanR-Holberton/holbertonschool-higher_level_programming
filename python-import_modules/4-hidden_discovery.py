#!/usr/bin/python3
import hidden_4
for module_name in dir(hidden_4):
    if not module_name.startswith("__"):
        print(module_name)
