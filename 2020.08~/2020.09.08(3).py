

genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]
album = {}
for i in range(len(genres)):
    print(i)
    album[genres[i]] = plays[i]

print(album)
