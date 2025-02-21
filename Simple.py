from operator import getitem
from tkinter import getint, getdouble
import torch
from torch.xpu import get_arch_list
from ultralytics import YOLO
model = YOLO("yolov8m.pt")
model.train(data="data.yaml", epochs=30)
result = model.predict("1.jpg")
result = result[0]
dog = result.boxes;
for box in result.boxes:
    print("type:", result.names[getint(box.cls)])
    print("probability", getdouble(box.conf))
    cords = box.xyxy
    print("coordinate", cords[0])
