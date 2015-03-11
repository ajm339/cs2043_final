#! /bin/bash

# fetch and print the titles
#curl http://www.movies.com/rss-feeds/top-ten-box-office-rss | sed 's/<title><!CDATA[//g' | sed 's/]]></tilte>//g'

while true
do
  curl https://web.archive.org/web/20140301052344/http://www.movies.com/rss-feeds/top-ten-box-office-rss > problem2_toremove_movies.txt
  # extract titles
  cat problem2_toremove_movies.txt | grep '<title>' > problem2_toremove_titles.txt
  # extract description
  cat problem2_toremove_movies.txt | grep '<description>' > problem2_toremove_descriptions.txt

  # clean up titles
  # delete <title><![CDATA[ ______ ]]></title>
  cat problem2_toremove_titles.txt | sed 's/<title><!\[CDATA\[//g' | sed 's/\]\]><\/title>//g'

  # clean up descriptions
  cat problem2_toremove_descriptions.txt | sed 's/<description><!\[CDATA\[//g' | sed 's/\]\]><\/description>//g' > problem2_toremove_descriptions_2.txt

  # create array
  IFS=$'\n'
  array=($(cat problem2_toremove_descriptions_2.txt))

  # user input
  read -p "Choose a movie (1-10) > " movie

  if [ $movie -ge 1 -a $movie -le 10 ]
  then
    # print description for this
    echo "Movie $movie"
    echo Synopsis
    echo ${array[$movie]}
  fi

  # clean up
  rm problem2_toremove*
done

