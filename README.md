# Proyecto SAM Analyzer

Proyecto para analizar archivos SAM y contar lecturas con MAPQ = 60.

## Instalación

```bash
git clone https://github.com/tu-usuario/proyecto-sam.git
cd proyecto-sam
uv sync
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

```
Total de lecturas alineadas: 153284
Lecturas con MAPQ = 60: 81234
Porcentaje: 53.0%
```

## Archivos

- `main.py` - Script de análisis
- `main.nf` - Pipeline Nextflow
- `pyproject.toml` - Dependencias
