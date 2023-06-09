import os
import sys
import ast


def parse_code(file_path):
  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      code = file.read()
      parsed_tree = ast.parse(code)
      return parsed_tree
  except FileNotFoundError:
    print(f"File not found: {file_path}")
    return None


def compare_ast_trees(tree1, tree2):
  similarity = 0.0

  if type(tree1) == type(tree2):
    if isinstance(tree1, ast.AST):
      for child1, child2 in zip(ast.iter_child_nodes(tree1),
                                ast.iter_child_nodes(tree2)):
        similarity += compare_ast_trees(child1, child2)
      similarity += 1.0

    elif isinstance(tree1, (list, tuple)):
      for item1, item2 in zip(tree1, tree2):
        similarity += compare_ast_trees(item1, item2)

    else:
      similarity += float(tree1 == tree2)

  return similarity


def check_plagiarism(file1, file2, threshold=90):
  tree1 = parse_code(file1)
  tree2 = parse_code(file2)

  if tree1 and tree2:
    similarity = compare_ast_trees(tree1, tree2)
    similarity_percentage = (similarity / 2.0) * 100

    if similarity_percentage >= threshold:
      print("Plagiarism detected!")
      print(f"Similarity: {similarity_percentage}%")
    else:
      print("No plagiarism detected.")
      print(f"Similarity: {similarity_percentage}%")


def check_directory(directory,
                    threshold=90,
                    exclude_dirs=None,
                    exclude_files=None):
  if exclude_dirs is None:
    exclude_dirs = []
  if exclude_files is None:
    exclude_files = []

  for root, dirs, files in os.walk(directory):
    # Exclude directories
    dirs[:] = [d for d in dirs if d not in exclude_dirs]

    for file in files:
      if file in exclude_files:
        continue

      file_path = os.path.join(root, file)

      for other_file in files:
        if other_file == file or other_file in exclude_files:
          continue

        other_file_path = os.path.join(root, other_file)

        check_plagiarism(file_path, other_file_path, threshold)


# Example usage
file1 = 'file1.py'
file2 = 'file2.py'
check_plagiarism(file1, file2)

directory = 'code_directory'
exclude_dirs = ['tests', 'data']
exclude_files = ['config.py']
check_directory(directory,
                exclude_dirs=exclude_dirs,
                exclude_files=exclude_files)
