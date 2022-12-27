# аналог POSIX-утилиты head для показa строк из файлов
def gen_head(file):
    with open(file,'r') as file:
        for line in file:
            yield line
            
def head(file, lines=10):
    gen = gen_head(file)
    for i in range(lines):
        print(next(gen))

head("text.txt")