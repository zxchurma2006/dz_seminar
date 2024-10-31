import pandas as pd
import random
import tkinter as tk
from tkinter import messagebox
films = pd.read_csv('imdb_top_250.csv')
film_genres_list = []
for film_genre in films['Genre']:
    genres = film_genre.split(' | ')
    film_genres_list.extend(genres)
genres_set = set(film_genres_list)
def get_random_film_by_genre(genre):
    filtered_films = films[films['Genre'].str.contains(genre, regex=False)]
    if not filtered_films.empty:
        random_film = filtered_films.sample(1)
        title = random_film['Title'].values[0]
        messagebox.showinfo("Случайный фильм", f"Фильм: {title}")
    else:
        messagebox.showwarning("Ошибка", "Фильмы данного жанра не найдены.")
def show_genre_window():
    genre = genre_entry.get()
    if genre in genres_set:
        get_random_film_by_genre(genre)
    else:
        messagebox.showwarning("Ошибка", "Неправильный жанр, попробуйте еще раз.")
app = tk.Tk()
app.title("Случайный фильм по жанру")
tk.Label(app, text="Введите жанр фильма:").pack()
genre_entry = tk.Entry(app)
genre_entry.pack()
tk.Button(app, text="Получить фильм", command=show_genre_window).pack()
app.mainloop()