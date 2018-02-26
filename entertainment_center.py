import media

import fresh_tomatoes

# Creating instances for different movies
toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys which come to life",
                        "https://goo.gl/vQQPhg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc&t=5s")

captain_america = media.Movie("Captain America",
                              "A war amongst the hero's",
                              "https://goo.gl/zz4X93",
                              "https://www.youtube.com/watch?v=dKrVegVI0Us")

justice_league = media.Movie("Justice League",
                             "Woman fights against her enemy",
                             "https://goo.gl/M8BLUD",
                             "https://www.youtube.com/watch?v=3cxixDgHUYw")

# Creating a list to store the movies
movies = [toy_story, captain_america, justice_league]
# To display the movie on  a website
fresh_tomatoes.open_movies_page(movies)
