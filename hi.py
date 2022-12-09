import cv2,pygame
pygame.init()
cap = cv2.VideoCapture('1.MOV') 
pygame.mixer.music.load("1.mp3")
pygame.mixer.music.play()
while cap.isOpened():
    ret, frame = cap.read()    
    cv2.namedWindow("frame", 0)  
    cv2.resizeWindow("frame", 1600, 900)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break
while True:
    pygame.mixer.music.stop()       
    break
