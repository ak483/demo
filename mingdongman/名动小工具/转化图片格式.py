import os

from PIL import Image

path1 = "C:\\Users\\Adminitrator03\\Desktop\\baike\\"
path2 = "C:\\Users\\Adminitrator03\\Desktop\\baikeform\\"


def jpeg2jpg(path_in, path_out):
    img = Image.open(path_in)
    img = img.convert("RGB")
    img.save(path_out, "JPEG", quality=80, optimize=True, progressive=True)


def png2jpg(path_in, path_out):
    img = Image.open(path_in)
    img = img.convert("RGB")
    img.save(path_out, "JPEG", quality=80, optimize=True, progressive=True)


def JPG2jpg(path_in, path_out):
    img = Image.open(path_in)
    img = img.convert("RGB")
    img.save(path_out, "JPEG", quality=80, optimize=True, progressive=True)


def PNG2jpg(path_in, path_out):
    img = Image.open(path_in)
    img = img.convert("RGB")
    img.save(path_out, "JPEG", quality=80, optimize=True, progressive=True)


def jpg2jpg(path_in, path_out):
    img = Image.open(path_in)
    img = img.convert("RGB")
    img.save(path_out, "JPEG", quality=80, optimize=True, progressive=True)


images = os.listdir(path1)
for i in images:
    print(i)
    if os.path.splitext(i)[1] == ".jpeg":
        source = path1 + "\\" + str(i.split(".")[0]) + ".jpeg"
        target = path2 + "\\" + str(i.split(".")[0]) + ".jpg"
        jpeg2jpg(source, target)
    elif os.path.splitext(i)[1] == ".png":
        source = path1 + "\\" + str(i.split(".")[0]) + ".png"
        target = path2 + "\\" + str(i.split(".")[0]) + ".jpg"
        png2jpg(source, target)
    elif os.path.splitext(i)[1] == ".JPG":
        source = path1 + "\\" + str(i.split(".")[0]) + ".JPG"
        target = path2 + "\\" + str(i.split(".")[0]) + ".jpg"
        JPG2jpg(source, target)
    elif os.path.splitext(i)[1] == ".PNG":
        source = path1 + "\\" + str(i.split(".")[0]) + ".PNG"
        target = path2 + "\\" + str(i.split(".")[0]) + ".jpg"
        PNG2jpg(source, target)
    elif os.path.splitext(i)[1] == ".jpg":
        source = path1 + "\\" + str(i.split(".")[0]) + ".jpg"
        target = path2 + "\\" + str(i.split(".")[0]) + ".jpg"
        jpg2jpg(source, target)