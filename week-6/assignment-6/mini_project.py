numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

#finding the minimum number 
def find_mini(numbers):
    if not numbers:
        return None
    
    current_min = numbers[0]
    for num in numbers:
        if num < current_min:
          current_min = num 
    return current_min      

#finding the maximum number
def find_max(numbers):
    if not numbers:
        return None
    
    current_max = numbers[0]
    for num in numbers:
      if  num > current_max:
       current_max = num 
    return current_max

# Searching for a number in the list
def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

# using bubble sort to sort the list
def bubble_sort(numbers):
    sorted_list = list(numbers)  # Creates a copy so the original remains untouched
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(sorted_list) - 1):
            if sorted_list[i] > sorted_list[i + 1]:
                # Swap elements
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[i + 1]
                sorted_list[i + 1] = temp
                swapped = True
    return sorted_list


def show_menu():
    """Prints the menu options and returns the user's choice as a string."""
    print("\n=== Number Cruncher Menu ===")
    print("1. Find Minimum")
    print("2. Find Maximum")
    print("3. Search for a Number")
    print("4. Sort List (Bubble Sort)")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")
    return choice

# Main while loop that calls show_menu() and dispatches to the correct function.
def main():
    
    while True:
        choice = show_menu()
        
        if choice == '1':
            minimum = find_mini(numbers)
            print(f"The minimum value is: {minimum}")
            
        elif choice == '2':
            maximum = find_max(numbers)
            print(f"The maximum value is: {maximum}")
            
        elif choice == '3':
            try:
                target = int(input("Choose a number to search for: "))
                index = search(numbers, target)
                
                
                if index != -1:
                    print(f"Found at index {index}")
                else:
                    print("Not found")
            except ValueError:
                print("Please enter a valid integer.")
                
        elif choice == '4':
            sorted_nums = bubble_sort(numbers)
            print(f"Sorted list: {sorted_nums}")
            
        elif choice == '5':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Call main() at the bottom of the file
if __name__ == "__main__":
    main()