# 手势识别的人机交互系统
基于mediapipe+opencv+autopy的人机交互系统
# 功能
通过手势实现对电脑的操作，如鼠标左右键，键盘的上下键（可对PPT进行翻页）
# 所需环境
python == 3.8

mediapipe

opencv-python

numpy

aytopy == 4.0.0
# 手势说明
![e74fa2f075bc4dc29d59935e398095fa](https://user-images.githubusercontent.com/118904918/215310808-4cacbe5c-bf1e-425d-82ae-c4d8798c12b8.png)

鼠标右键：关键点4靠近关键点5

![Desktop Screenshot 2023 01 29 - 15 11 24 43](https://user-images.githubusercontent.com/118904918/215312474-33991f09-3e72-4d55-86bb-36df52f2e02b.png)


鼠标左键：食指伸直，中指下垂

![Desktop Screenshot 2023 01 29 - 15 11 32 09](https://user-images.githubusercontent.com/118904918/215312424-dc7b175a-1585-4b14-8488-2a54c451ca5e.png)


键盘上键：食指、中指伸直，无名指和尾值靠拢，然后再伸直

![Desktop Screenshot 2023 01 29 - 15 11 43 97](https://user-images.githubusercontent.com/118904918/215312432-f9444a1c-eeb6-4d44-8608-88a55ecb0034.png)


键盘下键：无名指和尾值向下收缩不动，食指和中指靠拢，靠拢的同时向下弯曲

![Desktop Screenshot 2023 01 29 - 15 11 38 22](https://user-images.githubusercontent.com/118904918/215312367-c568e352-790e-4028-964e-ce7dd9d493b0.png)


注意：1、出现在镜头时的手势建议和下面图片的手势一样

![Desktop Screenshot 2023 01 29 - 15 11 50 70](https://user-images.githubusercontent.com/118904918/215312374-bae8115d-55c1-4759-ab4a-87032acaa2a4.png)

2、完成一次手势操作后要恢复原样，不然会占用性能，导致卡顿
