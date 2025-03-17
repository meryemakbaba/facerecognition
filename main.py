import cv2

# Yüz tespiti için Haar Cascade sınıflandırıcısını yükle
face_cascade = cv2.CascadeClassifier(r"classifier/haarcascade_frontalface_default.xml")

# Kamerayı başlat
video_capture = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare yakala
    ret, frame = video_capture.read()

    # Görüntüyü gri tonlamaya çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit et
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Yüzlerin etrafını dikdörtgenle çizebilmek için döngü
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Görüntüyü ekranda göster
    cv2.imshow('Video', frame)

    # 'q' tuşuna basarak çıkış yapabilirsin
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve pencereleri kapat
video_capture.release()
cv2.destroyAllWindows()

