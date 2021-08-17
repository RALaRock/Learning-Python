# 8-8. User Albums:
# Start with your program from Exercise 8-7. Write a while loop
# that allows users to enter an album’s artist and title. Once you
# have that information, call make_album() with the user’s input
# and print the dictionary that’s created. Be sure to include a quit
# value in the while loop.


def make_album(artist=None, title=None, song_count=0):
    """return a dictionary with info about an album"""

    if artist or title:
        album = {"artist": artist.title(), "title": title.title()}
        if song_count:
            album["songs"] = song_count

    return album


print(make_album("devo", "really bad juju"))
print(make_album("the beach boys", "summertime"))
print(make_album("the beatles", "rubber soul"))

print(make_album("the eagles", "hotel california", 10))

while True:
    artist = input("Enter the album artist's name (or 'q' to quit): ")
    if artist == "q" or artist == "":
        break
    title = input("Enter the title of the album (or 'q' to quit): ")
    if title == "q" or artist == "":
        break

    album = make_album(artist, title)
    print(album)
