import cv2
from ultralytics import YOLO
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.preview_configuration.main.size = (1280,720)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

# Загрузка предварительно обученной модели YOLOv8
model = YOLO('yolov8n.pt')  # Используйте yolov8n.pt для наименьшей модели

# Открытие видеопотока (например, веб-камера или видеофайл)
video_source = 0  # 0 для веб-камеры, или укажите путь к видеофайлу
#cap = cv2.VideoCapture(video_source)
#cap.isOpened()
while True:
    # Чтение кадра из видеопотока
    annotated_frame = picam2.capture_array()
    
    # Выполнение предсказания на текущем кадре
    results = model(annotated_frame)

    # Визуализация результатов на кадре
    #annotated_frame = results.plot()
    
    for result in results:
        # Извлеките bounding boxes
        boxes = result.boxes.xyxy  
        # Получите координаты bounding boxes в формате [x1, y1, x2, y2]
        scores = result.boxes.conf  # Получите вероятности
        classes = result.names  # Получите имена классов
        class_ids = result.boxes.cls  # Получите индексы классов
    
    for box, score, class_id in zip(boxes, scores, class_ids):                         
        x1, y1, x2, y2 = map(int, box)  
        # Преобразуйте координаты в целые числа
        # Рисуем прямоугольник на изображении
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (255, 0, 0), 2)          
        # Подготовьте текст для отображения
        # Имя объекта и вероятность
        label = f"{model.names[int(class_id)]}: {score:.2f}"   
        # Определите позицию текста
        # Позиция чуть выше прямоугольника
        text_position = (x1, y1 + 20)  
        # Добавьте текст на изображение
        cv2.putText(annotated_frame, label, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)        
    
    # Отображение аннотированного кадра
    cv2.imshow("YOLOv8 Inference", annotated_frame)

    # Прерывание цикла при нажатии клавиши 'q'й
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
#cap.release()
cv2.destroyAllWindows()
