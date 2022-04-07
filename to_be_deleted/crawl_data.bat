set root=D:\Users\Administrator\Anaconda3_6

call %root%\Scripts\activate.bat %root%

cd C:\batfile\set up server\crawl facebook
autopep8 -i crawl_thongtin_json_5.py
call python crawl_thongtin_json_5.py
PAUSE
