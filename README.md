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

![Desktop Screenshot 2023 01 29 - 15 11 24 43](https://user-images.githubusercontent.com/118904918/215311249-6d2dc6bb-b189-42a4-bd74-a464d51f583d.png)

鼠标左键：食指伸直，中指下垂

![Desktop Screenshot 2023 01 29 - 15 11 32 09](https://user-images.githubusercontent.com/118904918/215311285-3aa3919e-9434-4632-ba9a-e22c1c33b9ad.png)

键盘上键：食指、中指伸直，无名指和尾值靠拢，然后再伸直

![Desktop Screenshot 2023 01 29 - 15 11 43 97](https://user-images.githubusercontent.com/118904918/215311652-db53bb88-4dc5-4697-9085-2a3cf871c565.png)


键盘下键：无名指和尾值向下收缩不动，食指和中指靠拢，靠拢的同时向下弯曲

![Desktop Screenshot 2023 01 29 - 15 11 38 22](https://user-images.githubusercontent.com/118904918/215311641-ede7eaa8-bc2f-484c-b443-d121f4833f85.png)

注意：1、出现在镜头时的手势建议和下面图片的手势一样

![Desktop Screenshot 2023 01 29 - 15 11 50 70](https://user-images.githubusercontent.com/118904918/215311919-f8d794df-f8b7-4692-8b95-feb8546ce79e.png)

2、完成一次手势操作后要恢复原样，不然会占用性能，导致卡顿
