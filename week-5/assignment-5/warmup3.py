#hardcoded list of Ghanaian names
fav_names = ["Kwame","Yaw", "Kwadwo","Kofi","Kwasi","kwabena","Kweku"]
search_name=input("Enter a name to search for:").capitalize()
found_index = -1
for i in range(len(fav_names)):
   if fav_names[i] == search_name:
       found_index = i
       print(f"Found '{search_name}' at index {found_index}. ")
       break
if found_index != -1:
           print(f"Found {search_name} at index {found_index}.")
else :
       print(f"Sorry, '{search_name}' was not found in the list.")
