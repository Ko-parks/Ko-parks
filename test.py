import pyupbit

access = "0"
secret = "0"

upbit = pyupbit.upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))
print(upbit.get_balance("KRW"))
