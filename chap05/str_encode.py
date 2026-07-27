data = 'こんにちは'
encoded = data.encode('shift-jis')
print(encoded)
print(encoded.decode('shift-jis'))
# print(encoded.decode('euc-jp', 'replace'))
