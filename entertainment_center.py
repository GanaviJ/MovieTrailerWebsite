import media

import fresh_tomatoes

# Creating instances for different movies
toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys which come to life",
                        "https://goo.gl/vQQPhg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

captain_america = media.Movie("Captain America",
                              "A war amongst the hero's",
                              "https://goo.gl/zz4X93",
                              "https://www.youtube.com/watch?v=SqLNDxbh1sM")

justice_league = media.Movie("Justice League",
                             "Woman fights against her enemy",
                             "https://goo.gl/M8BLUD",
                             "https://www.youtube.com/watch?v=r9-DM9uBtVI")

# Creating a list to store the movies
movies = [toy_story, captain_america, justice_league]
# To display the movie on  a website
fresh_tomatoes.open_movies_page(movies)
