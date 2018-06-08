#coding=utf-8
import re
yuanwenjian=r'C:\Users\michiko\Downloads\FDD站点清单LOG\FDD站点清单LOG\汇总.txt'
log='E:\GTPU-resoult.txt'
zhandian='E:\GTPU-jizhan.txt'
with open(yuanwenjian) as  f1:#打开'weibo_train_data.txt'文件
    f11 = f1.read()
    for m in range(len(f11)):
        if f11[m+1:m+15]=='静态检测开关  =  去使能':
            print(f11[m-450:m+15])
