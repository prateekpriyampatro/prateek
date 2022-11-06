import cv2
img = cv2.imread('solar-system.jpg')


tS= 'sun'
tS1 = 'mercury'
tS2 = 'venus'
tS3 = 'earth'
tS4 = 'mars'
tS5 = 'jupiter'
tS6 = 'saturn'
tS7 = 'uranus'
tS8 = 'neptune'
cv2.putText(img,tS,(50,20),fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=0.8,color=(0,0,255))
cv2.putText(img,tS1,(100,270),fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=0.6,color=(255,255,255))
cv2.putText(img,tS2,(200,270),fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=0.6,color=(255,255,255))
cv2.putText(img,tS3,(300,270),fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=0.6,color=(255,255,255))
cv2.putText(img,tS4,(400,270),fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=0.6,color=(255,255,255))
cv2.putText(img,tS5,(500,400),fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=0.6,color=(255,255,255))
cv2.putText(img,tS6,(700,270),fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=0.6,color=(255,255,255))
cv2.putText(img,tS7,(950,300),fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=0.6,color=(255,255,255))
cv2.putText(img,tS8,(1070,300),fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=0.6,color=(255,255,255))
cv2.imshow('gong',img)
cv2.waitKey(0)