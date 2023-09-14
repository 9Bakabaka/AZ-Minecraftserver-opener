#本程序于2023.03.28加密
#加密工具：pyobfuscate
#©AZ工作室 官网：https://az.zenglingkun.cn
#本软件承诺，终生不收取任何费用
#严禁使用任何反编译工具
#版权所有 侵权必究
from tkinter import *
import os
import win32api , win32con
import requests
import psutil
import os
import subprocess
import setproctitle
import multiprocessing
import sys
if 64 - 64: i11iIiiIii
#版本配置
OO0o = "2.0"
if 81 - 81: Iii1I1 + OO0O0O % iiiii % ii1I - ooO0OO000o
if 4 - 4: IiII1IiiIiI1 / iIiiiI1IiI1I1
setproctitle . setproctitle ( "AZ开服器-" + OO0o )
if 87 - 87: OoOoOO00
if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
o0OOO = "开服器v2.0更新内容\n1.优化下载，软件和下载改为多线程"
if 13 - 13: ooOo + Ooo0O
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
O0oOO0o0 = "下载版本(会自动在后台下载，下载时可能会卡住，以防杀后\n台，下载完成会自动弹出提示，下载时，您可以正常使用电脑)"
if 9 - 9: ooOo - ii1I
if 12 - 12: Ooo00oOo00o / OoOoOO00 - Oo - ii1I * ii1I % iIiiiI1IiI1I1
o0oO0 = "点击确定开始在后台下载,请勿关闭软件，下载完成会有提示，在此期间，您可以正常使用电脑"
if 100 - 100: ii1I
if 27 - 27: I1Ii111 * iiiii + Ooo0O * o00O0oo - i11iIiiIii - IiII
IiiiIiI1iIiI1 = "单击确定以启动,启动需等待1-2分钟会出现MC服务器的GUI"
if 85 - 85: OoOoOO00
if 28 - 28: iII111i
oOOoo00O0O = { "eula.txt" : "\n系统已为您找到该问题的解决方案：请打开开服器目录下 server/[服务器版本]/eula.txt 文件，将false改为true" , "Only up to" : "\n系统已为您找到该问题的解决方案：Java版本过高或过低，请安装错误信息提示的Java版本" }
i1111 = len ( oOOoo00O0O )
i1111 = i1111 - 1
if 22 - 22: iII111i . I1Ii111
if 41 - 41: ooOoO0o . o00O0oo * I1Ii111 % i11iIiiIii
if os . path . exists ( "logs" ) == False :
 os . makedirs ( "logs" )
if os . path . exists ( "server" ) == False :
 os . makedirs ( "server" )
if os . path . exists ( "icon.ico" ) == False :
 o000o0o00o0Oo = requests . get ( "https://az.zenglingkun.cn/kaifu/icon.ico" )
 open ( "icon.ico" , 'wb' ) . write ( o000o0o00o0Oo . content )
if os . path . exists ( "logs/memory.log" ) == False :
 oo = open ( "logs/memory.log" , "w" )
 IiII1I1i1i1ii = psutil . virtual_memory ( )
 IiII1I1i1i1ii = u'%.4f ' % ( IiII1I1i1i1ii . total / 1024 / 1024 / 1024 )
 IiII1I1i1i1ii = int ( int ( float ( IiII1I1i1i1ii ) ) / 2 )
 oo . write ( str ( IiII1I1i1i1ii ) )
 oo . close ( )
if os . path . exists ( "logs/yuan.log" ) == False :
 oo = open ( "logs/yuan.log" , "w" )
 oo . close ( )
if os . path . exists ( "logs/" + OO0o + ".log" ) == False :
 oo = open ( "logs/" + OO0o + ".log" , "w" )
 oo . write ( )
 oo . close ( )
oo = open ( "logs/" + OO0o + ".log" , "r" )
IIIII = oo . read ( )
oo . close ( )
print ( IIIII )
if IIIII != "yes" :
 win32api . MessageBox ( 0 , o0OOO , "开服器v" + OO0o + "更新内容" , win32con . MB_OK )
 oo = open ( "logs/" + OO0o + ".log" , "w" )
 oo . write ( "yes" )
 oo . close ( )
 if 26 - 26: ooOoO0o . Ooo0O - ooOo % Iii1I1 + ooOo
