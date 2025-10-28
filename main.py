from PIL import Image
import os

#create new pdf and convert
def new_pdf(img_list, fn):
    pdf_path = fn + ".pdf"
    img_list[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=img_list[1:]    #save and append all
    )

def check_all_img(files):
    for f in files:
        try:
            with Image.open(f) as img:
                img.verify()  # verify that it is, indeed, an image
        except Exception:
            return False
    return True


#get images
path = "."

items = os.listdir(path)  #check all current files
dirr = [item for item in items if os.path.isdir(os.path.join(path, item))]
files = sorted([item for item in items if os.path.isfile(os.path.join(path, item))])

#Convert if:
#   All items in dirr are img
#   All files are img

for d in dirr:
    f_in_d = [os.path.join(d, f) for f in sorted(os.listdir(d))]    #create full file paths
    if check_all_img(f_in_d):
        new_pdf([Image.open(f) for f in f_in_d], d)

if check_all_img(files):
    new_pdf([Image.open(f) for f in files], files[0])    #name of first item sorted

