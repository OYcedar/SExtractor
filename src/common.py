import bisect
import re
from var_extract import *

ExVar = gExtractVar

#----------------------------------------------------------
globalDic = {}

def GetG(key):
	return globalDic[key]

def SetG(key, value):
	globalDic[key] = value

def printError(tip, *args):
    if not ExVar.printSetting[4]: return
    print(f'\033[31m{tip}\033[0m', end=' ')
    for arg in args:
        print(arg, end=' ')
    print('')

def printWarning(tip, *args):
    if not ExVar.printSetting[3]: return
    print(f'\033[33m{tip}\033[0m', end=' ')
    for arg in args:
        print(arg, end=' ')
    print('')

def printWarningGreen(tip, *args):
    if not ExVar.printSetting[2]: return
    print(f'\033[32m{tip}\033[0m', end=' ')
    for arg in args:
        print(arg, end=' ')
    print('')

def printInfo(tip, *args):
    if not ExVar.printSetting[1]: return
    print(tip, end=' ')
    for arg in args:
        print(arg, end=' ')
    print('')

def printDebug(tip, *args):
    if not ExVar.printSetting[0]: return
    print(tip, end=' ')
    for arg in args:
        print(arg, end=' ')
    print('')

#----------------------------------------------------------
#判断是否是日文
def isShiftJis(byte1, byte2):
    # 检查字节范围
    if (byte1 >= 0x81 and byte1 <= 0x9F) or (byte1 >= 0xE0 and byte1 <= 0xEF):
        if (byte2 >= 0x40 and byte2 <= 0x7E) or (byte2 >= 0x80 and byte2 <= 0xFC):
            return 2
    return 0

def checkJIS(bytes, reg):
    pos = 0
    end = len(bytes)
    while pos < end:
        #检查允许的单字节
        if reg != '' and re.match(reg, bytes[pos:pos+1]):
        #if chr(bytes[pos]) in '\r\n':
            pos += 1
            continue
        #检查双字节
        if end - pos < 2:
            return False
        offset = isShiftJis(bytes[pos], bytes[pos+1])
        if offset <= 0: 
            return False
        else:
            pos += offset
    return True

#查找第一个UTF-8
def findFirstUTF8(data, pos):
    length = 0
    #查询长度
    if (data[pos] & 0x80) == 0x00:
        length = 1
    elif (data[pos] & 0xE0) == 0xC0:
        length = 2
    elif (data[pos] & 0xF0) == 0xE0:
        length = 3
    elif(data[pos] & 0xF8) == 0xF0:
        length = 4
    else:
        return -1
    #检查后续字节是否合法
    for i in range(1, length):
        if (data[pos+i] & 0xC0) != 0x80:
            return -1
    return length

#----------------------------------------------------------
#编码生成目标长度的字节数组，会截断和填充字节
def generateBytes(text, lenOrig, NewEncodeName):
    transData = None
    try:
        transData = text.encode(NewEncodeName)
    except Exception as ex:
        print(ex)
        return None
    if ExVar.cutoff == False:
         return transData
    # 检查长度
    count = lenOrig - len(transData)
    #print('Diff', count)
    if count < 0:
        dic = ExVar.cutoffDic
        if text not in dic:
            if ExVar.cutoffCopy:
                 dic[text] = [text, count]
            else:
                dic[text] = ['', count]
        elif dic[text][0] != '':
            #从cutoff字典读取
            transData = dic[text][0].encode(NewEncodeName)
            count = lenOrig - len(transData)
            dic[text][1] = count #刷新长度
        if count < 0:
            print('\033[33m译文长度超出原文，部分截断\033[0m', text)
            transData = transData[0:lenOrig]
            try:
                transData.decode(NewEncodeName)
            except Exception as ex:
                #print('\033[31m截断后编码错误\033[0m')
                return None
    if count > 0:
        # 右边补足空格
        #print(transData)
        empty = bytearray(count)
        for i in range(int(count)):
            empty[i] = 0x20
        transData += empty
    return transData

#----------------------------------------------------------
def findInsertIndex(sortedList, target):
    position = bisect.bisect_left(sortedList, target)
    return position

def findNearestIndex(sortedList, target):
    position = bisect.bisect_left(sortedList, target)
    if position >= len(sortedList):
        position = len(sortedList) - 1
    elif position > 0:
        left = sortedList[position - 1]
        right = sortedList[position]
        if right - target >= target - left:
            position -= 1
    return position

def readInt(data, pos, byteNum=4):
    return int.from_bytes(data[pos:pos+byteNum], byteorder='little')

def int2bytes(i, l=4):
    return int.to_bytes(i, byteorder='little', length=l)

def xorBytes(input, xorTable):
    result = bytearray()
    xorLen = len(xorTable)
    for i, b in enumerate(input):
        xorByte = xorTable[i % xorLen]
        result.append(b ^ xorByte)
    return result

#----------------------------------------------------------
def getMatchItem(lst, target):
    for item in lst:
        if item['min'] <= target <= item['max']:
            return item
    return None