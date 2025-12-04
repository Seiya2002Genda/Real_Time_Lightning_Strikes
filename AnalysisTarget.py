import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class AnalysisTarget:
    """
    Excel + SPSS レベルの分析をすべて搭載したクラス
    記述統計、クロス集計、相関分析、可視化、簡易回帰
    """

    def __init__(self, df):
        self.df = df

    # --- 1. 記述統計 ---
    def descriptive_stats(self):
        print("\n=== DESCRIPTIVE STATISTICS ===")
        print(self.df.describe())
        return self.df.describe()

    # --- 2. 欠損値チェック ---
    def missing_values(self):
        print("\n=== MISSING VALUES ===")
        print(self.df.isnull().sum())
        return self.df.isnull().sum()

    # --- 3. クロス集計（SPSS頻度表）---
    def crosstab_region_strikes(self):
        if 'Region' in self.df.columns and 'Strikes' in self.df.columns:
            print("\n=== CROSSTAB: Region × Strikes (平均) ===")
            ct = self.df.groupby("Region")["Strikes"].mean()
            print(ct)
            return ct
        else:
            print("[WARNING] 必要な列がありません")
            return None

    # --- 4. 相関分析 (SPSS: Correlation Matrix) ---
    def correlation_matrix(self):
        print("\n=== CORRELATION MATRIX ===")
        corr = self.df.corr(numeric_only=True)
        print(corr)
        return corr

    # --- 5. 可視化（Excelグラフ再現）---
    def visualize(self):
        print("\n=== VISUALIZATION: 軽微なグラフ生成 ===")

        # 折れ線グラフ
        if "Date" in self.df.columns and "Strikes" in self.df.columns:
            plt.figure(figsize=(8, 4))
            plt.plot(self.df["Date"], self.df["Strikes"])
            plt.title("Strikes Over Time")
            plt.xlabel("Date")
            plt.ylabel("Strikes")
            plt.show()

        # 散布図
        if "Strikes" in self.df.columns and "Energy" in self.df.columns:
            sns.scatterplot(data=self.df, x="Strikes", y="Energy")
            plt.title("Strikes vs Energy")
            plt.show()

    # --- 6. 簡易回帰分析（SPSSの線形回帰）---
    def regression(self):
        if "Strikes" not in self.df.columns or "Energy" not in self.df.columns:
            print("[WARNING] 回帰に必要な変数が存在しません。")
            return None

        print("\n=== SIMPLE LINEAR REGRESSION (Energy ~ Strikes) ===")

        x = self.df["Strikes"]
        y = self.df["Energy"]

        coef = np.polyfit(x, y, 1)
        slope, intercept = coef

        print(f"回帰式: Energy = {round(intercept, 3)} + {round(slope, 3)} * Strikes")

        return {"intercept": intercept, "slope": slope}
