dlib是一个C++写的库，支持Python引用，这里介绍如何安装和使用，作者使用开发环境Ubuntu16.04+Python2.7

# 1.安装重要依赖库

## 1.1. 安装dlib

### 方法一：Python package index

规规矩矩按照[Python package index](https://pypi.python.org/pypi/dlib) 中描述步骤安装
咳咳，这个方法按说是最‘正规’的，但是我就是没成功.......
有兴趣的同学可以尝试一下链接内的安装步骤。

### 方法二：Anaconda安装

使用 anaconda 包管理工具 conda(类似pip)
一行搞定 ``` conda install dlib==19.04```(最新版本是19.7.0)
但是存在一个问题是：我使用virtualenv建立了虚拟环境，其中并未安装Anaconda，所以dlib安装在系统的Anaconda内，虚拟环境内并未安装，等时间充裕会尝试一下

## 1.2.安装opencv

具体可参考作者的一篇博客《深度学习图像处理Ubuntu环境搭建》

# 2.应用阶段

## 2.1.人脸关键点提取

关键点提取需要一个特征提取器(predictor)，构建特征提取器可以训练模型。当然我们也可以使用官方提供的一个模型‘shape_predictor_68_face_landmarks.dat’，可以去官网也可以在我的网盘里下载: https://pan.baidu.com/s/1dF7z26H 密码: 54i9

如下提供一张dlib提取到的关键点参考图
![这里写图片描述](http://img.blog.csdn.net/20171012175144111?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZ2l0aHViXzM1OTY1MzUx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

下面可以看一张效果图，作者进行了灰度转换
![这里写图片描述](http://img.blog.csdn.net/20171114140147722?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZ2l0aHViXzM1OTY1MzUx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

待续。。。