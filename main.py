#Script to analyze a SAM file and report alignment statistics
#Python 3.11

#Script by Marina Parres
#2026-03-30

#input: SAM file
#output: total aligned reads, reads with MAPQ=60 and percentatge
#usage: uv run python main.py sample.sam


import sys
from rich.console import Console

#define path to SAM
sam_file = sys.argv[1]

#Counters
total_reads = 0
mapq60_reads = 0

#Open file and read line by line
with open(sam_file) as f:

    for linea in f:
        linea = linea.strip()

        #Skip header lines (start with @)
        if not linea.startswith('@'):
 
            columnas = linea.split('\t')
 
            mapq = int(columnas[4])
 
            total_reads += 1
 
            if mapq ==60:
                mapq60_reads += 1

porcentaje = mapq60_reads / total_reads * 100

#Display results using rich
console = Console ()
console.print ("[bold]Total de lecturas alineadas:[/bold]", total_reads)
console.print ("[bold green]Lecturas con MAPQ = 60:[/bold green]", mapq60_reads)
console.print ("[bold blue]Porcentaje:[/bold blue]", round(porcentaje, 1), "%")


