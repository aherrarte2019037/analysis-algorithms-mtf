from pathlib import Path
from mtf_linked_list import mtf_linked, imtf_linked
from cases import CASES, INITIAL_CONFIG

ALGO_MAP = {
    "mtf_linked": mtf_linked,
    "imtf_linked": imtf_linked,
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
            fh.write(f"Total access cost: {total}\n\n")
    print(f"Reporte generado en {output_path.resolve()}")

if __name__ == "__main__":
    generate_report() 