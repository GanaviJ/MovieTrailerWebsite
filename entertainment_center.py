import media

import fresh_tomatoes

# Creating instances for different movies
toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys which come to life",
                        "https://goo.gl/vQQPhg",
                        "https://goo.gl/i5AvND")

captain_america = media.Movie("Captain America",
                              "A war amongst the hero's",
                              "https://goo.gl/zz4X93",
                              "https://goo.gl/WoJVUk")

justice_league = media.Movie("Justice League",
                             "Woman fights against her enemy",
                             "https://goo.gl/M8BLUD",
                             "https://goo.gl/xYjL7s")

# Creating a list to store the movies
movies = [toy_story, captain_america, justice_league]
# To display the movie on  a website
fresh_tomatoes.open_movies_page(movies)
