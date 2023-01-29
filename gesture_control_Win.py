#打包用pyinstaller test.py --add-data="E:\Anaconda\envs\gesture\Lib\site-packages\mediapipe\modules;\mediapipe\modules" -F -w
import cv2
import autopy
import numpy as np
import time
import mediapipe as mp
import math
class gesTure:
#初始化
    def __init__(self):
        self.mphands = mp.solutions.hands #mediapipe手部关键点检测的方法
        self.hands = self.mphands.Hands(min_detection_confidence=0.75,min_tracking_confidence=0.75)
        self.mpDraw = mp.solutions.drawing_utils #绘制手部关键点的连线的方法
        self.pointStyle = self.mpDraw.DrawingSpec(color=(255, 0, 255), thickness=4)  # 点的样式
        self.lineStyle = self.mpDraw.DrawingSpec(color=(0, 0, 255), thickness=4)  # 线的样式
#主函数
    def Control(self):
        cap = cv2.VideoCapture(0)
        self.plocx,self.plocy,self.smooth = 0,0,6  #上一帧时的鼠标所在位置,自定义平滑系数，让鼠标移动平缓一些
        self.resize_w,self.resize_h= 640,480 #原窗口大小
        self.pt1,self.pt2 = (50,50),(600,300) # 虚拟鼠标的移动范围，左上坐标pt1，右下坐标pt2
        self.wcam,self.hcam = autopy.screen.size() # 返回电脑屏幕的宽和高(1920.0, 1080.0)
        self.pTime = 0  # 设置第一帧开始处理的起始时间

        while cap.isOpened():
            red,self.img = cap.read()
            if red:
                self.img = cv2.flip(self.img, 1)  # 镜头翻转
                self.GesTure_control()

                cv2.rectangle(self.img,self.pt1,self.pt2,(138,12,92),3) #弄一个框
                self.Frame_Rate()

                cv2.imshow("img",self.img)
            if cv2.waitKey(1) == 27: #ESC退出
                break

#手势识别
    def GesTure_control(self):
        imgRGB = cv2.cvtColor(self.img,cv2.COLOR_BGR2RGB) #把BGR转换为RGB
        result = self.hands.process(imgRGB)
        if result.multi_hand_landmarks: #判断是否检测到手
            for self.handLms in result.multi_hand_landmarks: # 获得手的坐标，线，画出来
                self.mpDraw.draw_landmarks(self.img,self.handLms,self.mphands.HAND_CONNECTIONS, self.pointStyle, self.lineStyle) #把关键点连起来
                self.Count()

