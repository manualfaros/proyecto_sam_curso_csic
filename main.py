import sys
from rich.console import Console
from rich.table import Table

# Leer archivo SAM
archivo_sam = sys.argv[1]

total_lecturas = 0
lecturas_mapq60 = 0

# Abrir archivo
archivo = open(archivo_sam, 'r')

for linea in archivo:
    # Ignorar cabeceras
    if linea.startswith('@'):
        continue
    
    # Separar por tabuladores
    campos = linea.split('\t')
    
    # Contar lectura
    total_lecturas = total_lecturas + 1
    
    # MAPQ está en columna 5
    mapq = int(campos[4])
    
    if mapq == 60:
        lecturas_mapq60 = lecturas_mapq60 + 1

archivo.close()

# Calcular porcentaje
porcentaje = (lecturas_mapq60 / total_lecturas) * 100

# Imprimir con rich
console = Console()
tabla = Table()
tabla.add_column("Estadística")
tabla.add_column("Valor")
tabla.add_row("Total de lecturas alineadas", str(total_lecturas))
tabla.add_row("Lecturas con MAPQ = 60", str(lecturas_mapq60))
tabla.add_row("Porcentaje", f"{porcentaje:.1f}%")
console.print(tabla)

# Imprimir también en texto simple
print(f"Total de lecturas alineadas: {total_lecturas}")
print(f"Lecturas con MAPQ = 60: {lecturas_mapq60}")
print(f"Porcentaje: {porcentaje:.1f}%")

