import cv2
import mediapipe as mp

# 匯入繪圖套件
mp_drawing = mp.solutions.drawing_utils

# 匯入繪圖風格套件
mp_drawing_styles = mp.solutions.drawing_styles

# 匯入手部辨識權重
mp_hands = mp.solutions.hands

# 判斷是否有其他鏡頭資源，若沒有的話則使用原本的鏡頭
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) if cv2.VideoCapture(1).isOpened() else cv2.VideoCapture(0, cv2.CAP_DSHOW)

# 建立手部辨識物件
with mp_hands.Hands(
                    model_complexity=0,             # 模型複雜度，範圍:1~2，越大越複雜，判斷時間越久、但越準確
                    min_detection_confidence=0.5,   # 最小偵測信心程度，小於此值將直接忽略
                    min_tracking_confidence=0.5     # 最小追蹤信心程度，小於此值將直接忽略
                    ) as hands:

    # 如果鏡頭開啟，則進入迴圈
    while cap.isOpened():

        # success -> 使用影片才會用到，用於判斷影片是否結束
        # image -> 每一幀影像
        success, image = cap.read()
        
        # 若是沒有串流資源，則離開迴圈
        if not success:
            break

        # 一開始偵測的影像不進行繪圖，提高運算速度
        image.flags.writeable = False


        # 轉換色彩通道順序
        # openCV -> BGR，mediapipe偵測使用 RGB，因此需轉換
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # mediapipe 對每一幀影像進行處理
        results = hands.process(image)


        # 因為要看到效果，因此要把繪圖功能打開
        image.flags.writeable = True

        # 因為顯示是使用openCV，因此需再將色彩通道轉回來
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # 判斷是否有偵測到物件
        if results.multi_hand_landmarks:
            # 將偵測到的每一個物件取出
            for hand_landmarks in results.multi_hand_landmarks:

                # 畫出地標
                mp_drawing.draw_landmarks(
                                            image,
                                            hand_landmarks,
                                            mp_hands.HAND_CONNECTIONS,
                                            mp_drawing_styles.get_default_hand_landmarks_style(),
                                            mp_drawing_styles.get_default_hand_connections_style()
                                            )

        # 顯示影像
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))

        # 判斷q是否被按下(不分大小寫)
        if cv2.waitKey(5) == ord('q'):
            # q被按下 -> 離開迴圈
            break

    # 釋放鏡頭資源
    cap.release()