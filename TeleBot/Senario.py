import json
import re


# Declare the senarios fun

def senarios(Name, T, P, PM):

    with open(r"E:\Business\MIG\Codes\MIG-py\TeleBot\new_json_data.json", 'r', encoding="utf-8") as f:
        file = f.read()
        filedata1 = json.loads(file)
    #  with open("manage_senario.json", 'r', encoding="utf-8") as f:
    #    filedata2 = json.loads(f.read())
    file_len = len(filedata1["ID"])


senarios(1, 1, 2, 3)
