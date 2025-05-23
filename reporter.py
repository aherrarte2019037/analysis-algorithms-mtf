from pathlib import Path
from importlib import import_module

from algorithms import mtf, imtf
from cases import CASES, INITIAL_CONFIG

ALGO_MAP = {
    "mtf": mtf,
    "imtf": imtf,
}


def generate_report(output_path: Path = Path("output.txt")) -> None:
    with output_path.open("w", encoding="utf-8") as fh:
        for title, sequence, algo_key in CASES:
            algo_func = ALGO_MAP[algo_key]
            fh.write("=" * 80 + "\n")
            fh.write(title + "\n")
            fh.write("-" * 80 + "\n")
            total, logs = algo_func(sequence, INITIAL_CONFIG)
            for line in logs:
                fh.write(line + "\n")
            fh.write(f"Total access cost ({algo_key.upper()}): {total}\n\n")
    print(f"Reporte generado en {output_path.resolve()}")


if __name__ == "__main__":
    generate_report() 