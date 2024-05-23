# import qrcode
#
# son = 'https://www.instagram.com/hm_son7/'
# qr = qrcode.make((son))
# qr.save('son.png')
#
#
# from gtts import gTTS
# text = '오늘이 지나면 내일은 금요일  소리질러! 비트코인도 오른다!'
# a = gTTS(text,lang='ko')
# a.save(('result.mp3'))

import yfinance

t =  yfinance.Ticker("NVDA")
stock = t.history(period='5d')
current = stock['Close'].iloc[-1]
print(stock)
print(current)
