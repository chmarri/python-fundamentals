# GitHub Instructions for Python Fundamentals Repository

This document provides instructions for working with this Python Fundamentals learning repository on GitHub.

## 📋 Table of Contents
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Setting Up Your Environment](#setting-up-your-environment)
- [Working with the Repository](#working-with-the-repository)
- [Contributing Guidelines](#contributing-guidelines)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## 🚀 Getting Started

### Prerequisites
- Git installed on your computer ([Download Git](https://git-scm.com/downloads))
- Python 3.8+ installed ([Download Python](https://www.python.org/downloads/))
- GitHub account ([Sign up](https://github.com/signup))

### Cloning the Repository

1. **Clone via HTTPS:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/python-fundamentals.git
   cd python-fundamentals
   ```

2. **Clone via SSH (recommended if you have SSH keys set up):**
   ```bash
   git clone git@github.com:YOUR_USERNAME/python-fundamentals.git
   cd python-fundamentals
   ```

---

## 📁 Repository Structure

This repository is organized by course sections (numbered folders):

```
python-fundamentals/
├── 05 - Sequence Types/        # Lists, tuples, strings, slicing
├── 06 - Strings/                # Unicode, string methods, interpolation
├── 07 - Iteration/              # Loops, range, break/continue
├── 08 - Dictionaries/           # Dictionary operations
├── 09 - Sets/                   # Set operations
├── 10 - Comprehensions/         # List/dict/set comprehensions
├── 11 - Exceptions/             # Exception handling
├── 12 - Iterables and Iterators/
├── 14 - Some Additional Built-In Functions/
├── 15 - Practice Test 1/        # First exam
├── 17 - Sorting and Filtering/
├── 18 - Decorators/
├── 20 - Modules and Imports/
├── 22 - CSV Module/
├── 23 - Random Module/
├── 24 - Math and Statistics Module/
├── 25 - Decimal Module/
├── 27 - Practice Test 2/        # Second exam
├── 29 - NumPy/                  # NumPy tutorials
├── 30 - Pandas/                 # Pandas tutorials
├── 31 - Matplotlib/             # Plotting and visualization
├── 32 - Practice Test 3/        # Third exam
└── create_practice_files.py     # Utility script
```

Each section contains:
- Jupyter notebooks with lessons
- Exercise notebooks
- Solution notebooks
- Any necessary data files

---

## ⚙️ Setting Up Your Environment

### 1. Create a Virtual Environment

**On Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**On Windows:**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install Required Packages

**Basic Requirements:**
```bash
pip install jupyter notebook ipython
```

**For NumPy, Pandas, and Matplotlib sections (29-31):**
```bash
cd "29 - NumPy"
pip install -r requirements.txt
```

This will install:
- numpy
- scipy
- pandas
- matplotlib
- mplfinance

### 3. Launch Jupyter Notebook

```bash
jupyter notebook
```

This will open Jupyter in your browser at `http://localhost:8888`

---

## 💻 Working with the Repository

### Daily Workflow

1. **Pull latest changes** (before starting work):
   ```bash
   git pull origin main
   ```

2. **Create a new branch** for your work:
   ```bash
   git checkout -b feature/section-05-exercises
   ```

3. **Make your changes** and save your work

4. **Check what files changed**:
   ```bash
   git status
   ```

5. **Stage your changes**:
   ```bash
   # Add specific files
   git add "05 - Sequence Types/09 - Exercises/my_solution.ipynb"
   
   # Or add all changes
   git add .
   ```

6. **Commit your changes**:
   ```bash
   git commit -m "Complete Sequence Types exercises"
   ```

7. **Push to GitHub**:
   ```bash
   git push origin feature/section-05-exercises
   ```

### Managing Jupyter Notebooks

**Note:** Jupyter notebooks can create merge conflicts due to metadata and cell execution counts.

**Best practices:**
- Clear all outputs before committing: Cell → All Output → Clear
- Or use this command:
  ```bash
  jupyter nbconvert --clear-output --inplace "path/to/notebook.ipynb"
  ```

### Using the Practice Files Generator

The repository includes a utility script to create practice versions of notebooks:

```bash
python create_practice_files.py
```

This creates practice notebooks with empty code cells, allowing you to practice without seeing solutions.

---

## 🤝 Contributing Guidelines

### For Personal Learning

If you're using this as a personal learning repository:

1. **Fork the repository** to your own GitHub account
2. Work on your fork and push changes there
3. Keep your fork updated with the original repository:
   ```bash
   # Add original repository as upstream
   git remote add upstream https://github.com/ORIGINAL_OWNER/python-fundamentals.git
   
   # Fetch and merge updates
   git fetch upstream
   git merge upstream/main
   ```

### Commit Message Guidelines

Use clear, descriptive commit messages:

**Good examples:**
- `Complete Section 5 list exercises`
- `Add solution for dictionary iteration problems`
- `Fix typo in NumPy array creation example`

**Avoid:**
- `update`
- `changes`
- `fix`

### Branching Strategy

- `main` - Stable, working code
- `feature/*` - New exercises or sections
- `fix/*` - Bug fixes or corrections

---

## 📝 Best Practices

### 1. Keep Your Repository Clean

Add a `.gitignore` file to exclude unnecessary files:
```gitignore
# Python
__pycache__/
*.py[cod]
*.so
.Python

# Virtual Environment
.venv/
venv/
ENV/

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

### 2. Document Your Work

- Add comments to complex code
- Create markdown cells in notebooks to explain your thought process
- Update README files if you add new sections

### 3. Regular Commits

- Commit frequently with meaningful messages
- Don't wait until you've completed an entire section

### 4. Backup Your Work

- Push to GitHub regularly (at least daily)
- Keep your local and remote repositories in sync

---

## 🔧 Troubleshooting

### Common Issues

**Problem: Jupyter notebook won't start**
```bash
# Reinstall Jupyter
pip install --upgrade jupyter notebook
```

**Problem: Import errors for NumPy/Pandas**
```bash
# Ensure you're in the correct directory and install requirements
cd "29 - NumPy"
pip install -r requirements.txt
```

**Problem: Git merge conflicts in notebooks**
```bash
# Accept your version
git checkout --ours "path/to/notebook.ipynb"

# Accept incoming version
git checkout --theirs "path/to/notebook.ipynb"

# Then continue
git add "path/to/notebook.ipynb"
git commit -m "Resolve merge conflict in notebook"
```

**Problem: Virtual environment not activating**
```bash
# Recreate the virtual environment
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows
```

### Getting Help

- Check existing issues on GitHub
- Review the Jupyter documentation: https://jupyter.org/documentation
- Python documentation: https://docs.python.org/3/

---

## 📚 Additional Resources

- **Git Documentation:** https://git-scm.com/doc
- **GitHub Guides:** https://guides.github.com/
- **Jupyter Tutorial:** https://jupyter-notebook.readthedocs.io/
- **Python Official Tutorial:** https://docs.python.org/3/tutorial/
- **Udemy Course:** [Python Fundamentals Course Link]

---

## 📄 License

Please refer to the repository's LICENSE file for usage terms.

---

**Happy Learning! 🐍✨**

*Last updated: December 26, 2025*
