#!/usr/bin/env nextflow

/*
 * Parameter: path to SAM file
 */

params.sam = "$HOME/dia9/nf/2-Align/WT.sam"

/*
 * Process
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
 * Main workflow
 */

workflow {
    analyze_sam(params.sam)
}

