from datetime import datetime

file = open('./chap07/access.log', 'a', encoding='UTF-8')
file.write(f'{datetime.now()}\n')
file.close()

# with open('./chap07/access.log', 'a', encoding='UTF-8') as file:
#     file.write(f'{datetime.now()}\n')
print('現在時刻をファイルに保存しました。')
