from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName("exam").getOrCreate()
data = spark.read.option("header", True).csv("C:/Users/jsl11/SparkCourse/survey.csv")
lines = data['_c0', 'country', 'salary_midpoint']
# lines.show()

CanadaRating = lines.filter(lines[1] == 'Canada')
# CanadaRating.show()
print("국적이 Canada인 응답자 수 : ", CanadaRating.count())

print("전체 응답자 수 : ", lines.count())

salaryRating = lines.filter(lines[2].isNull())
# salaryRating.show()
print("salary_midpoint 항목이 무응답인 응답자 수 : ", salaryRating.count())
