import requests
import json
import os

replay = "s"
os.system('cls')


while replay == "s" or replay == "S":
    
    req = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")

    cotacao = req.json()
    moeda = cotacao["USD"]["name"]
    valorDolar = float(cotacao["USD"]["bid"])
    data = cotacao["USD"]["create_date"]
    print("---------------------------------------------------------------------------")
    print("COATAÇÃO DO DOLAR")
    print("---------------------------------------------------------------------------")
    print("Moeda: " + moeda)
    print("---------------------------------------------------------------------------")
    print("Valor: R$" + "%.2f" % valorDolar)
    print("---------------------------------------------------------------------------")
    print("Data: " + data)
    print("---------------------------------------------------------------------------")
    valorReal = float(input("Digite o valor em real que deseja converter para dólar: "))
    print("---------------------------------------------------------------------------")

    valorConvertido = valorReal/valorDolar  
    print("R$" , valorReal ,"em dólar é: USD","%.2f" % valorConvertido)
    print("---------------------------------------------------------------------------")

    x = input("Deseja refazer o processo? Sim = s / Não = n: ")
    print("---------------------------------------------------------------------------")  
    
    while not(replay == "s" or replay == "S" or replay == "n" or replay == "N"):
        print("Opção invalida!")
        x = input("Deseja refazer o processo? Sim = s / Não = n: ")
    os.system('cls')    

    if x=="S" or x=="s":
        replay = "s"

    elif x == "n" or x == "N":
        replay = "n"


print("Saindo...")

