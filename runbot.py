from mm import *
from utils import *

print('runbot')
data = fetch_data(100, 'histoday', 'BTC')

signal = mm_job('BTC', 'histoday', data)
print(signal)

get_bal()
#go long and send a message to telegram
if signal == 'up':
#telegram_bot_sendtext('XBT: bot going long')
    i=0

#the other thing
if signal == 'down':
#telegram_bot_sendtext('XBT: bot closing long, standing by for next entry')
    i=0
