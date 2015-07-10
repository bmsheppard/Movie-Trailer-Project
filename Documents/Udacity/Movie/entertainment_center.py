import media
import fresh_tomatoes

# Instances that are run in the 'Movie' class by using the tile, poster image url,
#and trailer url for each movie
interstellar = media.Movie("Interstellar",
                           "https://blurppy.files.wordpress.com/2014/09/benmcleodintersteller.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

oceans_eleven = media.Movie("Ocean's Eleven",
                            "https://s-media-cache-ak0.pinimg.com/originals/37/90/c5/3790c59a2b37b2a87ad5829ae68f9d22.jpg",
                            "https://www.youtube.com/watch?v=u7VTkceSsEw")

kingsman = media.Movie("Kingsman:The Secret Service",
                       "http://ia.media-imdb.com/images/M/MV5BMTkxMjgwMDM4Ml5BMl5BanBnXkFtZTgwMTk3NTIwNDE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                       "https://www.youtube.com/watch?v=xkX8jKeKUEA")

the_dark_knight = media.Movie("The Dark Knight",
                              "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                              "https://www.youtube.com/watch?v=5y2szViJlaY")

inception = media.Movie("Inception",
                        "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX214_AL_.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

walle = media.Movie("Wall-e",
                    "http://img3.wikia.nocookie.net/__cb20150108180934/disney/images/thumb/a/a3/WALL-E_-_Poster.jpg/320px-WALL-E_-_Poster.jpg" ,
                    "https://www.youtube.com/watch?v=ZisWjdjs-gM")

# Creates an array that lists the movies that will be on the website
movies = [interstellar, oceans_eleven, kingsman, the_dark_knight, inception, walle]
fresh_tomatoes.open_movies_page(movies)
