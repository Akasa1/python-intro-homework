numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    
    choice = int(input("Choose an option (1-5): "))
# Finds the smallest/minimum number
    if choice == 1:
      if not numbers:
            print("The list is empty.")
      else :
        minimum = numbers[0]
        for num in numbers:
            if num < minimum:
                minimum = num
        print(f"The minimum number is: {minimum}")
        
# Finds the maximun number  
    elif choice == 2:
      if not numbers:
            print("The list is empty.")
      else :
        maximun = numbers[0]
        for num in numbers:
            if num > maximun:
                maximun = num
        print(f"The maximum number is: {maximun}")

# Search for a number 
    elif choice == 3:
      try :
        user_num = int(input("Choose a number: "))
        num_index = -1
        
        for i in range(len(numbers)):
            if numbers[i] == user_num : 
                num_index = i 
                break

        if num_index != -1:
            print(f"Found {user_num} at index {num_index}.")
        else:
            print(f"Sorry, Number {user_num} not found in the list.")  
      except ValueError:
            print("Please enter a valid integer.")  
        
      # Sort the list using Bubble Sort
    elif choice == 4:
        sorted_list = list(numbers)
        
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(sorted_list) - 1):
                if sorted_list[i] > sorted_list[i + 1]:
                    temp = sorted_list[i]
                    sorted_list[i] = sorted_list[i + 1]
                    sorted_list[i + 1] = temp
                    swapped = True
                    
        print(sorted_list)

    # Quit the program
    elif choice == 5:
        print("Goodbye! Thank you for using Number Cruncher.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

