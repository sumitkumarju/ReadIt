import pandas as pd
import requests

df=pd.read_csv("books.csv");


avg_rating=[]
work_ratings_count=[]
c=0;
for isbn in df['isbn']:
  res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "uoXUmK6whATCXt3Za6jloQ", "isbns": isbn})
  if res.status_code != 200:
     print(res.status_code)
     avg_rating.append("NULL")
     work_ratings_count.append("NULL")
  else:
     data = res.json()
     avg_rating.append(data['books'][0]['average_rating'])
     work_ratings_count.append(data['books'][0]['work_ratings_count'])
  c+=1
  print(c)



with open('average_rating.txt', 'w+') as filehandle:
    for listitem in avg_rating:
        filehandle.write('%s\n' % listitem)

with open('work_ratings_count.txt', 'w+') as filehandle:
    for listitem in work_ratings_count:
        filehandle.write('%s\n' % listitem)


