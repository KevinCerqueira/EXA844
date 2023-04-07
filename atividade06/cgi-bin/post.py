#!/usr/bin/env python3
#coding: utf8
import os, cgi
import time
import json

form = cgi.FieldStorage()

with open("http://192.168.0.120:8000/mensagens.json") as file:
    mensagens = json.load(file)

msg = dict()
msg['name'] = form["nome"].value
msg['end'] = form["end"].value
msg['time'] = time.time()

mensagens["Mensagens"].append(msg)
print("<h1>")
print("AAAAAAAAAAAAAAAAAAAAAAAAA", mensagens)
print("</h1>")
print("Content-type: text/html; charset=utf-8")
print()
print("<html>")
print("<head>")
print("<title>Seu Post</title>")
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
print("<h1 align=\"center\">Seu Post</h1>")
print("<p>Autor: "+ msg['name'] + "</p>")
print("<p>Mensagem: "+ msg['end'] + "</p>")
print("<p>Data: "+ str(msg['time']) + "</p>")
print("<hr>")
print("<h1 align=\"center\">Todas as mensagens</h1>")
print("<ul>")
for x in mensagens["Mensagens"]:
    print("<li>")
    print("<p>Autor: "+ x['name'] + "</p>")
    print("<p>Mensagem: "+ x['end'] + "</p>")
    print("<p>Data: "+ str(x['time']) + "</p>")
    print("</li>")
print("</ul>")
print("</body>")
print("</html>")

with open("http://192.168.102:8000/cgi-bin/mensagens.json", 'w') as file:
    json.dump(mensagens, file)
