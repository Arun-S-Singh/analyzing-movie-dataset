# --------------
from csv import reader


def explore_data(dataset, start, end, rows_and_columns=False):
    """Explore the elements of a list.
    
    Print the elements of a list starting from the index 'start'(included) upto the index 'end'         (excluded).
    
    Keyword arguments:
    dataset -- list of which we want to see the elements
    start -- index of the first element we want to see, this is included
    end -- index of the stopping element, this is excluded 
    rows_and_columns -- this parameter is optional while calling the function. It takes binary          values, either True or False. If true, print the dimension of the list, else dont.
    """
    # Exception handling
    if start > end :
        raise Exception("Invalid parameters")
        
    if rows_and_columns:
        rows = len(dataset)
        cols = len(dataset[0])
        print("The dimension of the list is {0} rows and {1} columns".format(rows,cols))

    for item in dataset:
        print(item)
        print('\n')
   
    return


def duplicate_and_unique_movies(dataset, index_):
    """Check the duplicate and unique entries.
    
    We have nested list. This function checks if the rows in the list is unique or duplicated based     on the element at index 'index_'.
    It prints the Number of duplicate entries, along with some examples of duplicated entry.
    
    Keyword arguments:
    dataset -- two dimensional list which we want to explore
    index_ -- column index at which the element in each row would be checked for duplicacy 
    
    """
    duplicates = []
    uniques = []
    
    for movie in dataset:
        movie_name = movie[index_]
        if movie_name in uniques:
            duplicates.append(movie_name)
        else:
            uniques.append(movie_name)
    
    print('Number of duplicate entries = {}'.format(len(duplicates)))
    print('\n')
    print(duplicates[0:10])

    return

    
def movies_lang(dataset, index_, lang_):
    """Extract the movies of a particular language.
    
    Of all the movies available in all languages, this function extracts all the movies in a            particular laguage.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.

    Keyword arguments:
    dataset -- list containing the details of the movie
    index_ -- index which is to be compared for langauges
    lang_ -- desired language for which we want to filter out the movies
    
    Returns:
    movies_ -- list with details of the movies in selected language
    
    """
    movies_ = []

    for movie in dataset:
        movie_lang = movie[index_]
        if movie_lang == lang_ :
            movies_.append(movie)

    explore_data(movies_,1,5,True)

    return movies_
    

def rate_bucket(dataset, rate_low, rate_high):
    """Extract the movies within the specified ratings.
    
    This function extracts all the movies that has rating between rate_low and high_rate.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.
    
    Keyword arguments:
    dataset -- list containing the details of the movie
    rate_low -- lower range of rating
    rate_high -- higher range of rating
    
    Returns:
    rated_movies -- list of the details of the movies with required ratings
    """
    rated_movies = []
    #movie_rating = 0.0

    for movie in dataset:
        movie_rating = float(movie[11])
        if ( movie_rating >= rate_low) and (movie_rating <= rate_high) :
            rated_movies.append(movie)
    
    explore_data(rated_movies,1,3,False)

    return rated_movies



# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)


# The first row is header. Extract and store it in 'movies_header'.
movies_header = movies[0]

# Subset the movies dataset such that the header is removed from the list and store it back in movies
movies.pop(0)

# Delete wrong data

# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
#print(movies[4553])

# Hence drop this row.
movies.pop(4553)


# Using explore_data() with appropriate parameters, view the details of the first 5 movies.
print("Displaying first 5 movies in the list ..............")
explore_data(movies,1,6,True)

# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.
print("Displaying duplicates  ..............")
#print(movies_header[13])
duplicate_and_unique_movies(movies,13)


# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.

reviews_max = {}

for movie in movies:
    movie_name = movie[13]
    movie_review_count = float(movie[12])

    if (movie_name in reviews_max) and (reviews_max[movie_name] < movie_review_count):
        reviews_max[movie_name] = movie_review_count
    elif (movie_name not in reviews_max):
        reviews_max[movie_name] = movie_review_count

#print(reviews_max)

# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 

movies_clean = []
added = []

for movie in movies:
    movie_name = movie[13]
    movie_review_count = float(movie[12])

    if (reviews_max[movie_name] == movie_review_count) and (movie_name not in added):
        movies_clean.append(movie)
        added.append(movie)
print(len(movies))
print(len(movies_clean))
# Calling movies_lang(), extract all the english movies and store it in movies_en.
print("Displaying english movies in the list ..............")
print(movies_header[3])
movies_en = movies_lang(movies_clean,3,'en')
print(len(movies_en))

# Call the rate_bucket function to see the movies with rating higher than 8.
print("Displaying movies with rating >= 8 in the list ..............")
high_rated_movies = rate_bucket(movies_en , 8 ,10 )
print(len(high_rated_movies))



