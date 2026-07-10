id = "y"
case = "yes"

with open("products.txt", "a") as list_shopping:
    while id == "y" or id == case:
        name = input("name product: ")
        price = input("price product: ")

        list_shopping.write(name+",")
        list_shopping.write(price+ "\n")

        id = input("Do you want to continue? (y/yes/n): ")

print("Products saved successfully")