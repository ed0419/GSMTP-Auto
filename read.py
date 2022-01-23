import csv
from sendmail import send2
# 開啟 CSV 檔案
with open('test', newline='', encoding = 'utf-8') as csvfile:

    # 以冒號分隔欄位，讀取檔案內容 , delimiter='  '
    rows_stu = list(csv.reader(csvfile))
    with open('mc25', newline='', encoding = 'utf-8') as csvfile_acc:
        rows_acc = list(csv.reader(csvfile_acc))

        # 以迴圈輸出每一列
        for i in range(len(rows_stu)):
            tomail = rows_stu[i][0] 
            name = rows_stu[i][1] 
            mcemail = rows_acc[i][0] 
            mcpass = rows_acc[i][1]
            print(tomail,name,mcemail,mcpass)
            send2(tomail,name,mcemail,mcpass)
            