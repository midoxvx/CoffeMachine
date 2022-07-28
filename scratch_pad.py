my_dict = {'key1': 50}

def modifier():
    print(f"printing from within function {my_dict['key1']}")

modifier()


print(f"printing from outside function {my_dict['key1']}")