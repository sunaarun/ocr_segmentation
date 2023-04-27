import  cv2
import glob
from pre_processing import preProcessing

# myImage= cv2.imread('pngImgs/t2.png')
pngImages = glob.glob("pngImgs/*.PNG")
jpgImages = glob.glob("jpgImgs/*.JPG")
EjpgImages = glob.glob("jepgImgs/*.JPEG")
def main():
    print("From Main function")
    #PNG Images
    for png in pngImages:
        print(png)
        image = cv2.imread(png)
        returnImage =preProcessing(image)
        cv2.imshow(f'After Processed Image ${png}',returnImage)
        cv2.waitKey()
    # JPG Images
    for jpg in jpgImages:
        print(jpg)
        image = cv2.imread(jpg)
        returnImage = preProcessing(image)
        cv2.imshow(f'After Processed Image ${jpg}', returnImage)
        cv2.waitKey()
    #JPEG images
    for ejpg in EjpgImages:
        print(ejpg)
        image = cv2.imread(ejpg)
        returnImage = preProcessing(image)
        cv2.imshow(f'After Processed Image ${ejpg}', returnImage)
        cv2.waitKey()

main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#------------------------------------------------------------
