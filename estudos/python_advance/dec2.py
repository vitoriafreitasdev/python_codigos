
def ola(func):
    def wrapper(*args, **kargs):
        print("Ola")
        res = func(*args, **kargs)
        print("Tchau")
        print(res)
        
    return wrapper
        
@ola
def saudacao(nome):
    print(nome)
    return nome

saudacao("Vitória")