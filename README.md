---
title: 编码/解码工具 @huayang V1.0
author: huayang
time: 2021.4.10-2021.4.17
tags: 解码/编码,加密
category: 原创工具
---



# 项目介绍

避免有些库大家没有安装建议大家下载编译好的文件！

归纳了常用的编码格式，无论是CTF还是渗透测试应该都能在此工具找到相应的格式

一共两个版本分别是windows及macOS版本，已经分别编译好了点击右方的Releases选择版本下载即可直接食用

## 项目截图
<center>Windows</center>
![Endecode-win](https://hellohy.top/imgs/Endecode-win.png)
<center>macOS</center>
![Endecode-mac](https://hellohy.top/imgs/Endecode-mac.png)

## 初衷

很早之前就有要写此工具的想法了苦于GUI实在麻烦且丑就搁置下来了，最近因为毕设方面的问题重新开始写此工具

还有个原因是没找到很符合我常用的编码解码工具，特别是hex和ascii中的一些编/解码。

如有更好的工具欢迎推荐。

## 展望

未来主要是对其进行美化或是换框架，采用面向对象进行编程以方便同学们更直观的在此项目上添加新功能

MD5解密也应该会加的毕竟传统艺能（爬虫）不能忘

不会扩展密码学方面的东西

## 实现功能

+ base编码/解码

	+ 字符串 <<=============>> base64
	
	+ 字符串 <<=============>> base32
	
	+ 字符串 <<=============>> base16

+ MD5加密

	+ 字符串  =============>> MD5
	
+ 进制转换
	
	+ 二进制<=============>>八进制
	
	+ 二进制<=============>>十进制
	
	+ 二进制<=============>>十六进制
	
	+ 八进制<=============>>十进制
	
	+ 八进制<=============>>十六进制
	
	+ 十进制<=============>>十六进制

+ URL编码
	+ 字符串 <<=============>> URL编码

+ JSON格式化

	+ 数组   ==============>> JSON字符串

+ hex编码

	+ 字符串 <<=============>> hex编码（基本型）
	
	+ 字符串 <<=============>> hex编码（0x型）
	
	+ 字符串 <<=============>> hex编码（%型）
	
	+ 字符串 <<=============>> hex编码（\x型）
	
+ 特殊的ascii

	+ 字符串 <<=============>> ascii（八进制）
	
	+ 字符串 <<=============>> ascii（unicode中文）
	
	+ 字符串 <<=============>> ascii（unicode英文数字）

+ 骚操作

	+ 归纳的一些常用加密/解密及骚操作网站


## 其他

师傅们还有什么需要添加的编码或是建议记得在Github或是博客给我里留言哦

师傅们看我这么用心个Star✩不过分吧*ଘ(੭*ˊᵕˋ)੭* ੈ✩‧₊˚

本工具未来还会持续更新美化的，比如外观，功能，面向对象手法上

这只是我毕业设计项目的一个分类，未来还会有更多工具项目，请大家多多关照

[浅浅淡淡](https://hellohy.top/)
