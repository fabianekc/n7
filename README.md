# n+7
Many years ago (I think it was in 2001) I participated in a class about *Mathematics & Literature*. Beside others the "n+7 method" was presented: You replace in a text each noun with the noun in a dictionary which is 7 places after the original noun, e.g., "a man meets a woman" is transformed to "a mandrake meets a wonder" using the Langenscheidt dictionary.  

This repository contains the files I submitted to the [Algorithmia Shorties Contest](http://blog.algorithmia.com/2015/12/the-algorithmia-shorties-contest/).

```bash
curl -X POST -d '{"url":"http://www.gutenberg.org/cache/epub/97/pg97.txt", "start":32, "end":551}' -H 'Content-Type: application/json' -H 'Authorization: Simple YOUR_API_KEY' https://api.algorithmia.com/v1/algo/fabianekc/n7/0.1.0
```
Notes for running this on Algorithmia:
* replace `YOUR_API_KEY` with your personal API key from your Algorithmia.com account
* running this algorithm with the full text of Flatland costs about 1-2 credits
* executing this algorithm too often per day will block Algorithmia.com from accessing Project Gutenberg for 24 hours

Comments:
* the original list of nouns is from http://www.desiquintans.com/nounlist (downloaded on Dec 21s, 2015); I like the idea of a simple list with only the most commonly used but added anyway a few words
