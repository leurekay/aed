# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 15:03:43 2018

@author: zee
"""

def suggest(x1,x2,x3):
    sug_dic={0:'',
             1:'总体治疗效果不佳，面罩漏气大，检查面罩情况包含佩戴，大小，类型以及仪器设置',
             2:'治疗效果一般，检测仪器设置等',
             3:'总体治疗效果不佳，检测仪器设置等',
             4:'治疗效果良好但仍有少量暂停继续观察，坚持佩戴',
             5:'治疗效果非常好继续加油，坚持佩戴',
             6:'暂停治疗良好，仍有低氧，检查身体其他疾病情况',
             7:'低氧治疗良好，仍有暂停和漏气，检查面罩情况包含佩戴，大小，类型以及仪器设置，坚持佩戴',
             8:'暂停治疗良好，仍有低氧和漏气，检查面罩情况包含佩戴，大小，类型，检查身体其他疾病情况',
             9:'总体治疗效果非常好，仍有漏气。检查面罩情况包含佩戴，大小，类型，坚持佩戴'
            }
    

    if (x1>=30) and (x2>=5) and (x3<90):
        return sug_dic[1]
    if (x1<30) and (x2<15 and x2>=5) and (x3<90):
        return sug_dic[2]

    if (x1<30) and (x2>=15) and (x3<90):
        return sug_dic[3]    
    if (x1<30) and (x2<15 and x2>=5) and (x3>=90):
        return sug_dic[4]

    if (x1<30) and (x2<5) and (x3>=90):
        return sug_dic[5]
    
    if (x1<30) and (x2<5) and (x3<90):
        return sug_dic[6]
    if (x1>=30) and (x2>=5) and (x3>=90):
        return sug_dic[7]

    if (x1>=30) and (x2<5) and (x3<90):
        return sug_dic[8]
    if (x1>=30) and (x2<5) and (x3>=90):
        return sug_dic[9] 
    
    return sug_dic[0]
    