#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import shlex
import subprocess
import os


# função escolhe perguntas sem respostas
def prova(Questoes_prova, qtd_N1, qtd_N2, qtd_N3, instituicao, data_prova):
    prova = []

    # Pega a quantidade de questões solicitadas
    while(qtd_N1 > 0):
        possiv_quest = random.randint(0, len(Questoes_prova)-1)
        if(Questoes_prova[possiv_quest][0] == [1] and not(Questoes_prova[possiv_quest][1] in prova)):
            prova.append(Questoes_prova[possiv_quest][1])
            qtd_N1 = qtd_N1 - 1
    while(qtd_N2 > 0):
        possiv_quest = random.randint(0, len(Questoes_prova)-1)
        if(Questoes_prova[possiv_quest][0] == [2] and not(Questoes_prova[possiv_quest][1] in prova)):
            prova.append(Questoes_prova[possiv_quest][1])
            qtd_N2 = qtd_N2 - 1
    while(qtd_N3 > 0):
        possiv_quest = random.randint(0, len(Questoes_prova)-1)
        if(Questoes_prova[possiv_quest][0] == [3] and not(Questoes_prova[possiv_quest][1] in prova)):
            prova.append(Questoes_prova[possiv_quest][1])
            qtd_N3 = qtd_N3 - 1
    armazenador_arquivo = r'''\documentclass{article}
    \usepackage[utf8]{inputenc}
    \usepackage[T1]{fontenc}
    \begin{document}
    ... P \& B
    \textbf{\huge %(school)s \\}
    \vspace{1cm}
    \textbf{\Large %(title)s \\}
    ...
    \end{document}
    '''
    # Usamos um modelo
    with open("avaliacao.tex", "r", encoding="utf-8") as f:
        armazenador_arquivo = f.read()
    # trocamos no latex os valores
    avaliacao_modificada = {'university': instituicao, 'class': "Cálculo 1 ",
                            'date': data_prova, 'question1': prova[0][0],
                            'question2': (prova[1][0]),
                            # Criamos um arquivo novo com o resultado da mudança
                            'question3': prova[2][0],
                            'question4': (prova[3][0]),
                            'question5': (prova[4][0]),
                            'question6': (prova[5][0]),
                            'question7': (prova[6][0]),
                            'question8': (prova[7][0]),
                            'question9': (prova[8][0]),
                            'question10': prova[9][0]}
    print(armazenador_arquivo % avaliacao_modificada)

    with open('cover.tex', 'w', encoding="utf-8") as f:
        f.write(armazenador_arquivo % avaliacao_modificada)
    # compilamos o arquivo novo (preservando o modelo original)ss
    cmd = ['pdflatex', '-interaction', 'nonstopmode', 'cover.tex']
    proc = subprocess.Popen(cmd)
    proc.communicate()
    retcode = proc.returncode
    if not retcode == 0:
        os.unlink('cover.pdf')
        raise ValueError('Error {} executing command: {}'.format(
            retcode, ' '.join(cmd)))
    os.unlink('cover.tex')
    os.unlink('cover.log')

# função que pega exercícios e coloca as respostas no final


