import datetime
import pytz

# d = datetime.date(2016, 7, 24)
# print(d)

tday = datetime.date.today()
# print(tday)
# print(tday.day)
# print(tday.year)
# print(tday.month)
#
# # monday = 0 sunday = 6
# print(tday.weekday())
# # monday = 1 sunday = 7
# print(tday.isoweekday())

# mengukur waktu yang akan di tentukan di hari selanjutnya atau sebelumnya
tdelta = datetime.timedelta(hours=12)
# tdelta = datetime.timedelta(days=12)
# print(tday + tdelta)
# print(tday - tdelta)
#
# bday = datetime.date(2017, 10, 31)
# till_bday = bday - tday
# print(till_bday.days)
# print(till_bday.total_seconds())
#
# t = datetime.time(9, 30, 45, 100000)
# print(t.hour)
#
# dt = datetime.datetime(2017, 10, 31, 20, 30, 45, 100000)
# print(dt)
# print(dt.year)
# print(dt + tdelta)

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)


#menggunakan library pytz
dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('Asia/Jakarta'))
print(dt_mtn)

# # melihat semua timezone yg ada
# for tz in pytz.all_timezones:
#     print(tz)

dt_jakarta = datetime.datetime.now(tz=pytz.timezone('Asia/Jakarta'))
print(dt_jakarta.strftime('%B %d, %Y'))

# konversi string waktu ke waktu digital
dt_str = 'September 23, 2017'
dtz = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dtz)