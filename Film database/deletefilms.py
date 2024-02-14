from connectfilms import *

def delete_films():
     # use the primary key to delete a record
    idField= input("Enter the filmID of the record to be deleted: ")
 
    # DELETE FROM songs WHERE SongID = 1/2/3/4.....
    dbCursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField}")
    dbCon.commit()
 
    print(f"Record {idField} deleted from the films table! ")
if __name__ == "__main__":
    delete_films()


#Enter the filmID of the record to be deleted: 37
#Record 37 deleted from the films table! 
#PS C:\Users\ACER\Desktop\Software Bootcamp> 