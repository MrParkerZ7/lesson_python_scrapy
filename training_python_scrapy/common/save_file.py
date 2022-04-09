from typing import List
from parsel.selector import SelectorList


def save_links_to_file(Class,  links: SelectorList):
    lines: List[str] = []

    for link in links:
        url = link.getall()
        lines.append(*url)

    with open(f"output/{Class.name}-{Class.fileNo}.txt", 'w') as file:
        file.write('\n'.join(lines))
        Class.fileNo += 1
