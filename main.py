from Covid19.src.covid19_kr import CovidInfokr
from Covid19.src.covid19_wd import CovidInfowd
from Covid19.src.covid19_seoul import CovidInfoSeoul
from Web.scrape import ThrowInfo as scrape
import Web.web as web

if __name__ == '__main__':
    covidkr = CovidInfokr() # Korean Stats for Covid-19
    covidkr.run()
    
    covidwd = CovidInfowd() # new World Stats that has more accurate
    covidwd.run()
    
    
    seoul = CovidInfoSeoul()
    seoul.run()
    web.app.run(port=8080,debug=True)
    