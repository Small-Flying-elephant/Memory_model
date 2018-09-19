#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: linsheng
# time:2017.6.28

import json
import os
import os.path
from uiautomator import Device
import time
import xlrd
import xlwt
from echarts import Axis
from echarts import Echart, Bar
from echarts import Legend
from xlutils.copy import copy
from launcher_ui import UiAuto


cmd_install_num = 'adb -s '
cmd_install_in = ' install '
cmd_install_dev = ' install -r '
cmd_uninstall = ' uninstall '
rmfile = 'rm '
mkfile = 'echo nul >'
chmodfile = 'chmod 777 '
package_name = "com.ksmobile.launcher"
splashpath = os.getcwd()
casepath = os.getcwd()
adb_s = 'adb -s '
install_s = ' install '
uninstall_s = ' uninstall '
launcher = ' com.ksmobile.launcher '
start_launcher = ' shell am start com.ksmobile.launcher/.Launcher '
stop_launcher = ' shell am force-stop com.ksmobile.launcher '
back_back = ' shell input keyevent 4'
home_home = ' shell input keyevent 3'
adb_clear = ' shell pm clear com.ksmobile.launcher '
launcher = ' com.ksmobile.launcher '
start_launcher = ' shell am start com.ksmobile.launcher/.Launcher '
stop_launcher = ' shell am force-stop com.ksmobile.launcher '
cm_setting = ' shell am start -n com.ksmobile.launcher/com.ksmobile.launcher.switchpanel.SwitchPanelActivity'
setting_home = ' Util.splash_home_app '
ps_pid1 = '  shell  ps  |grep "com.ksmobile.launcher"'
ps_pid = '  shell  ps  |findstr "com.ksmobile.launcher"'

def start_setting(devicesid):
    command = adb_s + devicesid + cm_setting
    os.system(command)



def back_backs(devicesid):
    os.popen(adb_s + devicesid + back_back)




    
def set_theme(devicesid,themeActivity):
    ui = UiAuto(devicesid)
    start_theme = 'adb -s ' + devicesid + ' shell am start ' + themeActivity
    print start_theme
    os.popen(start_theme).read()
    time.sleep(10)
    ui.click_theme()
    time.sleep(10)
    ui.home()
    ui.back()


def change_themes(devicesid):
    themeActivitys = ['edge.phone.s7/com.ksmobile.launcher.theme.ThemeActivity','neat.galaxy.thema.system/com.ksmobile.launcher.theme.ThemeActivity','golden.galaxy.theme/com.ksmobile.launcher.theme.ThemeActivity']
    for activityTheme in themeActivitys:
        set_theme(devicesid,activityTheme)
        time.sleep(15)

def begin_run(devicesid, case_case_info,d):
    print 'script end ' + devicesid
    try:
        with open(casepath + '/case_all/' + str(case_case_info) + '.txt') as caseread:
            caseitem = caseread.readlines()
    except Exception:
        print  'case corresponds to the resolution of the case does not exist'
        return

    for i in caseitem:
        print i
        if i[0] == '#':
            continue
        if 'leftslide' in i:
            rightitem = i.strip().split('(')
            number = rightitem[1].strip().split(')')

            itemnumber = number[0].split(',')

            os.popen(adb_s + devicesid + ' shell  input swipe  "%s"  "%s"  "%s"  "%s" ' % (
                int(itemnumber[0]),
                int(itemnumber[1]),
                int(itemnumber[2]),
                int(itemnumber[3])))

            time.sleep(int(itemnumber[4]))

        elif 'rightslide' in i:
            rightitem = i.strip().split('(')
            number = rightitem[1].strip().split(')')

            itemnumber = number[0].split(',')

            os.popen(adb_s + devicesid + ' shell  input swipe  "%s"  "%s"  "%s"  "%s" ' % (
                int(itemnumber[0]),
                int(itemnumber[1]),
                int(itemnumber[2]),
                int(itemnumber[3])))
            time.sleep(int(itemnumber[4]))

        elif 'change_theme' in i:
            change_themes(devicesid)


        elif 'themes_wallpapers' in i:

            rightitem = i.strip().split('(')

            number = rightitem[1].strip().split(')')

            itemnumber = number[0].split(',')

            if d(text='SET WALLPAPER').exists:

                print 'No advertising'

            else:

                d.press.back()

            time.sleep(int(itemnumber[0]))


        elif 'daily_wappaper' in i:

            rightitem = i.strip().split('(')

            number = rightitem[1].strip().split(')')

            itemnumber = number[0].split(',')

            if d(resourceId="com.ksmobile.launcher:id/btn_daily_wallpaper").exists:

                d(resourceId="com.ksmobile.launcher:id/btn_daily_wallpaper").click()


            else:

                print "old version"

            time.sleep(int(itemnumber[0]))


        elif 'wallpaper_free_download' in i:

            rightitem = i.strip().split('(')

            number = rightitem[1].strip().split(')')

            itemnumber = number[0].split(',')

            if d(text="Wallpapers").exists:

                print 'No advertising Wallpaper HD'

            else:

                if d(resourceId="com.ksmobile.launcher:id/cancel").exists:

                    d(resourceId="com.ksmobile.launcher:id/cancel").click()

                elif d(resourceId="com.ksmobile.launcher:id/au1").exists:

                    d(resourceId="com.ksmobile.launcher:id/au1").click()

            time.sleep(int(itemnumber[0]))

        elif 'click' in i:
            rightitem = i.strip().split('(')

            number = rightitem[1].strip().split(')')

            itemnumber = number[0].split(',')

            os.popen(adb_s + devicesid + ' shell  input tap  "%s"  "%s"  ' % (
                int(itemnumber[0]),
                int(itemnumber[1])))
            time.sleep(int(itemnumber[2]))

        elif 'upslide' in i:

            rightitem = i.strip().split('(')

            number = rightitem[1].strip().split(')')

            itemnumber = number[0].split(',')
            os.popen(adb_s + devicesid + ' shell  input swipe  "%s"  "%s"  "%s"  "%s" ' % (
                int(itemnumber[0]),
                int(itemnumber[1]),
                int(itemnumber[2]),
                int(itemnumber[3])))
            time.sleep(int(itemnumber[4]))

        elif 'downslide' in i:
            rightitem = i.strip().split('(')

            number = rightitem[1].strip().split(')')

            itemnumber = number[0].split(',')
            os.popen(adb_s + devicesid + ' shell  input swipe  "%s"  "%s"  "%s"  "%s" ' % (
                int(itemnumber[0]),
                int(itemnumber[1]),
                int(itemnumber[2]),
                int(itemnumber[3])))
            time.sleep(int(itemnumber[4]))


        elif 'back' in i:
            os.popen(adb_s + devicesid + ' shell input keyevent 4')
            rightitem = i.strip().split('(')

            number = rightitem[1].strip().split(')')

            itemnumber = number[0].split(',')
            time.sleep(int(itemnumber[0]))
        elif 'home' in i:
            os.popen(adb_s + devicesid + ' shell input keyevent 3')
            rightitem = i.strip().split('(')

            number = rightitem[1].strip().split(')')

            itemnumber = number[0].split(',')
            time.sleep(int(itemnumber[0]))

        elif 'bright_screen' in i:
            os.popen(adb_s + devicesid + ' shell input keyevent 26')
            rightitem = i.strip().split('(')

            number = rightitem[1].strip().split(')')

            itemnumber = number[0].split(',')
            time.sleep(int(itemnumber[0]))

        elif 'long_swipe' in i:
            rightitem = i.strip().split('(')

            number = rightitem[1].strip().split(')')

            itemnumber = number[0].split(',')
            os.popen(adb_s + devicesid + ' shell  input touchscreen  swipe  "%s"  "%s"  "%s"  "%s" "%s"' % (
                int(itemnumber[0]),
                int(itemnumber[1]),
                int(itemnumber[2]),
                int(itemnumber[3]),
                int(itemnumber[4]) * 1000))
            time.sleep(int(itemnumber[5]))

        elif 'sleep' in i:
            rightitem = i.strip().split('(')
            number = rightitem[1].strip().split(')')
            itemnumber = number[0].split(',')
            time.sleep(itemnumber)

        elif 'change_theme' in i:
            change_themes(devicesid)

        elif 'themes_wallpapers' in i:

            rightitem = i.strip().split('(')

            number = rightitem[1].strip().split(')')

            itemnumber = number[0].split(',')

            ui = UiAuto(devicesid)
            ui.skip_ad_wallpaper()

            time.sleep(int(itemnumber[0]))


        elif 'daily_wappaper' in i:

            rightitem = i.strip().split('(')

            number = rightitem[1].strip().split(')')

            itemnumber = number[0].split(',')

            ui = UiAuto(devicesid)
            ui.daily_wallpaper()

            time.sleep(int(itemnumber[0]))


        elif 'wallpaper_free_download' in i:

            rightitem = i.strip().split('(')

            number = rightitem[1].strip().split(')')

            itemnumber = number[0].split(',')

            ui = UiAuto(devicesid)
            ui.skip_HD()

            time.sleep(int(itemnumber[0]))

        elif "openlock" in i:
            ui = UiAuto(devicesid)
            ui.open_locker()
            ui.screen_off()
            ui.screen_on()
            ui.back()
            ui.skip_set_password()

        elif 'set_wallpaper' in i:
            rightitem = i.strip().split('(')
            number = rightitem[1].strip().split(')')
            itemnumber = number[0].split(',')

            ui = UiAuto(devicesid)
            ui.set_wallpaper()

            time.sleep(int(itemnumber[0]))

    print 'script end ' + devicesid

