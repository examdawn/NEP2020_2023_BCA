import os
import frontmatter
import json
import sys

def scan_files():
    matrix_data = {}
    
    # Walk through the directory
    for root, dirs, files in os.walk("."):
        if ".git" in root:
            continue
            
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                try:
                    post = frontmatter.load(filepath)
                    
                    # Check for explicit clanker: true
                    if post.get('clanker') is True:
                        # Check if "use-AI-here-please" exists in content text
                        if "use-AI-here-please" in post.content:
                            
                            # Parse Path structure: ./3rdsem/SubjectName/file.md
                            parts = os.path.normpath(filepath).split(os.sep)
                            
                            if len(parts) >= 3:
                                category = parts[1] # e.g., 3rdsem
                                subcategory = parts[2] # e.g., Computer-Communications-Networks
                                
                                key = f"{category}/{subcategory}"
                                
                                if key not in matrix_data:
                                    matrix_data[key] = {
                                        "category": category,
                                        "subcategory": subcategory,
                                        "path": os.path.join(category, subcategory)
                                    }
                except Exception as e:
                    print(f"Error parsing {filepath}: {e}", file=sys.stderr)

    # Convert to list for GitHub Actions Matrix
    output_list = list(matrix_data.values())
    
    # Print JSON to stdout for GITHUB_OUTPUT
    print(f"matrix={json.dumps(output_list)}")
    
    # Append to GITHUB_OUTPUT environment file
    if os.getenv('GITHUB_OUTPUT'):
        with open(os.getenv('GITHUB_OUTPUT'), 'a') as f:
            f.write(f"matrix={json.dumps(output_list)}\n")

if __name__ == "__main__":
    scan_files()