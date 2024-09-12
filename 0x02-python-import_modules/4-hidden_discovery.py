#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util

    # Load the compiled module from the file hidden_4.pyc
    spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get all the names defined by the module and filter out names starting with __
    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    
    # Sort the names in alphabetical order
    for name in sorted(names):
        print(name)
