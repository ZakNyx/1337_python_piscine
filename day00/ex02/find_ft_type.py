def all_thing_is_obj(object: any) -> int:
    # Get the name of the type as a string 
    type_name = type(object).__name__
    
    # Define a set of known types that we want to handle explicitly
    known_types = {"list", "tuple", "set", "dict", "str"}
    
    if type_name == "str":
        print(f"{object} is in the kitchen: {type(object)}")
    # Check if the type is in the set of known types
    elif type_name in known_types:
        print(f"{type_name.capitalize()}: {type(object)}")
    else:
        print("Type not found")
    
    return 42