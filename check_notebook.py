import json

with open('imv_task_faim_workflow.ipynb', 'r') as f:
    nb = json.load(f)

# Find cells with huge outputs
for i, cell in enumerate(nb['cells']):
    if 'outputs' in cell:
        output_size = len(json.dumps(cell['outputs']))
        if output_size > 1000000:  # 1MB
            print(f"Cell {i} has large output: {output_size/1000000:.1f}MB")

