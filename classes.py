class Mickey:
    def __init__(self, date_watched, movie_title, mickey_rating):
        self.date_watched = date_watched
        self.movie_title = movie_title
        self.mickey_rating = self._convert_rating(mickey_rating)
    
    def _convert_rating(self, rating):
        rating = rating.strip().upper()
        if rating == "O":
            return "Okay"
        elif rating == "G":
            return "Good"
        elif rating == "B":
            return "Bad"
        else:
            return "Unknown"

    def get_movie_title(self):
        return self.movie_title

    def get_movie_Rating(self):
        return self.mickey_rating

    def get_movie_date(self):
        return self.date_watched

    def __str__(self):
        return f"Date Watched: {self.date_watched}, Movie Title: {self.movie_title}, Mickey Rating: {self.mickey_rating}"

class Domain:
    def __init__(self, title, year, rated, released, runtime, genre, director,
                 actors, country, mickeyRating, dateWatched):
        self.title = title
        self.year = year
        self.rated = rated
        self.released = released
        self.runtime = runtime
        self.genre = genre
        self.director = director
        self.actors = actors
        self.country = country
        self.mickeyRating = mickeyRating
        self.dateWatched = dateWatched

    

