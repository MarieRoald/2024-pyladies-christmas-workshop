from pathlib import Path
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import holoviews as hv
import pandas as pd
import seaborn as sns


# Load the recipe ingredients
recipe_parent = Path(__file__).parent / "recipes"
recipes = {
    recipe_file.stem: set(recipe_file.read_text().splitlines())
    for recipe_file in recipe_parent.glob("*.txt")
}

# Add space before ingredient names to place the captions nicely
for recipe, ingredients in recipes.copy().items():
    recipes[recipe] = {f"  {ingredient.capitalize()}" for ingredient in ingredients}


# Create inverse index pointing ingredients to their recipes
ingredient_lookup = defaultdict(set)
for recipe_name, ingredients in recipes.items():
    for ingredient in ingredients:
        ingredient_lookup[ingredient].add(recipe_name)


# Create edge lists on the format
# { 
#     'ingredient1': {'ingredient2': {'weight': n_12}, ...}
#     ...
# }
# Where `n_12` is the number of recipes where ingredient 1 and ingredient 2 co-occur.
edge_lists = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
for ingredient, recipe_names in ingredient_lookup.items():
    for recipe_name in recipe_names:
        for ingredient2 in recipes[recipe_name]:
            edge_lists[ingredient][ingredient2]["weight"] += 1

# Remove all self links. We don't want the following (notice the same ingredient in the key and value):
# {
#     'ingredient1': {'ingredient1': {'weight': n_11}}
#     ...
# }
for ingredient, edges in edge_lists.items():
    del edges[ingredient]

# Create NetworkX graph from the edge lists and convert into a Pandas dataframe
g = nx.from_dict_of_dicts(edge_lists)
g.remove_edges_from(nx.selfloop_edges(g))
links = nx.to_pandas_edgelist(g)

# Enumerate the ingredients
nodes = pd.Series({i: node for i, node in enumerate(edge_lists)}, name="name")
node_ids = {v: k for k, v in nodes.items()}
links = links.assign(
    source=links["source"].map(node_ids),
    target=links["target"].map(node_ids),
)
print(links.head(3))

# Create plot
hv.extension("matplotlib")
hv.output(size=500)

# Create a dataframe that maps the node id to the ingredient name
nodes = hv.Dataset(
    pd.DataFrame({"name": nodes, "group": 1}, index=nodes.index), "index"
)
print(nodes.data.head())

# Create the plot
chord = hv.Chord((links, nodes)).opts(
    hv.opts.Chord(
        labels="name",
        cmap=sns.color_palette(
            ["#287548", "#F9F7E7", "#E9BB4F", "#C58C35", "#800B1A", "#AB1818"],
            as_cmap=True,
        ),
        edge_cmap=sns.color_palette(
            ["#287548", "#F9F7E7", "#E9BB4F", "#C58C35", "#800B1A", "#AB1818"],
            as_cmap=True,
        ),
        edge_color=hv.dim("weight"),
        node_edgecolors=(0, 0, 0, 0),  # Set alpha to 0 to remove the border
        node_color=hv.dim("index").str(),
        edge_linewidth=2,
    )
)
fig = hv.render(chord, backend="matplotlib")

# Update the font size
for text in fig.axes[0].texts:
    text.set_size(24)
fig.savefig("something.pdf", dpi=300)
plt.show()
