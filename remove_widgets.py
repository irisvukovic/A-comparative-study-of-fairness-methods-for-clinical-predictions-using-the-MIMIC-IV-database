import json
import glob

def remove_widgets_metadata(filename):
    print(f"Processing {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Remove widgets metadata completely
    changed = False
    if 'metadata' in nb:
        if 'widgets' in nb['metadata']:
            del nb['metadata']['widgets']
            changed = True
            print(f"  ✓ Removed widgets metadata")
    
    # Also check each cell for widget metadata
    if 'cells' in nb:
        for cell in nb['cells']:
            if 'metadata' in cell and 'widgets' in cell['metadata']:
                del cell['metadata']['widgets']
                changed = True
                print(f"  ✓ Removed widgets from cell")
    
    if changed:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print(f"  ✓ Saved changes")
    else:
        print(f"  - No widgets found")

# Find all notebooks
notebooks = glob.glob('**/*.ipynb', recursive=True)

print(f"Found {len(notebooks)} notebook(s)\n")
for notebook in notebooks:
    if '.ipynb_checkpoints' not in notebook:
        remove_widgets_metadata(notebook)

print("\n✓ Done!")
