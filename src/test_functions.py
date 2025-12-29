"""
Script de verificación rápida para las funciones del challenge.
Ejecuta cada función y verifica que retornen datos válidos.
"""

import time
from datetime import date
from q1_time import q1_time
from q1_memory import q1_memory
from q2_time import q2_time
from q2_memory import q2_memory
from q3_time import q3_time
from q3_memory import q3_memory

# Ruta al archivo de datos
FILE_PATH = "../farmers-protest-tweets-2021-2-4.json"

def test_function(func_name, func, expected_type):
    """Prueba una función y mide su tiempo de ejecución."""
    print(f"\n{'='*60}")
    print(f"Testing: {func_name}")
    print('='*60)

    try:
        start = time.time()
        result = func(FILE_PATH)
        elapsed = time.time() - start

        # Validaciones básicas
        assert isinstance(result, list), f"Result should be a list, got {type(result)}"
        assert len(result) == 10, f"Should return 10 items, got {len(result)}"
        assert all(isinstance(item, tuple) for item in result), "All items should be tuples"

        print(f"✓ Tiempo: {elapsed:.2f}s")
        print(f"✓ Retornó {len(result)} resultados")
        print(f"✓ Primeros 3 resultados:")
        for i, item in enumerate(result[:3], 1):
            print(f"  {i}. {item}")

        return result, elapsed

    except Exception as e:
        print(f"✗ Error: {str(e)}")
        raise

def main():
    print("\n" + "="*60)
    print("VERIFICACIÓN DE FUNCIONES - CHALLENGE DATA ENGINEERING")
    print("="*60)

    results = {}

    # Test Q1
    print("\n\n### Q1: Top 10 Fechas con Más Tweets ###")
    q1_time_res, q1_time_elapsed = test_function("q1_time", q1_time, (date, str))
    q1_mem_res, q1_mem_elapsed = test_function("q1_memory", q1_memory, (date, str))

    # Verificar que ambas versiones dan el mismo resultado
    assert q1_time_res == q1_mem_res, "Q1: Time and Memory versions should return same results"
    print(f"\n✓ Q1: Ambas versiones retornan resultados idénticos")
    print(f"  - Diferencia de tiempo: {abs(q1_time_elapsed - q1_mem_elapsed):.2f}s")

    # Test Q2
    print("\n\n### Q2: Top 10 Emojis ###")
    q2_time_res, q2_time_elapsed = test_function("q2_time", q2_time, (str, int))
    q2_mem_res, q2_mem_elapsed = test_function("q2_memory", q2_memory, (str, int))

    assert q2_time_res == q2_mem_res, "Q2: Time and Memory versions should return same results"
    print(f"\n✓ Q2: Ambas versiones retornan resultados idénticos")
    print(f"  - Diferencia de tiempo: {abs(q2_time_elapsed - q2_mem_elapsed):.2f}s")

    # Test Q3
    print("\n\n### Q3: Top 10 Usuarios Más Mencionados ###")
    q3_time_res, q3_time_elapsed = test_function("q3_time", q3_time, (str, int))
    q3_mem_res, q3_mem_elapsed = test_function("q3_memory", q3_memory, (str, int))

    assert q3_time_res == q3_mem_res, "Q3: Time and Memory versions should return same results"
    print(f"\n✓ Q3: Ambas versiones retornan resultados idénticos")
    print(f"  - Diferencia de tiempo: {abs(q3_time_elapsed - q3_mem_elapsed):.2f}s")

    # Resumen final
    print("\n\n" + "="*60)
    print("RESUMEN DE TIEMPOS")
    print("="*60)
    print(f"{'Función':<20} {'Tiempo (s)':>15}")
    print("-"*60)
    print(f"{'q1_time':<20} {q1_time_elapsed:>15.2f}")
    print(f"{'q1_memory':<20} {q1_mem_elapsed:>15.2f}")
    print(f"{'q2_time':<20} {q2_time_elapsed:>15.2f}")
    print(f"{'q2_memory':<20} {q2_mem_elapsed:>15.2f}")
    print(f"{'q3_time':<20} {q3_time_elapsed:>15.2f}")
    print(f"{'q3_memory':<20} {q3_mem_elapsed:>15.2f}")
    print("="*60)

    print("\n✓✓✓ TODAS LAS PRUEBAS PASARON EXITOSAMENTE ✓✓✓\n")

if __name__ == "__main__":
    main()
