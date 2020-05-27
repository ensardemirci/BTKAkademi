word = input('Kelimeyi giriniz: ')
tekrar = int(input('Kaç kere tekrar edilsin: '))

def rep(word,tekrar):
    word = word + '\n'
    print(f'{word*tekrar}')
rep(word,tekrar)