def lista(Questoes_prova):
    prova = []
    lista_respostas = []
    # Pega a quantidade de questões que voce pediu com as respostas no final
    while qtd_N1 > 0:
        possiv_quest = random.randint(0, len(Questoes_prova)-1)
        if (Questoes_prova[possiv_quest][0] == 1 and not(Questoes_prova[possiv_quest][1] in prova)):
            lista_perguntas.append(Questoes_prova[possiv_quest][1])
            lista_respostas.append(Questoes_prova[possiv_quest][2])
            qtd_N1 -= 1
    while qtd_N2 > 0:
        possiv_quest = random.randint(0, len(Questoes_prova)-1)
        if (Questoes_prova[possiv_quest][0] == 2 and not(Questoes_prova[possiv_quest][1] in prova)):
            lista_perguntas.append(Questoes_prova[possiv_quest][1])
            lista_respostas.append(Questoes_prova[possiv_quest][2])
            qtd_N2 -= 1
    while qtd_N3 > 0:
        possiv_quest = random.randint(0, len(Questoes_prova)-1)
        if (Questoes_prova[possiv_quest][0] == 3 and not(Questoes_prova[possiv_quest][1] in prova)):
            lista_perguntas.append(Questoes_prova[possiv_quest][1])
            lista_respostas.append(Questoes_prova[possiv_quest][2])
            qtd_N3 -= 1
    lista_perguntas.append("\n Respostas \n")
    lista_perguntas.append(lista_respostas)
    armazenador_arquivo = r'''\documentclass{article}
    \usepackage[utf8]{inputenc}
    \usepackage[T1]{fontenc}
    \begin{document}
    ... P \& B
    \textbf{\huge %(school)s \\}
    \vspace{1cm}
    \textbf{\Large %(title)s \\}
    ...
    \end{document}
    '''
    # Usamos um modelo
    with open("listas.tex", "r", encoding="utf-8") as f:
        armazenador_arquivo = f.read()
    # trocamos no latex os valores
    avaliacao_modificada = {'university': instituicao, 'class': "Cálculo 1 ",
                            'date': data_prova,
                            'question1': prova[0][0],
                            'question2': prova[1][0],
                            'question3': prova[2][0],
                            'question4': prova[3][0],
                            'question5': prova[4][0],
                            'question6': prova[5][0],
                            'question7': prova[6][0],
                            'question8': prova[7][0],
                            'question9': prova[8][0],
                            'question10': prova[9][0],
                            'question11': lista_respostas[0][0],
                            'question12': lista_respostas[1][0],
                            'question13': lista_respostas[2][0],
                            'question14': lista_respostas[3][0],
                            'question15': lista_respostas[4][0],
                            'question16': lista_respostas[5][0],
                            'question17': lista_respostas[6][0],
                            'question18': lista_respostas[7][0],
                            'question19': lista_respostas[8][0],
                            'question20': lista_respostas[9][0]
                            }
    print(armazenador_arquivo % avaliacao_modificada)

    with open('cover.tex', 'w', encoding="utf-8") as f:
        f.write(armazenador_arquivo % avaliacao_modificada)
    # compilamos o arquivo novo (preservando o modelo original)ss
    cmd = ['pdflatex', '-interaction', 'nonstopmode', 'cover.tex']
    proc = subprocess.Popen(cmd)
    proc.communicate()
    retcode = proc.returncode
    if not retcode == 0:
        os.unlink('cover.pdf')
        raise ValueError('Error {} executing command: {}'.format(
            retcode, ' '.join(cmd)))
    os.unlink('cover.tex')
    os.unlink('cover.log')


