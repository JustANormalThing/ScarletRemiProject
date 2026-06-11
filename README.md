## About project
This project is a trained model made using [YOLO5](https://github.com/ultralytics/yolov5) view [credits](https://github.com/JustANormalThing/ScarletRemiProject#credit) 

This project is about counting grape vine trees.

|<img height="260" src="./runs/train/exp4/val_batch1_pred.jpg" description="Raw frame" width="480"/>|
|<img height="260" src="./runs/train/exp4/val_batch0_pred.jpg" description="Raw frame" width="480"/>|

## Geting started
```
git clone https://github.com/ultralytics/yolov5
```
If you want to you can clone this.
```
git clone https://github.com/JustANormalThing/ScarletRemiProject.git
```
But all you need from this project is detectForTests.py Camera_YOLO.py and model from exp4 best.pt

```
Libs to download pip install -r requirements.txt
```
```
pip install -r requirements.txt
```
## How to run the model
```
py -3.12 Camera_YOLO.py
```
If you need more information check the file it self, I wrote about it there  

## Data
|<img height="260" src="./runs/train/exp4/val_batch0_labels.jpg" description="Raw frame" width="480"/>|
|---------------------------------------------------------------------------------------|
|Results of validation                                                                                                    |

Here is all the data for and from traing my model

For more information check this: [Results](https://github.com/JustANormalThing/ScarletRemiProject/tree/main/runs/train/exp4)

<img height="400" src="./runs/train/exp4/results.png" description="Raw frame" width="400"/><img height="400" src="./runs/train/exp4/F1_curve.png" description="Raw frame" width="400"/>

|Results of the                                                                                                |
## Credit
This project is made using [YOLO5:](https://github.com/ultralytics/yolov5) all credit to them for making this possible

Jocher, G. (2020). YOLOv5 by Ultralytics (Version 7.0) [Computer software]. https://doi.org/10.5281/zenodo.3908559


This project also used [Lable Studio:](https://github.com/HumanSignal/label-studio) for boundig boxes detection

The name of the project is form Touhou project(https://en.touhouwiki.net/wiki/Remilia_Scarlet)
