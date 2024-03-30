# pip install textstat

from textstat import textstat

text1 = "The ethereal glow of the morning sun cast delicate hues across the idyllic meadow, where a symphony of birdsong filled the air. A gentle breeze rustled through the verdant leaves, while wildflowers swayed gracefully in the meadow's embrace. Nature's tapestry unfolded, captivating the senses with its timeless beauty."

print(textstat.flesch_reading_ease(text1))

text2 = "As the day unfolded, a solitary figure emerged, adorned in a flowing robe that billowed in the wind. With each step, the figure exuded an air of wisdom and mystery, their eyes gleaming with ancient knowledge. They approached a weathered stone, upon which intricate symbols were etched, as if whispering secrets of a forgotten time."

print(textstat.flesch_kincaid_grade(text2))
print(textstat.gunning_fog(text2))
print(textstat.automated_readability_index(text2))
print(textstat.coleman_liau_index(text2))
print(textstat.linsear_write_formula(text2))

text3 = "The figure raised their hands, tracing the symbols with a delicate touch. A surge of energy pulsed through the air, as the stone came alive with a soft, ethereal light. Words, written in an ancient language, glowed and swirled, forming a portal into another realm. The figure stepped forward, disappearing into the mystical gateway, leaving behind an aura of intrigue and wonder."

print(textstat.dale_chall_readability_score(text3))
print(textstat.difficult_words(text3))

text4 = "In this distant realm, mythical creatures roamed, their iridescent wings fluttering in harmony. The sky above was a mesmerizing canvas of vibrant hues, as if painted by the gods themselves. Majestic castles rose in the distance, their spires reaching towards the heavens, beckoning curious souls to unravel the secrets within."

print(textstat.difficult_words_list(text4))

"Time seemed to stand still in this enchanting world, where imagination danced and dreams took flight. It was a realm where ordinary boundaries dissolved, and the extraordinary became the norm. As the figure ventured deeper into this wondrous realm, new wonders awaited, promising untold adventures and endless possibilities."

"And so, the cup of text overflowed with a rich tapestry of imagery and complexity, inviting readers to delve into a realm of magic and mystery. Each word and phrase wove together to create a vivid landscape that sparked the imagination and beckoned the curious to explore the depths of their own creativity."

