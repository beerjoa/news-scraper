# news_scraper

### INSTALL

  
    pip install -r requirements.txt



### USAGE
 
  ##### 1. og, o로 신문사를 선택, from-to로 날짜 선택, k로 키워드를 선택합니다.
  #####    신문사 리스트: [참조](https://github.com/yoooong2/news_scraper/blob/master/newsOffice.txt)
  #####    키워드: [네이버 검색 연산자](https://m.blog.naver.com/magnking/220959044231) 사용 가능 
  
  


  ###### ex)


      -og: newsOfficeGroup
      -o: newsOffice
      -from: from date (YYYYMMDD)
      -to: to date (YYYYMMDD)
      -k: news keyword

      python news-scraper.py -og=방송/통신 -o=1109,1079 -from=20200202 -to=20200205 -k="야구"
      python news-scraper.py -o=1109,1079 -o=1109,1079 -from=201901102 -to=20200205 -k="날씨 | 미세먼지"
      python news-scraper.py -og=경제/IT -o=1109,1079 -from=20130101 -to=20200205 -k="금리 인상"

  ![run_git](https://user-images.githubusercontent.com/22663614/74081564-c260e780-4a93-11ea-94bc-2574f560f3ca.gif)






  ##### 2. outputNews 폴더에 "{from}-{to}-{k}.json"으로 저장


