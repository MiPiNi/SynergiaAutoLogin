from datetime import datetime, timedelta
from threading import Timer
import requests

x=datetime.today()

dzien = int(input('Za ile dni?: '))
godzina = int(input('O ktorej godzinie?(minute podaj pozniej): '))
minuta = int(input('W ktorej minucie?: '))

y = x.replace(day=x.day, hour=godzina, minute=minuta, second=0, microsecond=0) + timedelta(days=dzien)
delta_t=y-x

secs=delta_t.total_seconds()

def do_login():
    
    session = requests.session()
    session.get('https://api.librus.pl/OAuth/Authorization?client_id=46&response_type=code&scope=mydata')
    session.post('https://api.librus.pl/OAuth/Authorization/Grant?client_id=46', data={
        'action': 'login',
        'login': login,
        'pass': password
    })
    session.get('https://api.librus.pl/OAuth/Authorization/Grant?client_id=46')
    print(session.get('https://synergia.librus.pl/uczen/index').text)
    input('Wcisnij ENTER aby sie wylogować...')

login = input('Login: ')
password = input('Password: ')

t = Timer(secs, do_login)
t.start()
