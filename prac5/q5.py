movies = {
    "War": [3, 5],
    "Bourne": [18, 5],
    "Gully boy": [15, 5],
    "Uri": [12, 5]
}
print(list(movies.keys()))


movie = input("Enter the movie: ")
if movie in movies:
    age = int(input("Enter your age: "))
    if age >= movies[movie][0]:
        print("You can watch the movie")
        if movies[movie][1] > 0:
            print("There are", movies[movie][1], "tickets available")
            tickets = int(input("Enter the number of tickets you want: "))
            if tickets <= movies[movie][1]:
                print("Tickets booked")
                movies[movie][1] -= tickets
            else:
                print("Tickets not available")
        else:
            print("Tickets not available")
    else:
        print("You cannot watch the movie")
