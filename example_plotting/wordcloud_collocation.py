import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import dhlab.text.conc_coll
import dhlab.api.dhlab_api

search_term = "jul"

# Use DHLab to set up a corpus that we sample the collocation counts from
corpus_type = "digibok"
print("Getting corpus", flush=True)
corpus = dhlab.api.dhlab_api.document_corpus(
    doctype=corpus_type,
    from_year=1980,  # 1990
    to_year=1989,  # 1999
    limit=20_000,
    fulltext=search_term,
)

# Get the reference frequencies
reference = pd.read_csv(
    "https://raw.githubusercontent.com/NationalLibraryOfNorway/dhlab-app-collocations/refs/heads/main/reference/nob-nno_1800_2022.csv"
)
reference.columns = ["word", "freq"]
reference = reference.set_index("word")

# Fetch the collocation counts
print("Getting collocations", flush=True)
colls = (
    dhlab.text.conc_coll.Collocations(words=search_term, corpus=corpus, reference=reference)
    .coll.sort_values("relevance", ascending=False)
    .head(20)["relevance"]
    .to_dict()
)

# Remove all words that are equal to the search term
to_delete = [key for key in colls if key.lower() == search_term]
for key in to_delete:
    del colls[key]


# Create the wordcloud
## First, we create a circular mask
x, y = np.ogrid[:3000, :3000]
mask = (x - 1500) ** 2 + (y - 1500) ** 2 > 1300**2
mask = 255 * mask.astype(int)
## Create the word cloud using the circular mask
wc = WordCloud(background_color="white", repeat=True, mask=mask)
wc.generate_from_frequencies(colls)

## Save the wordcloud
plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
plt.savefig("collocations.pdf")
plt.show()
