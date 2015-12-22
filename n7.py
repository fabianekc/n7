#!/usr/bin/python
import urllib, inflect, string, json, sys, Algorithmia

# initialize
p = inflect.engine()
text = ""
start_line = -1
end_line = -1
new_text = []
new_line = []
table = string.maketrans("", "")
dict_url = "https://raw.githubusercontent.com/fabianekc/n7/master/nounlist.txt"

# parse input; sample URL: 'http://www.gutenberg.org/cache/epub/97/pg97.txt'
input = json.loads(str(sys.argv[1]))
if 'url' in input:
    text = urllib.urlopen(input['url']).read()
    # using html2text from Algorithmia
    #client = Algorithmia.client(input['auth'])
    #text = client.algo('util/Html2Text/0.1.3').pipe(input['url'])
elif 'text' in input:
    text = input['text']
else:
    text = urllib.urlopen(input).read()
if 'dict' in input:
    dict_url = input['dict']
if 'start' in input:
    start_line = input['start']
if 'end' in input:
    end_line = input['end']
if text == "":
    print("Error: no input text provided")
    sys.exit()
text = text.decode('utf-8')
text = text.encode('ascii', 'replace')
text_split = text.split('\n')
if end_line > -1:
    text_split = text_split[0:end_line]
if start_line > -1:
    text_split = text_split[start_line:]
dict = urllib.urlopen(dict_url).read().split()
ld = len(dict)

# iterate over text
for line in text_split:
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
