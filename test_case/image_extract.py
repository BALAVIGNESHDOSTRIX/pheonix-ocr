import requests

img_data = requests.get("https://media.nngroup.com/media/articles/opengraph_images/Slide31articlestext-over-images.png").content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)