# 检验是否存在是否连接有效设备，并获取到设备的ip，打开tcpip端口
def devicesConnectInfo():
    devicesId = []

    connResult = os.popen('adb devices').readlines()

    connDevicesInfo = connResult[1:len(connResult) - 1]

    connDevicesNum = len(connDevicesInfo)

    if connDevicesNum > 0:
        for i in range(connDevicesNum):
            address = connDevicesInfo[i].split('\t')[0]

            if address.find('.') < 0:
                devicesId.append(address)

    return devicesId

def getVerFromPackageName(packageName):
    if packageName == '':
        return ''

    version = packageName.strip().split('_')
    version = version[1].split('.apk')
    print 'current version=',str(version[0])
    return version[0]

def getDalvikMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Dalvik Heap' in infoitem:
            infoiteminfod = infoitem.split('   ')
            print infoiteminfod
            if len(infoiteminfod) > 4:
                for i in range(5):
                    if infoiteminfod[infoiteminfod.index('  Dalvik Heap') + i + 1] == '':
                        print 'null'
                    else:
                        break;
                print infoitem
                print int(infoiteminfod[infoiteminfod.index('  Dalvik Heap') + i + 1].strip())
                return int(infoiteminfod[infoiteminfod.index('  Dalvik Heap') + i + 1].strip())
            return 0
    return 0

