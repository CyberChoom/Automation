class Songs:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in lyrics:
            print(line)


lyrics = ["Yesterday", "All my troubles seemed so far away",
          "Now it looks as though they're here to stay", "Oh, I believe in yesterday"]
beatles = Songs(lyrics)
beatles.sing_me_a_song()
