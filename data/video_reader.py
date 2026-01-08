import cv2

def read_video(path, max_frames=200):
    cap = cv2.VideoCapture(path)
    frames = []

    while cap.isOpened() and len(frames) < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    return frames
