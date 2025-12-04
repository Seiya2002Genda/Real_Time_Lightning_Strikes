class PrintTarget:
    """
    DataFrame の中身・基本情報を出力するクラス
    """

    def __init__(self, df):
        self.df = df

    def show(self):
        print("\n=== TARGET DATA HEAD ===")
        print(self.df.head())

        print("\n=== DATA INFO ===")
        print(self.df.info())
