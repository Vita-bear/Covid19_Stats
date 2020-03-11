# Covid19-Scraper
코로나-19 에 대한 확진/완치/사망 에 대한 한국, 해외 정보를 수집합니다. <br />
Data scrapes Covid-19 Confirmed/Cured/Deceases Cases in Korea and rest of the World.<br />

## Contents 

* Time recording is based on UTC (+0900 for KST) 
* 자료 파일의 시간은 UTC 기준입니다.(UTC+0900가 한국기준시 입니다.)

* [Korea - Covid-19 Daily Statistics](https://github.com/KKodiac/Covid19-Scraper/blob/master/Covid-19/Data/)

* [World - Covid-19 Daily Statistics](https://github.com/KKodiac/Covid19-Scraper/blob/master/Covid-19/Data/covid_dat.csv)

## Getting Started
### Prerequisites
Create a virtual environment.<br />
파이썬 가상환경을 만드세요.<br />
```
python3 -m venv .covid
```
Install modules in `requirements.txt`.<br /><br />
`requirements.txt` 에 있는 파이썬 모듈을 다운 받으세요.<br />
```
python3 -m pip install -r requirements.txt
```

## Built With/사용된 파이썬 모듈
* [Python3](https://www.python.org/doc)<br />
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) <br />
- [Requests](https://requests.readthedocs.io/en/master/)<br />

## Authors

* **Sean Hong(홍성민)** <br />
-현재 군인 현역으로 있는 학생이기 때문에 많이 부족합니다. 보완점을 가르쳐주시면 감사하겠습니다!<br />
-Any lacking parts in my code are welcome to any suggestions and criticism.<br />

## Acknowledgments

* World data scraped from - *github repo* - [Covid-19](https://github.com/CSSEGISandData/COVID-19) - [Service](https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer)
* Korea data scraped from [질병관리본부(Korea CDC)](http://ncov.mohw.go.kr/index_main.jsp) and [zeroday0619/COVID-19API](https://github.com/zeroday0619/COVID-19API/)

### Any problems please contact me at seanhong2000@gmail.com

