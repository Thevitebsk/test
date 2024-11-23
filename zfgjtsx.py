import cv2
import numpy as np
import tensorflow as tf

# Загрузите предобученную модель (например, MobileNet SSD)
model = tf.saved_model.load('ssd_mobilenet_v2_fpnlite_320x320/saved_model')

# Функция для обнаружения объектов
def detect_objects(image):
    input_tensor = tf.convert_to_tensor(image)
    input_tensor = input_tensor[tf.newaxis, ...]
    
    detections = model(input_tensor)
    return detections

# Загрузите стартовое изображение
image_path = 'path/to/your/image.jpg'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Выполните обнаружение объектов
detections = detect_objects(image_rgb)

# Извлеките найденные объекты (например, только людей)
height, width, _ = image.shape
for i in range(len(detections['detection_boxes'][0])):
    box = detections['detection_boxes'][0][i].numpy()
    score = detections['detection_scores'][0][i].numpy()
    if score > 0.5:  # Убедитесь, что уверенность достаточно высока
        (ymin, xmin, ymax, xmax) = (box * np.array([height, width, height, width])).astype('int')
        
        # Наложите свое изображение на обнаруженный паттерн
        mask_image = cv2.imread('path/to/your/mask_image.png')
        mask_image = cv2.resize(mask_image, (xmax - xmin, ymax - ymin))
        
        # Наложение маски на исходное изображение
        image[ymin:ymax, xmin:xmax] = mask_image

# Сохранение или отображение результата
cv2.imwrite('output_image.jpg', image)
cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
