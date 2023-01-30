#_*_ coding:utf-8 _*_
import pyttsx3
import time
import numpy as np

print('enter reader file line5')
#engine = pyttsx3.init()

#engine.iterate()
#print('enter reader file line7,engine:', type(engine))
dictData = {'engine':None, 'readingTimes':1, 'rate':15, 'interval':5}
#readingTimes = np.array([0]*2)
#print('readingTimes len:', len(readingTimes))
def config(times, rate, interval):
    # 设定语速
    #rate = engine.getProperty('rate')  # rate default 200
    dictData['readingTimes'] = times
    dictData['rate'] = rate
    dictData['interval'] = interval

    print('reader file times:', dictData['readingTimes'], 'reader file rate:', dictData['rate'])
    if dictData['engine'] is not None:
        dictData['engine'].setProperty('rate', 50+rate*10)

def play(fileName):
    print('enter func play')
    dictData['engine'] = pyttsx3.init()
    with open(fileName,'r',encoding='gbk') as f:
        print('enter func play,line22')
        #eng_init()
        line = f.readline()
        while line and dictData['engine'] is not None:
            print(line)
            for i in range(dictData['readingTimes']):
                if dictData['engine'] is not None:
                    #print('i:', i, 'readingTimes[0]:', dictData['readingTimes'])
                    dictData['engine'].say(line)
                    dictData['engine'].runAndWait()
                    if dictData['readingTimes'] == 1:
                        pass
                    else:
                        time.sleep(dictData['interval'])
                        #print('interval:', dictData['interval'])
            line = f.readline()

def stop():
    if dictData['engine'] is not None:
        dictData['engine'].stop()
        dictData['engine'] = None

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

