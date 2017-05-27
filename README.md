# Spiders:

The following are the spiders currently present in this repository.

## seat-sale
This is intended to regularly poll the CebuPacific [seat-sale-table](https://www.cebupacificair.com/pages/seats-on-sale-per-route) to see if any of the specified origins came up.

##### Usage:
```
scrapy crawl seat-sale -a origins=Manila,Cagayan De Oro
```  
