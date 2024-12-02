import os
import textwrap

def write_repository_to_text_file(repo_path, output_file, max_line_length=80):
    repo_name = os.path.basename(os.path.abspath(repo_path))  # Get the repository name
    with open(output_file, "w", encoding="utf-8") as outfile:
        for root, dirs, files in os.walk(repo_path):
            # Exclude hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for file in files:
                # Exclude hidden files
                if file.startswith('.') or file.endswith(('.db', '.jpeg', '.png')):
                    continue
                
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, repo_path)
                full_relative_path = os.path.join(repo_name, relative_path)  # Include repo name
                outfile.write(f"{full_relative_path}\n")  # Write the file path
                outfile.write("-" * 80 + "\n")  # Separator for clarity
                try:
                    with open(file_path, "r", encoding="utf-8") as infile:
                        for line in infile:
                            wrapped_lines = textwrap.wrap(line, width=max_line_length)
                            for wrapped_line in wrapped_lines:
                                outfile.write(wrapped_line + "\n")
                except Exception as e:
                    outfile.write(f"[Error reading file: {e}]\n")
                outfile.write("\n" + "=" * 80 + "\n\n")  # Separator between files

# Update with your repository path and desired output file path
repository_path = "/home/dmp/Workspace/GenAI/langchain-chatbot"
repo_name = os.path.basename(os.path.abspath(repository_path))
output_file_path = os.path.join(os.getcwd(), repo_name + "_output_file.txt")

write_repository_to_text_file(repository_path, output_file_path)
print(f"Contents written to {output_file_path}")