# lugar aonde ficam as perguntas , dific 1 = facil, 2 = media, 3= dificil,pergunta em modo LaTex assim como resposta
repositorio_questoes = [[[1], [".Calcule:\begin{enumerate} [(a)]\item $\lim_{x\rightarrow1}x + 2$ \item $\lim_{x\rightarrow0}3x + 1$\end{enumerate}"], ["\begin{enumerate}[(a)]\item Como $f(x) = x + 2$ é uma função contínua, segue que: $$\lim_{x\rightarrow1}x + 2 = 1 + 2 = 3$$\item Analogamente, temos que: $$\lim_{x\rightarrow0}3x + 1 = 3.0 + 1 = 1$$\end{enumerate}"]], [[1], ["2.Determine L para que a função $f(x)=\frac{x^2 - 4}{x - 2}$, com $x \neq 2$ e L, com $x = 2$ seja contínua em $p = 2$."], ["Note que, $\lim_{x\rightarrow2} \frac{x^2 - 4}{x - 2} = \lim_{x\rightarrow2}x + 2 = 2 + 2 = 4$. E, portanto, para que $f(x)$ seja contínua em $p = 2$, é necessário que $L = 4$."]], [[1], ["Calcule $$\lim_{x\rightarrow1} \frac{x^4 - -2x + 1}{x^3 + 3x^2 + 1}$$."], ["$\lim_{x\rightarrow1} \frac{x^4 - -2x + 1}{x^3 + 3x^2 + 1} = \frac{0}{5} = 0 $."]], [[1], ["Prove que $$\lim_{x\rightarrow p} f(x) = 0 \Leftrightarrow \lim_{x\rightarrow p} |f(x)| = 0$$."], ["$\lim_{x\rightarrow p} f(x) = 0 \Leftrightarrow \forall \epsilon > 0$, $\exists \delta > 0$ tal que $\forall x \in D_{f}$, temos que $0 < |x - p| < \delta \Rightarrow |f(x) - 0| < \epsilon$ $\Leftrightarrow \forall \epsilon > 0, \exists \delta$ tal que $\forall x \in D_{f}$, temos que $0 < |x - p| < \delta \Rightarrow ||f(x)| - 0| < \epsilon \Leftrightarrow \lim_{x\rightarrow p} f(x) = 0$."]], [[1], ["Calcule. $$\lim_{x\rightarrow -1} \frac{x^3 + 1}{x^2 - 1}$$."], ["Note que, $\lim_{x\rightarrow -1} \frac{x^3 + 1}{x^2 - 1} = \lim_{x\rightarrow -1} \frac{(x^2 - 1).x}{x^2 - 1} + \lim_{x\rightarrow -1} \frac{x + 1}{(x+1).(x-1)} = \lim_{x\rightarrow -1} x + \lim_{x\rightarrow -1} \frac{1}{x - 1} = -1 + \frac{1}{-1 - 1} = - 1 -\frac{1}{2} = \frac{-3}{2}$."]], [[1], ["Calcule  $\lim_{x\rightarrow 3} \frac{x^2 - 9}{x^2 + 9}$."], ["Como $f(x) = \frac{x^2 - 9}{x^2 + 9}$ é contínua, decorre que:$$\lim_{x\rightarrow 3} \frac{x^2 - 9}{x^2 + 9} = \frac{3^2 - 9}{3^2+9} = \frac{0}{18} =  0$$."]], [[1], ["Calcule $\lim_{h \rightarrow 0} \frac{f(x+h) - f(x)}{h}$, sendo $f(x) = x^2$."], ["Note que, para $f(x) = x^2$, temos que: $$\lim_{h \rightarrow 0} \frac{f(x+h) - f(x)}{h} = \lim_{h \rightarrow 0} \frac{(x+h)^2 - (x)^2}{h} = \lim_{h \rightarrow 0} \frac{x^2 + 2.x.h + h^2 - x^2}{h} = \lim_{h \rightarrow 0} \frac{2.x.h + h^2}{h} = \lim_{h \rightarrow 0} \frac{h(2.x + h)}{h} = \lim_{h \rightarrow 0} 2.x + h = 2.x + 0 = 2.x$$."]], [[1], ["Calcule $\lim_{x \rightarrow 1+} \frac{|x - 1|}{x - 1}$."], ["Calcule $\lim_{x \rightarrow 1+} \frac{|x - 1|}{x - 1}$."]], [[1], ["Calcule $\lim_{x \rightarrow 1+} \frac{f(x) - f(1)}{x - 1}$, onde $f(x) = x + 1$, se $x >= 1$ e $f(x)=2x$, se $x <1$."], ["Observe que, $$\lim_{x \rightarrow 1+} \frac{f(x) - f(1)}{x - 1} = \lim_{x \rightarrow 1+} \frac{(x + 1) - 2}{x - 1} = \lim_{x \rightarrow 1+} \frac{x - 1}{x - 1} = 1$$."]], [[1], ["Calcule $\lim_{x \rightarrow 2+} \frac{x^2 - 2x + 1}{x - 1}$."], ["Note que, $$\lim_{x \rightarrow 1+} \frac{x^2 - 2x + 1}{x - 1} = \frac{2^2 - 2.2 + 1}{2 - 1} = \frac{1}{1} = 1$$."]], [[1], ["Seja f definida em $R$.Suponha que $\lim_{x \rightarrow 0} \frac{f(x)}{x} = 1$.Calcule, $\lim_{x \rightarrow 0} \frac{f(3x)}{x}$."], ["Observe que, $$\lim_{xs \rightarrow 0} \frac{f(x3)}{x} = \lim_{xs \rightarrow 0} \frac{3.f(3x)}{3.x} = 3.1 = 3$$."]], [[2], ["Seja $f$ definida em $\mathbb{R}$ e tal que, $\forall\, x$, $|f(x)-3|\leq 2|x-1|$. Calcule $\lim_{x\rightarrow1}f(x)$ e justifique."], ["\begin{align*} &|f(x)-3|\leq 2|x-1| \iff -2|x-1|\leq f(x)-3 \leq 2|x-1|\iff\\ &\iff 3-2|x-1| \leq f(x) \leq 3+2|x-1|. \end{align*} Fazendo $g(x) = 3-2|x-1|$ e $h(x)= 3+2|x-1|$ e observando que $\lim_{x\rightarrow1}3-2|x-1| = lim_{x\rightarrow1}3+2|x-1|=3$, pelo Teorema do Confronto, uma vez que $g(x)\leq f(x) \leq h(x)$, vem: $\lim_{x\rightarrow1}f(x)=3$"]], [[2], [" Calcule : $$lim_{x\rightarrow1}\frac{\sin(\pi x)}{x-1}$$ "], ["Fazendo $x-1=u$, para $x\rightarrow1$,\,$u\rightarrow0$. Daí, \begin{align*}  &\lim_{x\rightarrow1}\frac{\sin(\pi x)}{x-1}= \lim_{u\rightarrow0}\frac{\sin(\pi(u+1))}{u} = \lim_{u\rightarrow0}\frac{\sin(u\pi+\pi)}{u}= \\ &=\lim_{u\rightarrow0}\frac{\sin(u\pi)\cos(\pi)+\sin(\pi)\cos(u\pi)}{u}\\ &= \lim_{u\rightarrow0}\frac{\sin(u\pi) \cos(\pi)}{u}+ \lim_{u\rightarrow0}\frac{\sin(\pi)\cos(u\pi)}{u} = \lim_{u\rightarrow0}\frac{\sin(u\pi)\cos(\pi)\pi}{u\pi}+ \lim_{u\rightarrow0}\frac{\sin(\pi)\cos(u\pi)}{u} \\  &= \lim_{u\rightarrow0}\frac{\sin(u\pi)}{u\pi}\cdot \lim_{u\rightarrow0}\cos(\pi)\cdot \pi + \lim_{u\rightarrow0}\frac{\sin(\pi)\cos(u\pi)}{u} = \cos(\pi) \cdot \pi = - \pi \end{align*} "]], [[2], ["Calcule : $$\lim_{x\rightarrow+\infty}{\left(\frac{x+2}{x+1}\right)}^x$$ "], ["mistura os dois"]], [[2], ["Sagu ou frango??"], ["\begin{align*} \lim_{x\rightarrow+\infty}{\left(\frac{x+2}{x+1}\right)}^x = \lim_{x\rightarrow+\infty}{\left[\frac{(x+1)+1}{x+1}\right]}^x = \lim_{x\rightarrow+\infty}{\left(1+\frac{1}{x+1}\right)}^x \end{align*} Fazendo $x+1=u$, para $x\rightarrow+\infty$,$u\rightarrow+\infty$. Donde, $$\lim_{x\rightarrow+\infty}{\left(1+\frac{1}{x+1}\right)}^x = \lim_{u\rightarrow+\infty}{\left(1+\frac{1}{u}\right)}^{u-1}=\lim_{u\rightarrow+\infty}{\left(1+\frac{1}{u}\right)}^u\cdot \lim_{u\rightarrow+\infty}{\left(1+\frac{1}{u}\right)}^{-1} = e$$"]], [[2], ["Prove que a equação $ x^3 -4x+ 2 =0$ admite três raízes reais distintas."], ["Como $f(x)=x^3-4x+2$ é polinomial, $f$ é contínua. Temos que, $f(-3)<0$ e $f(-2)>0$, assim, pelo Teorema de Bolzano, dado que $f(-3)$ e $f(-2)$ possuem sinais contrários, $\exists$ $c$ em $[-3,-2]$ tal que $f(c)=0$. Procedendo analogamente, concluí-se que $f$ possui uma raiz em $[0,1]$ e em $[\frac{3}{2},2]$."]], [[2], [" Sabe-se que $f$ é contínua em $2$ e que $f(2)=8$. Mostre que existe $\delta$ tal que para todo $x\in D_{f}, 2 - \delta< x < 2 + \delta \Longrightarrow f(x)>7$."], ["Temos que,\\ $f$ é contínua em $2$ $\iff$ Para todo $\mathcal{E}>0$ dado, $\exists\,\, \delta>0$ tal que, $\forall \,\, x\in D_{f}, |x-2| < \delta \Longrightarrow |f(x) - f(2)| < \mathcal{E}$.\\ $|f(x)-f(2)| = |f(x)-8|< \mathcal{E}>0 \iff 8 - \mathcal{E} < f(x) < 8 + \mathcal{E}$. Basta tomar $\mathcal{E} = 1$. "]], [[2], [" Calcule, pela definição , a derivada da função $f: \mathbb{R} \rightarrow \mathbb{R}$ definida por $f(x) = \cos(x)$, num ponto p arbitrário."], ["\begin{align*} &f'(p) = \lim_{h\rightarrow0}\frac{f(p+h)-f(p)}{h} = \lim_{h\rightarrow0}\frac{\cos(p+h)-\cos(p)}{h} = \\ & = \lim_{h\rightarrow0}\frac{\cos(p)\cos(h)-\sin(p)\sin(h)-\cos(p)}{h} = \lim_{h\rightarrow0}\frac{[\cos(p)\cos(h)-\cos(p)]-\sin(p)\sin(h)}{h} = \\ & = \lim_{h\rightarrow0}\frac{\cos(p)[\cos(h)-1]}{h}- \lim_{h\rightarrow0}\frac{\sin(p)\sin(h)}{h} = \lim_{h\rightarrow0}\frac{\cos(p)[\cos(h)-1]}{h} \cdot {\left[\frac{\cos(h)+1}{\cos(h)+1}\right]} \\ & - \lim_{h\rightarrow0}\frac{\sin(p)\sin(h)}{h} \lim_{h\rightarrow0}\frac{\cos(p)[\cos^2(h)-1]}{h[\cos(h)+1]} - \lim_{h\rightarrow0}\frac{\sin(p)\sin(h)}{h} \end{align*} De $\cos^2(h) + \sin^2(h) = 1$, resulta:\\ \begin{align*} &- \lim_{h\rightarrow0}\frac{\cos(p)\sin(h)\sin(h)}{h \cdot [\cos(h)+1]} \cdot {\left[\frac{h}{h}\right]} - \lim_{h\rightarrow0}\frac{\sin(p)\sin(h)}{h} = \\ & \lim_{h\rightarrow0}\frac{\cos(p)}{\cos(h)+1} \cdot \lim_{h\rightarrow0}{\left[\frac{\sin(h)}{h}\right]}^2 - \lim_{h\rightarrow0}\frac{\sin(p)\sin(h)}{h} = - \frac{\cos(p) \cdot 0 }{2} - \sin(p) = - \sin(p) \end{align*}"]], [[2], ["Calcule e justifique $$\lim_{x\rightarrow+\infty}\frac{1}{x}$$"], [
    "Intuitivamente, observamos que, conforme os valores no denominador crescem, o valor do quociente considerado aproxima-se de zero. Então, é plausível supor que: \\ $$\lim_{x\rightarrow+\infty}\frac{1}{x} = 0$$\\ \\ De fato, pela definição, \\ \\\begin{align*} \lim_{x\rightarrow+\infty}\frac{1}{x} = 0 \iff &\forall\,\,\,\mathcal{E}>0\text{ dado, }\exists\,\,\delta>0, \text{ com }\delta>a\,\, (a\in\mathbb{R}_{+}^*\subsetneqq D_{f} )\\ &\text{tal que, } x>\delta \,\Longrightarrow\,\left\vert\frac{1}{x}-0\right\vert<\mathcal{E} \end{align*} \\ Donde, $$x>\delta \iff \frac{1}{x}<\frac{1}{\delta}$$\\ Uma vez que $\dfrac{1}{x}>0$ e $\dfrac{1}{\delta}>0$, a desigualdade anterior pode ser reescrita como \\ $$\left\vert\frac{1}{x}\right\vert<\left\vert\frac{1}{\delta}\right\vert \iff \left\vert\frac{1}{x}-0\right\vert<\frac{1}{\delta}$$\\ \\ Assim, tomando-se $\delta= \frac{1}{\mathcal{E}}>0$,$$x>\delta \Longrightarrow \left\vert\frac{1}{x}-0\right\vert<\mathcal{E}.$$\\ Logo, \\ $$\lim_{x\rightarrow+\infty}\frac{1}{x} = 0$$\qed "]], [[2], ["Calcule $$\lim_{x\rightarrow+\infty}\sqrt{x+\sqrt{x}} - \sqrt{x-1}$$"], ["\begin{align*} &\lim_{x\rightarrow+\infty}\sqrt{x+\sqrt{x}} - \sqrt{x-1} = \lim_{x\rightarrow+\infty}\sqrt{x+\sqrt{x}} - \sqrt{x-1} \cdot {\left[\frac{\sqrt{x+\sqrt{x}}+ \sqrt{x-1}}{\sqrt{x+\sqrt{x}}+ \sqrt{x-1}}\right]}= \\   =& \lim_{x\rightarrow+\infty}\frac{\sqrt{x}+1}{\sqrt{x+\sqrt{x}}+ \sqrt{x-1}} \cdot {\left[\frac{\frac{1}{\sqrt{x}}}{\frac{1}{\sqrt{x}}}\right]} = \frac{\lim_{x\rightarrow+\infty}\frac{\sqrt{x}}{\sqrt{x}} \cdot {\left(1+\frac{1}{\sqrt{x}}\right)}}{\lim_{x\rightarrow+\infty}\frac{1}{\sqrt{x}} \cdot {\left(\sqrt{x+\sqrt{x}}+\sqrt{x-1}\right)}} = \\  = & \frac{ \lim_{x\rightarrow+\infty}{\left(1+\frac{1}{\sqrt{x}}\right)}}{ \lim_{x\rightarrow+\infty}\sqrt{\frac{x}{x}+\frac{\sqrt{x}}{x}} + \sqrt{\frac{x}{x}-\frac{1}{x}}} = \frac{ \lim_{x\rightarrow+\infty}{\left(1+\frac{1}{\sqrt{x}}\right)}}{\lim_{x\rightarrow+\infty}\sqrt{1+\sqrt{\frac{x}{x^2}}} + \sqrt{1-\frac{1}{x}}} = \\  = & \frac{ \lim_{x\rightarrow+\infty}{\left(1+\frac{1}{\sqrt{x}}\right)}}{ \lim_{x\rightarrow+\infty}\sqrt{1+\sqrt{\frac{1}{x}}} + \sqrt{1 - \frac{1}{x}}} = \frac{1}{2} \end{align*}"]], [[2], ["Prove pela definição que $f(x) = x^2+ x - 2$ é contínua em $p = 1$."], ["Sabemos que,\\ $f$ é contínua em $1 \iff$ Para todo $\mathcal{E}>0$ dado,$\exists\,\, \delta>0$ tal que $\forall\,\, x \in D_{f}$,\\ $|x-1|< \delta \Longrightarrow |f(x)-f(1)|< \mathcal{E}$.\\ \\ Temos, $$|f(x)-f(1)|= |(x^2+x-2)-0| = |x-1| \cdot |x+2| < \mathcal{E}$$. \\ \\ Como $|x-1| < \delta \Longrightarrow |x-1|\cdot|x+2| < \delta\cdot|x+2|$ . Seja $\delta1 = 1$. Daí, $|x|-|1| \leq |x-1| \text{ e } |x-1|< 1$, pela transitivade, $|x|-1<1$ , qual seja, \\ $|x|<2$. Ademais, $|x+2| \leq |x| + |2| = 4$, o que acarreta $|x-1| \cdot |x+2| < \delta\cdot |x+2| < 4\delta \Longrightarrow \delta2 = \dfrac{\mathcal{E}}{4}\text{.}$\\ \\ Assim, tomando-se $\delta=$ mín$\left[\frac{\mathcal{E}}{4},1\right]$,$$\text{dado }\mathcal{E}>0, |x-1|< \delta \Longrightarrow |f(x)-f(1)|< \mathcal{E} \text{.}$$\\ Logo, $f$ é contínua em $1$."]], [[2], ["Seja $a>0\text{, }a\neq 1$. Mostre que: $$\lim_{h\rightarrow0}\frac{a^h-1}{h}= \ln a$$ "], ["Fazendo $a^h - 1 = u$, como $a^h>0$ para todo $h$ em $\mathbb{R}$, então $a^h - 1 > -1$. Ademais, $u=a^h -1 > -1 \iff u + 1 > -1 + 1 \iff u + 1 > 0$. Assim, $$a^h - 1 = u \Longrightarrow a^h = u + 1 \Longrightarrow \log_a a^h = \log_a (u+1) \Longrightarrow h = log_a (u+1)$$\\ \\ Além disso, observando que, para $h \rightarrow 0\text{, } u \rightarrow 0$, temos: \\ \\ $$\lim_{h\rightarrow0}\frac{a^h-1}{h} = \lim_{u\rightarrow0}\frac{u}{\log_a (u+1)} = \lim_{u\rightarrow0}\frac{1}{\frac{1}{u} \cdot \log_a (u+1)} = \lim_{u\rightarrow0}\frac{1}{\log_a (u+1)^\frac{1}{u}}$$\\ Da continuidade das funções logarítmicas e afins, segue que: $$\lim_{u\rightarrow0}\frac{1}{\log_a (u+1)^\frac{1}{u}} = \frac{ \lim_{u\rightarrow0}1}{\log_a \lim_{u\rightarrow0}(1+u)^\frac{1}{u}} $$ \\ \\ Por fim, lembrando que $ \lim_{u\rightarrow0}(1+u)^\frac{1}{u} = e$ e empregando a mudança de base, vem: $$ \frac{ \lim_{u\rightarrow0}1}{\log_a \lim_{u\rightarrow0}(1+u)^\frac{1}{u}} = \frac{1}{\log_a e} = \ln a$$\\ \qed"]], [[3], ["Determine a equação da reta tangente ao gráfico de $f(x) = \frac{1}{x}$ no ponto de abscissa 2."], ["Temos que, se $f(x) = \frac{1}{x}$, então $f'(x) = \frac{-1}{x^2}$. E portanto, $f'(2) = \frac{-1}{2^2} = \frac{-1}{4}$. Pela equação da reta tangente, dados o ponto e o coeficiente angular da reta no ponto dados, segue que $y = \frac{-1}{4}x + 1$."]], [[3], ["Determine a equação da reta tangente ao gráfico de $f(x) = \frac{1}{x^2}$ no ponto de abscissa 1."], ["Temos que, se $f(x) = \frac{1}{x^2}$, então $f'(x) = \frac{-2}{x^3}$. E portanto, $f'(1) = \frac{-2}{1^3} = -2$. Pela equação da reta tangente, dados o ponto e o coeficiente angular da reta no ponto dados, segue que $y = -2x + 3$."]], [[3], ["Calcule pela definição $g'(x)$, sabendo que $g(x) = x^2$."], ["Note que, $$g'(x) = \lim_{x \rightarrow p} \frac{g(x) - g(p)}{x - p} = \lim_{x \rightarrow p} \frac{x^2 - p^2}{x - p} = \lim_{x \rightarrow p} \frac{(x - p)(x + p)}{x - p} = \lim_{x \rightarrow p} x + p = p + p = 2p$$."]], [[3], ["Calcule pela definição $g'(x)$, sabendo que $g(x) = \frac{1}{x}$."], ["Note que, $$g'(x) = \lim_{x \rightarrow p} \frac{g(x) - g(p)}{x - p} = \lim_{x \rightarrow p} \frac{p - x}{-(p-x)xp} = \lim_{x \rightarrow p} \frac{-1}{xp}= \frac{-1}{p^2}$$."]], [[3], ["Calcule pela definição $g'(x)$, sabendo que $g(x) = x$."], ["Note que, $$g'(x) = \lim_{x \rightarrow p} \frac{g(x) - g(p)}{x - p} = \lim_{x \rightarrow p} \frac{x - p}{x - p} = \lim_{x \rightarrow p} 1 = 1$$."]], [[3], ["Sagu ou frango??"], ["mistura os dois"]], [[3], ["Seja $f(x) = x + 1$, se $x < 2$ e $f(x) = 1$, se $x >=2$. $f(x) é contínua em x = 2$?"], ["Note que, $\lim_{x \rightarrow 2+}f(x) = \lim_{x \rightarrow 2+} 1 = 1 $ e, $\lim_{x \rightarrow 2-}f(x) = \lim_{x \rightarrow 2-}x + 1 = 2 + 1 = 3$. Como os limites laterais são diferente, segue que $f(x)$ não é contínua em $x = 2$."]], [[3], ["Seja $f(x) = x + 1$, se $x < 2$ e $f(x) = 1$, se $x >=2$. $f(x)$ é derivável em $x = 2$?"], ["Note que, $\lim_{x \rightarrow 2+} \frac{f(x) - f(2)}{x - 2} = \lim_{x \rightarrow 2+} \frac{1 - 1}{x - 2} = \lim_{x \rightarrow 2+} \frac{0}{x - 2} = 0$ e, $\lim_{x \rightarrow 2-} \frac{x + 1 - 3}{x - 2} = \lim_{x \rightarrow 2-} \frac{x - 2}{x - 2} = \lim_{x \rightarrow 2-} 1 = 1$. E, portanto, $f(x)$ não é derivável em $x = 2$."]], [[3], ["Seja $f(x) = x^2$, se $x <= 0$ e, $f(x) = -x^2$ se $x>0$. $f(x)$ é diferenciável em $x = 0$."], ["Note que, $\lim_{x \rightarrow 0+} \frac{-x^2 - 0^2}{x - 0} = \lim_{x \rightarrow 0+} \frac{-x^2}{x} = \lim_{x \rightarrow 0+} -x = 0$ e, $\lim_{x \rightarrow 0-} \frac{x^2 - 0^2}{x - 0} = \lim_{x \rightarrow 0-}\frac{x^2}{x} = \lim_{x \rightarrow 0-} x = 0 $. Logo, $f(x)$ é derivável em $x = 0$. “]],  [[3],[“Seja $f(x) = x^2$, se $x <= 0$ e, $f(x) = -x^2$ se $x>0$. $f(x)$ é diferenciável em $x = 0$. “], [“Note que, $\lim_{x \rightarrow 0+} \frac{-x^2 - 0^2}{x - 0} = \lim_{x \rightarrow 0+} \frac{-x^2}{x} = \lim_{x \rightarrow 0+} -x = 0$ e, $\lim_{x \rightarrow 0-} \frac{x^2 - 0^2}{x - 0} = \lim_{x \rightarrow 0-}\frac{x^2}{x} = \lim_{x \rightarrow 0-} x = 0 $. Logo, $f(x)$ é derivável em $x = 0$. Como $f(x)$ é derivável em $x = 0$, segue que $f(x)$ é contínua em $x = 0$."]]]


