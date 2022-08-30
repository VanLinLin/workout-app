import cv2
import mediapipe as mp
import time


# 匯入物件辨識所需權重
mp_objectron = mp.solutions.objectron

# 匯入繪圖風格套件
mp_drawing_styles = mp.solutions.drawing_styles

# 匯入繪圖方法
mp_drawing = mp.solutions.drawing_utils

# 建立鏡頭物件
cap = cv2.VideoCapture(1)

# 建立3D物件辨識的物件
with mp_objectron.Objectron(
    static_image_mode=False,        # 偵測照片時才需開啟
    max_num_objects=5,              # 最大物件數量
    min_detection_confidence=0.2,   # 最小偵測信心程度，小於此值將直接忽略
    min_tracking_confidence=0.5,    # 最小追蹤信心程度，小於此值將直接忽略
    model_name='Shoe'               # 要偵測的物件
) as objectron:

    # 如果鏡頭開啟，則進入迴圈
    while cap.isOpened():

        # success -> 使用影片才會用到，用於判斷影片是否結束
        # image -> 每一幀影像
        success, image = cap.read()

        # 若是沒有串流資源，則離開迴圈
        if not success:
            break

        # 每一幀影像開始處理時間
        start = time.time()

        # 轉換色彩通道順序
        # openCV -> BGR，mediapipe偵測使用 RGB，因此需轉換
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 一開始偵測的影像不進行繪圖，提高運算速度
        image.flags.writeable = False

        # mediapipe 對每一幀影像進行處理
        result = objectron.process(image)

        # 因為顯示是使用openCV，因此需再將色彩通道轉回來
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # 因為要看到效果，因此要把繪圖功能打開
        image.flags.writeable = True

        # 判斷是否有偵測到物件
        if result.detected_objects:

            # 將偵測到的每一個物件取出
            for detected_object in result.detected_objects:

                # 畫出地標
                mp_drawing.draw_landmarks(
                    image,
                    detected_object.landmarks_2d,
                    mp_objectron.BOX_CONNECTIONS,
                )

                # 畫出軸
                mp_drawing.draw_axis(image, detected_object.rotation, detected_object.translation)

        # 每一幀影像處理結束時間
        end = time.time()

        # 處理每一幀影像時間間隔
        total_time = end - start

        # 計算fps
        fps = 1 / total_time

        # 用於將文字顯示在影像上
        cv2.putText(image, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 2)

        # 顯示影像
        cv2.imshow('3D object detection', image)

        # 判斷q是否被按下(不分大小寫)
        if cv2.waitKey(5) == ord('q'.casefold()):
            # q被按下 -> 離開迴圈
            break

# 釋放鏡頭資源
cap.release()