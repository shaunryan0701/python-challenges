from datetime import datetime

dt = datetime(2020,11,4, 14, 53, 0)
print(dt.strftime('%Y/%m/%d %H:%M:%S'))
print(dt.strftime('%Y/%B/%d %H:%M:%S'))
print(dt.strftime('%a, %Y %b %d'))