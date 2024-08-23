import math

def NULL_not_found(object: any) -> int:
    type_name = type(object).__name__  # Get the type name of the object
    
    # Dictionary of "null-like" values
    NULL_dict = {
        "NoneType": None,
        "float": float("NaN"),
        "int": 0,
        "str": "",
        "bool": False
    }
    
    # Dictionary to map values to descriptive names
    name_dict = {
        None: "Nothing",
        0: "Zero",
        "": "Empty",
        False: "Fake",
    }
    
    # Special case for NaN, as NaN is not equal to itself
    if type_name == "float" and isinstance(object, float) and math.isnan(object):
        key_name = "Cheese"
        value_display = "nan"
    # Check if the object matches the expected "null-like" value
    elif type_name in NULL_dict and object == NULL_dict[type_name]:
        key_name = name_dict[object]
        value_display = str(object)
    else:
        print("Type not Found")
        return 1
    
    # Print the result in the desired format
    print(f"{key_name}: {value_display} {type(object)}")
    return 0
