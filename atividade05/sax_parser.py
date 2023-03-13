from html.parser import HTMLParser
import urllib.request

class MyHTMLParser(HTMLParser):
  def __init__(self):
    super().__init__()
    self.currentData = ""
    self.title = ""
    self.image = ""

  def handle_starttag(self, tag, attrs):
    self.currentData = ""
    
    if tag =="img":  
      for k, v in attrs:
        if k == "src":
          self.image = v

  def handle_endtag(self, tag):
    if tag =="title": 
      self.title = self.currentData      

  def handle_data(self, data):
    self.currentData += data    


print("""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        
        <title>Atividade 05 - Kevin Cerqueira</title>
    </head>
    <body>
""")
with open('seeds.txt', 'rb') as seed:
    for line in seed.readlines():
        line = line.decode("utf-8")
        try:
            page = urllib.request.urlopen(line)
            parser = MyHTMLParser()
            parser.feed(str(page.read().decode('utf-8')))
            
            print("Título:", parser.title)
            print("Imagem:", parser.image)
            print('<br>')
            if(parser.image.count("http") != 0):
                url = parser.image.replace('\n', '')
            else:
                url = "{}{}".format(line.replace('\n', ''), parser.image.replace('\n', ''))
            print('<img src="{}" style="width: 20%;">'.format(url))
            print('<br><br>')
        except:
           pass
        
print("""
            </body>
            </html>
""")