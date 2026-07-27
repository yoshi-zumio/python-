lang = ['Python', 'Guido van Rossum', 1991]

match lang:
    case ['Python', author, created]:
        print(f'Pythonは{author}によって{created}年に作られました。')
    case ['Ruby', author, created]:
        print(f'Rubyが登場したのは{created}年、作者は{author}です。')
