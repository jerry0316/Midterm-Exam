animals=['rat','ox','tiger','rabbit','dragon','snake','horse','sheep','monkey','rooster','dog','pig']
year1=int(input('請輸入出生年份:'))
year2=year1-4
if year2>=12:
    year3=year2%12
else:
    year3=year2
print(animals[year3])