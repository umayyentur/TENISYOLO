from ultralytics import YOLO

model = YOLO("yolov8x")

model.predict()


!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="ohBMiPh8HlOanJDFOo7J")
project = rf.workspace("viren-dhanwani").project("tennis-ball-detection")
version = project.version(6)
dataset = version.download("yolov5")
                