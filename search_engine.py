import os

folder = "data"

query = input("Enter word to search: ").lower()

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    with open(path, "r") as f:
        content = f.read().lower()

        if query in content:
            print("Found in:", file)