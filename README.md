# :camera: Upload Image

upload image using Python and local mockup

## :octocat: Installation

Clone the repository

```bash

git@github.com:LuizaAlanis/upload-image.git

```

## :snake: Usage

The idea is simple. We have a kind of mockup: config.json that contains all image url. And we will make a filter to upload each information:

```python

# loop for upload icons
def upload_logos():

    # search on json file where product config equals 'A'
    product_config = get_config('A')
    
    # start to look at app logo, inside of json
    app_logos = product_config['custom_interface'].values[0]['app_icon']
    
    '''
      call the function using a loop, and enter the image size plus image name. 
      in my case, i'll use this for dinamic mobile logo.
    
      app logo sizes: 108x108, 162x162, 216x216, 324x324 and 432x432.
    '''
    for logo in app_logos:
        print(app_logos[logo])
        upload_file(app_logos[logo], logo)
```
