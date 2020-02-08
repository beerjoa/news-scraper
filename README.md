# news_scraper

### INSTALL

  
    pip install -r requirements.txt



### USAGE


  ##### 1. 


  ##### 2. 


  ###### ex)


      -og: newsOfficeGroup
      -o: newsOffice
      -from: from date (YYYYMMDD)
      -to: to date (YYYYMMDD)
      -k: news keyword

      python news-scraper.py -og=방송/통신 -o=1109,1079 -from=20200202 -to=20200205 -k="야구"
      python news-scraper.py -o=1109,1079 -o=1109,1079 -from=201901102 -to=20200205 -k="날씨 | 미세먼지"
      python news-scraper.py -og=경제/IT -o=1109,1079 -from=20130101 -to=20200205 -k="금리 인상"







  ##### 3. outputNews 폴더에 "{from}-{to}-{k}.json"으로 저장


