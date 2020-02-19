# print.sc screenshot scraper

Simple prnt.sc screenshot scraper with Cloudflare bypass. It was made as a side project to practice Python. Please, don't abuse it.

## Dependencies

- Python 3.x
- [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [cfscrape](https://github.com/Anorov/cloudflare-scrape)
- [Node.js](https://nodejs.org/en/) for cfscrape


## Usage

```bash
python main.py
```
There are two modes:
- **Random url** - generates given amount of random prnt.sc urls and  downloads image to img folder.
- **Predefined url part** - takes a part of the url (3 - 5 characters) and loops through every possible combination. E.g. mjj*** will have 46656 possible combinations, but you can limit the amount.

## TO-DO list

- [X] Threading
- [ ] ...
- [ ] ...

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
