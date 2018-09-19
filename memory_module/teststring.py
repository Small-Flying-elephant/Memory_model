import os
import json
import random

import xlrd
import xlwt

gConfigTableApkPath = []
gConfigTableCaseArray = []
gConfigTableRunninginterval = []
gCurrentCursor = {}  # group groupData


class groupData:
    def __init__(self, begin, end):
        self.java_begin = begin
        self.java_end = end

    java_begin = 0
    java_end = 0


def readConfigContent(processName):
    adbCommand = 'adb -s ' + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName
        print adbCommand

    configTable = os.getcwd()
    tableName = configTable + '/config.json'

    success = False
    if os.path.exists(tableName) == True:
        with open(tableName) as f:
            jsonContent = json.load(f)

            # try:
            for apk in jsonContent[u'apkPath']:
                gConfigTableApkPath.append(apk)
            # print gConfigTableApkPath
            caseArray = jsonContent[u'caseArray']
            for case in caseArray:
                print case.get(u'process_name', '')
                # print case[u'model'], case[u'loopCount'], case[u'process_name']
                gConfigTableCaseArray.append((case[u'model'], case[u'loopCount'], case.get(u'process_name', '')))
            gConfigTableRunninginterval.append(jsonContent[u'Runninginterval'])
            print gConfigTableCaseArray
            success = True
            # except Exception as e:
            #   print e

    return success


from xlrd import open_workbook
from xlutils.copy import copy


def getExcelName(devicesid, index):
    ''' '/instructions/' + '''
    fileName = os.getcwd() + '/launcher_' + str(index) + '_' + devicesid + '.xls'
    return fileName


def writeHeader(sheetPtr, group, version):
    sheetPtr.write_merge(0, 0, group * 2 + 1, group * 2 + 2, version)
    sheetPtr.write(1, (group * 2) + 1, u'Javapss_begin')
    sheetPtr.write(1, (group * 2) + 2, u'Javapss_end')
    pass


def createExcel(apkList, devicesid,index):
    filename = getExcelName(devicesid, index)
    version = []
    for apk in apkList:
        version.append(getVerFromPackageName(apk))
    # print 'version', version

    file = xlwt.Workbook()
    sheetPtr = file.add_sheet("Sheet")
    group = 0
    for ver in version:
        writeHeader(sheetPtr, group, ver)
        group += 1
    file.save(filename)


def getVerFromPackageName(packageName):
    if packageName == '':
        return ''

    version = packageName.strip().split('_')
    ver = version[1].strip().split('.')
    return ver[0]


def WriteExcel1(apkName, caseName, group):
    if gCurrentCursor.has_key(group) == False:
        gCurrentCursor[group] = groupData(1, 2)

    object = gCurrentCursor.get(group)


def initExcel(apkList, devicesid, index):
    excelFile = getExcelName(devicesid, index)
    if os.path.exists(excelFile) == False:
        createExcel(apkList, devicesid,index)
    return excelFile


def WriteExcel(excelFile, x, y, javapss_begin, javapss_end):
    print x, '_', y
    excelOld = xlrd.open_workbook(excelFile)
    excelPtr = copy(excelOld)
    sheetPtr = excelPtr.get_sheet(0)
    sheetPtr.write(x, y, javapss_begin)
    sheetPtr.write(x, y + 1, javapss_end)
    excelPtr.save(excelFile)
    pass


if __name__ == '__main__':
    # readConfigContent('a')
    # getExcel()
    # createExcel()
    # WriteExcel('launcher_203123.apk', 'case1', 'qowerlkjladf',0)
    # # WriteExcel('launcher_203123.apk', 'case1', 'qowerlkjladf',0)
    # # WriteExcel('launcher_203123.apk', 'case1', 'qowerlkjladf',0)
    # # WriteExcel('launcher_203123.apk', 'case1', 'qowerlkjladf',1)
    # # WriteExcel('launcher_203123.apk', 'case1', 'qowerlkjladf',1)
    # WriteExcel('launcher_203123.apk', 'case1', 'qowerlkjladf',1)
    # WriteExcel('launcher_203123.apk', 'case1', 'qowerlkjladf',2)
    gCurrentCursor.setdefault(0, []).append(groupData(1, 2))
    gCurrentCursor.setdefault(0, []).append(groupData(1, 2))
    gCurrentCursor.setdefault(0, []).append(groupData(2, 2))
    gCurrentCursor.setdefault(0, []).append(groupData(3, 2))
    gCurrentCursor.setdefault(0, []).append(groupData(4, 2))
    gCurrentCursor.setdefault(0, []).append(groupData(5, 2))

    gCurrentCursor.setdefault(1, []).append(groupData(1, 2))
    gCurrentCursor.setdefault(1, []).append(groupData(1, 2))
    gCurrentCursor.setdefault(1, []).append(groupData(2, 2))
    gCurrentCursor.setdefault(1, []).append(groupData(3, 2))
    gCurrentCursor.setdefault(1, []).append(groupData(4, 2))
    gCurrentCursor.setdefault(1, []).append(groupData(5, 2))
    excelFile = initExcel(['launcher_203123.apk', 'launcher_203123.apk',
                           'launcher_203125.apk'], 'devicesid',3)
    list = gCurrentCursor.get(0, [])
    group = 0
    rows = 2

    keyList = gCurrentCursor.keys()
    for keyValue in keyList:
        rows = 2
        for item in gCurrentCursor.get(keyValue, []):
            print item
            WriteExcel(excelFile, rows, group * 2 + 1, item.java_begin, item.java_end)
            rows += 1
        group += 1
        # WriteExcel1('launcher_203123.apk', 'qowerlkjladf',2)
