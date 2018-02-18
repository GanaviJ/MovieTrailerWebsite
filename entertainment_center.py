import media

import fresh_tomatoes

# Creating instances for different movies
toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys which come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc&t=6s")

captain_america = media.Movie("Captain America",
                              "Political involvement in the Avengers' activities causes a rift between Captain America and Iron Man",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYzOTc2NzU3N15BMl5BanBnXkFtZTcwNjY3MDE3NQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                              "https://www.youtube.com/watch?v=dKrVegVI0Us&t=1s")

justice_league = media.Movie("Justice League",
                             "Justice League is a 2017 American superhero film based on the DC Comics superhero team of the same name, distributed by Warner Bros. ",
                             "https://images-na.ssl-images-amazon.com/images/I/61eMyYx93hL.jpg",
                             "https://www.youtube.com/watch?v=r9-DM9uBtVI")

# Creating a list to store the movies
movies = [toy_story, captain_america, justice_league]
# To display the movie on  a website
fresh_tomatoes.open_movies_page(movies)
