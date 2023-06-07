import cv2
import os

mainFolder='Images'
myFolders=os.listdir(mainFolder)
#载入图像根文件
# print(myFolders)

for folder in myFolders:
    path=mainFolder+'/'+folder
    #载入图像子目录
    images=[]#用于存放cv读取的图片
    myList=os.listdir(path)
    print(len(myList))
    for imgN in myList:
        curImg=cv2.imread(path+'/'+imgN)
        curImg=cv2.resize(curImg,(0,0),None,0.2,0.2)#缩小图片尺寸以便展示
        images.append(curImg)

    stitcher=cv2.Stitcher.create()#获取cv2提供的拼接类对象
    (status,result)=stitcher.stitch(images)#调用拼接函数
    if(status==cv2.STITCHER_OK):
        print('Panorama Generator')#判断是否能拼接为全景图
        cv2.imshow(folder,result)#打印图片
        cv2.waitKey(1)
    else:print('Panorama Generator Unsuccessful')
cv2.waitKey(0)