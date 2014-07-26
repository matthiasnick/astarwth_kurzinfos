#!/bin/bash

# Definiere Dateinamen
FILENAME="lernraeume_ws1314"
cp main.tex main_sw.tex
cp main.tex main_red.tex

# Erstelle bunte Version
pdflatex main.tex
mv main.pdf $FILENAME.pdf


# Erstelle schwarze Vorlage
sed -r -i 's/\\usepackage\{kurzinfo\}/\\usepackage\{kurzinfo\_sw\}/g' main_sw.tex
cp nowifi_print.pdf nowifi.pdf
cp noaccess_print.pdf noaccess.pdf
cp nopower_print.pdf nopower.pdf
cp nosilent_print.pdf nosilent.pdf
cp noethernet_print.pdf noethernet.pdf
cp wifi_print.pdf wifi.pdf
cp access_print.pdf access.pdf
cp power_print.pdf power.pdf
cp silent_print.pdf silent.pdf
cp ethernet_print.pdf ethernet.pdf

pdflatex main_sw.tex

mv main_sw.pdf $FILENAME"_sw.pdf"
rm -rf main_sw.tex main_sw.pdf

# Erstelle rote Vorlage
sed -r -i 's/\\usepackage\{kurzinfo\}/\\usepackage\{kurzinfo\_red\}/g' main_red.tex
sed -r -i 's/\\fcolorbox\{black\}\{light\}/\\fcolorbox\{white\}\{white\}/g' main_red.tex
cp nowifi_red.pdf nowifi.pdf
cp noaccess_red.pdf noaccess.pdf
cp nopower_red.pdf nopower.pdf
cp nosilent_red.pdf nosilent.pdf
cp noethernet_red.pdf noethernet.pdf
cp wifi_red.pdf wifi.pdf
cp access_red.pdf access.pdf
cp power_red.pdf power.pdf
cp silent_red.pdf silent.pdf
cp ethernet_red.pdf ethernet.pdf

pdflatex main_red.tex
mv main_red.pdf $FILENAME"_red.pdf"
rm -rf main_red.tex main_red.pdf

cp nowifi_online.pdf nowifi.pdf
cp noaccess_online.pdf noaccess.pdf
cp nopower_online.pdf nopower.pdf
cp nosilent_online.pdf nosilent.pdf
cp noethernet_online.pdf noethernet.pdf
cp wifi_online.pdf wifi.pdf
cp access_online.pdf access.pdf
cp power_online.pdf power.pdf
cp silent_online.pdf silent.pdf
cp ethernet_online.pdf ethernet.pdf