#计算关键点的距离(有_的是用来获取坐标的，没有_的是用来距离比较的)
    def Count(self):
        #0到食指关节
        p0x = self.handLms.landmark[0].x
        p0y = self.handLms.landmark[0].y
        p5x = self.handLms.landmark[5].x
        p5y = self.handLms.landmark[5].y
        distance_0_5 = pow(p0x - p5x, 2) + pow(p0y - p5y, 2)
        self.dis05 = pow(distance_0_5, 0.5) #0到5的距离

        #拇指坐标
        p4x = self.handLms.landmark[4].x
        p4y = self.handLms.landmark[4].y
        p4_x = math.ceil(p4x * self.resize_w)
        p4_y = math.ceil(p4y * self.resize_h)
        self.thumb = (p4_x,p4_y)
        distance_4_5 = pow(p4x - p5x, 2) + pow(p4y - p5y, 2)
        self.dis45 = pow(distance_4_5, 0.5) #拇指到5的距离

        #食指坐标
        p8x = self.handLms.landmark[8].x
        p8y = self.handLms.landmark[8].y
        self.p8_x = math.ceil(self.handLms.landmark[8].x * self.resize_w)
        self.p8_y = math.ceil(self.handLms.landmark[8].y * self.resize_h)
        self.index = (self.p8_x,self.p8_y)
        distance_0_8 = pow(p0x - p8x, 2) + pow(p0y - p8y, 2)
        self.dis08 = pow(distance_0_8, 0.5) #0到食指的距离

        #中指坐标
        p12x = self.handLms.landmark[12].x
        p12y = self.handLms.landmark[12].y
        self.p12_x = math.ceil(self.handLms.landmark[12].x * self.resize_w)
        self.p12_y = math.ceil(self.handLms.landmark[12].y * self.resize_h)
        self.middle = (self.p12_x,self.p12_y)
        distance_0_12 = pow(p0x-p12x,2) + pow(p0y-p12y,2)
        self.dis012 = pow(distance_0_12,0.5) #0到中指的距离
        distance_8_12 = pow(p8x - p12x,2) + pow(p8y - p12y,2)
        self.dis812 = pow(distance_8_12,0.5)

        #无名指坐标
        p16x = self.handLms.landmark[16].x
        p16y = self.handLms.landmark[16].y
        self.p16_x = math.ceil(self.handLms.landmark[16].x * self.resize_w)
        self.p16_y = math.ceil(self.handLms.landmark[16].y * self.resize_h)
        self.ring = (self.p16_x,self.p16_y)
        distance_0_16 = pow(p0x-p16x,2) + pow(p0y-p16y,2)
        self.dis016 = pow(distance_0_16,0.5) #无名指到0的距离

        #尾指的坐标
        p20x = self.handLms.landmark[20].x
        p20y = self.handLms.landmark[20].y
        self.p20_x = math.ceil(self.handLms.landmark[20].x * self.resize_w)
        self.p20_y = math.ceil(self.handLms.landmark[20].y * self.resize_h)
        self.caudal = (self.p20_x,self.p20_y)
        distance_0_20 = pow(p0x-p20x,2) + pow(p0y-p20y,2)
        self.dis020 = pow(distance_0_20,0.5) #尾指到0的位置
        distance_16_20 = pow(p16x-p20x,2) + pow(p16y-p20y,2)
        self.dis1620 = pow(distance_16_20,0.5) #16到20的距离
        print(self.dis1620)

        self.img = cv2.circle(self.img, self.index, 10, (255, 0, 0), cv2.FILLED) #食指的样式
        self.img = cv2.circle(self.img, self.thumb, 10 ,(255, 0, 0), cv2.FILLED) #拇指样式
        self.img = cv2.circle(self.img, self.middle, 10, (255, 0, 0), cv2.FILLED) #中指样式
        self.img = cv2.circle(self.img, self.ring, 10, (0, 255, 0), cv2.FILLED) #无名指的样式
        self.img = cv2.circle(self.img, self.caudal, 10, (0, 255, 0), cv2.FILLED) #尾指的样式
        self.EXEcute_judge()


#判断手势
    def EXEcute_judge(self):
        #把虚拟鼠标的移动范围映射到电脑屏幕上
        sx = np.interp(self.p8_x,(self.pt1[0],self.pt2[0]),(0,self.wcam))
        sy = np.interp(self.p8_y,(self.pt1[1],self.pt2[1]),(0,self.hcam))
        #平滑，使手指在移动鼠标时，鼠标箭头不会一直晃动  (cLocx = pLocx + (x3 - pLocx) / smooth)
        clocx = self.plocx + (sx - self.plocx) / self.smooth
        clocy = self.plocy + (sy - self.plocy) / self.smooth
        autopy.mouse.move(clocx, clocy)
        # 更新前一帧的鼠标所在位置坐标，将当前帧鼠标所在位置，变成下一帧的鼠标前一帧所在位置
        self.plocx,self.plocy = clocx,clocy

#手势指令
        #鼠标左键
        if self.dis45 < 0.02:
            autopy.mouse.click(autopy.mouse.Button.LEFT)
            time.sleep(0.2)

        # 下一页
        if self.dis012 < self.dis05 and self.dis08 < self.dis05 and self.dis812 < 0.05:
            autopy.key.toggle(autopy.key.Code.DOWN_ARROW, True)
            time.sleep(0.5)

        # 鼠标右键
        if self.dis012 < self.dis05 and self.dis08 > self.dis05*1.4 and self.dis812 > 0.07:
            autopy.mouse.click(autopy.mouse.Button.RIGHT)
            time.sleep(0.2)

        #上一页
        if self.dis016 > self.dis05 and self.dis020 > self.dis05 and self.dis1620 < 0.1:
            autopy.key.toggle(autopy.key.Code.UP_ARROW, True)
            time.sleep(0.5)
#显示FPS
    def Frame_Rate(self):
        self.cTime = time.time()  # 处理完一帧图像的时间
        self.fps = 1 / (self.cTime - self.pTime)
        self.pTime = self.cTime #重置起始时间
        cv2.putText(self.img,str(int(self.fps)),(70,40),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)


x = gesTure()
x.Control()