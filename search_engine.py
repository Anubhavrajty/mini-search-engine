import os

folder = "data"
query = input("Enter the keyword to search: ").lower()

found_any = False

# Loop through all items in the data folder
for file_name in os.listdir(folder):
    path = os.path.join(folder, file_name)
    
    # Skip directories
    if os.path.isdir(path):
        continue
    
    # Open the file safely
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if query in line.lower():
                print(f"Found in: {file_name}")
                found_any = True
                break  # Stop after first match in this file

if not found_any:
    print("No files found containing:", query)