# repositorio_aux = json.loads(repositorio_questoes)
repositorio_aux = repositorio_questoes

opcao = 666
# aqui jaz cracudoBarbudo , sua memoria não será esquecida
N1 = 0
N2 = 0
N3 = 0
qtd_N1 = 0
qtd_N2 = 0
qtd_N3 = 0
print("\n"*1000)
print("""____ ____ ____ ____ ___  ____ ____    ___  ____    ___  ____ ____ _  _ ____
| __ |___ |__/ |__| |  \ |  | |__/    |  \ |___    |__] |__/ |  | |  | |__|    .
|__] |___ |  \ |  | |__/ |__| |  \    |__/ |___    |    |  \ |__|  \/  |  |    .
                                                                                 """)
print("""___ _  _ ____    _  _ ____ ____ _ _    ____    ____ ___  _ ___ _ ____ _  _
 |  |__| |___    |  | |__| |    | |    |  |    |___ |  \ |  |  | |  | |\ |
 |  |  | |___     \/  |  | |___ | |___ |__|    |___ |__/ |  |  | |__| | \|
                                                                              """)

print("-"*20)
print("\n Olá, \n Das opções abaixo, quais você deseja para gerar um PDF? \n -Prova \n -Lista \n -porrada na cara \n")
print("-"*20)
opcao = input("\n")
# menu para selecionar função
while (opcao != "Prova") and(opcao != "Lista") and (opcao != "porrada na cara"):
    print("\n Opção inválida! Digite a opção novamente. \n")
    opcao = input("")


