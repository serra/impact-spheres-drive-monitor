from md2py import md2py
import pypandoc


def markdown2practice(markdown):
    toc = md2py(markdown)
    p = Practice()

    p.name = toc.h1.string
    p.description = _extract_description(toc.h1)

    for h2 in toc.h1.h2s:
        g = h22guide(h2)
        for i, h3 in enumerate(h2.h3s):
            step = h32step(h3)
            step.number = i + 1
            g.steps.append(step)
        p.guides.append(g)

    return p


def h22guide(h2):
    g = Guide()
    g.title = h2.string
    g.description = _extract_description(h2)
    return g


def h32step(h3):
    s = Step()
    s.instruction = h3.string
    s.explanation = _extract_description(h3)
    return s


def _extract_description(header, terminators=['h1', 'h2', 'h3', 'h4']):
    elem = []
    for sibling in header.source.next_siblings:
        if sibling.name in terminators:
            break
        elem.append(str(sibling))

    html = ''.join(elem)
    output = pypandoc.convert_text(html, 'md', format='html')
    return output


class Practice:
    def __init__(self):
        self.name = ''
        self.description = ''
        self.guides = []


class Guide:
    def __init__(self):
        self.title = ''
        self.description = ''
        self.steps = []


class Step:
    def __init__(self):
        self.number = 1
        self.instruction = ''
        self.explanation = ''
