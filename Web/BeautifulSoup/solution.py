from bs4 import BeautifulSoup
import unittest


def parse(path):
    # bridge = build_bridge(start, end, path)

    with open(path, 'r', encoding="utf-8") as data:
        soup = BeautifulSoup(data, "lxml")
        body = soup.find(id="bodyContent")

        imgs = len(body.find_all('img', width=lambda x: int(x or 0) > 199))
        headers = sum(
            1 for tag in body.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) if tag.get_text()[0] in "ETC"
        )

        lists = sum(1 for tag in body.find_all(['ol', 'ul']) if not tag.find_parent(['ol', 'ul']))

        linkslen = 0
        counter = 1
        for link in body('a'):
            if link.find_next_sibling():
                if link.find_next_sibling().name == 'a':
                    counter += 1
                else:
                    if counter > linkslen: linkslen = counter
                    counter = 1
            else:
                if counter > linkslen: linkslen = counter
                counter = 1

    out = [imgs, headers, linkslen, lists]

    return out


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()