import smtplib, time
from email.mime.text import MIMEText

smtp = smtplib.SMTP('smtp.office365.com', 587)
print("")
while(True):
    
    # smtp 설정
    smtp.ehlo()      # say Hello
    smtp.starttls()  # TLS 사용시 필요
    smtp.login('scrpa01@sorincorp.com', 'Rhkdqhr76*')
    
    msg = MIMEText('본문 테스트 메시지')
    msg['Subject'] = '테스트'
    sender = 'scrpa01@sorincorp.com'
    receiver = 'scrpa01@sorincorp.com'
    #메일 보내기
    smtp.sendmail(sender,receiver, msg.as_string())
    # 딜레이3시간
    time.sleep(3600 * 3)