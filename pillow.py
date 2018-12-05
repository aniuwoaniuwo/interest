#-*-coding:utf-8-*-
from PIL import Image,ImageFilter
pic=Image.open('888.jpg')
print(pic)
print(pic.format,pic.size,pic.mode)#图像的格式，尺寸，图像的模式，rgb：3×8位像素，真彩
pic.show()
w,h=pic.size#获取尺寸
print(w,h)
pic.thumbnail((w/2,h/4))
pic.save('guitar1.jpg')
im2 = pic.filter(ImageFilter.BLUR)#模糊处理
im2.save('guitar2.jpg', 'jpeg')
#粘贴拷贝合并
box=(50,60,150,100)#前后分别是一个坐标
region=pic.crop(box)#拷贝的区域
region=region.transpose(Image.ROTATE_180)#转了180
pic.paste(region,box)#把旋转过的region粘贴回原来的位置
pic.save('paste.jpg')
#分离合并通道
r,g,b=pic.split()#分割通道
pic1=Image.merge('RGB',(g,b,r))
pic1.save('split.jpg')
pic1.show()
#几何变换,transpose和rotate都可以旋转变换
out=pic.resize((3120,3120))#重置大小
out.save('kkk.jpg')
out = out.rotate(45)#旋转45度
out.show()
out=pic.transpose(Image.FLIP_LEFT_RIGHT)#左右旋转
out.show()
out=pic.transpose(Image.FLIP_TOP_BOTTOM)#上下旋转
out.show()
#黑白变换
am = pic.convert('L')
am.show()
#滤镜
out = pic.filter(ImageFilter.DETAIL)#ImageFilter.BLUR是模糊处理
out.show()
#其他
fp = open("guitar.jpg", "rb")
im = Image.open(fp)
im.show()
out = im.point(lambda i : i *  2.3)#亮度增强
im.show()
out.save('hhh.jpg')
from PIL import ImageEnhance
enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("30% more contrast")
#enh.save('lll.jpg')
#生成其他格式图片
'''import os
for infile in sys.argv[1:]:#此函数第二个开始是运行该文件时加的参数，也就是我们可以加的图片路径
    f,e=os.path.split(infile)
    outfile=f+'.jpg'
    if infile != outfile:
        Image.open(infile).save(outfile)'''
