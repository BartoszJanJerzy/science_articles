import bs4
import urllib, urllib.request
from datetime import datetime
from src.schema import Article


class ArticlesMetadataLoader:
    """
    https://info.arxiv.org/help/api/index.html
    Thank you to arXiv for use of its open access interoperability
    """

    def load(
            self,
            query: str,
            start: int = 0,
            max_results: int = 1,
            date_min: str | None = "20200101",
            date_max: str | None = None
    ) -> list[Article]:
        assert max_results > 0

        if not date_max:
            now = datetime.now()
            y = now.year
            m = f"0{now.month}" if now.month < 10 else str(now.month)
            d = f"0{now.day}" if now.day < 10 else str(now.day)
            date_max = f"{y}{m}{d}"

        results = []
        while start < max_results:
            file = self.run_request(query, start, 1, date_min, date_max)
            results.append(Article(**self.parse_single_record(file)))
            start += 1

        return results

    @staticmethod
    def run_request(
            query: str,
            start: int = 0,
            max_results: int = 1,
            date_min: str | None = "20200101",
            date_max: str | None = None
    ):
        url = (f'http://export.arxiv.org/api/query?'
               f'search_query={query}'
               f'+AND+submittedDate:[{date_min}+TO+{date_max}]'
               f'&start={start}'
               f'&max_results={max_results}')
        data = urllib.request.urlopen(url)
        xml_text = data.read().decode('utf-8')
        file = bs4.BeautifulSoup(xml_text, "xml")

        return file

    @staticmethod
    def parse_single_record(file: bs4.BeautifulSoup):
        published = file.find("published").text.replace("<published>", "").replace("</published>", "").strip()
        title = file.find_all("title")[1].text.replace("<title>", "").replace("</title>", "").strip()
        abstract = file.find('summary').text.replace("<summary>", "").replace("</summary>", "").strip()
        authors = []
        for x in file.find_all("author"):
            authors.append(x.find("name").text)

        return dict(
            title=title,
            abstract=abstract,
            authors=authors,
            published=published
        )

