#!/bin/bash

./umlaute.sh main.tex
cd texte
for f in *.tex
do
	./"../umlaute.sh" $f
done
cd ..


