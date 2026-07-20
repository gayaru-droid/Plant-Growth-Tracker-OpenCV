import cv2

def resize(image,xfac=.5,yfac=.5):
    reimg=cv2.resize(image,(0,0),fx=xfac,fy=yfac,interpolation=cv2.INTER_LINEAR)
    return reimg
for i in range(5,15):
    img=cv2.imread(rf"C:\Users\User\Documents\Python\Python Tuto\DAY 03\codes\plants\D{i}.png",-1)
    hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    l_lim=(24,64,109)
    u_lim=(44,240,255)

    mask=cv2.inRange(hsv_img,l_lim,u_lim)
    ret=cv2.bitwise_and(img,img,mask=mask)

    contours,hirachey=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(img,contours,-1,(255,255,255),1)
    print(len(contours))

    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>500:
            print(area)
            cv2.drawContours(img,[cnt],-1,[0,0,255],2)
            x,y,w,h=cv2.boundingRect(cnt)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

            cv2.circle(img,(int(x+(w/2)),y),3,(0,0,255),-1)
            cv2.circle(img,(int(x+(w/2)),y+h),3,(0,0,255),-1)

            cv2.putText(img,"Heigth : "+str(h),((x+w),(y+h)),cv2.FONT_HERSHEY_SIMPLEX,.7,(0,0,255),2)

    cv2.imshow("Mask",resize(mask))
    cv2.imshow("Image",resize(img,.7,.7))
    cv2.waitKey(0)
cv2.destroyAllWindows