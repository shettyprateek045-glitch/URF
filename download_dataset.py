from roboflow import Roboflow
rf = Roboflow(api_key="YOUR_KEY")
project = rf.workspace("apiruk-95dey").project("water-pollution-zldff")
version = project.version(3)
dataset = version.download("yolov8")
