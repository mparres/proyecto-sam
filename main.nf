#!/usr/bin/env nextflow

/*
 * Parámetro de entrada: ruta al fichero SAM
 */

params.sam = "$HOME/dia9/nf/2-Align/WT.sam"

/*
 * Proceso que ejecuta el script Python
 */

process analyze_sam {
    publishDir "results/", mode: 'copy'

    input:
    path sam_file

    output:
    file "resultado.txt"

    script:
    """
    uv run python $HOME/proyecto-sam/main.py ${sam_file} > resultado.txt
    """
}

/*
 * Workflow principal
 */

workflow {
    analyze_sam(params.sam)
}

