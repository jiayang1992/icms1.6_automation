;ControlFocus()方法用于识别Window窗口。WinWait()设置10秒钟用于等待窗口的显示，其用法与WebDriver 所提供的implicitly_wait()类似。ControlSetText()用于向“文件名”输入框内输入本地文件的路径。
;这里的Sleep()方法与Python中time模块提供的Sleep()方法用法一样，不过它是以毫秒为单位，Sleep(2000)表示固定休眠2000毫秒。ControlClick()用于点击上传窗口中的“打开”按钮。

;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("文件上传","","Edit1")

; Wait 10 seconds for the Upload window to appear
  WinWait("[CLASS:#32770]","",10)

; Set the File name text on the Edit field
ControlSetText("文件上传","","Edit1","C:\Users\admin\Desktop\云澜三农_7-27Bug反应情况.xlsx")
Sleep(2000)

; Click on the Open button
ControlClick("文件上传","","Button1");

