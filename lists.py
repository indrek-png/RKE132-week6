import random



""" print(f"We have {len(shopping_list)} items on the list.") """

""" shopping_list.append(["flour", "sugar", "baking powder"]) """

""" shopping_list.extend(["flour", "sugar", "baking powder"]) """

#shopping_list.remove("cheese")

""" for item in shopping_list.copy():
    if item == "cheese":
        shopping_list.remove(item) """

""" n = shopping_list.count("cheese") """
""" print(f"There are {n} cheese itmes on the list") """


""" apple_index = shopping_list.index("apples")
shopping_list[apple_index] = "bananas" """


""" found = "milk" in shopping_list """

""" for item in shopping_list:
    if item == "soy milk":
        found = True
        break """

""" if found:
    print("Milk is already on the list.")
else:
    print("There is no milk on the list.") """





""" print(shopping_list)

shopping_list.sort(reverse=True)
print(shopping_list) """


shopping_list = ["cheese", "apples", "bread", "cheese", "milk", "eggs", "cheese"]
""" print(shopping_list)
shopping_list.reverse()
print(shopping_list) """

shopping_list = ["cheese", "apples", "bread", "cheese", "milk", "eggs", "cheese"]

random_item = random.choice(shopping_list)
print(random_item)


""" for item in shopping_list:
    print(item) """
