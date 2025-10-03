import pandas as pd

# Cargar ratings
ratings = pd.read_csv("data/u.data", sep="\t", names=["user_id", "item_id", "rating", "timestamp"])
# Cargar películas
movies = pd.read_csv("data/u.item", sep="|", encoding="latin-1", 
                     names=["item_id", "title", "release_date", "video_release_date", "IMDb_URL",
                            "unknown","Action","Adventure","Animation","Children","Comedy","Crime",
                            "Documentary","Drama","Fantasy","Film-Noir","Horror","Musical","Mystery",
                            "Romance","Sci-Fi","Thriller","War","Western","actores"])

