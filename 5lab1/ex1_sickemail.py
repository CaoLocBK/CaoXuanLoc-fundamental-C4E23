from gmail import GMail, Message
from random import randint, random, randrange, choice
from time import asctime
# from datetime import timezone, date, now
import datetime as dt
hour = dt.datetime.now().hour
print(hour)

while True:
    if hour == 7:
        gmail = GMail('pythonmen123@gmail.com',"12345678aA")
        template1 = "Chào sếp, hôm thức dậy em thấy {{symptom}}, bác sĩ nói rằng em bị {{sick}}"
        template = '''
        <p>Ch&agrave;o Sếp,</p>
        <p>H&ocirc;m nay em ngủ dậy, thấy {{symptom}}, b&aacute;c sỹ bảo em bị {{sick}}.</p>
        <p>Sếp cho em nghỉ l&agrave;m nh&eacute; :V</p>
        <p>Nh&acirc;n vi&ecirc;n của sếp</p>
        '''
        s_list = ["cảm cúm","cảm lạnh","tiêu chảy"]
        symptom = "đau đầu"

        ntent = template.replace("{{sick}}",choice(s_list)).replace("{{symptom}}",symptom)
        message = Message('Đơn xin nghỉ làm ngày hôm nay',to="cookiedeptraivl@gmail.com",html=ntent)
        gmail.send(message)
        break
