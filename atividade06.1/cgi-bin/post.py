#!/usr/bin/env python3
import cgi
import cgitb
import datetime

# Habilitar a exibição de erros CGI
cgitb.enable()

# Localização do arquivo de mensagens
arquivo = 'mensagens.txt'

# Função para ler as mensagens do arquivo
def ler_mensagens():
    with open(arquivo, 'r') as f:
        mensagens = f.readlines()
    return mensagens

# Função para adicionar uma nova mensagem ao arquivo
def adicionar_mensagem(mensagem):
    data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(arquivo, 'a') as f:
        f.write('{}: {}\n'.format(data, mensagem))

# Configurar o cabeçalho HTTP para exibir a resposta como HTML
print("Content-Type: text/html\n")

# Obter os dados do formulário
form = cgi.FieldStorage()
print(form)
# Se houver dados no formulário, adicionar a nova mensagem e exibir a lista de mensagens atualizada
if form.getvalue('nome'):
    mensagem = form.getvalue('nome')
    adicionar_mensagem(mensagem)

# Exibir o formulário e a lista de mensagens atualizada
print('''
<html>
<head>
    <title>Blog</title>
</head>
<body>
    <h1>Blog</h1>
    <form method="post">
        <label>Autor:</label>
        <input type="text" name="autor"><br>
        <label>Mensagem:</label>
        <textarea name="mensagem"></textarea><br>
        <input type="submit" value="Enviar">
    </form>
    <hr>
    <h2>Mensagens:</h2>
''')

# Ler as mensagens do arquivo e exibir na página
mensagens = ler_mensagens()
for mensagem in mensagens:
    print('<p>{}</p>'.format(mensagem))

print('''
</body>
</html>
''')
