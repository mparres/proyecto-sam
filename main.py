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

    for line in f:
        line = line.strip()

        #Skip header lines (start with @)
        if not line.startswith('@'):
 
            columns = line.split('\t')
 
            mapq = int(columns[4])
 
            total_reads += 1
 
            if mapq ==60:
                mapq60_reads += 1

percentage = mapq60_reads / total_reads * 100

#Display results using rich
console = Console ()
console.print ("[bold]Total aligned reads:[/bold]", total_reads)
console.print ("[bold green]Reads with MAPQ = 60:[/bold green]", mapq60_reads)
console.print ("[bold blue]Percentage:[/bold blue]", round(porcentaje, 1), "%")


