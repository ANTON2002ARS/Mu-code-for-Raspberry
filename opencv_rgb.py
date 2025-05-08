import cv2

# Попытка открыть первую камеру (индекс 0)
cap = cv2.VideoCapture(0, cv2.CAP_V4L)
#cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


if not cap.isOpened():
    print("Ошибка открытия камеры")
    
else:
    while True:
        ret, frame = cap.read()
        
        
        #print(f"Ширина: {frame.shape[1]}, Высота: {frame.shape[0]}")
        
        cv2.imshow('Video', frame)
        
        if ret == false:
            print("Failed to capture frame")
        if image is None:
            print("Image could not be loade")
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
