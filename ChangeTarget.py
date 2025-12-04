import pandas as pd

class ChangeTarget:
    """
    CSVファイルを読み込み DataFrame を返すクラス
    """

    def __init__(self, filename):
        self.filename = filename

    def load(self):
        try:
            df = pd.read_csv(self.filename)
            print(f"[OK] {self.filename} を正常に読み込みました。")
            return df

        except FileNotFoundError:
            print(f"[WARNING] {self.filename} が見つかりません。ダミーデータを作成します。")

            data = {
                'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04']),
                'Strikes': [100, 150, 90, 210],
                'Energy': [5.5, 7.2, 4.8, 8.1],
                'Region': ['East', 'West', 'East', 'North']
            }
            return pd.DataFrame(data)
