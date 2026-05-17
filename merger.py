import os
import nbformat
import nbmerge

dir_path = "PV"

# 1. Ensure the files are sorted (optional but recommended for consistent order)
nb_files = sorted([os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith(".ipynb")])

# 2. Call merge_notebooks using the directory or the specific list
# Note: Some versions of nbmerge prefer the directory path directly
try:
    # Attempting to pass the list of file paths explicitly
    merged_nb = nbmerge.merge_notebooks(dir_path, file_paths=nb_files)

    # 3. nbmerge returns a NotebookNode, so we use nbformat to write it properly
    with open("merged.ipynb", "w", encoding="utf-8") as f:
        nbformat.write(merged_nb, f)

    print("Successfully merged notebooks into 'merged.ipynb'")

except Exception as e:
    print(f"An error occurred: {e}")