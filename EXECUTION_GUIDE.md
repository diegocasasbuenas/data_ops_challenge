# Guía de Ejecución - Challenge Data Engineering

## Instalación de Dependencias

```bash
cd challenge_data_ops_eng
pip install -r requirements.txt
```

## Estructura de Archivos

```
challenge_data_ops_eng/
├── farmers-protest-tweets-2021-2-4.json  # Dataset (389MB)
├── requirements.txt                       # Dependencias Python
├── src/
│   ├── q1_time.py                        # Q1 optimizado para tiempo
│   ├── q1_memory.py                      # Q1 optimizado para memoria
│   ├── q2_time.py                        # Q2 optimizado para tiempo
│   ├── q2_memory.py                      # Q2 optimizado para memoria
│   ├── q3_time.py                        # Q3 optimizado para tiempo
│   ├── q3_memory.py                      # Q3 optimizado para memoria
│   └── challenge.ipynb                   # Notebook con análisis completo
```

## Ejecución del Análisis

### Opción 1: Jupyter Notebook (Recomendado)

```bash
cd challenge_data_ops_eng/src
jupyter notebook challenge.ipynb
```

El notebook incluye:
- Importación de todas las funciones
- Ejecución y medición de tiempo de cada función
- Profiling de memoria con `memory_profiler`
- Comparación de resultados
- Análisis detallado y conclusiones

### Opción 2: Usar las Funciones Directamente

```python
from q1_time import q1_time
from q1_memory import q1_memory

# Ejecutar Q1
file_path = "../farmers-protest-tweets-2021-2-4.json"
result = q1_time(file_path)
print(result)
```

## Resultados Esperados

### Q1: Top 10 Fechas con Más Tweets
Formato: `[(datetime.date, str), ...]`
```python
[(datetime.date(2021, 2, 12), "username1"), ...]
```

### Q2: Top 10 Emojis Más Usados
Formato: `[(str, int), ...]`
```python
[("🙏", 5000), ("❤️", 4500), ...]
```

### Q3: Top 10 Usuarios Más Mencionados
Formato: `[(str, int), ...]`
```python
[("narendramodi", 2000), ("RahulGandhi", 1500), ...]
```

## Profiling de Performance

### Medir Tiempo de Ejecución

```python
import time

start = time.time()
result = q1_time(file_path)
elapsed = time.time() - start
print(f"Tiempo: {elapsed:.4f} segundos")
```

### Medir Memoria

```python
# En Jupyter Notebook
%load_ext memory_profiler
%memit q1_time(file_path)
```

```bash
# Desde línea de comandos
python -m memory_profiler script.py
```

## Notas Técnicas

### Estrategias de Optimización

**Time-Optimized:**
- Una sola pasada por el archivo
- Uso de Counter y defaultdict
- Mayor consumo de memoria
- Menor tiempo de ejecución

**Memory-Optimized:**
- Múltiples pasadas cuando es necesario
- Uso de dict básico
- Menor consumo de memoria
- Mayor tiempo de ejecución

### Manejo de Datos

- Encoding: UTF-8
- Formato: JSONL (una línea por tweet)
- Tamaño: ~389MB
- Campos utilizados: `date`, `user.username`, `content`, `mentionedUsers`

## Troubleshooting

### Error: FileNotFoundError
Asegúrate de que el archivo JSON esté en la carpeta `challenge_data_ops_eng/`

### Error: Memory Error
Si tienes problemas de memoria, usa las versiones `*_memory.py`

### Jupyter Kernel Issues
```bash
python -m ipykernel install --user --name=challenge
```

## Próximos Pasos

Para mejorar estas soluciones:
1. Implementar procesamiento paralelo (multiprocessing)
2. Usar formatos más eficientes (Parquet)
3. Agregar tests unitarios
4. Implementar logging y monitoreo
5. Considerar soluciones cloud (BigQuery, Spark)
