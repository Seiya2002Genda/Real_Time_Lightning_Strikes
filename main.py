from SetTarget import SetTarget
from ChangeTarget import ChangeTarget
from PrintTarget import PrintTarget
from AnalysisTarget import AnalysisTarget
from ChooseAnalysisMethod import ChooseAnalysisMethod


def main():

    # 1. ファイル名設定
    target = SetTarget().get_target()

    # 2. CSV読み込み
    df = ChangeTarget(target).load()

    # 3. 表示
    PrintTarget(df).show()

    # 4. 分析クラス生成
    analyzer = AnalysisTarget(df)

    # 5. メソッド選択
    ChooseAnalysisMethod(analyzer).run()


if __name__ == "__main__":
    main()
