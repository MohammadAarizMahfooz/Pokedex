import pypokedex
import PIL.Image, PIL.ImageTk
import urllib3
import tkinter as tk
from io import BytesIO

# making the gui window
window = tk.Tk()
window.geometry("750x700")
window.title("Pokedex")
window.config(padx=10, pady=10)

# adding a heading label
title_label = tk.Label(window, text="Pokedex")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

# adding the image label
pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

# adding the name and index label
pokemon_info = tk.Label(window)
pokemon_info.config(font=("Arial", 20))
pokemon_info.pack(padx=10, pady=10)

# adding types label
pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

# adding abilities label
pokemon_ability = tk.Label(window)
pokemon_ability.config(font=("Arial", 20))
pokemon_ability.pack(padx=10, pady=10)

# function to load and display pokemon image and infos
def load_pokemon():
    try:
        pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

        http = urllib3.PoolManager()
        response = http.request('GET', pokemon.sprites.front.get("default"))
        image = PIL.Image.open(BytesIO(response.data))

        img = PIL.ImageTk.PhotoImage(image)
        pokemon_image.config(image=img)
        pokemon_image.image = img

        pokemon_info.config(text=f"{pokemon.dex} - {pokemon.name}".title())
        pokemon_types.config(text="Type: "+" , ".join([t for t in pokemon.types]).title())
        pokemon_ability.config(text="Abilities: "+" , ".join([a.name for a in pokemon.abilities]).title())
    except Exception as e:
        pokemon_info.config(text=e)

label_id_name = tk.Label(window, text="Enter ID or Name to search:")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text="Search", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)

window.mainloop()