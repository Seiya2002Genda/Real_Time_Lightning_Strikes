class SetTarget:
    """
    CSVファイル名を設定するクラス
    """

    def __init__(self, filename="lightning.csv"):
        self.filename = filename

    def get_target(self):
        return self.filename
