telDic = {"ivanov":1191630, "petrov":3892818, (3,):3}
print(type(telDic),telDic)
#hash(telDic)
print(telDic.values())
print(telDic.keys())
print(telDic.items())

print(telDic.get("ivanov"))
print(telDic.pop("petrov"))
print(telDic)
telDic["sidorov"] = 1123456
print(telDic)
print(telDic.popitem())