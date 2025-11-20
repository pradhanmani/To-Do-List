# user_input = "random"

# def show_menu():
#     print("Menu:")
#     print("1.Add an item")
#     print("2. Mark as done")
#     print("3. View items")
#     print("4. Exit")

# while user_input != "4":
    
#     show_menu()
#     user_input = input("Enter your choice:")

#     if user_input == "1":
#         print("Add an item")
#     elif user_input == "2":
#         print("Mark as done")
#     elif user_input == "3":
#         print("View the to do items ")
#     elif user_input == "4":
#         print("Goodbye!!!")
#     else:
#         print("Please enter 1 , 2 , 3 or 4")
        
# def print_sq_values(numbers):
#     for n in numbers:
#         sq = n*n
#         print ("Square of" , n , "is" , sq)
# numbers = [ 1, 2, 3 , 4 ,5]
    
# print_sq_values(numbers)

user_input = "random"
data = []
def show_menu():
    print("Menu:")
    print("1. Add an item")
    print("2. Mark as done")
    print("3. View Items")
    print("4. Exit")

while user_input != "4":
    show_menu()
    user_input = input(">>>")
    
    if user_input == "1":
        item = input("What is to be done? >>")
        data.append(item)
        print("Added item:", item)
    elif user_input == "2":
        item = input ("What is to be marked as done?")
        if item in data:
            data.remove(item)
            print("Removed item:", item)
        else:
            print("Item does not exist in the list")
        # print("Mark as Done")
    elif user_input == "3":
        print("List of to-do- items")
        for item in data:
            print(item)
    elif user_input == "4":
        print("Goodbye!!!")
    else:
        print("Please enter one of 1,2,3,4")
        


# TO DO LIST APP
