import os
import re
import shutil

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"C:\Blog\thesinglerun\content\posts" 
attachments_dir = r"C:\Obsidian\obsidian - celestia\1. Projects\The Single Run\posts\img"
static_images_dir = r"C:\Blog\thesinglerun\static\images"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        print(filepath)

        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        print(content)
        # Step 2: Find all image links in the format ![Image Description](/images/Pasted%20image%20...%20.png)
        images = re.findall(r'\[\[([^]]*\.(png|jpeg))\]\]', content)
        print(images)
        print(images[0][0])

        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image in images:
            image = image[0]
            print(image)

            # Prepare the Markdown-compatible link with %20 replacing spaces
            markdown_image = f"[Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"[[{image}]]", markdown_image)
            
            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            print(image_source)
            print(static_images_dir)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")
