# scrapy-cebupacific
<a href="https://codeclimate.com/github/BurnzZ/scrapy-cebupacific"><img src="https://codeclimate.com/github/BurnzZ/scrapy-cebupacific/badges/gpa.svg" /></a>

## Usage
Make sure to install the packages on a **virtualenv**:
```
python3 -m venv env
source env/bin/activate

pip3 install -r requirements.txt
```

## Spiders
The following are the spiders currently present in this repository.

### seat-sale
This is intended to regularly poll the CebuPacific [seat-sale-table](https://www.cebupacificair.com/pages/seats-on-sale-per-route) to see if any of the specified origins came up.

##### Usage:
```
scrapy crawl seat-sale -a origins="Manila,Cagayan De Oro"
scrapy crawl seat-sale -a origins="IloIlo"
```  
