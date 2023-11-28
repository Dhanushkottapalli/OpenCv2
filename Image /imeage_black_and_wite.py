#importing cv2 library to a program
import cv2
img = ('path')
#Reading an image from a folder by using imred() function and path of a image.
img1=cv2.imread(img,1)
#Re-sizing an immage by using resize() function as required.
img1=cv2.resize(img1,(1280,700))
#Showing/displaying the immage by using imshow() function.
cv2.imshow("My image",img1)
#printing the immage in Arrays matrix
print("Image ==\n",img1)


#Reading an image from a folder by using imred() function and path of a image.
img2=cv2.imread(img,0)
#Re-sizing an immage by using resize() function as required.
img2=cv2.resize(img2,(1280,700))
#Showing/displaying the immage by using imshow() function.
cv2.imshow("Gray Scale Image",img2)
#printing the immage in Arrays matrix
print("Image in gray scale==\n",img2)


#Reading an image from a folder by using imred() function and path of a image.
img3=cv2.imread(img,-1)
#Re-sizing an immage by using resize() function as required.
img3=cv2.resize(img3,(1280,700))
#Showing/displaying the immage by using imshow() function.
cv2.imshow("Original image",img3)
#printing the immage in Arrays matrix
print("Orginal image==\n",img3)

#cv2.waitKey(0) It will control life time of an displayed imeage
cv2.waitKey(0)
#cv2.destroyAllWindows() It will clear all the data left by the user in previous program
cv2.destroyAllWindows()


img1=cv2.imread(img,1)
img1=cv2.resize(img1,(700,700))
img1=cv2.flip(img1,0)
cv2.imshow("Converted image==",img1)
k=cv2.waitKey(0)& 0xFF
if k==ord("q"):
    cv2.destroyAllWindows()
elif k==ord("s"):
    cv2.imwrite("output.png",img1)
    cv2.destroyAllWindows()
