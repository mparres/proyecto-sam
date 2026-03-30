#Script para analizar un fichero SAM

import sys
from rich.console import Console

#definir ruta al fichero SAM
sam_file = sys.argv[1]

#Contadores
total_reads = 0
mapq60_reads = 0

#Abrir el fichero y leer línea a línea
with open(sam_file) as f:

    for linea in f:
        linea = linea.strip()

        #Ignorar líneas de cabecera (empiezan por @)
        if not linea.startswith('@'):
 
            columnas = linea.split('\t')
 
            mapq = int(columnas[4])
 
            total_reads += 1
 
            if mapq ==60:
                mapq60_reads += 1

porcentaje = mapq60_reads / total_reads * 100

#mostrar resulatdos con rich
console = Console ()
console.print ("[bold]Total de lecturas alineadas:[/bold]", total_reads)
console.print ("[bold green]Lecturas con MAPQ = 60:[/bold green]", mapq60_reads)
console.print ("[bold blue]Porcentaje:[/bold blue]", round(porcentaje, 1), "%")


