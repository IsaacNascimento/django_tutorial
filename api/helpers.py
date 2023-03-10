def orderListByDescrent(list):
    tamanhoLista = len(list)
    for i in range(tamanhoLista):
        for j in range(0, tamanhoLista - i - 1):
            if list[j].id < list[j + 1].id:
                (list[j], list[j + 1]) = (list[j + 1], list[j])