from ultralytics import YOLO
model = YOLO("yolov8m.pt")

model.train(data="train.yaml", epochs=30)

result = model.predict("cat_dog.jpg")
result = result[0]
for box in result.boxes:
    cords = box.xyxy[0].tolist()
    cords = [round(x) for x in cords]
    print("Detect Name:", result.names[box.cls.item()])
    print("Detect Coordinates:", cords)
    print("Probability:", box.conf.item())
    
