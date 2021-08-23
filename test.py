import pyupbit

access = "0JUha51dikDvTPPrlzggeoYAbW0uxvxbmfui4O5D"
secret = "GxuqNVfasqffaQToK5mwiWx4zalp41he1dnEaR2j"

upbit = pyupbit.upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))
print(upbit.get_balance("KRW"))
