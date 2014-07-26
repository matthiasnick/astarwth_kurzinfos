#!/usr/bin/python
# coding=utf-8
import xml.etree.ElementTree as ET
tree = ET.parse('lernraeume.xml')
root = tree.getroot()
roomnr = len(root.findall('room'))
f = open('liste1.tex', 'w')
f.write('\\centering')
f.write('\\setlength{\\tabcolsep}{3pt}\n')
f.write('\\begin{longtabu} to 1.002\\linewidth {|c|c|c|c|c|c|ccccc|X|}\n')
f.write('\\hline\n')
f.write('\\multirow{2}{*}{Gebäude} & \\multirow{2}{*}{Adresse} & \\multirow{2}{*}{Pl.} & \\multirow{2}{*}{Raumbez.} & \\multicolumn{2}{c|}{\\multirow{2}{*}{Öffnungszeiten}} & \\multicolumn{5}{c|}{\\multirow{2}{*}{Ausstattung}} & \\centering \\multirow{2}{*}{\\centering Bemerkungen}\\\\\n')
f.write('&&&&\\multicolumn{2}{c|}{~}&&&&&&\\\\\\hline\n')
f.write('\\endfirsthead\n\\hline\n\n')
grey = 1
i = 0
for room in root.findall('room'):
    i = i + 1
    if (i == 19):
        grey = 1
        f.write('\\end{longtabu}\n')
        f.close()
        f = open('liste2.tex', 'w')
        f.write('\\centering')
        f.write('\\setlength{\\tabcolsep}{3pt}\n')
        f.write('\\begin{longtabu} to 1.000\\linewidth {|c|c|c|c|c|c|ccccc|X|}\n')
        f.write('\\hline\n')
        f.write('\\multirow{2}{*}{Gebäude} & \\multirow{2}{*}{Adresse} & \\multirow{2}{*}{Pl.} & \\multirow{2}{*}{Raumbez.} & \\multicolumn{2}{c|}{\\multirow{2}{*}{Öffnungszeiten}} & \\multicolumn{5}{c|}{\\multirow{2}{*}{Ausstattung}} & \\centering \\multirow{2}{*}{\\centering Bemerkungen}\\\\\n')
        f.write('&&&&\\multicolumn{2}{c|}{~}&&&&&&\\\\\\hline\n')
        f.write('\\endfirsthead\n\\hline\n\n')
    if grey == 1:
        grey = 0
        color = '\\rg'
    else:
        grey = 1
        color = '\\rw'
    f.write(color)
    f.write(' &&&& ')
    f.write(room.find('open-l1').find('days').text.encode('utf-8'))
    f.write(' & ')
    f.write(room.find('open-l1').find('time').text.encode('utf-8'))
    f.write(' &&&&&& \\\\\n')
    f.write(color)
    f.write(' &&&& ')
    f.write(room.find('open-l2').find('days').text.encode('utf-8'))
    f.write(' & ')
    f.write(room.find('open-l2').find('time').text.encode('utf-8'))
    f.write(' &&&&&& \\\\\n')
    f.write(color)
    f.write(' \\mr{2.2cm}{')
    f.write(room.find('build-name').text.encode('utf-8'))
    f.write('} & \\mr{2.5cm}{\\href{http://maps.rwth-aachen.de/app/index.html?b=')
    f.write(room.find('build-nr').text.encode('utf-8'))
    f.write('}{')
    f.write(room.find('address').text.encode('utf-8'))
    f.write('}} & \\mr{0.7cm}{')
    f.write(room.find('seats').text.encode('utf-8'))
    f.write('} & \\mr{2.2cm}{')
    f.write(room.find('room-name').text.encode('utf-8'))
    f.write('} & ')
    f.write(room.find('open-l3').find('days').text.encode('utf-8'))
    f.write(' & ')
    f.write(room.find('open-l3').find('time').text.encode('utf-8'))
    f.write(' & ')
    if (room.find('specials').find('accessibility').text == 'true'):
        f.write('\\access'.encode('utf-8'))
    elif (room.find('specials').find('accessibility').text == 'false'):
        f.write('\\noaccess'.encode('utf-8'))
    else:
        f.write('\\dash'.encode('utf-8'))
    f.write(' & ')
    if (room.find('specials').find('wifi').text == 'true'):
        f.write('\\wifi'.encode('utf-8'))
    elif (room.find('specials').find('wifi').text == 'false'):
        f.write('\\nowifi'.encode('utf-8'))
    else:
        f.write('\\dash'.encode('utf-8'))
    f.write(' & ')
    if (room.find('specials').find('rj45').text == 'true'):
        f.write('\\ethernet'.encode('utf-8'))
    elif (room.find('specials').find('rj45').text == 'false'):
        f.write('\\noethernet'.encode('utf-8'))
    else:
        f.write('\\dash'.encode('utf-8'))
    f.write(' & ')
    if (room.find('specials').find('power').text == 'true'):
        f.write('\\power'.encode('utf-8'))
    elif (room.find('specials').find('power').text == 'false'):
        f.write('\\nopower'.encode('utf-8'))
    else:
        f.write('\\dash'.encode('utf-8'))
    f.write(' & ')
    if (room.find('specials').find('silent').text == 'true'):
        f.write('\\silent'.encode('utf-8'))
    elif (room.find('specials').find('silent').text == 'false'):
        f.write('\\nosilent'.encode('utf-8'))
    else:
        f.write('\\dash'.encode('utf-8'))
    f.write(' & ')
    if (room.find('comment').text != None):
        f.write('\\mr{3.8cm}{\\scriptsize \\raggedright ')
        f.write(room.find('comment').text.encode('utf-8'))
        f.write('}')
    f.write('\\\\\\hline\n\n')

f.write('\\end{longtabu}\n')
f.close()
