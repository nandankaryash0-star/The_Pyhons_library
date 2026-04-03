import os 
import shutil

target_dir = os.path.expanduser('~/Downloads')

EXTENSIONS = {
    "Images":[".jpg",".jpeg",".png"],
    "Documents":[".pdf",".docx",".txt"]
}

def organize_files():
    os.chdir(target_dir)

    for file in os.listdir(target_dir):
        if os.path.isdir(file):
            continue


    filename, extension = os.path.splitext(file)
    extension = extension.lower()

    for category, ext_list in EXTENSIONS.items():
        if extension in ext_list:
            if not os.path.exists(category):
                os.makedirs(category)

            print(f"Moving {file} -> {category}/")
            shutil.move(file,os.path.join(category,file))
            break


if __name__ == "__main__":
    organize_files()
    print("Folder organized")