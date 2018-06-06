WinWait("CLASS:#32770","",5)
ControlFocus("打开", "", "Edit1")
WinWait("[CLASS:#32770]", "", 10)
ControlSetText("打开" ,"", "Edit1", 'E:\ws版本\iWSNII.WS.Firmware.1.5.3.2.bin')
Sleep(200)
ControlClick("打开", "","Button1");
