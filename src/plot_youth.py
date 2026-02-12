import pandas as pd
import matplotlib.pyplot as plt
from src.config import FIGURES

def main():
    FIGURES.mkdir(parents=True, exist_ok=True)

    # 仮データ（後で実データに置き換える）
    df = pd.DataFrame({
        "year": [2000, 2005, 2010, 2015, 2020, 2022],
        "hyogo_15_29": [1, 1, 1, 1, 1, 1],
        "japan_15_29": [1, 1, 1, 1, 1, 1],
    })

    fig, ax = plt.subplots()
    ax.plot(df["year"], df["hyogo_15_29"], label="Hyogo (15-29)")
    ax.plot(df["year"], df["japan_15_29"], label="Japan (15-29)")
    ax.set_title("Youth population trend (placeholder)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Population (placeholder)")
    ax.legend()

    out = FIGURES / "output1_youth_trend_placeholder.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    print(f"Saved: {out}")

if __name__ == "__main__":
    main()
