import json
from time import sleep
from datetime import datetime


def Pricedata(status):
    if status == "read":
        # Open price databases to read
        with open(r"E:\Business\MIG\Codes\MIG-py\TeleBot\new_json_data.json", 'r', encoding="utf-8") as f1:
            filedata1 = json.loads(f1.read())
        return (filedata1, f1)
    elif status == "write":
        pass


def Senariodata(status):
    if status == "read":
        # Open the senario database read
        with open(r"E:\Business\MIG\Codes\MIG-py\TeleBot\manage_senario.json", 'r', encoding="utf-8") as f2:
            filedata2 = json.loads(f2.read())
        return (filedata2, f2)
    elif status == "write":
        pass


def Sharpdata(status):
    if status == "read":
        # Open the sharp database read
        with open(r"E:\Business\MIG\Codes\MIG-py\TeleBot\manage_sharp.json", 'r', encoding="utf-8") as f3:
            filedata3 = json.loads(f3.read())
        return (filedata3, f3)
    elif status == "write":
        # Open the sharp database write
        with open(r"E:\Business\MIG\Codes\MIG-py\TeleBot\manage_sharp.json", 'w', encoding="utf-8") as f3:
            filedata3 = json.loads(f3.read())
        return (filedata3, f3)

# Declare the senarios function


def senarios(Name, T, P):

    # call the data and files
    (filedata1, f1) = Pricedata("read")
    (filedata2, f2) = Senariodata("read")

    # Check the size of time span to number of records in DataBase
    # or senario name isn't a string object
    file_len = len(filedata1["ID"])
    if T > file_len:
        raise ValueError(
            'Number of required records is more than the file size')
    elif type(Name) != str:
        raise Exception('Senario name must be string')

    # Calculate max, min and desired price span from database
    prices = filedata1["ABSHODE FARDAII"][-T:]
    maxPrice = max(prices)
    minPrice = min(prices)
    SpanPrice = float(maxPrice.replace(',', '')) - \
        float(minPrice.replace(',', ''))

    # check the senario if recognize the sharp
    if SpanPrice >= P:
        f1.close()
        f2.close()
        return (minPrice, maxPrice)
    else:
        pass


def sharp(Name, T, P, Mov, tdelay=5):
    i = 1
    (minPrice, maxPrice) = senarios(Name, T, P)
    sharpdata = {}
    sharpdic = {"ID": [], "maxPrice": [], "minPrice": [], "lastPrice": []}
    sharpdata[Name] = sharpdic
    (filedata1, f1) = Pricedata("read")
    lastPrice = filedata1["ABSHODE FARDAII"][-1]
    f1.close()
    # Check the last price to get motivation price
    while lastPrice - minPrice < Mov:

        sleep(tdelay*60)  # Wait 5 min to get new value for the last price
        (filedata1, f1) = Pricedata("read")
        lastPrice = filedata1["ABSHODE FARDAII"][-1]
        f1.close()
        print("آلارم شماره: %d \
            از نوع سناریو: %s منقضی شد \n %s " % (sharpdic["ID"], sharpdic["senario"][0], datetime.now()))

    else:

        print("آلارم شماره: %d \
               از سناریو نوع: %s معتبر می باشد \
                \n بیشترین قیمت این شارپ: %d \
                \n کمترین قیمت این شارپ: %d \
                \n آخرین قیمت اعلام شده: %d \
                \n %s" % (Sharpdic["ID"], Sharpdic["senario"][0], maxPrice, minPrice, lastPrice, datetime.now()))


print(senarios("Ali", 20, 2000))
print("\n")
print(sharp())