if (opcao == "Prova"):
    total = 10
    print("Lembrando que é  para ter {} questões.".format(total))
    print(type(repositorio_aux))
    for questao in repositorio_aux:

        if questao[0] == [1]:
            N1 += 1
        elif questao[0] == [2]:
            N2 += 1
        elif questao[0] == [3]:
            N3 += 1

    while(total != 0):
        qtd_N1 = int(
            input("Quantas do N1?\n (No maximo {} questões desse nivel\n 0/10) ".format(N1)))
        while qtd_N1 > N1 or qtd_N1 < 0:
            qtd_N1 = int(input(
                " \n Opção inválida, escolha um numero inteiro entre 0 e {} ! \n".format(N1)))
        qtd_N2 = int(input(
            "Quantas do N2?\n (No maximo {} questões desse nivel\n {}/10) ".format(N2, qtd_N1)))
        while qtd_N2 > N2 or qtd_N2 < 0:
            qtd_N2 = int(input(
                " \n Opção inválida, escolha um numero inteiro entre 0 e {} ! \n".format(N2)))
        qtd_N3 = int(input(
            "Quantas do N3?\n (No maximo {} questões desse nivel\n {}/10) ".format(N3, qtd_N1+qtd_N2)))
        while qtd_N3 > N3 or qtd_N3 < 0:
            qtd_N3 = int(input(
                " \n Opção inválida, escolha um numero inteiro entre 0 e {} !\n ".format(N3)))
        if (total == (qtd_N1+qtd_N2+qtd_N3)):
            total = 0
        else:
            print("Poxa meu jovem, eu falei que é pra ter {}, isso não é nem {} , nem {} , {} entendeu ?".format(
                total, total-1, total+1, total))
    instituicao = input("\n Digite o nome Instituição.\n")
    data_prova = input("\nDigite a data da prova\n")
    prova(repositorio_aux, qtd_N1, qtd_N2, qtd_N3, instituicao, data_prova)

