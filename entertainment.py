import media
import fresh_tomatoes
Difret = media.Movie("Difret", "abduction into marriage",
                     "https://upload.wikimedia.org/wikipedia/en/b/bf/Difret_poster.jpg",
                     "https://www.youtube.com/watch?v=s63ovvCDTj0")
Teza = media.Movie("Teza", "A stroy of an Ethiopian intellectual anberbr in the derg regime.",
                   "http://cdn6.bigcommerce.com/s-e2q5po/products/4319/images/8208/Teza_DVD__85686.1458672251.1280.1280.jpg?c=2",
                   "https://www.youtube.com/watch?v=1Rhzzit8yzk")
Prince_of_love = media.Movie("Prince of love",
                             "A young Addis Ababa taxi driver gets caught up in the dark side of love",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/Price_of_Love_2015_film_poster.png/220px-Price_of_Love_2015_film_poster.png",
                             "https://www.youtube.com/watch?v=qXNM4j8UrHY")
Difret2 = media.Movie("Difret", "abduction into marriage",
                     "https://upload.wikimedia.org/wikipedia/en/b/bf/Difret_poster.jpg",
                     "https://www.youtube.com/watch?v=s63ovvCDTj0")
Teza2 = media.Movie("Teza", "A stroy of an Ethiopian intellectual anberbr in the derg regime.",
                   "https://tseday.files.wordpress.com/2008/09/teza_poster.jpg",
                   "https://www.youtube.com/watch?v=1Rhzzit8yzk")
Prince_of_love2 = media.Movie("Prince of love",
                             "A young Addis Ababa taxi driver gets caught up in the dark side of love",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/Price_of_Love_2015_film_poster.png/220px-Price_of_Love_2015_film_poster.png",
                             "https://www.youtube.com/watch?v=qXNM4j8UrHY")
movies = (Difret,Teza,Prince_of_love,Difret2,Teza2,Prince_of_love2)
fresh_tomatoes.open_movies_page(movies)
