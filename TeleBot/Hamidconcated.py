import json
from time import sleep
from datetime import datetime, timedelta

# Open price databases to read
with open(r"E:\Business\MIG\Codes\MIG-py\TeleBot\new_json_data.json", 'r', encoding="utf-8") as f1:
    filedata1 = json.loads(f1.read())

# Open the senario database read
with open(r"E:\Business\MIG\Codes\MIG-py\TeleBot\manage_senario.json", 'r', encoding="utf-8") as f2:
    filedata2 = json.loads(f2.read())

# open the prices files
IDlist = filedata1["ID"]
abshodelist = filedata1["ABSHODE FARDAII"]
timelist = filedata1["TIME"]

# convert time string to time object
timeobject = len(timelist) * [0]
for id, t in enumerate(timelist):
    timeobject[id] = datetime.strptime(t, '%Y-%m-%d %H:%M:%S')

senario_namelist = filedata2["senario_name"]

# notice that the type of elements in this list is string! not INTEGER
senario_Plist = [float(i) for i in filedata2["senario_P"]]

# notice that the type of elements in this list is string! not INTEGER
senario_Tlist = [float(i) for i in filedata2["senario_T"]]

# sharps = {}
# for name in senario_namelist:
#    sharps[name] =

# Initial varialbes for prices and
idT = len(senario_Tlist) * [0]
prices = idT[:]
maxprices = idT[:]
minprices = idT[:]
spanprices = idT[:]
lastprices = idT[:]

pricemotivation = 1000  # must get from json file

# determine the time id from time span for all senario_T and prices
for i, item in enumerate(idT):
    for id, tobj in enumerate(timeobject[::-1], start=1):

        timediff = timeobject[-1] - tobj
        timediff2 = timeobject[-1] - timeobject[-2]
        if timediff.total_seconds() <= timedelta(seconds=senario_Tlist[i]).total_seconds():
            idT[i] = -id-1
        elif timediff2.total_seconds() > timedelta(seconds=senario_Tlist[i]).total_seconds():
            idT[i] = -2
    prices[i] = abshodelist[idT[i]:]
    maxprices[i] = max(prices[i])
    minprices[i] = min(prices[i])
    spanprices[i] = float(maxprices[i].replace(',', '')) - \
        float(minprices[i].replace(',', ''))
    lastprices[i] = float(abshodelist[-1].replace(',', ''))

    if spanprices[i] >= senario_Plist[i]:
        # maxprices[i] must insert into json file
        # minprices[i] must insert into json file
        # lastprices[i] must insert into json file

        if lastprices[i] - float(minprices[i].replace(',', '')) > pricemotivation:
            print("آلارم شماره: %d \
               از سناریو نوع: %s معتبر می باشد \
                \n بیشترین قیمت این شارپ: %d \
                \n کمترین قیمت این شارپ: %d \
                \n آخرین قیمت اعلام شده: %d \
                \n %s" % (Sharpdic["ID"], Sharpdic["senario"][0], maxPrice, minPrice, lastPrice, datetime.now()))
        else:
            print("آلارم شماره: %d \
            از نوع سناریو: %s منقضی شد \n %s " % (sharpdic["ID"], sharpdic["senario"][0], datetime.now()))