i1iiIIiiI111 = "https://az.zenglingkun.cn/kaifu/get"
oooOOOOO = requests . get ( i1iiIIiiI111 )
oooOOOOO . close ( )
i1iiIII111ii = oooOOOOO . text
if i1iiIII111ii == OO0o :
 pass
else :
 i1iIIi1 = "版本过低，当前版本为：" + OO0o + "，最新版为：" + oooOOOOO . text + "。点击确定自动下载最新版,下载完成后请打开最新版的开服器"
 win32api . MessageBox ( 0 , i1iIIi1 , "版本过低" , win32con . MB_ICONWARNING )
 o000o0o00o0Oo = requests . get ( "https://az.zenglingkun.cn/kaifu/exe/" + OO0o + ".exe" )
 if i1iiIII111ii [ 2 ] == "0" :
  i1iiIII111ii = "正式版"
 elif i1iiIII111ii [ 2 ] != "0" :
  i1iiIII111ii = "测试版"
 open ( "AZ开服器-" + oooOOOOO . text + "-" + i1iiIII111ii + ".exe" , 'wb' ) . write ( o000o0o00o0Oo . content )
 if 50 - 50: i11iIiiIii - iII111i
def oo0Ooo0 ( dic , va ) :
 I1I11I1I1I = [ OooO0OO for OooO0OO , oo0Ooo0 in dic . items ( ) if oo0Ooo0 == va ]
 return I1I11I1I1I
 if 28 - 28: ooO0OO000o
def iii11iII ( value ) :
 try :
  oo = open ( "logs/yuan.log" , "r" , encoding = "utf-8" )
  i1I111I = oo . read ( )
  oo . close ( )
  if i1I111I == "官方源" :
   i1I111I = "https://download.getbukkit.org/spigot/"
  elif i1I111I == "Z站源(国内)" :
   i1I111I = "http://101.33.242.32/mc/"
  win32api . MessageBox ( 0 , o0oO0 , "下载" , win32con . MB_OK )
  i11I1IIiiIi = multiprocessing . Process ( target = IiIiIi ( value , i1I111I ) )
  i11I1IIiiIi . start ( )
  d . destroy ( )
 except TclError :
  win32api . MessageBox ( 0 , "请选择版本！" , "错误" , win32con . MB_ICONWARNING )
  if 40 - 40: I1IiI . OOOo0 . iIiiiI1IiI1I1 . ii1I
def IiIiIi ( version , url ) :
 i11I1IIiiIi = multiprocessing . Process ( target = iii11iII )
 I11iii = version
 version = "spigot-" + version + ".jar"
 url = url + version
 o000o0o00o0Oo = requests . get ( url )
 if os . path . exists ( "server" ) == False :
  os . makedirs ( "server" )
 if os . path . exists ( "server/" + I11iii ) == False :
  os . makedirs ( "server" + "/" + I11iii )
 open ( 'server/' + I11iii + "/" + version , 'wb' ) . write ( o000o0o00o0Oo . content )
 win32api . MessageBox ( 0 , "下载完成！请重启软件" , "下载" , win32con . MB_OK )
 sys . exit ( )
 if 54 - 54: ooOo + ooOo % ooOoO0o % i11iIiiIii / OO0O0O . ooOo
