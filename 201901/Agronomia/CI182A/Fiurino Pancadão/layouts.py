from importacoes import sg

# Layout do menu principal
layoutInicial = [
 [sg.Text('Bem-vindo!'),
  # Iniciar um novo cálculo
  sg.Button('Novo cálculo'),
  # Informações sobre o aplicativo
  sg.Button('Sobre')]]


# Layout da janela de cálculo
# Contém: etiquetas de cada item, formulário, botões de ação

layoutCalculo = [

 # Etiqueta da cultura desejada
 [sg.Text("Cultura desejada:",
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputCombo(
                ['Milho', 'Soja'],
                default_value="Milho",
                size=(35, 1),
                key='culturaDes')],

 # Etiqueta da cultura anterior
 [sg.Text("Cultura anterior:",
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputCombo([
           'Gramínea', 'Leguminosa'],
           default_value="Gramínea",
           size=(35, 1),
           key='culturaAnt')],

 # Etiqueta da produtividade esperada
 [sg.Text("Produtividade esperada em t.ha⁻¹:",
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputCombo([
           'Menor que 8 ', 'Entre 8 e 12 ',
           'Entre 13 e 16 ', 'Maior que 16 '],
           default_value="Menor que 8 ",
           size=(35, 1), key='produtividade')],

 # Etiqueta da interpretação do fosforo
 [sg.Text('Valor de interpretação do fósforo:',
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputCombo(['Pastagem', 'Argila', 'Olerícolas', 'Florestais'],
                default_value="Pastagem",
                size=(35, 1), key='interP')],

 # Etiqueta da interpretação do potassio
 [sg.Text('Valor de interpretação do potássio:',
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputCombo([
           'K trocável', 'Olerícolas, alfafa e café'],
           default_value="K trocável",
           size=(35, 1), key='interK')],

 # Etiqueta do pH do CaCl2
 [sg.Text('pH em CaCl2:',
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputText(default_text='0.00', size=(35, 1), key='phCaCl2')],

 # Etiqueta do pH do H2O
 [sg.Text('pH em H2O:',
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputText(default_text='0.00', size=(35, 1), key='phH2O')],

 # Etiqueta do centimol do aluminio
 [sg.Text('Centimol de carga/dm⁻³ do alumínio:',
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputText(default_text='0.000000', size=(35, 1), key='cmolAl')],

 # Etiqueta do centimol do H+
 [sg.Text('Centimol de carga/dm⁻³ do H+:',
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputText(default_text='0.000000', size=(35, 1), key='cmolH+')],

 # Etiqueta do centimol do Ca2+
 [sg.Text('Centimol de carga/dm⁻³ do Ca²⁺:',
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputText(default_text='0.000000', size=(35, 1), key='cmolCa2+')],

 # Etiqueta do centimol do Mg2+
 [sg.Text('Centimol de carga/dm⁻³ do Mg²⁺:',
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputText(default_text='0.000000', size=(35, 1), key='cmolMg2+')],

 # Etiqueta do centimol do Na2+
 [sg.Text('Centimol de carga/dm⁻³ do Na²⁺:',
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputText(default_text='0.000000', size=(35, 1), key='cmolNa+')],

 # Etiqueta do potassio
 [sg.Text('Centimol de carga/dm⁻³ do Potássio:',
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputText(default_text='0.000000', size=(35, 1), key='cmolK')],

 # Etiqueta do fosforo
 [sg.Text('Fósforo (mg/dm⁻³):',
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputText(default_text='0.0', size=(35, 1), key='fosforo')],

 # Etiqueta da argila
 [sg.Text('Porcentagem de argila:',
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputText(
               default_text='0.00', size=(35, 1),
               key='argila'), sg.Text('%')],

 # Etiqueta da matéria organica
 [sg.Text('Matéria orgânica:',
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputText(default_text='0.00', size=(35, 1),
               key='matOrganica'), sg.Text('%')],

 # Etiqueta do carbono organico
 [sg.Text('Carbono orgânico (g/dm⁻³):',
          # Tamanho da etiqueta, criação do input
          size=(35, 1)),
  sg.InputText(default_text='0.00', size=(35, 1), key='carbOrganico')],


 #####################
 # FIM DO FORMULÁRIO #
 #####################

 # Botões para calcular, limpar o formulário e sair do programa
 [sg.Submit('Calcular'),
  sg.Button('Limpar'),
  sg.Exit('Sair')]]

coluna = [
          [sg.Text('Cultura desejada: ',
                   text_color='white',
                   size=(35, 1),
                   background_color='green'),
           sg.Input('col input 1')],
          [sg.Text('Cultura Anterior: ',
                   text_color='white',
                   size=(35, 1),
                   background_color='green'),
           sg.Input('col input 1')],
          [sg.Text('Produtividade esperada em t.ha⁻¹: ',
                   size=(35, 1),
                   text_color='white',
                   background_color='green'),
           sg.Input('col input 2')],
          [sg.Text('Valor de interpretação do fósforo: ',
                   size=(35, 1),
                   text_color='white',
                   background_color='green'),
           sg.Input('col input 2')],
          [sg.Text('Valor de interpretação do potássio: ',
                   size=(35, 1),
                   text_color='white',
                   background_color='green'),
           sg.Input('col input 2')],
          [sg.Text('pH em CaCl2: ',
                   size=(35, 1),
                   text_color='white',
                   background_color='green'),
           sg.Input('col input 2')],
          [sg.Text('pH em H20: ',
                   size=(35, 1),
                   text_color='white',
                   background_color='green'),
           sg.Input('col input 2')],
          [sg.Text('Centimol de carga/dm⁻³ do alumínio: ',
                   size=(35, 1),
                   text_color='white',
                   background_color='green'),
           sg.Input('col input 2')],
          [sg.Text('Centimol de carga/dm⁻³ do H⁺: ',
                   size=(35, 1),
                   text_color='white',
                   background_color='green'),
           sg.Input('col input 2')],
          [sg.Text('Centimol de carga/dm⁻³ do Ca²⁺: ',
                   size=(35, 1),
                   text_color='white',
                   background_color='green'),
           sg.Input('col input 2')],
          [sg.Text('Centimol de carga/dm⁻³ do Mg²⁺: ',
                   size=(35, 1),
                   text_color='white',
                   background_color='green'),
           sg.Input('col input 2')],
          [sg.Text('Centimol de carga/dm⁻³ do Na²⁺: ',
                   size=(35, 1),
                   text_color='white',
                   background_color='green'),
           sg.Input('col input 2')],
          [sg.Text('Centimol de carga/dm⁻³ do K⁺: ',
                   size=(35, 1),
                   text_color='white',
                   background_color='green'),
           sg.Input('col input 2')],
          [sg.Text('Fósforo: (mg/dm⁻³)',
                   size=(35, 1),
                   text_color='white',
                   background_color='green'),
           sg.Input('col input 2')],
          [sg.Text('Porcentagem de argila: ',
                   size=(35, 1),
                   text_color='white',
                   background_color='green'),
           sg.Input('col input 2')],
          [sg.Text('Matéria orgânica: ',
                   size=(35, 1),
                   text_color='White',
                   background_color='green'),
           sg.Input('col input 2')],
          [sg.Text('Carbono orgânico (g/dm⁻³): ',
                   size=(35, 1),
                   text_color='white',
                   background_color='green'),
           sg.Input()],
           ]

layoutResultados = [
      [sg.Column(coluna)],
      [sg.OK()]]
