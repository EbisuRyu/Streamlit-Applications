import cv2
import numpy as np
import streamlit as st
from PIL import Image

# Đường dẫn đến các file mô hình và cấu hình
MODEL = "./Object-Detection/model/MobileNetSSD_deploy.caffemodel"
PROTOTXT = "./Object-Detection/model/MobileNetSSD_deploy.prototxt.txt"


def process_image(image):
    """
    Xử lý hình ảnh để phát hiện đối tượng sử dụng MobileNet SSD.

    Args:
        image (np.ndarray): Hình ảnh đầu vào.

    Returns:
        np.ndarray: Ma trận phát hiện đối tượng.
    """
    # Tạo blob từ hình ảnh đầu vào
    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5
    )
    # Đọc mô hình và cấu hình
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    net.setInput(blob)
    detections = net.forward()
    return detections


def annotate_image(image, detections, confidence_threshold=0.5):
    """
    Chú thích hình ảnh với các hộp giới hạn dựa trên phát hiện đối tượng.

    Args:
        image (np.ndarray): Hình ảnh đầu vào.
        detections (np.ndarray): Ma trận phát hiện đối tượng.
        confidence_threshold (float): Ngưỡng tin cậy để hiển thị phát hiện.

    Returns:
        np.ndarray: Hình ảnh đã được chú thích.
    """
    (h, w) = image.shape[:2]
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > confidence_threshold:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (start_x, start_y, end_x, end_y) = box.astype("int")
            cv2.rectangle(image, (start_x, start_y), (end_x, end_y), 70, 2)
    return image


def main():
    """
    Hàm chính để chạy ứng dụng Streamlit phát hiện đối tượng.
    """
    st.title("Object Detection for Images")  # Tiêu đề của ứng dụng

    # Tải lên hình ảnh
    file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
    if file is not None:
        # Hiển thị hình ảnh đã tải lên
        st.image(file, caption="Uploaded Image")

        # Chuyển đổi hình ảnh thành định dạng numpy array
        image = Image.open(file)
        image = np.array(image)

        # Xử lý hình ảnh và phát hiện đối tượng
        detections = process_image(image)

        # Chú thích hình ảnh với các hộp giới hạn
        processed_image = annotate_image(image, detections)

        # Hiển thị hình ảnh đã được chú thích
        st.image(processed_image, caption="Processed Image")


if __name__ == "__main__":
    main()
