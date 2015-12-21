import urllib, inflect, string

# initialize and get content
link = 'http://www.gutenberg.org/cache/epub/97/pg97.txt'
p = inflect.engine()
table = string.maketrans("", "")
dict = urllib.urlopen("http://www.desiquintans.com/downloads/nounlist/nounlist.txt").read().split()
ld = len(dict)
text = urllib.urlopen(link).read()

new_text = []
new_line = []
for line in text.split('\n'):
    for word in line.split():
        # when replacing words we need to take care for
        # - punc: punctuation
        # - sipl: singular / plural
        # - new vs final: uppercase / capitalize / lowercase
        punc = word.translate(table, string.punctuation)
        sipl = p.singular_noun(punc)
        if sipl:
            new = sipl
        else:
            new = punc
        if (new.lower() in dict):
            if punc == word:
                if sipl:
                    final = p.plural(dict[(dict.index(new.lower())+7)%ld])
                else:
                    final = dict[dict.index(new.lower())+7]
            else:
                if sipl:
                    final = word.replace(punc, p.plural(dict[(dict.index(new.lower())+7)%ld]))
                else:
                    final = word.replace(punc, dict[(dict.index(new.lower())+7)%ld])
            if new.lower() != new:
                if new.upper() == new:
                    final = final.upper()
                else:
                    final = final.capitalize()
        else:
            final = word
        new_line.append(final)
    new_text.append(" ".join(new_line))
    new_line = []
print "\n".join(new_text)
