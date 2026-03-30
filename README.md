# proyecto-sam
Script para analizar un fichero SAM y contar las lecturas alineadas

# Descripción
Lee un fichero SAM y calcula:
-Total de lecturas alineadas
-Número de lecturas con MAPQ = 60
-El porcentaje que representan sobre el total

# Requisitos
Requiere Python3, uv y Nextflow

Para instalar las dependencias: uv add rich

# Uso
Ejecutar directamente con Python:
uv run python main.py fichero.sam

Ejecutar con Nextflow:
nextflow run main.nf --sam fichero.sam

# Ejemplo
uv run python main.py ~/dia9/nf/2-Align/WT.sam

# Resultado esperado
Total de lecturas alineadas: 29190702
Lecturas con MAPQ = 60: 16488973
Porcentaje: 56.5 %
