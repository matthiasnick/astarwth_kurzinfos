#!/bin/bash

# Überflüssige erste Seite von PDFs entfernen
for f in *.pdf
do
	pdftk A=$f cat A2-3 output dummy.pdf
	mv dummy.pdf $f
done

