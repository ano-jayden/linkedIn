def merge_sort_strings_by_length(arr):
    if len(arr) <= 1:
        return arr
    
    # Split the list in half
    mid = len(arr) // 2
    left_half = merge_sort_strings_by_length(arr[:mid])
    right_half = merge_sort_strings_by_length(arr[mid:])
    
    # Merge the two halves
    return merge_by_length(left_half, right_half)

def merge_by_length(left, right):
    result = []
    i = 0
    j = 0

    # Merge elements from left and right based on the string lengths
    while i < len(left) and j < len(right):
        if len(left[i]) >= len(right[j]):  
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append the remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Three lists of video game names
games_list_1 = ["Red Dead Redemption", "GTA V", "Cyberpunk 2077", "Fortnite", "League of Legends", 
                "Minecraft", "The Last of Us", "FIFA 21", "Call of Duty", "Overwatch"]

games_list_2 = ["Dota 2", "Apex Legends", "Resident Evil Village", "Valorant", "Assassin's Creed Valhalla", 
                "Among Us", "God of War", "Battlefield", "Horizon Zero Dawn", "Far Cry 6"]

games_list_3 = ["Super Mario Odyssey", "The Legend of Zelda", "Spider-Man", "Halo Infinite", 
                "Mass Effect", "Final Fantasy VII", "Tetris", "Need for Speed", "The Witcher 3", "Sekiro"]

# Running the modified merge sort on the lists
sorted_games_list_1 = merge_sort_strings_by_length(games_list_1)
sorted_games_list_2 = merge_sort_strings_by_length(games_list_2)
sorted_games_list_3 = merge_sort_strings_by_length(games_list_3)

# Print the sorted lists
print("Sorted List 1 by length:", sorted_games_list_1)
print("Sorted List 2 by length:", sorted_games_list_2)
print("Sorted List 3 by length:", sorted_games_list_3)
