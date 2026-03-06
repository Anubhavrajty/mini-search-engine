import os
from collections import defaultdict

folder = "data"
query_input = input("Enter keyword(s) to search: ").strip().lower()
queries = query_input.split()

file_matches = defaultdict(list)  # store file_name: list of matched lines
file_counts = defaultdict(int)    # store file_name: number of matches

# Loop through all files in data/
for file_name in os.listdir(folder):
    path = os.path.join(folder, file_name)
    if os.path.isdir(path):
        continue  # ignore folders

    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for i, line in enumerate(lines, 1):
                line_lower = line.lower()
                for q in queries:
                    if q in line_lower:
                        # Highlight keyword in output
                        highlighted_line = line.replace(q, f"[{q.upper()}]")
                        file_matches[file_name].append(f"Line {i}: {highlighted_line.strip()}")
                        file_counts[file_name] += 1
    except Exception as e:
        print(f"Cannot read {file_name}: {e}")

# Sort files by number of matches (most relevant first)
sorted_files = sorted(file_counts.items(), key=lambda x: x[1], reverse=True)

if not sorted_files:
    print("No files found containing your keyword(s).")
else:
    for file_name, count in sorted_files:
        print(f"\nFound {count} match(es) in {file_name}:")
        for line in file_matches[file_name]:
            print(f"  {line}")