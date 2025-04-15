import os

# Create the folder for the generated pages
folder = "load_test_pages"
os.makedirs(folder, exist_ok=True)

# Generate 1000 Markdown files with simplified content
for i in range(1, 1001):
    with open(f"{folder}/page_{i:04d}.md", "w") as f:
        f.write(f"# Load Test Page {i}\n\n")
        f.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
                "when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n\n")
        f.write("Why do we use it? It is a long established fact that a reader will be distracted by the readable "
                "content of a page when looking at its layout.\n\n")
        f.write("Where does it come from? Contrary to popular belief, Lorem Ipsum is not simply random text. "
                "It has roots in classical Latin literature from 45 BC.\n")
        f.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
                "when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n\n")
        f.write("Why do we use it? It is a long established fact that a reader will be distracted by the readable "
                "content of a page when looking at its layout.\n\n")
        f.write("Where does it come from? Contrary to popular belief, Lorem Ipsum is not simply random text. "
                "It has roots in classical Latin literature from 45 BC.\n")
        f.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
                "when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n\n")
        f.write("Why do we use it? It is a long established fact that a reader will be distracted by the readable "
                "content of a page when looking at its layout.\n\n")
        f.write("Where does it come from? Contrary to popular belief, Lorem Ipsum is not simply random text. "
                "It has roots in classical Latin literature from 45 BC.\n")
        f.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
                "when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n\n")
        f.write("Why do we use it? It is a long established fact that a reader will be distracted by the readable "
                "content of a page when looking at its layout.\n\n")
        f.write("Where does it come from? Contrary to popular belief, Lorem Ipsum is not simply random text. "
                "It has roots in classical Latin literature from 45 BC.\n")
        f.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
                "when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n\n")
        f.write("Why do we use it? It is a long established fact that a reader will be distracted by the readable "
                "content of a page when looking at its layout.\n\n")
        f.write("Where does it come from? Contrary to popular belief, Lorem Ipsum is not simply random text. "
                "It has roots in classical Latin literature from 45 BC.\n")