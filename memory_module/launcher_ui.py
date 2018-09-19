#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: wangqi
#用uiautomator实现一些调用

from uiautomator import Device
import time
import os

#d = Device('03265fe709329537')
########################################################################
class UiAuto():
    """"""
    def __init__(self, DeviceId):
        """Constructor"""
        self.DeviceId = DeviceId
        self.device = Device(DeviceId)


    def set_home(self):
    	d = self.device
    	d.press.home()
        d.press.home()
        d.press.home()
    	#d.press.back()
    	#or d(text = u'猎豹3D桌面').exists
    	if d(text = 'CM Launcher').exists  :
    		d(text = 'CM Launcher').click()
    		if d(text = 'ALWAYS').exists :
    			d(text = 'ALWAYS').click()
    		elif d(text = 'Always').exists :
    			d(text = 'Always').click()
    		else:
    			d.press.home()
    	if d(text = 'Use CM Launcher as Home').exists :
    		if d(text = 'ALWAYS').exists :
    			d(text = 'ALWAYS').click()
    		elif d(text = 'Always').exists :
    			d(text = 'Always').click()
    	else:
    		if d(text = 'ALWAYS').exists :
    			d(text = 'ALWAYS').click()
    		elif d(text = 'Always').exists :
    			d(text = 'Always').click()

    	d.press.home()
    	if d(text = 'CM Launcher').exists :
    		raise Exception('Set Home Failed!!!!')
    	else:
    		print "Set Home app Success!!!"
    		d.press.home()

    def click_theme(self):
    	d = self.device
    	if d(text = 'Apply').exists :
    		d(text = 'Apply').click()
    	else:
    		d.press.back()
    		time.sleep(1)
    		if d(text = 'Apply').exists :
    			d(text = 'Apply').click()
    		else:
    			raise Exception('Set Theme Failed!!!!')

    def skip_HD(self):
        d = self.device
        if d(text = 'Live').exists:
            print "no skip_HD"
        else:
            d.press.back()
            if d(text = 'Wallpapers').exists:
                d(text = 'Wallpapers').click()
            print "skip_HD success!!"

    def skip_ad_wallpaper(self):
        d = self.device
        if d(text = 'SET WALLPAPER').exists:
            print "no skip_ad"
        else:
            d.press.back()
            if d(text = 'SET WALLPAPER').exists:
                print "skip_ad success!!"
            else:
                raise Exception('Enter wallpaper Failed!!!!')

    def daily_wallpaper(self):
        d = self.device
        if d(resourceId="com.ksmobile.launcher:id/btn_daily_wallpaper").exists:
            d(resourceId="com.ksmobile.launcher:id/btn_daily_wallpaper").click()
        else:
            print "old version"





# 以下是locker的一些函数
    def open_locker(self):
        d = self.device
        DeviceId = self.DeviceId
        #enter setting
        cmd = 'adb -s ' + DeviceId +  ' shell am start com.ksmobile.launcher/com.ksmobile.launcher.switchpanel.SwitchPanelActivity'
        os.popen(cmd).read()
        time.sleep(1)

        if d(resourceId="com.ksmobile.launcher:id/switch_panel_cm_settings").exists:
            d(resourceId="com.ksmobile.launcher:id/switch_panel_cm_settings").click()
            time.sleep(1)
            if d(resourceId="com.ksmobile.launcher:id/setting_smart_locker_index2").exists:
                d(resourceId="com.ksmobile.launcher:id/setting_smart_locker_index2").click()
                time.sleep(2)
                d.press.back()
                d.press.home()           
        else:
            raise Exception('Not Enter Setting!!!!')

    def disable_charge_master(self):
        d = self.device
        if d(resourceId="com.ksmobile.launcher:id/locker_option").exists:
            d(resourceId="com.ksmobile.launcher:id/locker_option").click()
            time.sleep(1)
            if d(text = 'Disable Charge Master').exists:
                d(text = 'Disable Charge Master').click()
                time.sleep(2)
                if d(resourceId="com.ksmobile.launcher:id/activate_screen_saver").exists:
                    d(resourceId="com.ksmobile.launcher:id/activate_screen_saver").click()
                    time.sleep(2)
        else:
            raise Exception('Not locked!!!!')
        d.press.back()

    def click_locker_jiasu(self):
        d = self.device
        if d(resourceId="com.ksmobile.launcher:id/clear_tool_btn").exists:
            d(resourceId="com.ksmobile.launcher:id/clear_tool_btn").click()
            time.sleep(4)
        else:
            raise Exception('Not jisuqiu!!!!')
        d.press.back()

    def skip_set_password(self):
        d = self.device
        d.press.back()
        if d(text = 'NOT NOW').exists:
            d(text = 'NOT NOW').click()
            print "skip success!!"
        else:
            print "not skip"
        d.press.back()

    def set_wallpaper(self):
        d = self.device
        if d(text = 'SET WALLPAPER').exists:
            d(text = 'SET WALLPAPER').click()
            time.sleep(2)
            if d(text = 'Set Home Screen').exists:
                d(text = 'Set Home Screen').click()
                time.sleep(2)

        d.press.back()



    def home(self):
    	d = self.device
    	d.press.home()

    def back(self):
    	d = self.device
    	d.press.back()

    def screen_off(self):
    	d = self.device
    	d.screen.off()

    def screen_on(self):
    	d = self.device
    	d.screen.on()


if __name__ == '__main__':
	ui = UiAuto("056511d81b9862ba")
	ui.set_wallpaper()
	# ui.screen_off()
	# ui.screen_on()


