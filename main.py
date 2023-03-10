# imports
import os
from pathlib import Path
import pandas as pd
import wget

# product code = id
def get_config(product_code):
    df = pd.read_json('config.json')
    result_df = df.loc[df['product_code'] == product_code]
    # json that contains some product informations
    return result_df

# upload function
def upload_file(file, folder):
    file_name = "/ic_logo.png"
    directory = "/home/luiza/Pictures/"

    wget.download(file, directory + folder + file_name)

# loop for upload icons
def upload_logos():
    product_config = get_config('A')
    app_logos = product_config['custom_interface'].values[0]['app_icon']
    # sizes: 108x108, 162x162, 216x216, 324x324 e 432x432
    for logo in app_logos:
        print(app_logos[logo])
        upload_file(app_logos[logo], logo)


if __name__ == '__main__':
    upload_logos()