elif(opcao == "Lista"):
    total = 10
    print("Lembrando que é  para ter {} questões.".format(total))
    print(type(repositorio_aux))
    for questao in repositorio_aux:

        if questao[0] == [1]:
            N1 += 1
        elif questao[0] == [2]:
            N2 += 1
        elif questao[0] == [3]:
            N3 += 1

    while(total != 0):
        qtd_N1 = int(
            input("Quantas do N1?\n (No maximo {} questões desse nivel\n 0/10) ".format(N1)))
        while qtd_N1 > N1 or qtd_N1 < 0:
            qtd_N1 = int(input(
                " \n Opção inválida, escolha um numero inteiro entre 0 e {} ! \n".format(N1)))
        qtd_N2 = int(input(
            "Quantas do N2?\n (No maximo {} questões desse nivel\n {}/10) ".format(N2, qtd_N1)))
        while qtd_N2 > N2 or qtd_N2 < 0:
            qtd_N2 = int(input(
                " \n Opção inválida, escolha um numero inteiro entre 0 e {} ! \n".format(N2)))
        qtd_N3 = int(input(
            "Quantas do N3?\n (No maximo {} questões desse nivel\n {}/10) ".format(N3, qtd_N1+qtd_N2)))
        while qtd_N3 > N3 or qtd_N3 < 0:
            qtd_N3 = int(input(
                " \n Opção inválida, escolha um numero inteiro entre 0 e {} !\n ".format(N3)))
        if (total == (qtd_N1+qtd_N2+qtd_N3)):
            total = 0
        else:
            print("Poxa meu jovem, eu falei que é pra ter {}, isso não é nem {} , nem {} , {} entendeu ?".format(
                total, total-1, total+1, total))
    instituicao = input("\n Digite o nome Instituição.\n")
    data_prova = input("\nDigite a data da prova\n")
    lista(repositorio_aux, qtd_N1, qtd_N2, qtd_N3, instituicao, data_prova)

    lista(repositorio_aux)
elif(opcao == "porrada na cara"):
    print("\n Essa opção não faz nada no momento, mas bem que voce esta merecendo né vacilão? \n")

fim = input("")
