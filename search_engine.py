import os
from collections import defaultdict

folder = "data"
query_input = input("Enter keyword(s) to search (separate multiple words with space): ").strip().lower()
queries = query_input.split()

file_matches = defaultdict(list)  # store file_name: list of lines matched
file_counts = defaultdict(int)    # store file_name: number of matches

# Loop through all files in the data folder
for file_name in os.listdir(folder):
    path = os.path.join(folder, file_name)
    if os.path.isdir(path):
        continue  # skip folders
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for i, line in enumerate(lines, 1):
                line_lower = line.strip().lower()
                for q in queries:
                    if q in line_lower:
                        file_matches[file_name].append(f"Line {i}: {line.strip()}")
                        file_counts[file_name] += 1
    except Exception as e:
        print(f"Cannot read {file_name}: {e}")

# Sort files by number of matches
sorted_files = sorted(file_counts.items(), key=lambda x: x[1], reverse=True)

if not sorted_files:
    print("No files found containing your keyword(s).")
else:
    for file_name, count in sorted_files:
        print(f"\nFound {count} matches in {file_name}:")
        for matched_line in file_matches[file_name]:
            print(f"  {matched_line}")