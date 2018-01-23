# -*- coding:utf-8 -*-
import os
import time
# adb shell pm list packages  查看所有包名  jp.co.hit_point.tabikaeru
# adb shell dumpsys activity | grep -i run  查看类名net.gree.unitywebview.CUnityPlayerActivity  
# 具体像素点自查
nowtime = int(time.time())
cmd = 'adb shell date +%s '
ans = int(os.popen(cmd).read())
while ans < nowtime:
	cmd = 'adb shell am start -n jp.co.hit_point.tabikaeru/net.gree.unitywebview.CUnityPlayerActivity'
	a = os.system(cmd)
	time.sleep(0.1)
	cmd = 'adb shell input swipe 300 700 300 700 50'  #先点一下，防止来了朋友
	os.system(cmd)
	cmd = 'adb shell input swipe 50 700 1300 700 100'  #拖动画面
	os.system(cmd)
	cmd = 'adb shell input swipe 80 1550 1050 1550 100' 
	os.system(cmd)
	cmd = 'adb shell input swipe 80 1650 1050 1550 200'
	os.system(cmd)
	cmd = 'adb shell input swipe 80 1850 1050 1850 500'
	os.system(cmd)

	ans += 3*3600
	time_local = time.localtime(ans)
	dt_new = time.strftime("%m%d%H%M%Y.%S",time_local)
	cmd = 'adb shell "su 0 toybox date %s"' % dt_new
	os.system(cmd)
	




