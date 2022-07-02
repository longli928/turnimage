from PIL import Image
from PIL import Image
import os
def countFlieNum():
    for dirpatch,dirnames,filename in os.walk(dirName):
      file_counts = len(filename)
      print("图片总数为", file_counts)
    return file_counts
def imageTurn():
    i=0
    angle = int(input("请输入需要旋转的角度,-顺+逆\n"))
    for filename in os.listdir(dirName):
        img = Image.open(filename)
        img = img.rotate(angle, expand=True)
        img.save(os.path.join(dirName, filename))
        i=i+1
        print(filename,"已写入，剩余",file_count-i)
if __name__ == '__main__':
    dirName=str(input("请输入图片所在路径：\n"))
    os.chdir(dirName)
    file_count = countFlieNum()
    imageTurn()
    print("已全部完成")
