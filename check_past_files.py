#!/usr/bin/env python3
import os, datetime

articles_dir = "."
holidays = [('20221024', '20221106')]

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
days = int((end_date - start_date).days) + 7  # +7 to check next week
# but keep a counter for files found
file_num = 0
for day in range(days):
    the_date = start_date + datetime.timedelta(day)
    # holidays check
    on_holidays = False
    for holiday in holidays:
        startdate = datetime.datetime.strptime(holiday[0], '%Y%m%d')
        enddate   = datetime.datetime.strptime(holiday[1], '%Y%m%d')
        if startdate <= the_date <= enddate:
            on_holidays = True
            continue
    if on_holidays:
        continue
    wday = the_date.weekday()
    if wday >= 5:  # nothing on saturdays
        continue
    if not timetable[wday]:  # day with no lesson
        continue
    the_date_str = the_date.strftime('%Y%m%d')
    for lesson in timetable[wday]:
        expected_file = the_date_str + '-' + lesson + '.md'
        if file_num == len(school_posts):
            print("Expected", expected_file,
                  "but there's no file left.")
            exit(1)
        else:
            if expected_file == school_posts[file_num]:
                print(expected_file, "OK")
                file_num += 1
            else:
                print("Expected", expected_file,
                      "but got",  school_posts[file_num])
                exit(1)
