def all_thing_is_obj(object: any) -> int:
    # Get the name of the type as a string 
    type_name = type(object).__name__
    
    # Define a set of known types that we want to handle explicitly
    known_types = {"list", "tuple", "set", "dict", "str"}
    
    # Check if the type is 'str' for special handling
    if type_name == "str":
        # If the object is a string
        print(f"{object} is in the kitchen: {type(object)}")
    # Check if the type is in the set of known types
    elif type_name in known_types:
        # If the type is known, print the type name with a capitalized first letter
        print(f"{type_name.capitalize()}: {type(object)}")
    else:
        # If the type is not known
        print("Type not found")
    
    # Return 42 as required by the function specification
    return 42
