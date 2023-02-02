#_*_ coding:utf-8 _*_
import pyttsx3
import time

print('enter reader file line5')
#engine = pyttsx3.init()
#engine.iterate()

#engine.iterate()
#print('enter reader file line7,engine:', type(engine))
dictData = {'engine':None, 'readingTimes':1, 'rate':15, 'interval':5, 'fileInst':None}
dictData['flagPlay'] = True
dictData['engine'] = pyttsx3.init()

def config(times, rate, interval):
    #rate = engine.getProperty('rate')  # rate default 200
    dictData['readingTimes'] = times
    dictData['rate'] = rate
    dictData['interval'] = interval

    #print('reader file times:', dictData['readingTimes'], 'interval:', dictData['interval'])
    if dictData['engine'] is not None:
        # 设定语速
        dictData['engine'].setProperty('rate', 50+dictData['interval']*10)

def play(fileName):
    # if dictData['engine'] is None:
    #     print("dictData['engine'] is None, init engine")
        #dictData['engine'] = pyttsx3.init()
    # rate = dictData['engine'].getProperty('rate')
    # print('rate', rate)
    # 设定语速
    dictData['engine'].setProperty('rate', 50 + dictData['rate'] * 10)
    # print("dictData['rate']", dictData['rate'])
    # rate = dictData['engine'].getProperty('rate')
    # print('rate', rate)

    #with open(fileName,'r',encoding='gbk') as dictData['fileInst']:
    dictData['fileInst'] = open(fileName,'r',encoding='gbk')
    print("enter func play,line22 dictData['engine']", dictData['engine'])
    dictData['flagPlay'] = True

    if dictData['flagPlay'] == True:
        print("dictData['flagPlay'] == True")
    while dictData['engine'] is not None and dictData['flagPlay'] == True:
        line = dictData['fileInst'].readline()
        if line == '\n':
            dictData['fileInst'].close()
            return
        print('文本内容:',line)
        for i in range(dictData['readingTimes']):
            if dictData['engine'] is not None and dictData['flagPlay'] == True:
                # print('i:', i, 'readingTimes:', dictData['readingTimes'])
                # print('say(line)')
                dictData['engine'].say(line)
                dictData['engine'].runAndWait()
                'runAndWait()'
                if dictData['readingTimes'] == 1:
                    pass
                else:
                    time.sleep(dictData['interval'])
                    #print('interval:', dictData['interval'])

def stop():
    if dictData['engine'] is not None:
        dictData['flagPlay'] = False
        #dictData['engine'] = None
        #dictData['engine'].stop()
        if dictData['fileInst']:
            dictData['fileInst'].close()


if __name__ == '__main__':
    pass

# words=['毁灭','不可估量','举世闻名','众星拱月','金碧辉煌','殿堂','象征','依照','诗情画意'
#        ,'建筑','漫游','天南海北','饱览','风景名胜','境界','宏伟','奇珍异宝','博物馆','统统','搬运','销毁','罪证','奉命']
# words=['China','talk','May','June','January','February','March','April','July','August','September','October'
#        ,'November','December','email','hat','wear','yours','every year']
# words=['满江红·写怀。\
# 宋·岳飞。\
# 怒发冲冠，凭栏处、潇潇雨歇。抬望眼、仰天长啸，壮怀激烈。三十功名尘与土，八千里路云和月。莫等闲、白了少年头，空悲切。\
# 靖康耻，犹未雪。臣子恨，何时灭。驾长车，踏破贺兰山缺。壮志饥餐胡虏肉，笑谈渴饮匈奴血。待从头、收拾旧山河，朝天阙。']
# engine = pyttsx3.init()
# #设定语速
# rate = engine.getProperty('rate')#rate default 200
# print(rate)
# engine.setProperty('rate',rate-50)
# #设定男声女声
# # voices = engine.getProperty('voices')
# # print(voices,type(voices),len(voices))
# # print(voices[0])
# # print(voices[1])
# #engine.setProperty('voice',voices[1].id)
# print(len(words))
# for i in range(len(words)):
#     print(i,words[i])
#     for j in range(3):
#         engine.say(words[i])
#         engine.runAndWait()
#         time.sleep(1)

