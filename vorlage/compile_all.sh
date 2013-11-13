#!/bin/bash

# Definiere Dateinamen
FILENAME="Ein-Kurzinfo"

# Erstelle bunte Version
pdflatex main.tex
mv main.pdf $FILENAME.pdf


# Erstelle schwarze Vorlage
sed -r -i 's/\\usepackage\{kurzinfo\}/\\usepackage\{kurzinfo\_sw\}/g' main.tex
pdflatex main.tex
mv main.pdf $FILENAME"_sw.pdf"


# Erstelle rote Vorlage
sed -r -i 's/\\usepackage\{kurzinfo\_sw\}/\\usepackage\{kurzinfo\_red\}/g' main.tex
sed -r -i 's/\\fcolorbox\{black\}\{light\}/\\fcolorbox\{white\}\{white\}/g' main.tex
cd texte
for f in *.tex
do
	sed -r -i 's/\\fcolorbox\{black\}\{light\}/\\fcolorbox\{white\}\{white\}/g' $f
done
cd ..

pdflatex main.tex
mv main.pdf $FILENAME"_red.pdf"


# Aufräumen
sed -r -i 's/\\usepackage\{kurzinfo\_red\}/\\usepackage\{kurzinfo\}/g' main.tex
sed -r -i 's/\\fcolorbox\{white\}\{white\}/\\fcolorbox\{black\}\{light\}/g' main.tex
cd texte
for f in *.tex
do
	sed -r -i 's/\\fcolorbox\{white\}\{white\}/\\fcolorbox\{black\}\{light\}/g' $f
done
cd ..


