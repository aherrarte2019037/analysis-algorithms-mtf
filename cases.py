from typing import List, Tuple

INITIAL_CONFIG: List[int] = [0, 1, 2, 3, 4]

SEQ_1: List[int] = [i % 5 for i in range(20)]
SEQ_2: List[int] = [
    4, 3, 2, 1, 0, 1, 2, 3, 4,
    3, 2, 1, 0, 1, 2, 3, 4,
]
BEST_SEQ: List[int] = [0] * 20
WORST_SEQ: List[int] = [4, 3, 2, 1, 0] * 4
REPEAT_2: List[int] = [2] * 20
REPEAT_3: List[int] = [3] * 20

CASES: List[Tuple[str, List[int], str]] = [
    (
        "Ejercicio 1: MTF - Secuencia 0,1,2,3,4 repetida",
        SEQ_1,
        "mtf",
    ),
    (
        "Ejercicio 2: MTF - Secuencia 4,3,2,1,0,...",
        SEQ_2,
        "mtf",
    ),
    (
        "Ejercicio 3: Mejor caso MTF (20 solicitudes)",
        BEST_SEQ,
        "mtf",
    ),
    (
        "Ejercicio 4: Peor caso MTF (20 solicitudes)",
        WORST_SEQ,
        "mtf",
    ),
    (
        "Ejercicio 5a: MTF - Repetición elemento 2",
        REPEAT_2,
        "mtf",
    ),
    (
        "Ejercicio 5b: MTF - Repetición elemento 3",
        REPEAT_3,
        "mtf",
    ),
    (
        "Ejercicio 6: IMTF sobre mejor caso de MTF",
        BEST_SEQ,
        "imtf",
    ),
    (
        "Ejercicio 6: IMTF sobre peor caso de MTF",
        WORST_SEQ,
        "imtf",
    ),
] 