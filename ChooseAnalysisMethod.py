class ChooseAnalysisMethod:
    """
    どの分析方法を実行するかを選択するクラス
    """

    def __init__(self, analyzer):
        self.analyzer = analyzer

    def run(self):
        print("\n=== ANALYSIS MENU ===")
        print("1 → 記述統計")
        print("2 → 欠損値チェック")
        print("3 → クロス集計")
        print("4 → 相関分析")
        print("5 → 可視化")
        print("6 → 回帰分析（SPSS）")
        print("0 → 全て実行")

        choice = input("\nChoose method → ")

        if choice == "1":
            self.analyzer.descriptive_stats()
        elif choice == "2":
            self.analyzer.missing_values()
        elif choice == "3":
            self.analyzer.crosstab_region_strikes()
        elif choice == "4":
            self.analyzer.correlation_matrix()
        elif choice == "5":
            self.analyzer.visualize()
        elif choice == "6":
            self.analyzer.regression()
        else:
            # 全て実行
            self.analyzer.descriptive_stats()
            self.analyzer.missing_values()
            self.analyzer.crosstab_region_strikes()
            self.analyzer.correlation_matrix()
            self.analyzer.visualize()
            self.analyzer.regression()