def o0oO0o00oo ( ) :
 try :
  II1i1Ii11Ii11 = iII11i . get (
 iII11i . curselection ( )
 )
  O0O00o0OOO0 . destroy ( )
  oo = open ( "logs/memory.log" , "r" )
  Ii1iIIIi1ii = oo . read ( )
  oo . close ( )
  Ii1iIIIi1ii = int ( Ii1iIIIi1ii ) * 1024
  win32api . MessageBox ( 0 , IiiiIiI1iIiI1 , "AZ开服器" , win32con . MB_OK )
  o0oo0o0O00OO = open ( "run.bat" , "w" )
  o0oo0o0O00OO . write ( "cd server/" + II1i1Ii11Ii11 + " &" + "java -Xmx" + str ( Ii1iIIIi1ii ) + "M -Xms" + str ( Ii1iIIIi1ii ) + "M -jar spigot-" + II1i1Ii11Ii11 + ".jar" )
  o0oo0o0O00OO . close ( )
  o0oO = subprocess . getoutput ( "cd server/" + II1i1Ii11Ii11 + " &" + "java -Xmx" + str ( Ii1iIIIi1ii ) + "M -Xms" + str ( Ii1iIIIi1ii ) + "M -jar spigot-" + II1i1Ii11Ii11 + ".jar" )
  print ( o0oO )
  if "spigot" not in o0oO or "找不到" in o0oO or "Only up to" in o0oO or "eula.txt" in o0oO :
   I1i1iii = Tk ( )
   I1i1iii . title ( "错误" )
   I1i1iii . iconbitmap ( "icon.ico" )
   i1iiI11I = Scrollbar ( I1i1iii )
   I1i1iii . geometry ( "600x600" )
   iiii = Text ( I1i1iii , width = 70 , height = 50 , undo = True , autoseparators = False , yscrollcommand = i1iiI11I . set )
   iiii . pack ( )
   i1iiI11I . config ( command = iiii . yview )
   i1iiI11I . pack ( )
   iiii . insert ( INSERT , "————服务端运行出错————\n" )
   iiii . insert ( INSERT , o0oO )
   for oO0o0O0OOOoo0 in range ( 0 , i1111 ) :
    o0oo0o0O00OO = list ( oOOoo00O0O . keys ( ) )
    o0oo0o0O00OO = o0oo0o0O00OO [ oO0o0O0OOOoo0 ]
    IiIiiI = oOOoo00O0O . get ( o0oo0o0O00OO )
    if o0oo0o0O00OO in o0oO :
     iiii . insert ( INSERT , IiIiiI )
     if 31 - 31: iII111i . iII111i - Oo / OoOoOO00 + o00O0oo * IiII1IiiIiI1
   iiii . insert ( INSERT , "\n———————————————" )
   iiii . insert ( INSERT , "\n若本错误信息对你没有帮助，可打运行开服器目录下的run.bat文件，会有更清楚的信息" )
   iiii . insert ( INSERT , "\nAZ开服器-简洁好用的开服器" )
   I1i1iii . mainloop ( )
   if 63 - 63: ooOoO0o % ii1I / iiiii - iiiii
 except TclError :
  win32api . MessageBox ( 0 , "请选择版本！" , "错误" , win32con . MB_ICONWARNING )
  if 8 - 8: OOOo0
  if 60 - 60: Ooo0O / Ooo0O
def I1II1III11iii ( ) :
 o0oO = [ ]
 Oo000 = "server"
 for ooii11I in os . listdir ( Oo000 ) :
  o0oO . append ( ooii11I )
 return o0oO
def Ooo0OO0oOO ( v ) :
 ii11i1 = open ( "logs/memory.log" , "w" )
 ii11i1 . write ( v )
 ii11i1 . close ( )
 if 29 - 29: Ooo00oOo00o % IiII1IiiIiI1 + o00O0oo / Oo + ooOo * Oo
