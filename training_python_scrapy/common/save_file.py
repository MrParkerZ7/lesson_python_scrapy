from typing import List


def save_lines_to_file(Class,  links):
    lines: List[str] = []

    for link in links:
        url: str = link.get()
        lines.append(url)

    with open(f"output/{Class.name}-{Class.fileNo}.txt", 'w') as file:
        file.write('\n'.join(lines))
        Class.fileNo += 1
