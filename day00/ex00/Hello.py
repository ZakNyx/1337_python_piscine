ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Modifying the list
ft_list[1] = "World!"

# Modifying the tuple by converting to list and back to tuple
ft_temp_list = list(ft_tuple)
ft_temp_list[1] = "Morocco!"
ft_tuple = tuple(ft_temp_list)

# Modifying the set
ft_set.remove("tutu!")
ft_set.add("Benguerir!")

# Modifying the dictionary
ft_dict["Hello"] = "1337Benguerir"

# Printing the results
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
