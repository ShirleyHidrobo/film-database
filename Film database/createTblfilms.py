from connectfilms import *
dbCursor.execute(
    """
    CREATE TABLE IF NOT EXISTS "tblFilms" (
        "filmID"	INTEGER NOT NULL UNIQUE,
        "filmTitle"	TEXT,
        "filmyearReleased"	TEXT,
        "filmRating"	TEXT,
        "filmDuration"	TEXT,
        "filmGenre"	TEXT,
        PRIMARY KEY("filmID" AUTOINCREMENT) ) """
) 
