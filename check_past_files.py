#!/usr/bin/env python3
import os, datetime

articles_dir = "."

# grab files as a list of str
school_posts = ['20220905-0800-2SIOA.md']  # fake lesson (year started at 10AM)
for article in os.listdir(articles_dir):
    if article.startswith("20"):
        school_posts.append(article)
school_posts.sort()

timetable = [
        ["0800-2SIOA", "1000-1NSI", "1330-TNSI"],    # L
        ["0900-1SIO1", "1000-TNSI"],                 # M
        ["0800-1NSI"],                               # M
        ["1100-2SIOA", "1330-1SIO12", "1430-TNSI"],  # J
        ["1330-1SIO"]]                               # V

# generate and iterate through dates
start_date = datetime.datetime(2022, 9, 5)
end_date = datetime.datetime.now()
days = int((end_date - start_date).days)
# but keep a counter for files found
file_num = 0
for day in range(days):
    the_date = start_date + datetime.timedelta(day)
    the_date_str = the_date.strftime('%Y%m%d')
    wday = the_date.weekday()
    if wday >= 5:
        continue
    for lesson in timetable[wday]:
        expected_file = the_date_str + '-' + lesson + '.md'
        if expected_file == school_posts[file_num]:
            print(expected_file, "OK")
            file_num += 1
        else:
            print("Expected", expected_file, "but got", school_posts[file_num])
            exit(1)
