# Print the names which contain the character 'a' from the dictionary
# containing 2 lists of male and female students given below.

dictionary = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
}

for i in dictionary:
    for j in dictionary[i]:
        if 'a' in j:
            print(j)































movie_data = {
    "War": [3, 5],
    "Bourne": [18, 5],
    "Gully boy": [15, 5],
    "Uri": [12, 5]
}
input_movie = input("Enter the movie: ")
input_age = int(input("Enter your age: "))
if input_movie in movie_data:
    if input_age >= movie_data[input_movie][0]:
        print("You are eligible to watch the movie")
        print(f"The available seats are {movie_data[input_movie][1]} ")

    else:
        print("You are not eligible to watch the movie")
else:
    print("Movie is unavailable")
