import webbrowser

# Creates a movie class that gives a title, poster image url,
#and trailer url for each movie in the 'movies' array

class Movie ():
    # Creates a constructure used for the array 'movies'
    def __init__ (self, movie_title, image_url, trailer_url_link):
        self.title = movie_title
        self.poster_image_url = image_url
        self.trailer_youtube_url = trailer_url_link
    # Method used to link to the trailer website
    def show_trailer(self):
        webbrowser.open(self.trailer)
    


