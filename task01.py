# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 23:18:56 2020

@author: celia
"""


import numpy as np
#常数
print(np.nan==np.nan)
print(np.nan!=np.nan)#空值
print(np.inf)#无穷大
print(np.pi)#圆周率
print(np.e)#自然常数

#np的数值类型是dtype对象的实列，每个内建类型都有一个唯一定义它的字符代码
a=np.dtype('i2')
print(a.type)
print(a.itemsize)
#时间日期和时间增量
a1=np.datetime64('2020-03-08 20:20:04','s')#必须加零补全
# 从字符串创建 datetime64 类型时，可以强制指定使用的单位。
print(a1,a1.dtype)
#字符串创建 datetime64 数组时，如果单位不统一，则一律转化成其中最小的单位。
a2=np.array(['2020-04','2020-05-03','2020-04-05 03:22:03'],dtype='datetime64')
print(a2,a2.dtype)
# 使用arange()创建 datetime64 数组，用于生成日期范围。
a=np.arange('2020-02','2020-09',dtype=np.datetime64)
print(a)

#timedelta64 表示两个 datetime64 之间的差。timedelta64 也是带单位的，
#并且和相减运算中的两个 datetime64 中的较小的单位保持一致。


