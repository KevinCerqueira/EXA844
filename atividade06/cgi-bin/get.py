#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from urllib.parse import parse_qs
from pathlib import Path
from datetime import datetime

# Abre o arquivo JSON que armazena as mensagens
with open(str(Path('mensagens.json'))) as file:
    mensagens = json.load(file)

# Obtém os dados da mensagem enviados pelo formulário
qs = os.environ["QUERY_STRING"]
dados_formulario = parse_qs(qs, encoding="latin-1")
mensagem = {
    'autor': dados_formulario["nome"][0],
    'texto': dados_formulario["end"][0],
    'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
}

# Adiciona a mensagem à lista de mensagens existente
mensagens["Mensagens"].append(mensagem)

# Salva a lista atualizada de mensagens no arquivo JSON
with open(str(Path('mensagens.json')), 'w') as file:
    json.dump(mensagens, file)

# Exibe as mensagens na página HTML
print("Content-type: text/html; charset=utf-8")
print()
print("<html>")
print("<head>")
print("<title>EXA844</title>")
print("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">")
print("""
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
            }
            
            h1 {
                text-align: center;
                font-size: 24px;
            }
            
            hr {
                border: 1px solid #ccc;
                margin-bottom: 20px;
            }
            
            label {
                display: block;
                margin-bottom: 10px;
            }
            
            input[type="text"], textarea {
                width: 100%;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box;
                margin-bottom: 20px;
            }
            
            input[type="submit"], input[type="reset"] {
                background-color: #4CAF50;
                color: #fff;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                margin-right: 10px;
            }
            
            input[type="submit"]:hover, input[type="reset"]:hover {
                background-color: #3e8e41;
            }
        </style>
""")
print("</head>")
print("<body>")
print("<h1 align=\"center\">EXA844 ATIVIDADE 06</h1>")
print("<hr>")
print("<form method=\"GET\" action=\"http://192.168.102:8000/cgi-bin/get.py\">")
print("Remetente:<br>")
print("<input type=\"text\" size=\"64\" name=\"nome\" value=\"\"><br><br>")
print("Mensagem:<br>")
print("<textarea rows=\"3\" cols=\"46\" name=\"end\"></textarea><br><br>")
print("<input type=\"submit\">")
print("</form>")
print("<hr>")
print("<h1 align=\"center\">Todas as mensagens</h1>")
print("<hr>")

# Exibe todas as mensagens cadastradas
for i, mensagem in enumerate(mensagens["Mensagens"], start=1):
    print("<h2>Mensagem {}</h2>".format(i))
    print("<p>")
    print("<strong>Autor:</strong> {}<br>".format(mensagem["autor"]))
    print("<strong>Mensagem:</strong> {}<br>".format(mensagem["texto"]))
    print("<strong>Data:</strong> {}".format(mensagem["data"]))
    print("</p>")
    print("<hr>")

print("</body>")
print("</html>")
