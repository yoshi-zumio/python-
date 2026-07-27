import re

msg = '電話番号は080-111-9999です！'
ptn = re.compile(r'(\d{2,4})-(\d{2,4})-(\d{4})')

# result = ptn.search(msg)
# if result:

if result := ptn.search(msg):
    print(result.group(0))
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))
else:
    print('見つかりませんでした！')
