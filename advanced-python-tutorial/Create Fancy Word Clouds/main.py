# pip install wordcloud numpy matplotlib pillow

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

#text = "Hello World"
text = open('random.txt', 'r').read()
print(STOPWORDS)

python_mask = np.array(PIL.Image.open("music.png"))

colormap = ImageColorGenerator(python_mask)

#wc = WordCloud(stopwords=["luci"]).generate(text)
wc = WordCloud(stopwords=set(list(STOPWORDS)+["luci"]),
                mask=python_mask,
                background_color="white",
                contour_color="black",
                contour_width=3,
                min_font_size=3,
                max_font_size=100).generate(text)

wc.recolor(color_func=colormap)
plt.imshow(wc)
plt.axis("off")
plt.show()