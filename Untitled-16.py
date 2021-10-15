from bs4 import BeautifulSoup
import requests
import os
import re

def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html
rosadirect = "D:/datasets/"
id, seq, start, total =[], [], [], []

f = open(rosadirect + "rosalind_mprt.txt","r")
lines = f.readlines()
for line in lines:
   id.append(line.replace("\n", ""))
f.close()
p = re.compile(r"N[^P](S|T)[^P]")
for ide in id :
   URL = "https://www.uniprot.org/uniprot/%s.fasta" % ide
   html = get_html(URL)
   soup = BeautifulSoup(html, 'html.parser')
   f = open(rosadirect + "temp.txt", "w")
   f.write(soup.getText())
   f.close()
   f = open(rosadirect + "temp.txt", "r")
   lines = f.readlines()
   seq= ""
   totemp=[]
   for j in range(1,len(lines)):
       seq = seq + lines[j].replace("\n","")

   for k in range(len(seq)+1):
        a = seq[k:]
        m = p.match(a)
        if m is not None:
           totemp.append(k+1)
   if totemp == [[]]:
      total.append('None')
   else:
      total.append(totemp)
   f.close()
   total = list(map(str,total))
for z in range(len(id)):
   if total[z] == '[]':
      continue
   else:
      print(id[z])
      print(total[z].replace("[","").replace("]","").replace(",",""))
os.remove(rosadirect+"temp.txt")