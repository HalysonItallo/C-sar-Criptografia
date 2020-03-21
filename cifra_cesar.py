import requests
import json
import hashlib

def main():
    escrever_json()
    enviar_json()
   
    
def enviar_json():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=1ce86346346ebf0e7ac7e0d5de17accbc26ab525'
    files = {'answer': ('answer.json', open('answer.json', 'rb'))}
    send_request = requests.post(url, files=files)
    print(send_request.content)
    
def escrever_json():
    result_request = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=1ce86346346ebf0e7ac7e0d5de17accbc26ab525")
    num_casas = result_request.json()["numero_casas"]
    texto_criptografado = result_request.json()["cifrado"]
    
    texto_json = {
    "numero_casas": result_request.json()["numero_casas"],
    "token": result_request.json()["token"],
    "cifrado": result_request.json()["cifrado"],
    "decifrado": cifra_cesar(num_casas,texto_criptografado),
    "resumo_criptografico": hashlib.sha1(cifra_cesar(num_casas,texto_criptografado).encode('utf-8')).hexdigest()
    }
    escrever_arquivo(json.dumps(texto_json))
    
    
def cifra_cesar(num_casas, texto_criptografado):
    alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    texto_descriptografado = "" 
    for i in range(len(texto_criptografado)):
        for j in range (len(alfabeto)):
            if texto_criptografado[i] == alfabeto[j]:
                texto_descriptografado += alfabeto [j-num_casas]
            elif texto_criptografado[i] == " " and j == len(alfabeto) - 1:
                texto_descriptografado += " "
            return texto_descriptografado


def escrever_arquivo(resultado_json):
    arquivo = open('answer.json', 'w')
    arquivo.writelines(resultado_json)
    arquivo.close()


main()

