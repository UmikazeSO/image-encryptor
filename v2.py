import os
from PIL import Image


def encryption(img_name):
    img = Image.open(img_name)
    try:
        r, g, b, a = img.split()
    except:
        r, g, b = img.split()

    width = img.size[0]
    height = img.size[1]

    A = []
    u = 4
    x = 0.656
    for i in range(width * height):
        x = u * x * (1 - x)
        A.append(int(x*255))

    pixels_r = list(r.getdata())
    pixels_g = list(g.getdata())
    pixels_b = list(b.getdata())
    pix_r = pixels_r
    pix_g = pixels_g
    pix_b = pixels_b

    for index in range(len(A)):
        pix_r[index] = A[index] ^ pixels_r[index]
        pix_g[index] = A[index] ^ pixels_g[index]
        pix_b[index] = A[index] ^ pixels_b[index]

    r.putdata(pix_r)
    g.putdata(pix_g)
    b.putdata(pix_b)

    isExists = os.path.exists("./results")
    if not isExists:
        os.makedirs("./results")

    tmp = [r, g, b]
    merge_img = Image.merge("RGB", tmp)
    merge_img.save("./results/x_" + img_name, "png")


if __name__ == '__main__':
    filelist = os.listdir("./")
    print("该文件可将目录下所有的图片类文件加密 or 解密")

    for item in filelist:
        try:
            encryption(item)
            print("the image ----" + item + "----reborn successful _(:з」∠)_")
        except:
            print("unable to read ----" + item + "----as image")


