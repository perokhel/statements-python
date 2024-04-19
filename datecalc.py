from datetime import  datetime


def mdy_to_ymd(d):
    return datetime.strptime(d, '%b %d').strftime('%Y-%m-%d')


print(mdy_to_ymd('Mar 12'))
