def leiadinh(fras):
    while True:
        vali = input(fras).strip().replace(',', '.')
        if not vali.isalpha() and len(vali) > 0:
            return float(vali)
        else:
            print('\033[31m!ERRO! Por favor digite um preço válido\033[m')






