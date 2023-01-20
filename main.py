import os
from pathlib import Path
import pandas as pd
import wget


def get_config(product_code):
    df = pd.read_json('config.json')
    result_df = df.loc[df['product_code'] == product_code]

    return result_df


def upload_file(file):
    file_name = "/ic_logo.png"
    directory = "/home/luiza/Pictures"

    wget.download(file, directory + file_name)


def upload_logos():
    product_config = get_config('A')
    app_logos = product_config['custom_interface'].values[0]['app_icon']
    # sizes: 108x108, 162x162, 216x216, 324x324 e 432x432
    for logo in app_logos:
        print(app_logos[logo])
        upload_file(app_logos[logo])


if __name__ == '__main__':
    upload_logos()
