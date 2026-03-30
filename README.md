# Proyecto SAM Analyzer

Proyecto para analizar archivos SAM y contar lecturas con MAPQ = 60.

## Instalación

```bash
git clone https://github.com/manualfaros/proyecto_sam_curso_csic.git
cd proyecto-sam
```

## Uso

```bash
uv run python main.py archivo.sam
```

O con Nextflow:

```bash
nextflow run main.nf --sam archivo.sam
```

## Salida

WT.sam
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ Estadística                 ┃ Valor    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━┩
│ Total de lecturas alineadas │ 29190702 │
│ Lecturas con MAPQ = 60      │ 16488973 │
│ Porcentaje                  │ 56.5%    │
└─────────────────────────────┴──────────┘
Total de lecturas alineadas: 29190702
Lecturas con MAPQ = 60: 16488973
Porcentaje: 56.5%
...
test.sam

Total de lecturas alineadas: 153284
Lecturas con MAPQ = 60: 81234
Porcentaje: 53.0%
```

## Archivos

- `main.py` - Script de análisis
- `main.nf` - Pipeline Nextflow
- `pyproject.toml` - Dependencias
- `test.sam` - Un archivo SAM para probar los scripts.
- `uv.lock`  - Guarda las versiones exactas de las dependencias
- `Memoria.docx` - La memoria del proyecto.