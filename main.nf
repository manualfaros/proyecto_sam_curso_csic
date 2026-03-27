#!/usr/bin/env nextflow

// Pipeline para analizar archivo SAM

params.sam = null

// Proceso para analizar SAM
process analyze_sam {
    
    input:
    path sam_file
    
    script:
    """
    uv run python ${projectDir}/main.py ${sam_file}
    """
}

workflow {
    // Leer archivo SAM
    sam_channel = Channel.fromPath(params.sam)
    
    // Ejecutar análisis
    analyze_sam(sam_channel)
}