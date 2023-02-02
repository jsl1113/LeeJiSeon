from pyspark import SparkConf, SparkContext

def loadMovieNames():
    movieNames = {}
    with open("C:/Users/jsl11/SparkCourse/ml-100k/u-uni.item") as f:
        for line in f:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1]  # 0는 영화 아이디, 1은 영화 이름
    return movieNames  # 영화 이름


conf = SparkConf().setMaster("local").setAppName("PopularMovies")
sc = SparkContext(conf=conf)

nameDict = sc.broadcast(loadMovieNames())  # broadcast (연결시켜서 사용)
# {영화 번호 : 영화 이름 }
# print(nameDict.value)

lines = sc.textFile("file:///C:/Users/jsl11/SparkCourse/ml-100k/u.data")

movies = lines.map(lambda x: (int(x.split()[1]), 1))
# (영화 번호, 1)
# print(movies.collect())

movieCounts = movies.reduceByKey(lambda x, y: x + y)
# (영화 번호, 평점 개수)
# print(movieCounts.collect())

movies = lines.map(lambda x: (int(x.split()[1]), int(x.split()[2]), 1)) # 1: 영화 번호, 2: 평점
# (영화 번호, 평점, 1)
# print(movies.collect())

totalsRating = movies.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
# (영화 번호, (평점 합, 평점 개수 합))
# print(totalsRating.collect())

averagesRating = totalsRating.mapValues(lambda x: x[0] / x[1])
# (영화 번호, 평점 평균)
# print(averagesRating.collect())

flipped = averagesRating.map(lambda x: (x[1], x[0]))
# (평점 평균, 영화 번호)
# print(flipped.collect())

sortedMovies = flipped.sortByKey()
# (평점 평균, 영화 번호) 평점 낮은 순에서 높은 순으로 sort
# print(sortedMovies.collect())

sortedMoviesWithNames = sortedMovies.map(lambda x: (nameDict.value[x[1]], x[0]))
# (영화 이름['영화 번호'], 평점 평균)
print(sortedMoviesWithNames.collect())

results = sortedMoviesWithNames.collect()

for result in results[:10]:
    print(result[0], '=>>', result[1])

