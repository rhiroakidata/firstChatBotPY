# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot, response_selection
import logging

logging.basicConfig(level=logging.INFO)

bot = ChatBot(
    "Homem de Verde",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ]
)

talk = ['O que é Bacharelado em Ciência e Tecnologia?', 'O BC&T é um dos cursos obrigatórios de ingresso dos alunos' +
'na UFABC e está pautado nos conceitos de interdisciplinaridade e flexibilidade de formação profissional.' +
'Sua estrutura é baseada no regime quadrimestral e em um sistema de créditos que permite diferentes organizações' +
' curriculares, conforme os interesses e aptidões dos alunos', 'Quais os objetivos do Bacharelado em Ciência' +
' e Tecnologia?', 'O objetivo do BC&T é formar o aluno para atuar como pesquisador, gestor e consultor nas áreas' +
' de desenvolvimento científico e tecnológico. ', 'Onde está localizada a Universidade Federal do ABC', 'Está' +
' localizada em dois Campus: Santo André e São Bernardo.\nSanto André: Av. dos Estados, 5001 - Bangú, ' +
'Santo André - SP, 09210-580\nSão Bernardo: UFABC - Alameda da Universidade, s/n - Anchieta, ' +
'São Bernardo do Campo - SP, 09606-045', 'O que é Bacharelado em Ciências e Humanidades?', 'O Bacharelado ' +
'em Ciências e Humanidades (BC&H) é um curso de formação científica geral.\nA matriz curricular proporciona' +
' vivências educativas que deverão resultar em uma forte formação científica e na aquisição de habilidades que' +
' permitam ao educando se expressar como um ser que pensa e que tem no pensamento a inspiração para todas as' +
' suas formas de conduta.', 'Quais são os cursos de formação específica vinculados ao Bacharelado em Ciências ' +
'e Humanidades?', 'Bacharelados:Ciências Econômicas, Filosofia, Planejamento Territorial, Políticas Públicas e ' +
'Relações Internacionais\nLicenciatura: Filosofia', 'O que é UFABC?', 'Universidade Federal do UFABC']

bot.set_trainer(ListTrainer)
bot.train(talk)

def get_feedback():

    text = input('\nVocê: ')

    if 'sim' in text.lower():
        return False
    elif 'não' in text.lower():
        return True
    else:
        print('Por favor responda "Sim" ou "Não"')
        return get_feedback()

print("Olá! Sou o aluno robô da Universidade Federal do ABC, como posso te ajudar?")


# The following loop will execute each time the user enters input
while True:
    try:
        duvida=False
        print("\nHomem de Verde: Digite aqui sua pergunta que gostaria de fazer para mim")
        pergunta = input("Você: ")
        input_statement = bot.input.process_input_statement(pergunta)

        response_list = bot.storage.filter()
        response = response_selection.get_most_frequent_response(input_statement, response_list)
        bot.output.process_response(response)
        print('\nHomem de Verde: "{}" é uma resposta coerente para "{}"? \n'.format(response, input_statement))

        if get_feedback()==True:
            print("Homem de verde: Por favor insira qual seria a resposta correta")
            response1 = input("Você: ")
            response1_statement = bot.input.process_input_statement(response1)
            bot.learn_response(response1_statement, input_statement)
            print("Homem de Verde: Resposta adicionada!")

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break