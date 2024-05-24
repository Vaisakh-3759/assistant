import cv2

def camera():
       video=cv2.VideoCapture(0)
       while True:
              ret,img=video.read()
              img=cv2.flip(img,1)
                            
              font=cv2.FONT_HERSHEY_DUPLEX
              gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
              
              #cv2.putText(frame,'working on it',(50,250),font,2,(100,155,2555),2,cv2.LINE_4)

              cv2.imshow('capturing',img)
              
               
              key=cv2.waitKey(1)
              if key==ord('q'):
                     break
       video.release()
       cv2.destroyAllWindows