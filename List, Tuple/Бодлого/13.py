#Олимпиадын дүн бүхий оноонуудын жагсаалт өгөгдсөн бол хэд дэх хүн түрүүлсэн бэ.
leaderboard = input().split()
first_place = leaderboard[0]
for participant in leaderboard :
    if int(first_place) < int(participant) :
        first_place = participant 
print(leaderboard.index(first_place))