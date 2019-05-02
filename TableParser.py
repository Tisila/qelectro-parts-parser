from PIL import Image

def valuesToTable(first, second, third, fourth):
    line = '| {} | {} | {} | {} |\n'.format(first, second, third, fourth)
    return line

newfile = '| Label | Type | Designation | Manufacturer |\n'
newfile += '| --------------- | --------------- | --------------- | --------------- |\n'

with open('parts.csv','r') as file:

    for i, line in enumerate(file):
        if i > 3 or line == '':

            col = line.split(';')
            qet = col[3]
            label = col[5]
            designation = col[7]
            manufacturer = col[11]

            if qet == 'Corner' or qet == 'Splice' or qet == 'Ground':
                piu='piu'
            else: newfile += valuesToTable(label,qet,designation, manufacturer)
        
with open('parts.md', 'w') as mdfile: mdfile.write(newfile)

input('Generate the PNG file!')

base = Image.open('5_lista_de_artigos.png')
table = Image.open('parts.png')
newtable = table.resize((int(0.85*800),int(0.68*873)), Image.LANCZOS)
base.paste(newtable,(250,50))
base.save('5_lista_de_artigos.png')