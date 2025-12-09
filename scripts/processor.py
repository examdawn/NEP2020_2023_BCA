import os
import re
import frontmatter
import subprocess
import datetime
from pathlib import Path

# --- Master Prompt ---
SYSTEM_PROMPT = """
You are a helpful academic assistant. 
1. Answer the user's question accurately.
2. Skip diagrams unless they are Mermaid.js. Keep Mermaid diagrams short and simple.
3. Formatting:
   - Use #### (H4) headings and smaller. DO NOT use #, ##, or ###.
   - Avoid HTML divs and spans unless absolutely necessary.
   - Use Markdown for bolding and lists.
4. Be concise.
5. Keep in mind that the text will be fed to Vitepress. 
6. Code highlighting will be done with shiki. 
"""

def call_gh_copilot(prompt):
    """
    Uses GitHub CLI to generate text. 
    Assumes `gh` is authenticated in the workflow.
    Falls back to a mock if gh model fails (for safety).
    """
    full_prompt = f"{SYSTEM_PROMPT}\n\nTask: {prompt}"
    
    try:
        # Trying to use gh model (if 'models' extension is installed or built-in)
        # Using standard GPT-4o-mini for cost/speed efficiency if available
        cmd = ["gh", "model", "prompt", full_prompt] 
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            # Fallback: simple echo for debugging if API fails/not configured
            print(f"GH Model failed: {result.stderr}")
            return ""
    except Exception as e:
        return f""

def process_file(filepath):
    post = frontmatter.load(filepath)
    content = post.content
    original_content = content
    
    # Regex to find: use-AI-here-please: "some text"
    # Matches both: use-AI-here-please: "prompt" AND use-AI-here-please
    pattern = re.compile(r'use-AI-here-please(?::\s*"(.*?)")?', re.IGNORECASE)
    
    matches = list(pattern.finditer(content))
    
    # Iterate backwards to avoid index shifting issues during replacement
    for match in reversed(matches):
        full_match = match.group(0)
        user_prompt = match.group(1)
        
        if not user_prompt:
            # If no specific prompt, look at context or use default
            user_prompt = "Explain the concept related to this section."

        print(f"Generating for: {user_prompt[:30]}... in {filepath}")
        
        ai_response = call_gh_copilot(user_prompt)
        
        # Generate Disclaimer
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        disclaimer = f"\n\n<sub>This was AI generated from github copilot on {date_str}</sub>\n"
        
        replacement = f"\n{ai_response}\n{disclaimer}\n"
        
        # Replace the tag with response
        start, end = match.span()
        content = content[:start] + replacement + content[end:]

    # Check if we made changes
    if content != original_content:
        post.content = content
        
        # Cleanup: Check if any use-AI tags remain. If not, remove frontmatter key.
        if not pattern.search(content):
            if 'use-AI-here-please' in post.metadata:
                del post.metadata['use-AI-here-please']
            # Note: We keep 'clanker: true' so we know this file is tracked, 
            # unless you strictly want it removed too.
            # Uncomment below to remove clanker trigger when completely done:
            # if 'clanker' in post.metadata:
            #     del post.metadata['clanker']

        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))
        print(f"Updated {filepath}")

def main():
    target_dir = os.environ.get("TARGET_DIR", ".")
    print(f"Processing directory: {target_dir}")
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".md"):
                fp = os.path.join(root, file)
                
                # Double check frontmatter before processing
                try:
                    fm = frontmatter.load(fp)
                    if fm.get('clanker') is True:
                        process_file(fp)
                except:
                    continue

if __name__ == "__main__":
    main()