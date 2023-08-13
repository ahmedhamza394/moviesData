import csv
import requests
from classes import Mickey
from classes import Domain

def parse_csv(file_path):
    mickey_list = []
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                date_watched, movie_title, mickey_rating = row
                mickey = Mickey(date_watched.strip(), movie_title.strip(), mickey_rating.strip())
                mickey_list.append(mickey)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print("An error occurred:", e)

    return mickey_list

def handle_fun(mickey_objects : list):
    dto_list = []
    api_key = ""
    for mickey in mickey_objects:
        movie_title = mickey.get_movie_title()
        url = f"http://www.omdbapi.com/?t={movie_title.replace(' ', '+')}&apikey={api_key}"
        print(f"Fetching data for '{movie_title}':")
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for any errors in the response
            movie_data = response.json()
            if movie_data.get('Response') == 'True':
                title = movie_data.get("Title")
                year = movie_data.get("Year")
                rated = movie_data.get("Rated") 
                released = movie_data.get("Released")
                runtime = movie_data.get("Runtime")
                genre = movie_data.get("Genre")
                director = movie_data.get("Director")
                actors = movie_data.get("Actors")
                country = movie_data.get("Country")
                mickeyRating = mickey.get_movie_Rating()
                dateWatched = mickey.get_movie_date()

                data = Domain(title, year, rated, released, runtime, genre, director,
                actors, country, mickeyRating, dateWatched)
                dto_list.append(data)
            else:
                print(f"Movie details not found for '{movie_title}'")
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while fetching data for '{movie_title}':", e)
        
    return dto_list


def interpet_fun(domainData : list):
    fieldnames = [
        "title", "year", "rated", "released", "runtime", "genre", "director",
        "actors", "country", "mickeyRating", "dateWatched"
    ]
    
    csvFileName = "C:/Users/hamza/Desktop/MickeyMovie/outputFile.csv"

    with open(csvFileName, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for data in domainData:
            writer.writerow(vars(data))  # Convert movie object to dictionary using vars()

    print("Movie data written")
        

if __name__ == "__main__":
    file_path = "C:/Users/hamza/Desktop/MickeyMovie/MoviesData.csv"  # Replace with the actual file path

    mickey_objects = parse_csv(file_path)
    domainData = handle_fun(mickey_objects)
    interpet_fun(domainData)

    print("Done")
    