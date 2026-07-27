drink = 'ビール'

match drink:
    case 'ビール' | '日本酒' | 'ワイン':
        print('醸造酒です。')
    case 'ウイスキー' | 'ブランデー' | 'ジン':
        print('蒸留酒です。')
