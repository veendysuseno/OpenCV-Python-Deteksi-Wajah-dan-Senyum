
import cv2
import os

# Lokasi folder proyek
folder = os.path.dirname(os.path.abspath(__file__))

# Memuat file Haar Cascade dari folder proyek
path_wajah = os.path.join(
    folder, "haarcascade_frontalface_default.xml"
)
path_senyum = os.path.join(
    folder, "haarcascade_smile.xml"
)

cascade_wajah = cv2.CascadeClassifier(path_wajah)
cascade_senyum = cv2.CascadeClassifier(path_senyum)

# Periksa apakah file XML berhasil dibaca
if cascade_wajah.empty():
    raise FileNotFoundError(
        f"File cascade wajah tidak ditemukan: {path_wajah}"
    )

if cascade_senyum.empty():
    raise FileNotFoundError(
        f"File cascade senyum tidak ditemukan: {path_senyum}"
    )

font = cv2.FONT_HERSHEY_SIMPLEX


def detect(gray, frame):
    wajah = cascade_wajah.detectMultiScale(
        gray,
        scaleFactor=1.29,
        minNeighbors=6
    )

    for (x, y, w, h) in wajah:
        cv2.rectangle(
            frame, (x, y), (x + w, y + h),
            (255, 255, 0), 2
        )

        cv2.putText(
            frame, "Wajah", (x, y - 12),
            font, 1, (255, 255, 0), 2
        )

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        senyum = cascade_senyum.detectMultiScale(
            roi_gray,
            scaleFactor=1.7,
            minNeighbors=20,
            minSize=(20, 20)
        )

        for (sx, sy, sw, sh) in senyum:
            cv2.rectangle(
                roi_color,
                (sx, sy), (sx + sw, sy + sh),
                (0, 255, 255), 2
            )

            cv2.putText(
                roi_color, "Senyum", (sx, max(sy - 12, 20)),
                font, 0.7, (0, 255, 255), 2
            )

    return frame


# Membaca gambar dari folder proyek
path_gambar = os.path.join(folder, "gambar.jpg")
gambar = cv2.imread(path_gambar)

if gambar is None:
    raise FileNotFoundError(
        f"Gambar tidak ditemukan atau tidak bisa dibaca: {path_gambar}"
    )

# Konversi ke grayscale
ubahKeGray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

# Deteksi wajah dan senyum
hasil = detect(ubahKeGray, gambar)

# Tampilkan hasil
cv2.imshow("Deteksi Wajah dan Senyum", hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()
