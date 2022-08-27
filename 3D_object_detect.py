import cv2
import mediapipe as mp
import time

mp_objectron = mp.solutions.objectron
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(1)

with mp_objectron.Objectron(static_image_mode=False,
                            max_num_objects=5,
                            min_detection_confidence=0.2,
                            min_tracking_confidence=0.5,
                            model_name='Cup'
                            ) as objectron:
    
    while cap.isOpened():
        
        success, image = cap.read()

        start = time.time()

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image.flags.writeable = False

        result = objectron.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


        image.flags.writeable = True

        if result.detected_objects:
            for detected_object in result.detected_objects:
                mp_drawing.draw_landmarks(image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
                mp_drawing.draw_axis(image, detected_object.rotation, detected_object.translation)


        end = time.time()

        total_time = end - start

        fps = 1 / total_time

        cv2.putText(image, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 2)

        cv2.imshow('3D object detection', image)

        if cv2.waitKey(5) == ord('q'):
            break


cap.release()
