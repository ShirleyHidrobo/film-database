from connectfilms import *

# create a subroutine to add records in the film table 
def insert_films():
    # filmID is a primary autoincrement field, no data input is required
    # create three input statements respectively fot the Title, Artist and Genre fields
    filmTitle = input("Enter film Title:")
    filmyearReleased = input("Enter film yearReleased:")
    filmRating= input("Enter film Rating:")
    filmDuration = input("Enter Duration:")
    filmGenre= input("Enter film Genre:")

    # add data from saved in the variables (filmTitle,filmyearReleased,filmRating,filmDuration,filmGenre)
    dbCursor.execute("INSERT INTO tblFilms(title, yearReleased, rating, duration, genre)VALUES(?,?,?,?,?)",(filmTitle,filmyearReleased,filmRating,filmDuration,filmGenre)) #we use (?,?,?) to avoid sql injection so we add songTitle, songArtist, songGenre
    # save the changes permanently in the films in the db
    dbCon.commit()

    print(f"{filmTitle} inserted in the films table. ")

if __name__ == "__main__":
    insert_films()