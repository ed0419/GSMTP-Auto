from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
from pathlib import Path
import smtplib, json

with open('settings.json','r',encoding='utf8') as jFile:
    jdata = json.load(jFile)

content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "中部資電寒訓資料測試"  #郵件標題
content["from"] = "s1060015@st.fcjh.tc.edu.tw"  #寄件者
content["to"] = "genden80@gmail.com" #收件者
content.attach(MIMEText("Demo python send email"))  #郵件內容
content.attach(MIMEImage(Path("112314.jpg").read_bytes()))  # 郵件圖片內容

template = Template(Path("success_template.html").read_text())
body = template.substitute({ "user": "Mike" })
content.attach(MIMEText(body, "html"))  # HTML郵件內容

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("s1060015@st.fcjh.tc.edu.tw", jdata['GMAILTOKEN'])  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件
        print("Complete!")
    except Exception as e:
        print("Error message: ", e)