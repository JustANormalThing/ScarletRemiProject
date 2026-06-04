import subprocess

command = [
    "python", "C:/Users/Admin/Desktop/ReactProject/ProjectNew/ProjectThing/yolov5/detectForTests.py",
    "--weights", "C:/Users/Admin/Desktop/ReactProject/ProjectNew/ProjectThing/yolov5/runs/train/exp4/weights/best.pt",
    "--img", "640",
    "--source", "0",  
    "--classes", "0",
    "--project", "runs/camera_detection",
    "--name", "grape_trunk_detection",
    "--exist-ok"
]

subprocess.run(command)

#rtsp://admin:admin123456@169.254.235.193/ch=1&subtype=0 #external 
# 0 is build in camera
#2880x1620