;ControlFocus()��������ʶ��Window���ڡ�WinWait()����10�������ڵȴ����ڵ���ʾ�����÷���WebDriver ���ṩ��implicitly_wait()���ơ�ControlSetText()�������ļ���������������뱾���ļ���·����
;�����Sleep()������Python��timeģ���ṩ��Sleep()�����÷�һ�������������Ժ���Ϊ��λ��Sleep(2000)��ʾ�̶�����2000���롣ControlClick()���ڵ���ϴ������еġ��򿪡���ť��

;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("�ļ��ϴ�","","Edit1")

; Wait 10 seconds for the Upload window to appear
  WinWait("[CLASS:#32770]","",10)

; Set the File name text on the Edit field
ControlSetText("�ļ��ϴ�","","Edit1","C:\Users\admin\Desktop\������ũ_7-27Bug��Ӧ���.xlsx")
Sleep(2000)

; Click on the Open button
ControlClick("�ļ��ϴ�","","Button1");