def i1I1iI ( ) :
 if 1 == 1 :
  def oo0OooOOo0 ( ) :
   try :
    II1i1Ii11Ii11 = iII11i . get (
 iII11i . curselection ( )
 )
   except TclError :
    win32api . MessageBox ( 0 , "请选择版本！" , "错误" , win32con . MB_ICONWARNING )
   iii11iII ( II1i1Ii11Ii11 )
  def o0O ( ) :
   try :
    O00oO = I11i1I1I . get (
 I11i1I1I . curselection ( )
 )
    oo = open ( "logs/yuan.log" , "w" , encoding = "utf-8" )
    oo . write ( O00oO )
    oo . close ( )
    win32api . MessageBox ( 0 , "已保存！" , "保存下载源" , win32con . MB_OK )
   except TclError :
    win32api . MessageBox ( 0 , "请选择下载源！" , "错误" , win32con . MB_ICONWARNING )
    if 83 - 83: Ooo00oOo00o / o00O0oo
  iIIIIii1 = Tk ( )
  oo000OO00Oo = iIIIIii1 . winfo_screenwidth ( )
  O0OOO0OOoO0O = iIIIIii1 . winfo_screenheight ( )
  iIIIIii1 . geometry ( '%dx%d+%d+%d' % ( 415 , 255 , ( oo000OO00Oo - 340 ) / 2 , ( O0OOO0OOoO0O - 255 ) / 2 ) )
  iIIIIii1 . title ( "下载版本" )
  iIIIIii1 . iconbitmap ( "icon.ico" )
  I11i1I1I = Listbox ( iIIIIii1 , listvariable = 0 , width = 10 , height = 2 )
  O00Oo000ooO0 = Label ( iIIIIii1 , text = O0oOO0o0 )
  O00Oo000ooO0 . pack ( )
  OoO0O00 = [ "官方源" , "Z站源(国内)" ]
  for IIiII in OoO0O00 :
   I11i1I1I . insert ( "end" , IIiII )
   if 80 - 80: I1Ii111 . I1IiI
   if 25 - 25: OOOo0 . ooO0OO000o / IiII . ooOo * OoOoOO00 . IiII1IiiIiI1
  I11i1I1I . pack ( )
  Oo0oOOo = Button ( iIIIIii1 , text = "确定下载源" , command = o0O )
  Oo0oOOo . pack ( )
  iII11i = Listbox ( iIIIIii1 , listvariable = 1 , width = 10 , height = 4 )
  if 58 - 58: ooO0OO000o * ooOo * Ooo00oOo00o / ooOo
  oO0o0OOOO = [ "1.19.3" , "1.19" , "1.18" , "1.17" ]
  for oO0o0O0OOOoo0 in oO0o0OOOO :
   iII11i . insert ( "end" , oO0o0O0OOOoo0 )
   if 68 - 68: IiII - ooOoO0o - IiII1IiiIiI1 - Ooo00oOo00o + Ooo0O
  iII11i . pack ( )
  if 10 - 10: iiiii % OO0O0O
  O00o0O00 = Button ( iIIIIii1 , text = "下载版本" , command = oo0OooOOo0 )
  if 34 - 34: o00O0oo
  O00o0O00 . pack ( )
  if 15 - 15: Ooo0O * o00O0oo * iIiiiI1IiI1I1 % i11iIiiIii % OOOo0 - ooOo
  iIIIIii1 . mainloop ( )
  if 68 - 68: ooOoO0o % ii1I . I1Ii111 . Ooo00oOo00o
O0O00o0OOO0 = Tk ( )
O0O00o0OOO0 . title ( 'AZ开服器' )
oo000OO00Oo = O0O00o0OOO0 . winfo_screenwidth ( )
O0OOO0OOoO0O = O0O00o0OOO0 . winfo_screenheight ( )
O0O00o0OOO0 . iconbitmap ( "icon.ico" )
O0O00o0OOO0 . geometry ( '%dx%d+%d+%d' % ( 370 , 255 , ( oo000OO00Oo - 370 ) / 2 , ( O0OOO0OOoO0O - 255 ) / 2 ) )
o0 = Button ( O0O00o0OOO0 , text = "下载版本" , command = i1I1iI )
iII11i = Listbox ( O0O00o0OOO0 , listvariable = 1 , width = 10 , height = 4 )
oO0o0OOOO = I1II1III11iii ( )
for oO0o0O0OOOoo0 in oO0o0OOOO :
 iII11i . insert ( "end" , oO0o0O0OOOoo0 )
 if 91 - 91: OO0O0O + ooOoO0o
i1i = Label ( O0O00o0OOO0 , text = "请用鼠标拖动选择分配的内存：" )
if 46 - 46: ooOoO0o % Ooo0O + OoOoOO00 . OOOo0 . OoOoOO00
i1i . pack ( )
IiII1I1i1i1ii = psutil . virtual_memory ( )
IiII1I1i1i1ii = u'%.4f ' % ( IiII1I1i1i1ii . total / 1024 / 1024 / 1024 )
oO00o0 = Scale (
 O0O00o0OOO0 , from_ = 1 , to = int ( float ( IiII1I1i1i1ii ) ) ,
 orient = HORIZONTAL , command = Ooo0OO0oOO
 )
if 55 - 55: iIiiiI1IiI1I1 + OO0O0O / OOOo0 * I1IiI - i11iIiiIii - iII111i
oO00o0 . pack ( )
oo = open ( "logs/memory.log" , "r" )
oo0Ooo0 = oo . read ( )
oo . close ( )
oO00o0 . set ( value = oo0Ooo0 )
ii1ii1ii = Label ( O0O00o0OOO0 , text = "请选择版本：" )
if 91 - 91: I1Ii111
ii1ii1ii . pack ( )
iII11i . pack ( )
iiIii = Button ( O0O00o0OOO0 , text = "启动" , command = o0oO0o00oo )
iiIii . pack ( )
o0 . pack ( )
O0O00o0OOO0 . mainloop ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3