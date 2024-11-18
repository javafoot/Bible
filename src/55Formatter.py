
content = []
with open("55dayPrayers.txt",encoding='UTF-8') as f:
   for line in f:
       content.append(line)
    
with open("55dayPrayers.txt22",'wt',encoding='UTF-8') as f:
   for line in content:
       f.write(line)
       f.write('\n')

