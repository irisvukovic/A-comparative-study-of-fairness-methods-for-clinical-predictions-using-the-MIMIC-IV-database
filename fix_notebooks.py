import json
import os
import glob

def fix_notebook_add_state(filename):
    print(f"Processing {filename}...")
    with open(filename, 'r') as f:
        nb = json.load(f)
    
    # Add missing 'state' key to widgets
    if 'metadata' in nb and 'widgets' in nb['metadata']:
        if 'state' not in nb['metadata']['widgets']:
            nb['metadata']['widgets']['state'] = {}
            print(f"  ✓ Fixed widgets metadata")
        else:
            print(f"  - No fix needed")
    else:
        print(f"  - No widgets metadata found")
    
    with open(filename, 'w') as f:
        json.dump(nb, f, indent=2)

# Find all notebooks in current directory and subdirectories
notebooks = glob.glob('**/*.ipynb', recursive=True)

if not notebooks:
    print("No notebooks found!")
else:
    print(f"Found {len(notebooks)} notebook(s)\n")
    for notebook in notebooks:
        fix_notebook_add_state(notebook)
    print("\n✓ Done!")
