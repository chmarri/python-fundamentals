import json
import os
from pathlib import Path

def create_practice_notebook(source_path, practice_path):
    """Create a practice version of a notebook with empty code cells."""
    with open(source_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Create practice version by emptying code cells
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'code':
            # Keep the cell structure but empty the source
            cell['source'] = []
            # Clear outputs
            cell['outputs'] = []
            if 'execution_count' in cell:
                cell['execution_count'] = None
    
    # Save practice notebook
    os.makedirs(os.path.dirname(practice_path), exist_ok=True)
    with open(practice_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    return True

def find_all_notebooks(root_dir):
    """Find all .ipynb files in the directory structure."""
    notebooks = []
    root_path = Path(root_dir)
    
    for notebook_path in root_path.rglob('*.ipynb'):
        # Skip already created practice files and solution files
        if 'practice' not in notebook_path.stem.lower() and 'solution' not in notebook_path.stem.lower():
            notebooks.append(notebook_path)
    
    return notebooks

def main():
    # Get the script directory
    script_dir = Path(__file__).parent
    
    # Find all notebooks
    notebooks = find_all_notebooks(script_dir)
    
    print(f"Found {len(notebooks)} notebooks to process")
    
    created_count = 0
    for notebook_path in notebooks:
        # Create practice filename in the same directory
        practice_name = notebook_path.stem + ' - Practice.ipynb'
        practice_path = notebook_path.parent / practice_name
        
        if practice_path.exists():
            print(f"Skipping (already exists): {practice_path.relative_to(script_dir)}")
            continue
        
        try:
            create_practice_notebook(notebook_path, practice_path)
            print(f"Created: {practice_path.relative_to(script_dir)}")
            created_count += 1
        except Exception as e:
            print(f"Error processing {notebook_path.name}: {e}")
    
    print(f"\nCompleted! Created {created_count} practice notebooks")

if __name__ == "__main__":
    main()
