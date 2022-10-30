import requests
import pandas as pd
from pathlib import Path


def download(path, name: str):
    name = name.replace(" ", "").replace("'", "").replace("&", "").replace(".", "")
    url = f"https://lol-skin.weblog.vc/img/champion/{name}.png"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        print(200)
        with open(f"{path}/{name}.png", 'wb') as f:
            f.write(response.content)


if __name__ == '__main__':
    # get file paths
    path = Path('/').joinpath(Path().resolve(), 'champion')

    # champion list
    df = pd.read_csv('champion_list.csv')
    champion_list = list(df["英文名稱"])
    # print(champion_list)
    # print(len(champion_list))

    count = 0
    for champion in champion_list:
        download(path, champion)
        print(f'{count}. {champion} OK')
        print("---")
        count += 1