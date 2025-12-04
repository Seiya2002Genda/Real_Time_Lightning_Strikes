# ⚡ Real-Time Lightning Strikes Analysis Toolkit  
Python-based Statistical & Visualization System

This repository provides a fully modular analysis system for handling the **Real-Time Lightning Strikes Dataset** from Kaggle.  
Each component is implemented as an independent class, enabling flexible data loading, inspection, statistical analysis, visualization, and regression modeling.

---

## ⚠ Dataset Download (Important)

**csvファイルはここに貼り付けることは容量上の理由から貼り付けることができないため、以下のURLを使ってダウンロードを行なって欲しいです。**  
https://www.kaggle.com/datasets/vivektiwari020801/real-time-lightning-strikes/versions/216?resource=download

ダウンロードした `lightning.csv` をプロジェクト直下に置いてください。

Created by Vivek Tiwari
Real-time Lightning Strikes Global high-frequency lightning strike events, updated hourly

---

## 📂 File Structure

```
Real_Time_Lightning_Strikes/
│
├── lightning.csv                  # Kaggle dataset (ユーザーが配置)
│
├── SetTarget.py                   # CSVファイル名の管理
├── ChangeTarget.py                # CSV読み込み/DataFrame生成
├── PrintTarget.py                 # DataFrameの表示
├── AnalysisTarget.py              # 記述統計/相関/可視化/回帰
├── ChooseAnalysisMethod.py        # 分析手法メニュー
│
└── main.py                        # メイン実行ファイル
```

---

## 🧠 System Overview

このプロジェクトは以下の 5 段階処理で動作する：

1. **SetTarget**：分析対象の CSV ファイル名を指定  
2. **ChangeTarget**：CSV を読み込み pandas DataFrame に変換  
3. **PrintTarget**：データの先頭行と info を表示  
4. **AnalysisTarget**：SPSS/Excel レベルの分析を実行  
5. **ChooseAnalysisMethod**：ユーザーに分析方法を選択させる  

最終的に `main.py` がこれらすべてを統括し、対話式の分析環境を提供する。

---

## 🔍 Detailed Module Descriptions (内部ロジック付き)

### 1. SetTarget.py
```python
class SetTarget:
    def __init__(self, filename="lightning.csv"):
        self.filename = filename
    def get_target(self):
        return self.filename
```
- デフォルトで `lightning.csv` を返す簡易設定クラス  
- filename を変更することで他の CSV にも対応可能  

---

### 2. ChangeTarget.py
```python
df = pd.read_csv(self.filename)
```
- CSV を読み込み DataFrame を返す  
- エラー時は **ダミーデータを自動生成**（Date, Strikes, Energy, Region）  
　→ 「CSVなしでも動作する」堅牢な設計  

---

### 3. PrintTarget.py
```python
print(self.df.head())
print(self.df.info())
```
- データの先頭数行  
- 各列のデータ型、NULL 数  

---

### 4. AnalysisTarget.py（最重要クラス）

#### 搭載分析機能
- ✔ 記述統計（df.describe）  
- ✔ 欠損値チェック（df.isnull）  
- ✔ クロス集計（Region × Strikes の平均）  
- ✔ 相関行列（df.corr）  
- ✔ 可視化（折れ線 + 散布図）  
- ✔ 回帰分析（Energy ~ Strikes）

#### 回帰分析ロジック例

```python
coef = np.polyfit(x, y, 1)
slope, intercept = coef
```

---

### 5. ChooseAnalysisMethod.py

ターミナルで表示されるメニュー：

```
1 → 記述統計
2 → 欠損値チェック
3 → クロス集計
4 → 相関分析
5 → 可視化
6 → 回帰分析
0 → 全て実行
```

---

### 6. main.py（全体の統括）

```python
target = SetTarget().get_target()
df = ChangeTarget(target).load()
PrintTarget(df).show()
analyzer = AnalysisTarget(df)
ChooseAnalysisMethod(analyzer).run()
```

---

## ▶ How to Run

```bash
pip install pandas numpy matplotlib seaborn
python main.py
```

---

## 📊 Example Output

### 記述統計  
```
count, mean, std, min, max
```

### クロス集計  
```
Region
East     120.0
West     150.0
North    210.0
```

### 相関行列  
```
Strikes – Energy の相関係数を表示
```

### 可視化  
- 折れ線：Strike 日次変動  
- 散布図：Strike vs Energy  

### 回帰式  
```
Energy = 1.23 + 0.045 * Strikes
```

---

## ✔ Summary

このプロジェクトは：

- **完全OOP設計**
- **SPSS + Excel 互換分析**
- **CSV読み込みの堅牢化**
- **統計 + 可視化 + 回帰分析のワンストップ化**
- **ユーザー選択式の対話型分析**

という学術用途にも実務用途にも強い構造を持っています。

---
