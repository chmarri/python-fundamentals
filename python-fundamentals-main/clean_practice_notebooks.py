"""
Script to remove all markdown cells from practice notebooks.
Keeps only code cells for hands-on practice.
"""
import json
from pathlib import Path

def clean_notebook(notebook_path):
    """Remove all markdown cells from a notebook, keeping only code cells."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    original_count = len(notebook['cells'])
    
    # Keep only code cells
    notebook['cells'] = [cell for cell in notebook['cells'] if cell['cell_type'] == 'code']
    
    new_count = len(notebook['cells'])
    removed = original_count - new_count
    
    # Save the cleaned notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    return original_count, new_count, removed

def main():
    """Find and clean all practice notebooks."""
    base_path = Path(r'c:\OD\OneDrive - Microsoft\Python_Projects\python-fundamentals-main')
    
    # Find all practice notebooks
    practice_notebooks = list(base_path.rglob('*Practice*.ipynb'))
    
    print(f"Found {len(practice_notebooks)} practice notebooks\n")
    
    total_removed = 0
    for i, notebook_path in enumerate(practice_notebooks, 1):
        try:
            original, new, removed = clean_notebook(notebook_path)
            total_removed += removed
            
            rel_path = notebook_path.relative_to(base_path)
            if removed > 0:
                print(f"{i:3}. {rel_path}")
                print(f"     Removed {removed} markdown cells ({original} → {new} cells)")
        except Exception as e:
            print(f"ERROR processing {notebook_path.name}: {e}")
    
    print(f"\n✓ Processed {len(practice_notebooks)} notebooks")
    print(f"✓ Removed {total_removed} total markdown cells")

if __name__ == '__main__':
    main()
