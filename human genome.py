import urllib.request
import json
import socket
import time


HOST = "127.0.0.1"
PORTA = 6255


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

##contents = urllib.request.urlopen("https://ssd-api.jpl.nasa.gov/cad.api").read()
##contents = urllib.request.urlopen("https://songbpm.com/searches/africa").read()

##contents = urllib.request.urlopen("http://gggenome.dbcls.jp/hg38/TTCATTGACAACATT.json").read()
contents = urllib.request.urlopen("http://gggenome.dbcls.jp/hg38/TCATTGACAACTT.json").read()
varab = json.loads(contents)

allsnips = varab['results'][0]['snippet'] + varab['results'][1]['snippet'] + varab['results'][2]['snippet'] + varab['results'][3]['snippet'] + varab['results'][4]['snippet'] + varab['results'][5]['snippet'] + varab['results'][6]['snippet'] + varab['results'][7]['snippet'] + varab['results'][8]['snippet'] + varab['results'][9]['snippet'] + varab['results'][10]['snippet'] + varab['results'][11]['snippet'] + varab['results'][12]['snippet'] + varab['results'][13]['snippet'] + varab['results'][14]['snippet'] + varab['results'][15]['snippet'] + varab['results'][16]['snippet'] + varab['results'][17]['snippet'] + varab['results'][18]['snippet'] + varab['results'][19]['snippet'] + varab['results'][20]['snippet'] + varab['results'][9]['snippet'] + varab['results'][21]['snippet'] + varab['results'][22]['snippet']
print(allsnips)
s.sendto(str(allsnips).encode('utf-8'),(HOST,PORTA))
##print(contents)
