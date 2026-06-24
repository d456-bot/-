
from __future__ import annotations

import os

# данные из условия 2.5 (внутренними сопротивлениями пренебрегаем)
E1 = 2.0
E2 = 1.0
R1 = 1000.0
R2 = 500.0
R3 = 200.0
RG = 200.0


def solve_galvanometer_25() -> dict[str, float]:
    denom = R1 * (R2 + R3) + R1 * RG + (R2 + R3) * RG
    i_r1 = (E1 * RG + E2 * (R2 + R3)) / denom
    i_left = (i_r1 * R1 - E1) / (R2 + R3)
    i_g = -i_left - i_r1

    return {
        "I_R1": i_r1,
        "I_left": i_left,
        "I_galvanometer": i_g,
        "I_galvanometer_mA": i_g * 1000.0,
    }


def format_output(currents: dict[str, float]) -> str:

    lines = [
        "ЛР №2, задание 2.5. Ток гальванометра",
        "=" * 40,
        f"E1 = {E1} В, E2 = {E2} В",
        f"R1 = {R1} Ом, R2 = {R2} Ом, R3 = {R3} Ом, Rg = {RG} Ом",
        "",
        "Решение по законам Кирхгофа:",
        f"  Ток через R1:        {currents['I_R1']:.6f} А",
        f"  Ток через левую ветвь: {currents['I_left']:.6f} А",
        f"  Ток гальванометра:   {currents['I_galvanometer']:.6f} А",
        f"  Ток гальванометра:   {currents['I_galvanometer_mA']:.4f} мА",
        "",
        "Направление тока в гальванометре совпадает с выбранным",
        "положительным направлением в правой ветви цепи.",
    ]
    return "\n".join(lines)


def save_output_image(text: str) -> None:
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        return

    report_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Report")
    os.makedirs(report_dir, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.axis("off")
    ax.text(0.02, 0.98, text, va="top", ha="left", family="monospace", fontsize=10)
    path = os.path.join(report_dir, "lab2_galvanometer_output.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Скриншот сохранён: {path}")


def main() -> None:
    currents = solve_galvanometer_25()
    output = format_output(currents)
    print(output)
    save_output_image(output)


if __name__ == "__main__":
    main()
