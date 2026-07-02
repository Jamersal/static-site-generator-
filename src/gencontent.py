import os
from markdown_blocks import markdown_to_html_node
from pathlib import Path

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            return title
    raise Exception("no h1 header found")

def generate_page(from_path: str, template_path: str, dest_path: str | Path, basepath: str) -> None:
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    template = template.replace('href="/', 'href="' + basepath)
    template = template.replace('src="/', 'src="' + basepath)

    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path,basepath):
    entries = os.listdir(dir_path_content)
    for entry in entries:
       from_path = os.path.join(dir_path_content, entry)
       dest_path = os.path.join(dest_dir_path, entry)
       
       if os.path.isfile(from_path) and from_path.endswith(".md"):
           dest_path = Path(dest_path).with_suffix(".html")
           generate_page(from_path,template_path,dest_path,basepath)
       elif os.path.isdir(from_path):
           generate_pages_recursive(from_path, template_path, dest_path,basepath)
           
           

