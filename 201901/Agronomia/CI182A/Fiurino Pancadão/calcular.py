def calcular(lista):
    resultado = {}
    sb = lista['phCaCl2'] + lista['cmolK'] + lista['cmolMg2+'] + lista['cmolNa+']
    resultado['sb'] = sb
    phc = lista['phCaCl2']
    resultado['phCaCl2'] = ('Condição a evitar' if (phc >= 6) else
                            'Muito alto' if (phc > 5.5) else
                            'Alto' if (5 <= phc <= 5.5) else
                            'Médio' if (4.5 <= phc < 5) else
                            'Baixo' if (4 <= phc < 4.5) else 'Muito baixo'
                            )
    pha = lista['phH2O']
    resultado['phH2O'] = ('Condição a evitar' if (pha >= 6.7) else
                          'Muito alto' if (pha > 6.2) else
                          'Alto' if (5.7 <= pha <= 6.2) else
                          'Médio' if (5.2 <= pha < 5.7) else
                          'Baixo' if (4.7 <= pha < 5.2) else 'Muito baixo'
                          )
    al = lista['cmolAl']
    resultado['cmolAl'] = ('Muito alto' if (al > 2.5) else
                           'Alto' if (1.6 <= al <= 2.5) else
                           'Médio' if (0.8 <= al < 1.6) else
                           'Baixo' if (0.3 <= al < 0.8) else 'Muito baixo'
                           )
    ca = lista['cmolCa2+']
    resultado['cmolCa2+'] = ('Muito alto' if (ca > 6) else
                             'Alto' if (2.1 <= ca <= 6) else
                             'Médio' if (1.1 <= ca < 2.1) else
                             'Baixo' if (0.5 <= ca < 1.1) else 'Muito baixo'
                             )
    mg = lista['cmolMg2+']
    resultado['cmolMg2+'] = ('Muito alto' if (mg > 2) else
                             'Alto' if (1.1 <= mg <= 2) else
                             'Médio' if (0.5 <= mg < 1.1) else
                             'Baixo' if (0.2 <= mg < 0.5) else 'Muito baixo'
                             )
    interK = lista['interK']
    k = lista['cmolK']
    if interK == "K trocável":
        resultado['potassio'] = ('Muito alto' if (k > 0.45) else
                                 'Alto' if (0.22 <= k <= 0.45) else
                                 'Médio' if (0.13 <= k < 0.22) else
                                 'Baixo' if (0.06 <= k < 0.13) else
                                 'Muito baixo'
                                 )
    elif interK == "Olerícolas, alfafa e café":
        resultado['potassio'] = ('Muito alto' if (k > 1.2) else
                                 'Alto' if (0.46 <= k <= 1.2) else
                                 'Médio' if (0.31 <= k < 0.46) else
                                 'Baixo' if (0.15 <= k < 0.31) else
                                 'Muito baixo'
                                 )
    argila = lista['argila']
    interP = lista['interP']
    p = lista['fosforo']
    if interP == "Argila":
        if argila < 250:
            resultado['fosforo'] = ('Condição a evitar' if p > 120 else
                                    'Muito alto' if 24 < p <= 120 else
                                    'Alto' if 19 <= p <= 24 else
                                    'Médio' if 13 <= p < 19 else
                                    'Baixo' if 6 <= p < 13 else 'Muito baixo'
                                    )
        elif 250 <= argila <= 400:
            resultado['fosforo'] = ('Condição a evitar' if p > 90 else
                                    'Muito alto' if 18 < p <= 90 else
                                    'Alto' if 13 <= p <= 18 else
                                    'Médio' if 9 <= p < 13 else
                                    'Baixo' if 4 <= p < 9 else 'Muito baixo'
                                    )
        elif argila > 400:
            resultado['fosforo'] = ('Condição a evitar' if p > 60 else
                                    'Muito alto' if 12 < p <= 60 else
                                    'Alto' if 10 <= p <= 12 else
                                    'Médio' if 7 <= p < 10 else
                                    'Baixo' if 3 <= p < 7 else 'Muito baixo'
                                    )
    elif interP == 'Olerícolas':
        resultado['fosforo'] = (
         'Condição a evitar' if p > 300 else
         'Muito alto' if 100 < p <= 300 else
         'Alto' if 51 <= p <= 100 else
         'Médio' if 21 <= p < 51 else
         'Baixo' if 8 <= p < 21 else 'Muito baixo'
        )
    elif interP == 'Florestais':
        resultado['fosforo'] = (
         'Condição a evitar' if p > 28 else
         'Muito alto' if 7 < p <= 28 else
         'Alto' if 6 <= p <= 7 else
         'Médio' if 4 <= p < 6 else
         'Baixo' if 2 <= p < 4 else 'Muito baixo'
        )
    elif interP == 'Pastagem':
        resultado['fosforo'] = (
         'Condição a evitar' if p > 40 else
         'Muito alto' if 10 < p <= 40 else
         'Alto' if 7 <= p <= 10 else
         'Médio' if 4 <= p < 7 else
         'Baixo' if 2 <= p < 4 else 'Muito baixo'
        )
    cult = lista['culturaDes']
    ant = lista['culturaAnt']

    produaux = lista['produtividade']
    if produaux == 'Menor que 8 ':
        produ = 7
    elif produaux == "Entre 8 e 12 ":
        produ = 10
    elif produaux == 'Entre 13 e 16 ':
        produ = 14
    elif produaux == 'Maior que 16 ':
        produ = 17

    if cult == "Milho":
        if ant == "Gramínea" and produ < 8:
            resultado['Adubação nitrogenada'] = "80 à 120 Kg/ha"
        elif ant == "Gramínea" and produ >= 8 and produ <= 12:
            resultado['Adubação nitrogenada'] = "121 à 180 Kg/ha"
        elif ant == "Gramínea" and produ >= 13 and produ <= 16:
            resultado['Adubação nitrogenada'] = "181 à 260 Kg/ha"
        elif ant == "Gramínea" and produ > 16:
            resultado['Adubação nitrogenada'] = "261 à 340 Kg/ha"
        elif ant == "Leguminosa" and produ < 8:
            resultado['Adubação nitrogenada'] = "20 à 60 Kg/ha"
        elif ant == "Leguminosa" and produ >= 8 and produ <= 12:
            resultado['Adubação nitrogenada'] = "61 à 120 Kg/ha"
        if produ < 8:
            if resultado['fosforo'] == "Muito baixo":
                resultado['Adubação fosfatada'] = "110 à 130 Kg/ha"
            elif resultado['fosforo'] == "Baixo":
                resultado['Adubação fosfatada'] = "90 à 110 Kg/ha"
            elif resultado['fosforo'] == "Médio":
                resultado['Adubação fosfatada'] = "70 à 90 Kg/ha"
            elif resultado['fosforo'] == "Alto":
                resultado['Adubação fosfatada'] = "50 à 70 Kg/ha"
            elif resultado['fosforo'] == "Muito alto":
                resultado['Adubação fosfatada'] = "30 à 50 Kg/ha"
            else:
                print("Condição  evitar ")
        if produ >= 8 and produ <= 12:
            if resultado['fosforo'] == "Muito baixo":
                print("Inviavél")
            elif resultado['fosforo'] == "Baixo":
                resultado['Adubação fosfatada'] = "111 à 130 Kg/ha"
            elif resultado['fosforo'] == "Médio":
                resultado['Adubação fosfatada'] = "91 à 110 Kg/ha"
            elif resultado['fosforo'] == "Alto":
                resultado['Adubação fosfatada'] = "71 à 90 Kg/ha"
            elif resultado['fosforo'] == "Muito alto":
                resultado['Adubação fosfatada'] = "51 à 70 Kg/ha"
            else:
                print("Condição  evitar ")

        if produ >= 13 and produ <= 16:
            if resultado['fosforo'] == "Muito baixo":
                print("Inviavél")
            elif resultado['fosforo'] == "Baixo":
                resultado['Adubação fosfatada'] = "131 à 150 Kg/ha"
            elif resultado['fosforo'] == "Médio":
                resultado['Adubação fosfatada'] = "111 à 130 Kg/ha"
            elif resultado['fosforo'] == "Alto":
                resultado['Adubação fosfatada'] = "91 à 110 Kg/ha"
            elif resultado['fosforo'] == "Muito alto":
                resultado['Adubação fosfatada'] = "71 à 90 Kg/ha"
            else:
                print("Condição  evitar ")
        if produ > 16:
            if resultado['fosforo'] == "Muito baixo":
                print("Inviavél")
            elif resultado['fosforo'] == "Baixo":
                print("Inviavél")
            elif resultado['fosforo'] == "Médio":
                resultado['Adubação fosfatada'] = "131 à 150 Kg/ha"
            elif resultado['fosforo'] == "Alto":
                resultado['Adubação fosfatada'] = "111 à 130 Kg/ha"
            elif resultado['fosforo'] == "Muito alto":
                resultado['Adubação fosfatada'] = "91 à 110 Kg/ha"
            else:
                print("Condição  evitar ")
        if produ < 8:
            if resultado['potassio'] == "Muito baixo":
                resultado['Adubação potássica'] = "110 à 130 Kg/ha"
            elif resultado['potassio'] == "Baixo":
                resultado['Adubação potássica'] = "70 à 100 Kg/ha"
            elif resultado['potassio'] == "Médio":
                resultado['Adubação potássica'] = "40 à 70 Kg/ha"
            elif resultado['potassio'] == "Alto":
                resultado['Adubação potássica'] = "20 à 40 Kg/ha"
            elif resultado['potassio'] == "Muito alto":
                resultado['Adubação potássica'] = "20 Kg/ha"
            else:
                print("Condição  evitar ")
        if produ >= 8 and produ <= 12:
            if resultado['potassio'] == "Muito baixo":
                print("Inviavél")
            elif resultado['potassio'] == "Baixo":
                resultado['Adubação potássica'] = "101 à 130 Kg/ha"
            elif resultado['potassio'] == "Médio":
                resultado['Adubação potássica'] = "71 à 100 Kg/ha"
            elif resultado['potassio'] == "Alto":
                resultado['Adubação potássica'] = "41 à 70 Kg/ha"
            elif resultado['potassio'] == "Muito alto":
                resultado['Adubação potássica'] = "20 à 41 Kg/ha"
            else:
                print("Condição  evitar ")

        if produ >= 13 and produ <= 16:
            if resultado['potassio'] == "Muito baixo":
                print("Inviavél")
            elif resultado['potassio'] == "Baixo":
                resultado['Adubação potássica'] = "131 à 160 Kg/ha"
            elif resultado['potassio'] == "Médio":
                resultado['Adubação potássica'] = "101 à 130 Kg/ha"
            elif resultado['potassio'] == "Alto":
                resultado['Adubação potássica'] = "71 à 100 Kg/ha"
            elif resultado['potassio'] == "Muito alto":
                resultado['Adubação potássica'] = "41 à 70 Kg/ha"
            else:
                print("Condição  evitar ")
        if produ > 16:
            if resultado['potassio'] == "Muito baixo":
                print("Inviavél")
            elif resultado['potassio'] == "Baixo":
                resultado['Adubação potássica'] = "161 à 190 Kg/ha"
            elif resultado['potassio'] == "Médio":
                resultado['Adubação potássica'] = "131 à 160 Kg/ha"
            elif resultado['potassio'] == "Alto":
                resultado['Adubação potássica'] = "101 à 130 Kg/ha"
            elif resultado['potassio'] == "Muito alto":
                resultado['Adubação potássica'] = "71 à 100 Kg/ha"
            else:
                print("Condição  evitar ")
    elif cult == "Soja":
        print("Não a necessidade de adubção nitrogenada na soja")
        if produ < 3:
            if resultado['fosforo'] == "Muito baixo":
                resultado['Adubação fosfatada'] = "81 à 100 Kg/ha"
            elif resultado['fosforo'] == "Baixo":
                resultado['Adubação fosfatada'] = "61 à 80 Kg/ha"
            elif resultado['fosforo'] == "Médio":
                resultado['Adubação fosfatada'] = "41 à 60 Kg/ha"
            elif resultado['fosforo'] == "Alto":
                resultado['Adubação fosfatada'] = "20 à 40 Kg/ha"
            elif resultado['fosforo'] == "Muito alto":
                resultado['Adubação fosfatada'] = "0 Kg/ha"
            else:
                print("Condição  evitar ")
        if produ >= 3 and produ <= 4:
            if resultado['fosforo'] == "Muito baixo":
                resultado['Adubação fosfatada'] = "101 à 120 Kg/ha"
            elif resultado['fosforo'] == "Baixo":
                resultado['Adubação fosfatada'] = "81 à 100 Kg/ha"
            elif resultado['fosforo'] == "Médio":
                resultado['Adubação fosfatada'] = "61 à 80 Kg/ha"
            elif resultado['fosforo'] == "Alto":
                resultado['Adubação fosfatada'] = "41 à 60 Kg/ha"
            elif resultado['fosforo'] == "Muito alto":
                resultado['Adubação fosfatada'] = "20 à 40 Kg/ha"
            else:
                print("Condição  evitar ")

        if produ > 4 and produ <= 5:
            if resultado['fosforo'] == "Muito baixo":
                print("Inviavél")
            elif resultado['fosforo'] == "Baixo":
                resultado['Adubação fosfatada'] = "101 à 120 Kg/ha"
            elif resultado['fosforo'] == "Médio":
                resultado['Adubação fosfatada'] = "81 à 100 Kg/ha"
            elif resultado['fosforo'] == "Alto":
                resultado['Adubação fosfatada'] = "61 à 80 Kg/ha"
            elif resultado['fosforo'] == "Muito alto":
                resultado['Adubação fosfatada'] = "41 à 60 Kg/ha"
            else:
                print("Condição  evitar ")
        if produ > 5:
            if resultado['fosforo'] == "Muito baixo":
                print("Inviavél")
            elif resultado['fosforo'] == "Baixo":
                print("Inviavél")
            elif resultado['fosforo'] == "Médio":
                resultado['Adubação fosfatada'] = "101 à 120 Kg/ha"
            elif resultado['fosforo'] == "Alto":
                resultado['Adubação fosfatada'] = "81 à 100 Kg/ha"
            elif resultado['fosforo'] == "Muito alto":
                resultado['Adubação fosfatada'] = "61 à 80 Kg/ha"
            else:
                print("Condição  evitar ")
        if produ < 3:
            if resultado['potassio'] == "Muito baixo":
                resultado['Adubação potássica'] = "81 à 100 Kg/ha"
            elif resultado['potassio'] == "Baixo":
                resultado['Adubação potássica'] = "61 à 80 Kg/ha"
            elif resultado['potassio'] == "Médio":
                resultado['Adubação potássica'] = "41 à 60 Kg/ha"
            elif resultado['potassio'] == "Alto":
                resultado['Adubação potássica'] = "20 à 40 Kg/ha"
            elif resultado['potassio'] == "Muito alto":
                resultado['Adubação potássica'] = "0 Kg/ha"
            else:
                print("Condição  evitar ")
        if produ >= 3 and produ <= 4:
            if resultado['potassio'] == "Muito baixo":
                resultado['Adubação fosfatada'] = "101 à 120 Kg/ha"
            elif resultado['potassio'] == "Baixo":
                resultado['Adubação potássica'] = "81 à 100 Kg/ha"
            elif resultado['potassio'] == "Médio":
                resultado['Adubação potássica'] = "61 à 80 Kg/ha"
            elif resultado['potassio'] == "Alto":
                resultado['Adubação potássica'] = "41 à 60 Kg/ha"
            elif resultado['potassio'] == "Muito alto":
                resultado['Adubação potássica'] = "20 à 40 Kg/ha"
            else:
                print("Condição  evitar ")

        if produ > 4 and produ <= 5:
            if resultado['potassio'] == "Muito baixo":
                print("Inviavél")
            elif resultado['potassio'] == "Baixo":
                resultado['Adubação potássica'] = "101 à 120 Kg/ha"
            elif resultado['potassio'] == "Médio":
                resultado['Adubação potássica'] = "81 à 100 Kg/ha"
            elif resultado['potassio'] == "Alto":
                resultado['Adubação potássica'] = "61 à 80 Kg/ha"
            elif resultado['potassio'] == "Muito alto":
                resultado['Adubação potássica'] = "41 à 60 Kg/ha"
            else:
                print("Condição  evitar ")
        if produ > 5:
            if resultado['potassio'] == "Muito baixo":
                print("Inviavél")
            elif resultado['potassio'] == "Baixo":
                print("Inviavél")
            elif resultado['potassio'] == "Médio":
                resultado['Adubação potássica'] = "101 à 120 Kg/ha"
            elif resultado['potassio'] == "Alto":
                resultado['Adubação potássica'] = "81 à 100 Kg/ha"
            elif resultado['potassio'] == "Muito alto":
                resultado['Adubação potássica'] = "61 à 80 Kg/ha"
            else:
                print("Condição  evitar ")

    return resultado

    # sb = ca + k + mg + na
    # ctc = sb + h + al
    # m = 100*(al/ctc)
    # v = ( sb * 100)/ctc
    # t = sb + al
# =IF(C6>2.5,"Muito alto",IF(AND(C6>=1.6,C6<=2.5),"Alto",IF(AND(C6>=0.8,C6<1.6)
# ,"Médio",IF(AND(C6>=0.3,C6<0.8),"Baixo","Muito Baixo"))))

# dict_keys(['culturaDes', 'culturaAnt', 'produtividade', 'interP',
# 'interK', 'phCaCl2', 'phH2O', 'cmolAl', 'cmolH+', 'cmolCa2+', 'cmolMg2+',
# 'cmolNa+', 'cmolK', 'fosforo', 'argila', 'matOrganica', 'carbOrganico'])
# carga/dm⁻³    Mg²⁺     Na²⁺    t.ha⁻¹