def getDalvikMemoryInfo_18(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Dalvik' in infoitem:
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 5:
                return int(infoiteminfod[3].strip())

    return 0
            
def get_process_PID(devicesID,pid_map):
    print adb_s  + devicesID + ps_pid
    pidinfo = os.popen(adb_s  + devicesID + ps_pid).readlines()
    #print '-------->',pidinfo
    if len(pidinfo) == 0:
        #print "zou xin de "
        pidinfo = os.popen(adb_s  + devicesID + ps_pid1).readlines()
    for pidinfoitem in pidinfo:
        if 'com.ksmobile.launcher' in pidinfoitem :
            print pidinfoitem
            piditem=pidinfoitem.split(' ')
            for i in xrange(10):
                if piditem[i+1] != '':
                    #print piditem[i+1]
                    x = i+1
                    break
            pid_map.append(piditem[x])

def runGC(devicesID,phonestat):

    pid_map=[]

    get_process_PID(devicesID,pid_map)

    for  nbs in range(len(pid_map)):

        for i in range(4):
            #os.popen(adb_s+ devicesID + '  shell am dumpheap '+ pid_map[nbs] +' /data/local/tmp/test.hprof ')
            if 'su' in phonestat:
                #os.popen(adb_s + devicesID + '  shell dumpsys meminfo  ' + pid_map[nbs])
                print adb_s + devicesID + ' shell  "su -c \'kill -10  %s\'"'%(pid_map[nbs])
                os.popen(adb_s + devicesID + ' shell  "su -c \'kill -10  %s\'"'%(pid_map[nbs]))
                time.sleep(5)
            else:
                os.popen(adb_s + devicesID + '  shell dumpsys meminfo  ' + pid_map[nbs])

def uninstall(devicesID, package_name):
    print 'begin uninstall apk'
    command = cmd_install_num + devicesID + cmd_uninstall + package_name

    os.system(command)

    #time.sleep(5)
    print 'uninstall complete'

def install(devicesID, appmapnamepath):
    commands = cmd_install_num + devicesID + cmd_install_in + '"%s"' % str(appmapnamepath)
    reads = os.popen(commands).read()

def clear(devicesID):
    os.popen(adb_s + devicesID + ' shell pm clear com.ksmobile.launcher')

def getDeviceuid(ip):
    # uidinfo = os.popen('adb -s ' + ip +':5555  shell ps |grep com.ksmobile.launcher' ).readlines()
    uidinfo = os.popen(adb_s + ip + '  shell ps |grep com.ksmobile.launcher').readlines()
    # print uidinfo
    uidinfo = uidinfo[0].split('   ')[0]
    # print uidinfo
    uidinfo = uidinfo.split('_')
    uidinfo = uidinfo[0] + uidinfo[1]
    return uidinfo

def getBatterInfo(devicesID):
    # 获取手机的电量百分比

    batteryinfo = os.popen(adb_s + devicesID + ' shell  dumpsys battery').readlines()

    batteryArray = []
    for ii in range(len(batteryinfo) - 1):
        if 'level:' in batteryinfo[ii]:
            batteryinfos = batteryinfo[ii].split('  level: ')
            batteryArray.append(int(batteryinfos[1].strip()))
            break
    if len(batteryArray) <= 0:
        batteryArray.append(0)

    batterydetailedinfo = os.popen(
        adb_s + devicesID + ' shell  dumpsys batterystats  com.ksmobile.launcher').readlines()

    isAdded = False
    for i in range(len(batterydetailedinfo) - 1):
        if 'Capacity:' in batterydetailedinfo[i]:
            batinfo = batterydetailedinfo[i].split(',')
            batteryCapacity = batinfo[0].split('    Capacity: ')
            batteryComputed_drain = batinfo[1].split(' Computed drain: ')
            batteryArray.append(int(batteryCapacity[1].strip()))
            batteryArray.append(float(batteryComputed_drain[1].strip()))
            isAdded = True
            break

    if isAdded == False:
        batteryArray.append(0)
        batteryArray.append(0)
    return batteryArray

def map_drawing(dalvik_size_run_last, dalvik_size_run_first, savePath, saveFileName):
    print 'start drawing'
    xtick = []
    for i in range(len(dalvik_size_run_last)):
        xtick.append(i + 1)
    chart = Echart('memory', '红色:运行模块操作后。   深蓝色：执行模块操作前')
    chart.use(Bar('China', dalvik_size_run_last))
    chart.use(Bar('China1', dalvik_size_run_first))
    chart.use(Legend(['GDP']))
    chart.use(Axis('category', 'bottom', data=xtick))
    # chart.plot()

    chart.save(savePath, saveFileName)

def judge_resolution(devicesID):
    print 'start phone resolution'
    resolution = os.popen(adb_s + devicesID + ' shell wm size').readlines()
    for i in range(len(resolution)):
        if 'Physical' in resolution[i]:
            physical = resolution[i].split(':')
            fbl = physical[1].strip()
            return fbl

def startActivity(devicesID):
    start_activity = os.popen(adb_s + devicesID + ' shell am start com.ksmobile.launcher/.Launcher').readlines()
    return start_activity

def del_splash(devicesID):
    print 'Skip the splash page'
    try:
        for i in range(2):
            os.popen(adb_s + devicesID + ' shell am force-stop com.ksmobile.launcher')
            time.sleep(3)
            os.popen(adb_s + devicesID + ' shell am start com.ksmobile.launcher/.Launcher')
            time.sleep(30)
        for i in range(5):
            os.popen(adb_s + devicesID + ' shell input keyevent 4')
            time.sleep(1)
        print 'Skip the splash page complete '
    except Exception:
        print 'Skip the splash page error'

rootdir = './apk/'
def statistics_install():
    # 获取到apk
    for parent, dirnames, filenames in os.walk(rootdir):
        for files in filenames:
            if files.endswith('.apk'):
                return files

def readConfigContent(gConfigTableApkPath, gConfigTableCaseArray, gConfigTableRunninginterval):
    configTable = os.getcwd()
    tableName = configTable + '/config.json'

    success = False
    if os.path.exists(tableName) == True:
        with open(tableName) as f:
            jsonContent = json.load(f)

        try:
            for apk in jsonContent[u'apkPath']:
                gConfigTableApkPath.append(apk)
            caseArray = jsonContent[u'caseArray']
            for case in caseArray:
                gConfigTableCaseArray.append((case[u'model'], case[u'loopCount'], case.get(u'process_name', '')))
            gConfigTableRunninginterval.append(jsonContent[u'Runninginterval'])

            success = True
        except Exception as e:
            print e

    return success

def getSystemVersion(devicesID):
    ver = os.popen(adb_s + devicesID + ' shell getprop ro.build.version.sdk').readlines()
    for version in ver:
        return version

def initExcel(apkList, devicesid, index, number, gConfigTableCaseArray):
    excelFile = getExcelName_s(devicesid, index, number)
    if os.path.exists(excelFile) == False:
        createExcel_s(apkList, devicesid, index, number, gConfigTableCaseArray)
    return excelFile

class groupData:
    def __init__(self, begin, end,tempNative_Begin,tempNative_end,EGL_MTRACKbegin,EGL_MTRACKend,GL_sizebegin,GL_sizeend,Graphics_size_begin,Graphics_size_end,TOTAL_sizebegin,TOTAL_sizeend,tempUnknowBegin,tempUnknowEnd,tempother_mmapBegin,tempother_mmapEnd,tempart_mmap,tempart_mmap_End,tempoat_mmap,tempoat_mmapEnd,tempdex_mmap,tempdex_mmapEnd,tempttf_mmap,tempttf_mmapEnd,tempapk_mmap,tempapk_mmapEnd,tempjar_mmap,tempjar_mmapEnd,tempso_mmap,tempso_mmapEnd,temp_other_dev,temp_other_devEnd,tempgfx_dev,tempgfx_devEnd,tempashmem,tempashmemEnd,tempstack,tempstackEnd,tempdalvikother,tempdalvikotherEnd):
        self.java_begin = begin
        self.java_end = end
        self.tempNative_Begin = tempNative_Begin
        self.tempNative_end = tempNative_end
        self.EGL_MTRACKbegin = EGL_MTRACKbegin
        self.EGL_MTRACKend = EGL_MTRACKend
        self.GL_sizebegin = GL_sizebegin
        self.GL_sizeend = GL_sizeend
        self.Graphics_size_begin = Graphics_size_begin
        self.Graphics_size_end = Graphics_size_end
        self.TOTAL_sizebegin = TOTAL_sizebegin
        self.TOTAL_sizeend = TOTAL_sizeend
        self.tempUnknowBegin =tempUnknowBegin
        self.tempUnknowEnd = tempUnknowEnd
        self.tempother_mmapBegin = tempother_mmapBegin
        self.tempother_mmapEnd = tempother_mmapEnd
        self.tempart_mmap =tempart_mmap
        self.tempart_mmap_End =tempart_mmap_End
        self.tempoat_mmap = tempoat_mmap
        self.tempoat_mmapEnd = tempoat_mmapEnd
        self.tempdex_mmap = tempdex_mmap
        self.tempdex_mmapEnd = tempdex_mmapEnd
        self.tempttf_mmap =tempttf_mmap
        self.tempttf_mmapEnd = tempttf_mmapEnd
        self.tempapk_mmap = tempapk_mmap
        self.tempapk_mmapEnd = tempapk_mmapEnd
        self.tempjar_mmap =tempjar_mmap
        self.tempjar_mmapEnd = tempjar_mmapEnd
        self.tempso_mmap =tempso_mmap
        self.tempso_mmapEnd = tempso_mmapEnd
        self.temp_other_dev = temp_other_dev
        self.temp_other_devEnd = temp_other_devEnd
        self.tempgfx_dev = tempgfx_dev
        self.tempgfx_devEnd = tempgfx_devEnd
        self.tempashmem = tempashmem
        self.tempashmemEnd =tempashmemEnd
        self.tempstack = tempstack
        self.tempstackEnd =tempstackEnd
        self.tempdalvikother =tempdalvikother
        self.tempdalvikotherEnd = tempdalvikotherEnd

    java_begin = 0
    java_end = 0
    tempNative_Begin = 0
    tempNative_end = 0
    EGL_MTRACKbegin = 0
    EGL_MTRACKend = 0
    GL_sizebegin = 0
    GL_sizeend = 0
    Graphics_size_begin = 0
    Graphics_size_end = 0
    TOTAL_sizebegin = 0
    TOTAL_sizeend = 0
    tempUnknowBegin = 0
    tempUnknowEnd = 0
    tempother_mmapBegin =0
    tempother_mmapEnd =0
    tempart_mmap = 0
    tempart_mmap_End =0
    tempoat_mmap = 0
    tempoat_mmapEnd = 0
    tempdex_mmap = 0
    tempdex_mmapEnd = 0
    tempttf_mmap = 0
    tempttf_mmapEnd =0
    tempapk_mmap =0
    tempapk_mmapEnd =0
    tempjar_mmap =0
    tempjar_mmapEnd = 0
    tempso_mmap = 0
    tempso_mmapEnd =0
    temp_other_dev = 0
    temp_other_devEnd = 0
    tempgfx_dev = 0
    tempgfx_devEnd = 0
    tempashmem = 0
    tempashmemEnd = 0
    tempstack = 0
    tempstackEnd = 0
    tempdalvikother = 0
    tempdalvikotherEnd = 0

# def write_dates_excel(excelFile,caseinfo):
def write_dates_excel(excelFile, gCurrentCursor):
    group = 0
    rows = 2

    keyList = gCurrentCursor.keys()
    for keyValue in keyList:
        rows = 2
        for item in gCurrentCursor.get(keyValue, []):
            WriteExcel_s(excelFile, rows, group + 1, item.java_begin, item.java_end,item.tempNative_Begin,item.tempNative_end,item.EGL_MTRACKbegin,item.EGL_MTRACKend,item.GL_sizebegin,item.GL_sizeend,item.Graphics_size_begin,item.Graphics_size_end,item.TOTAL_sizebegin,item.TOTAL_sizeend,item.tempUnknowBegin,item.tempUnknowEnd,item.tempother_mmapBegin,item.tempother_mmapEnd,item.tempart_mmap,item.tempart_mmap_End,item.tempoat_mmap,item.tempoat_mmapEnd,item.tempdex_mmap,item.tempdex_mmapEnd,item.tempttf_mmap,item.tempttf_mmapEnd,item.tempapk_mmap,item.tempapk_mmapEnd,item.tempjar_mmap,item.tempjar_mmapEnd,item.tempso_mmap,item.tempso_mmapEnd,item.temp_other_dev,item.temp_other_devEnd,item.tempgfx_dev,item.tempgfx_devEnd,item.tempashmem,item.tempashmemEnd,item.tempstack,item.tempstackEnd,item.tempdalvikother,item.tempdalvikotherEnd)
            rows += 1
        group += 40

def createExcel_s(apkList, devicesid, index, number, gConfigTableCaseArray):
    filename = getExcelName_s(devicesid, index, number)
    version = []
    for apk in apkList:
        version.append(getVerFromPackageName(apk))

    file = xlwt.Workbook()
    sheetPtr = file.add_sheet("Sheet")
    group = 0
    for i in range(len(gConfigTableCaseArray)):
        sheetPtr.write(i + 2, 0, gConfigTableCaseArray[i][0] + '_' + gConfigTableCaseArray[i][1])
    for ver in version:
        writeHeader(sheetPtr, group, ver, gConfigTableCaseArray)
        group += 40
    file.save(filename)

def getExcelName_s(devicesid, index, number):
    ''' '/instructions/' + '''
    fileName = os.getcwd() + '/launcher_' + devicesid +'_' +str(number) + '.xls'
    return fileName

def WriteExcel_s(excelFile, x, y, javapss_begin, javapss_end,tempNative_Begin,tempNative_end,EGL_MTRACKbegin,EGL_MTRACKend,GL_sizebegin,GL_sizeend,Graphics_size_begin,Graphics_size_end,TOTAL_sizebegin,TOTAL_sizeend,tempUnknowBegin,tempUnknowEnd,tempother_mmapBegin,tempother_mmapEnd,tempart_mmap,tempart_mmap_End,tempoat_mmap,tempoat_mmapEnd,tempdex_mmap,tempdex_mmapEnd,tempttf_mmap,tempttf_mmapEnd,tempapk_mmap,tempapk_mmapEnd,tempjar_mmap,tempjar_mmapEnd,tempso_mmap,tempso_mmapEnd,temp_other_dev,temp_other_devEnd,tempgfx_dev,tempgfx_devEnd,tempashmem,tempashmemEnd,tempstack,tempstackEnd,tempdalvikother,tempdalvikotherEnd):
    print 'WriteExcel x=', x, '   y=', y
    excelOld = xlrd.open_workbook(excelFile)
    excelPtr = copy(excelOld)
    sheetPtr = excelPtr.get_sheet(0)
    sheetPtr.write(x, y, javapss_begin)
    sheetPtr.write(x, y + 1, javapss_end)
    sheetPtr.write(x, y + 2, tempNative_Begin)
    sheetPtr.write(x, y + 3, tempNative_end)
    sheetPtr.write(x, y + 4, EGL_MTRACKbegin)
    sheetPtr.write(x, y + 5, EGL_MTRACKend)
    sheetPtr.write(x, y + 6, GL_sizebegin)
    sheetPtr.write(x, y + 7, GL_sizeend)
    sheetPtr.write(x, y + 8, Graphics_size_begin)
    sheetPtr.write(x, y + 9, Graphics_size_end)
    sheetPtr.write(x, y + 10, TOTAL_sizebegin)
    sheetPtr.write(x, y + 11, TOTAL_sizeend)
    sheetPtr.write(x, y + 12, tempUnknowBegin)
    sheetPtr.write(x, y + 13, tempUnknowEnd)
    sheetPtr.write(x, y + 14, tempother_mmapBegin)
    sheetPtr.write(x, y + 15, tempother_mmapEnd)
    sheetPtr.write(x, y + 16, tempart_mmap)
    sheetPtr.write(x, y + 17, tempart_mmap_End)
    sheetPtr.write(x, y + 18, tempoat_mmap)
    sheetPtr.write(x, y + 19, tempoat_mmapEnd)
    sheetPtr.write(x, y + 20, tempdex_mmap)
    sheetPtr.write(x, y + 21, tempdex_mmapEnd)
    sheetPtr.write(x, y + 22, tempttf_mmap)
    sheetPtr.write(x, y + 23, tempttf_mmapEnd)
    sheetPtr.write(x, y + 24, tempapk_mmap)
    sheetPtr.write(x, y + 25, tempapk_mmapEnd)
    sheetPtr.write(x, y + 26, tempjar_mmap)
    sheetPtr.write(x, y + 27, tempjar_mmapEnd)
    sheetPtr.write(x, y + 28, tempso_mmap)
    sheetPtr.write(x, y + 29, tempso_mmapEnd)
    sheetPtr.write(x, y + 30, temp_other_dev)
    sheetPtr.write(x, y + 31, temp_other_devEnd)
    sheetPtr.write(x, y + 32, tempgfx_dev)
    sheetPtr.write(x, y + 33, tempgfx_devEnd)
    sheetPtr.write(x, y + 34, tempashmem)
    sheetPtr.write(x, y + 35, tempashmemEnd)
    sheetPtr.write(x, y + 36, tempstack)
    sheetPtr.write(x, y + 37, tempstackEnd)
    sheetPtr.write(x, y + 38, tempdalvikother)
    sheetPtr.write(x, y + 39, tempdalvikotherEnd)
    excelPtr.save(excelFile)

def writeHeader(sheetPtr, group, version, gConfigTableCaseArray):

    sheetPtr.write_merge(0, 0, group+1, group  +40, version)
    sheetPtr.write(1, (group) + 1, u'Dalvik_pss_begin')
    sheetPtr.write(1, (group ) + 2, u'Dalvik_pss_end')
    sheetPtr.write(1, (group) + 3, u'Native_pss_begin')
    sheetPtr.write(1, (group) + 4, u'Native_pss_end')
    sheetPtr.write(1, (group) + 5, u'Egl_mtrackbegin')
    sheetPtr.write(1, (group) + 6, u'Egl_mtrackend')
    sheetPtr.write(1, (group ) + 7, u'GL_sizebegin')
    sheetPtr.write(1, (group ) + 8, u'GL_sizeend')
    sheetPtr.write(1, (group) + 9 ,u'Graphics_size_begin')
    sheetPtr.write(1, (group) + 10 ,u'Graphics_size_end')
    sheetPtr.write(1, (group) + 11, u'TOTAL_SIZE_BEGIN')
    sheetPtr.write(1, (group) + 12, u'TOTAL_SIZE_end')
    sheetPtr.write(1, (group) + 13, u'UnknowBegin')
    sheetPtr.write(1, (group) + 14, u'UnknowEnd')
    sheetPtr.write(1, (group) + 15, u'other_mmapBegin')
    sheetPtr.write(1, (group) + 16, u'other_mmapEnd')
    sheetPtr.write(1, (group) + 17, u'art_mmap')
    sheetPtr.write(1, (group) + 18, u'art_mmap_End')
    sheetPtr.write(1, (group) + 19, u'oat_mmap')
    sheetPtr.write(1, (group) + 20, u'oat_mmapEnd')
    sheetPtr.write(1, (group) + 21, u'dex_mmap')
    sheetPtr.write(1, (group) + 22, u'dex_mmapEnd')
    sheetPtr.write(1, (group) + 23, u'ttf_mmap')
    sheetPtr.write(1, (group) + 24, u'ttf_mmapEnd')
    sheetPtr.write(1, (group) + 25, u'apk_mmap')
    sheetPtr.write(1, (group) + 26, u'apk_mmapEnd')
    sheetPtr.write(1, (group) + 27, u'jar_mmap')
    sheetPtr.write(1, (group) + 28, u'jar_mmapEnd')
    sheetPtr.write(1, (group) + 29, u'so_mmap')
    sheetPtr.write(1, (group) + 30, u'so_mmapEnd')
    sheetPtr.write(1, (group) + 31, u'other_dev')
    sheetPtr.write(1, (group) + 32, u'other_devEnd')
    sheetPtr.write(1, (group) + 33, u'gfx_dev')
    sheetPtr.write(1, (group) + 34, u'gfx_devEnd')
    sheetPtr.write(1, (group) + 35, u'ashmem')
    sheetPtr.write(1, (group) + 36, u'ashmemEnd')
    sheetPtr.write(1, (group) + 37, u'stack')
    sheetPtr.write(1, (group) + 38, u'stackEnd')
    sheetPtr.write(1, (group) + 39, u'dalvikother')
    sheetPtr.write(1, (group) + 40, u'dalvikotherEnd')

def judge_install_success(devicesID):
    startactivity_s = startActivity(devicesID)
    if len(startactivity_s) > 1:
        if 'Error' in startactivity_s[1]:
            return False

    return True

def find_devices(devicesID):

    command = os.popen('adb devices').readlines()
    for iditem in command:
        if str(devicesID) not in iditem:
            return False
    return True

def setting_homes(devicesID):

    ui = UiAuto(devicesID)
    ui.set_home()

def home_homes(devicesID):
    
    os.popen(adb_s + devicesID + home_home)

def getHeap_size(devicesID, processName):

    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Dalvik Heap' in infoitem:
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:
                return  (infoiteminfod[-3].strip())
    return 0

def getHeap_size_18(devicesID, processName):

    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Dalvik' in infoitem:
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:
                # print infoiteminfod
                return   (infoiteminfod[-3].strip())
    return 0

def getHeap_Alloc_size(devicesID, processName):

    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Dalvik Heap' in infoitem:
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:
                return  (infoiteminfod[-2].strip())
    return 0

def getHeap_Alloc_size_18(devicesID, processName):

    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Dalvik' in infoitem:
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:
                # print infoiteminfod
                return   (infoiteminfod[-2].strip())
    return 0

def getHeap_Free_size(devicesID, processName):

    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Dalvik Heap' in infoitem:
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:
                return   (infoiteminfod[-1].strip())
    return 0

def getHeap_Free_size_18(devicesID, processName):

    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Dalvik' in infoitem:
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:
                print infoiteminfod
                return    (infoiteminfod[-1].strip())
    return 0

def getHeap_dex_map_size(devicesID, processName):

    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if '.dex mmap' in infoitem:
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:

                return  (infoiteminfod[2].strip())
    return 0

def getHeap_dex_map_size_18(devicesID, processName):

    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if '.dex mmap' in infoitem:
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:
                # print infoiteminfod
                return  (infoiteminfod[2].strip())
    return 0

def getHeap_EGL_MTRACK_size(devicesID, processName):

    # 等待获取内存值
    adbCommand =adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'EGL mtrack' in infoitem:
            infoiteminfod = infoitem.split('   ')
            print infoiteminfod
            if len(infoiteminfod) > 4:

                for i in range(5):
                    if infoiteminfod[infoiteminfod.index('EGL mtrack') + i + 1] == '':
                        print 'null'
                    else:
                        break;
                # print infoitem
                print (infoiteminfod[infoiteminfod.index('EGL mtrack') + i + 1].strip())
                return (infoiteminfod[infoiteminfod.index('EGL mtrack') + i + 1].strip())
    return 0

def getHeap_GL_size(devicesID, processName):

    # 等待获取内存值
    adbCommand =adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'GL mtrack' in infoitem and 'E' not in infoitem:
            infoiteminfod = infoitem.split('   ')

            if len(infoiteminfod) > 4:

                return   (infoiteminfod[2].strip())
    return 0

def getHeap_TOTAL_size(devicesID, processName):

    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'TOTAL' in infoitem and 'Pss' not in infoitem  and 'PSS' not in infoitem  and 'SWAP' not in infoitem:
            infoiteminfod = infoitem.split('   ')
            print infoiteminfod
            if len(infoiteminfod) > 5:

                for i in range(5):
                    if infoiteminfod[infoiteminfod.index('  TOTAL') + i + 1] == '':
                        print 'null'
                    else:
                        break;
                # print infoitem
                print (infoiteminfod[infoiteminfod.index('  TOTAL') + i + 1].strip())
                return (infoiteminfod[infoiteminfod.index('  TOTAL') + i + 1].strip())
    return 0

def getGraphics_size(devicesID, processName):
    # 等待获取内存值

    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:

        if 'Graphics' in infoitem :
            infoiteminfod = infoitem.split('   ')
            print infoiteminfod
            if len(infoiteminfod) > 5:

                for i in range(5):
                    if infoiteminfod[infoiteminfod.index('Graphics:') + i + 1] == '':
                        print 'null'
                    else:
                        break;
                # print infoitem
                print (infoiteminfod[infoiteminfod.index('Graphics:') + i + 1].strip())
                return (infoiteminfod[infoiteminfod.index('Graphics:') + i + 1].strip())
    return 0

def getDalvikotherMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Dalvik Other' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:
                # print int(infoiteminfod[1].strip())
                return (infoiteminfod[1].strip())
    return 0

def getstackMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Stack' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            print infoiteminfod
            if len(infoiteminfod) > 4:
                for i in range(5):
                    if infoiteminfod[infoiteminfod.index('  Stack') + i + 1] == '':
                        print 'null'
                    else:
                        break;
                # print infoitem
                print (infoiteminfod[infoiteminfod.index('  Stack') + i + 1].strip())
                return (infoiteminfod[infoiteminfod.index('  Stack') + i + 1].strip())

    return 0

def getAshmemMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Ashmem' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:
                # print infoitem
                # print int(infoiteminfod[4].strip())
                return (infoiteminfod[4].strip())
    return 0

def getGfx_devMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Gfx dev' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:
                # print infoitem
                # print int(infoiteminfod[4].strip())
                return (infoiteminfod[4].strip())
    return 0

def getOther_devMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Other dev' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:
                # print infoitem
                # print int(infoiteminfod[3].strip())
                return (infoiteminfod[3].strip())
    return 0

def getso_mmapMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if '.so mmap' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            print infoiteminfod
            if len(infoiteminfod) > 4:
                for i in range(5):
                    if infoiteminfod[infoiteminfod.index('  .so mmap') + i + 1] == '':
                        print 'null'
                    else:
                        break;
                # print infoitem
                print (infoiteminfod[infoiteminfod.index('  .so mmap') + i + 1].strip())
                return (infoiteminfod[infoiteminfod.index('  .so mmap') + i + 1].strip())

    return 0

def getjar_mmapMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if '.jar mmap' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:
                print infoitem
                print (infoiteminfod[3].strip())
                return (infoiteminfod[3].strip())
    return 0

def getapk_mmapMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if '.apk mmap' in infoitem:

            infoiteminfod = infoitem.split('   ')
            # print infoiteminfod
            if len(infoiteminfod) > 4:

                for i in  range(5):
                    if infoiteminfod[infoiteminfod.index(' .apk mmap')+i+1] =='':
                        print 'null'
                    else:
                        break;
                # print infoitem
                print (infoiteminfod[infoiteminfod.index(' .apk mmap')+i+1].strip())
                return (infoiteminfod[infoiteminfod.index(' .apk mmap')+i+1].strip())
    return 0

def getttf_mmapMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if '.ttf mmap' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            print infoiteminfod
            if len(infoiteminfod) > 4:
                for i in  range(5):
                    if infoiteminfod[infoiteminfod.index(' .ttf mmap')+i+1] =='':
                        print 'null'
                    else:
                        break;
                print infoitem
                print (infoiteminfod[infoiteminfod.index(' .ttf mmap')+i+1].strip())
                return (infoiteminfod[infoiteminfod.index(' .ttf mmap')+i+1].strip())
    return 0

def getdex_mmapMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if '.dex mmap' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            print infoiteminfod
            if len(infoiteminfod) > 4:
                for i in range(5):
                    if infoiteminfod[infoiteminfod.index(' .dex mmap') + i + 1] == '':
                        print 'null'
                    else:
                        break;
                # print infoitem
                print (infoiteminfod[infoiteminfod.index(' .dex mmap') + i + 1].strip())
                return (infoiteminfod[infoiteminfod.index(' .dex mmap') + i + 1].strip())
    return 0

def getoat_mmapMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if '.oat mmap' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            print infoiteminfod
            if len(infoiteminfod) > 4:
                for i in range(5):
                    if infoiteminfod[infoiteminfod.index(' .oat mmap') + i + 1] == '':
                        print 'null'
                    else:
                        break;
                # print infoitem
                print (infoiteminfod[infoiteminfod.index(' .oat mmap') + i + 1].strip())
                return (infoiteminfod[infoiteminfod.index(' .oat mmap') + i + 1].strip())

    return 0

def getart_mmapMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if '.art mmap' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            print infoiteminfod
            if len(infoiteminfod) > 4:
                for i in range(5):
                    if infoiteminfod[infoiteminfod.index(' .art mmap') + i + 1] == '':
                        print 'null'
                    else:
                        break;
                # print infoitem
                print (infoiteminfod[infoiteminfod.index(' .art mmap') + i + 1].strip())
                return (infoiteminfod[infoiteminfod.index(' .art mmap') + i + 1].strip())
    return 0

def getOther_mmapMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Other mmap' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:
                print infoitem
                print (infoiteminfod[3].strip())
                return (infoiteminfod[3].strip())
    return 0

def getOther_mmapMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Other mmap' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            print infoiteminfod
            if len(infoiteminfod) > 4:
                for i in range(5):
                    if infoiteminfod[infoiteminfod.index('Other mmap') + i + 1] == '':
                        print 'null'
                    else:
                        break;
                # print infoitem
                print (infoiteminfod[infoiteminfod.index('Other mmap') + i + 1].strip())
                return (infoiteminfod[infoiteminfod.index('Other mmap') + i + 1].strip())
    return 0

def getUnknownMemoryInfo(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Unknown' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            print infoiteminfod
            if len(infoiteminfod) > 4:
                for i in range(5):
                    if infoiteminfod[infoiteminfod.index('Unknown') + i + 1] == '':
                        print 'null'
                    else:
                        break;
                # print infoitem
                print (infoiteminfod[infoiteminfod.index('Unknown') + i + 1].strip())
                return (infoiteminfod[infoiteminfod.index('Unknown') + i + 1].strip())
    return 0

def getNative_size(devicesID, processName):

    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:

        if 'Native Heap' in infoitem:
            infoiteminfod = infoitem.split('   ')

            if len(infoiteminfod) > 5:
                for i in range(5):
                    if infoiteminfod[infoiteminfod.index('  Native Heap') + i + 1] == '':
                        print 'null'
                    else:
                        break;
                print infoitem
                print (infoiteminfod[infoiteminfod.index('  Native Heap') + i + 1].strip())
                return (infoiteminfod[infoiteminfod.index('  Native Heap') + i + 1].strip())
            return 0
    return 0

def getNative_size_18(devicesID, processName):

    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:

        if 'Native' in infoitem:
            infoiteminfod = infoitem.split('   ')
            # print infoiteminfod
            if len(infoiteminfod) > 5:
                print infoiteminfod
                if len(infoiteminfod[3].strip())==0:
                    return   (infoiteminfod[4].strip())
                else:
                    return   (infoiteminfod[3].strip())
    return 0

def getstackMemoryInfo_18(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if 'Stack' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:
                print infoitem
                print (infoiteminfod[4].strip())
                return (infoiteminfod[4].strip())
    return 0

def getapk_mmapMemoryInfo_18(devicesID, processName):
    # 等待获取内存值
    adbCommand = adb_s + devicesID + '  shell dumpsys meminfo  com.ksmobile.launcher';
    if processName != '':
        adbCommand = adbCommand + ":" + processName

    meminfo = os.popen(adbCommand).readlines()
    for infoitem in meminfo:
        if '.apk mmap' in infoitem:
            # print infoitem
            infoiteminfod = infoitem.split('   ')
            if len(infoiteminfod) > 4:
                print infoitem
                print (infoiteminfod[3].strip())
                return (infoiteminfod[3].strip())
    return 0

def main():
    number = 0
    # phonestat=sys.argv[1]
    phonestat = 'su'
    while number < 10:

        try:
            gConfigTableApkPath = []
            gConfigTableCaseArray = []
            gConfigTableRunninginterval = []
            success_number = 0
            failure_number = 0
            number_number = 1
            gCurrentCursor = {}  # group groupData
            apkpath = os.getcwd()
            datetime1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            print 'begin time:', datetime1
            # 读取配置文件
            success = readConfigContent(gConfigTableApkPath, gConfigTableCaseArray, gConfigTableRunninginterval)
            if success == False:
                raise Exception('read config.json faile')
            #devicesInfo = devicesConnectInfo()
            #devicesnum = len(devicesInfo)
            #if devicesnum > 0:
            #    devicesID = devicesInfo[0]
            devicesID = '03265fe709329537'
            d=Device(devicesID)
            excelFile = initExcel(gConfigTableApkPath, str(devicesID), len(gConfigTableApkPath), number,
                                  gConfigTableCaseArray)

            for apkitem in range(len(gConfigTableApkPath)):
                try:
                    apks = gConfigTableApkPath[apkitem]

                    uninstall(devicesID, package_name)

                    appmapname = apks

                    appmapnamepath = apkpath + "/apk/" + appmapname.strip()
                    print 'start install '
                    # 安装apk包
                    install_success = True
                    for i in range(3):
                        install(devicesID, appmapnamepath)
                        time.sleep(10)
                        home_homes(devicesID)
                        #time.sleep(2)
                        setting_homes(devicesID)
                        if judge_install_success(devicesID) == True:
                            install_success = True
                            break
                        else:
                            install_success = False

                    if install_success == False:
                        continue
                    for caseitem in range(len(gConfigTableCaseArray)):

                        caseinfo = gConfigTableCaseArray[caseitem]

                        print str(caseitem) + 'caseitem'
                        print str(caseinfo) + 'caseinfo'

                        case_case_info = caseinfo[0]
                        valuse_number = caseinfo[1]
                        process_name = caseinfo[2]

                        dalvik_size_run_last = []
                        dalvik_size_run_first = []

                        batteryFirstTime = []
                        batteryEndTime = []
                        batteryLevels = []
                        batteryCapacity = []
                        batteryComputed = []
                        while True:
                            # 启动Launcher
                            startactivity_s = startActivity(devicesID)
                            # print startactivity_s
                            time.sleep(7)
                            # 跳过启动页
                            '''
                            apkversion = getVerFromPackageName(appmapname)
                            if len(apkversion) <= 5:
                                del_splash(devicesID)
                            else:
                                #time.sleep(20)
                                for i in range(10):
                                    back_backs(devicesID)
                                    #time.sleep(3)
                            '''        
                            del_splash(devicesID)
                            setting_homes(devicesID)        
                            # 记录开始时间
                            beginTimer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                            batteryFirstTime.append(beginTimer)

                            print 'begin time=', beginTimer
        
                            time.sleep(240)
                            if process_name == 'wallpaper':
                                wallpaperActivity = 'adb -s ' + devicesID + ' shell am start -n  com.ksmobile.launcher/.wallpaper.PersonalizationActivity' 
                                os.popen(wallpaperActivity)
                                time.sleep(15)
                                back_backs(devicesID)
                            # 清理一次内存
                            runGC(devicesID,phonestat)
                            os.system('adb -s ' + devicesID + ' shell dumpsys meminfo  com.ksmobile.launcher')
                            #time.sleep(60)
                            #runGC(devicesID,phonestat)
                            print 'gc accomplish'
                            systemversion = getSystemVersion(devicesID)
                            # print systemversion
                            if int(systemversion.strip()) > 18:
                                # 获取操作前的内存值
                                tempMemoryBegin = getDalvikMemoryInfo(devicesID, process_name)
                                tempNative_Begin = getNative_size(devicesID, process_name)
                                tempDex_EGL_MTRACK_Begin = getHeap_EGL_MTRACK_size(devicesID, process_name)
                                tempGL_size_Begin = getHeap_GL_size(devicesID, process_name)
                                tempGraphics_size_begin = getGraphics_size(devicesID, process_name)
                                tempMemoryTOTAL_Begin = getHeap_TOTAL_size(devicesID, process_name)
                                tempUnknowBegin=getUnknownMemoryInfo(devicesID, process_name)
                                tempother_mmapBegin=getOther_mmapMemoryInfo(devicesID, process_name)
                                tempart_mmap=getart_mmapMemoryInfo(devicesID, process_name)
                                tempoat_mmap=getoat_mmapMemoryInfo(devicesID, process_name)
                                tempdex_mmap=getdex_mmapMemoryInfo(devicesID, process_name)
                                tempttf_mmap=getttf_mmapMemoryInfo(devicesID, process_name)
                                tempapk_mmap=getapk_mmapMemoryInfo(devicesID, process_name)
                                tempjar_mmap=getjar_mmapMemoryInfo(devicesID, process_name)
                                tempso_mmap=getso_mmapMemoryInfo(devicesID, process_name)
                                temp_other_dev=getOther_devMemoryInfo(devicesID, process_name)
                                tempgfx_dev=getGfx_devMemoryInfo(devicesID, process_name)
                                tempashmem=getAshmemMemoryInfo(devicesID, process_name)
                                tempstack=getstackMemoryInfo(devicesID, process_name)
                                tempdalvikother=getDalvikotherMemoryInfo(devicesID, process_name)

                            else:
                                tempMemoryBegin = getDalvikMemoryInfo_18(devicesID, process_name)
                                tempNative_Begin = getNative_size_18(devicesID, process_name)
                                tempDex_EGL_MTRACK_Begin = getHeap_EGL_MTRACK_size(devicesID, process_name)
                                tempGL_size_Begin = getHeap_GL_size(devicesID, process_name)
                                tempGraphics_size_begin = getGraphics_size(devicesID, process_name)
                                tempMemoryTOTAL_Begin = getHeap_TOTAL_size(devicesID, process_name)
                                tempUnknowBegin=getUnknownMemoryInfo(devicesID, process_name)
                                tempother_mmapBegin=getOther_mmapMemoryInfo(devicesID, process_name)
                                tempart_mmap=getart_mmapMemoryInfo(devicesID, process_name)
                                tempoat_mmap=getoat_mmapMemoryInfo(devicesID, process_name)
                                tempdex_mmap=getdex_mmapMemoryInfo(devicesID, process_name)
                                tempttf_mmap=getttf_mmapMemoryInfo(devicesID, process_name)
                                tempapk_mmap=getapk_mmapMemoryInfo_18(devicesID, process_name)
                                tempjar_mmap=getjar_mmapMemoryInfo(devicesID, process_name)
                                tempso_mmap=getso_mmapMemoryInfo(devicesID, process_name)
                                temp_other_dev=getOther_devMemoryInfo(devicesID, process_name)
                                tempgfx_dev=getGfx_devMemoryInfo(devicesID, process_name)
                                tempashmem=getAshmemMemoryInfo(devicesID, process_name)
                                tempstack=getstackMemoryInfo_18(devicesID, process_name)
                                tempdalvikother=getDalvikotherMemoryInfo(devicesID, process_name)
                            # 清理系统电量缓存
                            os.popen(adb_s + devicesID + ' shell ' + 'dumpsys batterystats  --reset')

                            # 模块操作
                            for items in range(int(caseinfo[1])):
                               begin_run(devicesID, case_case_info,d)

                            runGC(devicesID,phonestat)
                            # 获取手机系统
                            if int(systemversion.strip()) > 18:
                                # 获取操作后的内存值
                                tempMemoryEnd = getDalvikMemoryInfo(devicesID, process_name)
                                tempNative_end = getNative_size(devicesID, process_name)
                                tempDex_EGL_MTRACKEnd=getHeap_EGL_MTRACK_size(devicesID, process_name)
                                tempGL_sizeEnd=getHeap_GL_size(devicesID, process_name)
                                tempGraphics_size_end = getGraphics_size(devicesID, process_name)
                                tempMemoryTOTALEnd=getHeap_TOTAL_size(devicesID, process_name)

                                tempUnknowEnd = getUnknownMemoryInfo(devicesID, process_name)
                                tempother_mmapEnd = getOther_mmapMemoryInfo(devicesID, process_name)
                                tempart_mmap_End = getart_mmapMemoryInfo(devicesID, process_name)
                                tempoat_mmapEnd = getoat_mmapMemoryInfo(devicesID, process_name)
                                tempdex_mmapEnd = getdex_mmapMemoryInfo(devicesID, process_name)
                                tempttf_mmapEnd = getttf_mmapMemoryInfo(devicesID, process_name)
                                tempapk_mmapEnd = getapk_mmapMemoryInfo(devicesID, process_name)
                                tempjar_mmapEnd = getjar_mmapMemoryInfo(devicesID, process_name)
                                tempso_mmapEnd = getso_mmapMemoryInfo(devicesID, process_name)
                                temp_other_devEnd = getOther_devMemoryInfo(devicesID, process_name)
                                tempgfx_devEnd = getGfx_devMemoryInfo(devicesID, process_name)
                                tempashmemEnd = getAshmemMemoryInfo(devicesID, process_name)
                                tempstackEnd = getstackMemoryInfo(devicesID, process_name)
                                tempdalvikotherEnd = getDalvikotherMemoryInfo(devicesID, process_name)
                                # 获取操作后的电量
                                batteryInfo = getBatterInfo(devicesID)
                                endtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                                batteryEndTime.append(endtime)
                                batteryLevels.append(batteryInfo[0])
                                batteryCapacity.append(batteryInfo[1])
                                batteryComputed.append(batteryInfo[2])
                            else:
                                tempMemoryEnd = getDalvikMemoryInfo_18(devicesID, process_name)
                                tempNative_end = getNative_size_18(devicesID, process_name)
                                tempDex_EGL_MTRACKEnd=getHeap_EGL_MTRACK_size(devicesID, process_name)
                                tempGL_sizeEnd = getHeap_GL_size(devicesID, process_name)
                                tempGraphics_size_end = getGraphics_size(devicesID, process_name)
                                tempMemoryTOTALEnd=getHeap_TOTAL_size(devicesID, process_name)

                                tempUnknowEnd = getUnknownMemoryInfo(devicesID, process_name)
                                tempother_mmapEnd = getOther_mmapMemoryInfo(devicesID, process_name)
                                tempart_mmap_End = getart_mmapMemoryInfo(devicesID, process_name)
                                tempoat_mmapEnd = getoat_mmapMemoryInfo(devicesID, process_name)
                                tempdex_mmapEnd = getdex_mmapMemoryInfo(devicesID, process_name)
                                tempttf_mmapEnd = getttf_mmapMemoryInfo(devicesID, process_name)
                                tempapk_mmapEnd = getapk_mmapMemoryInfo_18(devicesID, process_name)
                                tempjar_mmapEnd = getjar_mmapMemoryInfo(devicesID, process_name)
                                tempso_mmapEnd = getso_mmapMemoryInfo(devicesID, process_name)
                                temp_other_devEnd = getOther_devMemoryInfo(devicesID, process_name)
                                tempgfx_devEnd = getGfx_devMemoryInfo(devicesID, process_name)
                                tempashmemEnd = getAshmemMemoryInfo(devicesID, process_name)
                                tempstackEnd = getstackMemoryInfo_18(devicesID, process_name)
                                tempdalvikotherEnd = getDalvikotherMemoryInfo(devicesID, process_name)

                                batteryInfo = getBatterInfo(devicesID)
                                endtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                                batteryEndTime.append(endtime)
                                batteryLevels.append(batteryInfo[0])
                                batteryCapacity.append(batteryInfo[1])
                                batteryComputed.append(batteryInfo[2])

                            # 打印结束时间
                            print 'end time=', endtime

                            # 对比清理脏数据
                            print str(tempMemoryEnd) + 'tempMemoryEnd'
                            print str(tempMemoryBegin) + 'tempMemoryBegin'
                            if (tempMemoryBegin - tempMemoryEnd)/float(tempMemoryEnd) < 0.05:
                                dalvik_size_run_first.append(tempMemoryBegin)
                                dalvik_size_run_last.append(tempMemoryEnd)
                                gCurrentCursor.setdefault(apkitem, []).append(groupData(tempMemoryBegin, tempMemoryEnd,tempNative_Begin,tempNative_end,tempDex_EGL_MTRACK_Begin,tempDex_EGL_MTRACKEnd,tempGL_size_Begin,tempGL_sizeEnd,tempGraphics_size_begin,tempGraphics_size_end,tempMemoryTOTAL_Begin,tempMemoryTOTALEnd,tempUnknowBegin,tempUnknowEnd,tempother_mmapBegin,tempother_mmapEnd,tempart_mmap,tempart_mmap_End,tempoat_mmap,tempoat_mmapEnd,tempdex_mmap,tempdex_mmapEnd,tempttf_mmap,tempttf_mmapEnd,tempapk_mmap,tempapk_mmapEnd,tempjar_mmap,tempjar_mmapEnd,tempso_mmap,tempso_mmapEnd,temp_other_dev,temp_other_devEnd,tempgfx_dev,tempgfx_devEnd,tempashmem,tempashmemEnd,tempstack,tempstackEnd,tempdalvikother,tempdalvikotherEnd))
                                success_number += 1
                            else:
                                print 'Pollution data'
                                failure_number += 1
                            if len(dalvik_size_run_last) >= int(number_number):

                                write_dates_excel(excelFile, gCurrentCursor)
                                clear(devicesID)
                                break
                            clear(devicesID)
                            home_homes(devicesID)
                            time.sleep(2)
                            setting_homes(devicesID)
                        time.sleep(int(gConfigTableRunninginterval[0]))

                except Exception as e:
                    print e
        # break
        except Exception as e:
            print e

        #break
        number += 1

if __name__ == '__main__':

    main()
    # devicesID = '077f1bdb00d2aa1c'
    # phonestat = 'su'
    # runGC(devicesID,phonestat)
    # d=Device(devicesID)
    #case_case_info  = 'case_allapps'
    # case_case_info  = 'case_booster'
    # case_case_info  = 'case_change_themes'
    # case_case_info  = 'case_folder'
    # case_case_info  = 'case_fuyiping'
    # case_case_info  = 'case_locker'
    # case_case_info  = 'case_menu'
    # case_case_info  = 'case_personal'
    # case_case_info  = 'case_search'
    # case_case_info  = 'case_theme'
    # case_case_info  = 'case_wallpaper'
    #case_case_info  = 'case_weather'
    # begin_run(devicesID, case_case_info,d)





