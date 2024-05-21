from ultralytics import YOLO

model = YOLO('./processing/Doc_detect/runs/detect/train6/weights/best.pt')
model.fuse()