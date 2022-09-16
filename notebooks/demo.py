# -*- coding: utf-8 -*- 

def imprime_a():
    print('a')

def imprime_b():
    print('b')

# imprime_b é chamado quando o arquivo é importado.
imprime_b()

if __name__ == '__main__':
    # imprime_a é chamado quando o arquivo é executado diretamente
    imprime_a()