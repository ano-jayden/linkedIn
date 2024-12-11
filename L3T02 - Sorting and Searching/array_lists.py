#  Album class
class Album:
    def __init__(self, album_name, album_artist, number_of_songs):
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

# ist of albums 
albums1 = [
    Album("Views", "Drake", 20),
    Album("Scorpion", "Drake", 25),
    Album("DAMN.", "Kendrick Lamar", 14),
    Album("The Black Album", "Kendrick Lamar", 13),
    Album("2 Alivë", "Yeat", 22)
]


print("Albums1:")
for album in albums1:
    print(album)


albums1.sort(key=lambda album: album.number_of_songs)
print("\nAlbums1 sorted by number of songs:")
for album in albums1:
    print(album)

albums1[1], albums1[2] = albums1[2], albums1[1]
print("\nAlbums1 after swapping position 1 with position 2:")
for album in albums1:
    print(album)

# albums2
albums2 = [
    Album("Graduation", "Kanye West", 13),
    Album("The College Dropout", "Kanye West", 21),
    Album("Astroworld", "Travis Scott", 17),
    Album("Blonde", "Frank Ocean", 17),
    Album("Flower Boy", "Tyler, the Creator", 14)
]


print("\nAlbums2:")
for album in albums2:
    print(album)

albums2.extend(albums1)


albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
albums2.append(Album("Oops!... I Did It Again", "Britney Spears", 16))


albums2.sort(key=lambda album: album.album_name)
print("\nAlbums2 sorted alphabetically by album name:")
for album in albums2:
    print(album)

index = next((i for i, album in enumerate(albums2) if album.album_name == "Dark Side of the Moon"), -1)
print(f"\nIndex of 'Dark Side of the Moon' in albums2: {index}")
