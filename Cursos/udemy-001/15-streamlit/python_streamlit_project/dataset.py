from pathlib import Path
import json
import pandas as pd

BASE_DIR = Path(__file__).parent
file_path = BASE_DIR / "dados" / "vendas.json"

with open(file_path, encoding="utf-8") as file:
    data = json.load(file)

df = pd.DataFrame.from_dict(data)

df["Data da Compra"] = pd.to_datetime(df["Data da Compra"], format="%d/%m/%Y")
