print('Texto explicativo')

perguntas = {
    'Pergunta 1' : {
        'pergunta': 'Quando e 2+2? ',
        'respostas': {'a' : '1', 'b' : '4','c' : '1',},
        'resposta_certa':'b',
    },
    'Pergunta 2' : {
        'pergunta' : 'Quando e 2*4? ',
        'respostas' : {'a':'8', 'b':'9', 'c': '10', 'd':'11'},
        'resposta_certa': 'a',
    }
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta ')

    if resposta_usuario == pv['resposta_certa']:
        print('vc acertou')
        respostas_certas += 1
    else:
        print('resposta errada')

    print()
qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas *100

print(f'Voce acertou {respostas_certas} respostas')
print(f'sua porcentagem de acertos foi de {porcentagem_acerto}%.')