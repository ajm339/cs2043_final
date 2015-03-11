#! /bin/bash

# fetch and print the titles
#curl http://www.movies.com/rss-feeds/top-ten-box-office-rss | sed 's/<title><!CDATA[//g' | sed 's/]]></tilte>//g'

while true
do
  curl https://web.archive.org/web/20140301052344/http://www.movies.com/rss-feeds/top-ten-box-office-rss > problem2_toremove_movies.txt
  IFS=$'\n'
  # extract titles
  cat problem2_toremove_movies.txt | grep '<title>' | sed 's/<title><!\[CDATA\[//g' | sed 's/\]\]><\/title>//g'
  # extract description and create array
  array=($(cat problem2_toremove_movies.txt | grep '<description>' | sed 's/<description><!\[CDATA\[//g' | sed 's/\]\]><\/description>//g'))
  # clean up
  rm problem2_toremove*

  # user input
  read -p "Choose a movie (1-10) > " movie

  if [ $movie -ge 1 -a $movie -le 10 ]
  then
    # print description for this
    echo "Movie $movie"
    echo Synopsis
    echo ${array[$movie]}
  fi
done

