import itchat
from rest_api.HuobiServices import *
import pandas as pd
import json
import time

itchat.auto_login(hotReload=True)

xh_symbol = ['btcusdt']
xh_period = ['5min']
upper_threshold = 10200
lower_threshold = 9600

while True:
    for symbol in xh_symbol:
        for period in xh_period:
            data = get_kline(symbol, period)

            df = pd.read_json(json.dumps(data['data']))

            def timestamp_to_datetime(s):
                timeArray = time.localtime(s)
                return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

            df.id = pd.to_datetime(df.id.map(timestamp_to_datetime))

            amount_ratio = df.amount[1] / df.amount[2:].mean()
            upper = df.high[1]
            lower = df.low[1]
            span = upper - lower
            var = df.high[0] - df.low[0]

            sgn = 0

            if amount_ratio >= 2:
                amount_msg = f'{symbol} {period} amount is over {amount_ratio} times'
                sgn += 1
            elif amount_ratio <= 0.5:
                amount_msg = f'{symbol} {period} amount reaches {amount_ratio} times'
                sgn += 1
            else:
                amount_msg = amout_ratio

            if upper >= upper_threshold:
                upper_msg = f'{symbol} {period} high price is over {upper}'
                sgn += 1
            else:
                amount_msg = upper

            if lower <= lower_threshold:
                lower_msg = f'{symbol} {period} low price reaches {lower}'
                sgn += 1
            else:
                lower_msg = lower

            if span >= 200:
                span_msg = f'{symbol} {period} span is {span}'
                sgn += 1
            else:
                span_msg = span

            if var >= 100:
                var_msg = f'{symbol} {period} var is {var}'
                sgn += 1
            else:
                var_msg = var

            msg = {'amount_msg': amount_msg, 'upper_msg': upper_msg, 'lower_msg': lower_msg, 'span_msg', span_msg, 'var_msg': var_msg}

            if sgn > 0:
                itchat.send_msg(msg=json.dumps(msg), toUserName='muzhen')


            time.sleep(180)
