with open('./chap07/input.png', 'rb') as reader, \
     open('./chap07/output.png', 'wb') as writer:

    # while True:
    #     d = reader.read(1)
    #     if len(d) == 0:
    #         break
    #     writer.write(d)

    while d := reader.read(1):
        writer.write(d)
