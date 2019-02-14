import nltk
import re
import collections
from collections import defaultdict
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
from nltk.probability import FreqDist
from yattag import Doc, indent
import pickle




## Baut die HTML Struktur und uebergibt die Daten aus den dictionaries, liefert HTML Inhalt
def display_article(data_ger,data_lux):
    doc, tag, text = Doc().tagtext()
    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            doc.asis('<meta charset="utf-8"/>')
            doc.asis('<link rel="stylesheet" type="text/css" href="de_lu.css">')
            doc.asis('<script src="tablefilter/tablefilter.js"></script>')
            doc.asis('<script src="jquery-3.3.1.min.js"></script>')
            doc.asis('<script src="jquery-ui-1.12.1/jquery-ui.js"></script>')
            doc.asis('<script src="mark.js/dist/mark.min.js"></script>')
            doc.asis('<script src="mark.js/dist/jquery.mark.min.js"></script>')
        with tag('body'):
            with tag('div', id='btn1'):
                doc.asis('<button class="btn" value="" onclick="filter(event);">All</button>')
                doc.asis('<button class="btn" value="A" onclick="filter(event);">A</button>')
                doc.asis('<button class="btn" value="B" onclick="filter(event);">B</button>')
                doc.asis('<button class="btn" value="C" onclick="filter(event);">C</button>')
                doc.asis('<button class="btn" value="D" onclick="filter(event);">D</button>')
                doc.asis('<button class="btn" value="E" onclick="filter(event);">E</button>')
                doc.asis('<button class="btn" value="F" onclick="filter(event);">F</button>')
                doc.asis('<button class="btn" value="G" onclick="filter(event);">G</button>')
                doc.asis('<button class="btn" value="H" onclick="filter(event);">H</button>')
                doc.asis('<button class="btn" value="I" onclick="filter(event);">I</button>')
                doc.asis('<button class="btn" value="J" onclick="filter(event);">J</button>')
                doc.asis('<button class="btn" value="K" onclick="filter(event);">K</button>')
                doc.asis('<button class="btn" value="L" onclick="filter(event);">L</button>')
                doc.asis('<button class="btn" value="M" onclick="filter(event);">M</button>')
                doc.asis('<button class="btn" value="N" onclick="filter(event);">N</button>')
                doc.asis('<button class="btn" value="O" onclick="filter(event);">O</button>')
                doc.asis('<button class="btn" value="P" onclick="filter(event);">P</button>')
                doc.asis('<button class="btn" value="Q" onclick="filter(event);">Q</button>')
                doc.asis('<button class="btn" value="R" onclick="filter(event);">R</button>')
                doc.asis('<button class="btn" value="S" onclick="filter(event);">S</button>')
                doc.asis('<button class="btn" value="T" onclick="filter(event);">T</button>')
                doc.asis('<button class="btn" value="U" onclick="filter(event);">U</button>')
                doc.asis('<button class="btn" value="V" onclick="filter(event);">V</button>')
                doc.asis('<button class="btn" value="W" onclick="filter(event);">W</button>')
                doc.asis('<button class="btn" value="X" onclick="filter(event);">X</button>')
                doc.asis('<button class="btn" value="Y" onclick="filter(event);">Y</button>')
                doc.asis('<button class="btn" value="Z" onclick="filter(event);">Z</button>')
            with tag('div', id='btn2'):
                doc.asis('<button class="btn2" value="" onclick="filter2(event);">All</button>')
                doc.asis('<button class="btn2" value="A" onclick="filter2(event);">A</button>')
                doc.asis('<button class="btn2" value="B" onclick="filter2(event);">B</button>')
                doc.asis('<button class="btn2" value="C" onclick="filter2(event);">C</button>')
                doc.asis('<button class="btn2" value="D" onclick="filter2(event);">D</button>')
                doc.asis('<button class="btn2" value="E" onclick="filter2(event);">E</button>')
                doc.asis('<button class="btn2" value="F" onclick="filter2(event);">F</button>')
                doc.asis('<button class="btn2" value="G" onclick="filter2(event);">G</button>')
                doc.asis('<button class="btn2" value="H" onclick="filter2(event);">H</button>')
                doc.asis('<button class="btn2" value="I" onclick="filter2(event);">I</button>')
                doc.asis('<button class="btn2" value="J" onclick="filter2(event);">J</button>')
                doc.asis('<button class="btn2" value="K" onclick="filter2(event);">K</button>')
                doc.asis('<button class="btn2" value="L" onclick="filter2(event);">L</button>')
                doc.asis('<button class="btn2" value="M" onclick="filter2(event);">M</button>')
                doc.asis('<button class="btn2" value="N" onclick="filter2(event);">N</button>')
                doc.asis('<button class="btn2" value="O" onclick="filter2(event);">O</button>')
                doc.asis('<button class="btn2" value="P" onclick="filter2(event);">P</button>')
                doc.asis('<button class="btn2" value="Q" onclick="filter2(event);">Q</button>')
                doc.asis('<button class="btn2" value="R" onclick="filter2(event);">R</button>')
                doc.asis('<button class="btn2" value="S" onclick="filter2(event);">S</button>')
                doc.asis('<button class="btn2" value="T" onclick="filter2(event);">T</button>')
                doc.asis('<button class="btn2" value="U" onclick="filter2(event);">U</button>')
                doc.asis('<button class="btn2" value="V" onclick="filter2(event);">V</button>')
                doc.asis('<button class="btn2" value="W" onclick="filter2(event);">W</button>')
                doc.asis('<button class="btn2" value="X" onclick="filter2(event);">X</button>')
                doc.asis('<button class="btn2" value="Y" onclick="filter2(event);">Y</button>')
                doc.asis('<button class="btn2" value="Z" onclick="filter2(event);">Z</button>')
            with tag ('table', klass="table_ger"):
                doc.asis('<tr><td></td></tr>')          #first row always sticks, so placeholder row here
                for d in sorted(data_ger):
                    with tag ('tr'):
                        with tag('td', klass="key_ger", onclick="mark(event)"):
                            with tag ("p", klass="key_ger key_ger_lemma"):
                                text(d)
                            with tag('p', klass="key_ger key_ger_token"):
                                text(data_ger[d][0])
                        with tag('td', klass="value_ger"):
                            with tag('table'):
                                with tag('tr', klass="vorkommen"):
                                    with tag('th', klass="vorkommen"):
                                        text('Vorkommen anzeigen')
                                        with tag('td', klass="vorkommen"):
                                            with tag('p', klass="fdist_ger"):
                                                text("Kommt "+str(data_ger[d][1])+" Mal vor im Text")
                                            for entry in data_ger[d][3:]:
                                                with tag('p', klass="occur_ger"):
                                                    if (len(entry.split())>1):
                                                        text(entry)
                                with tag('tr', klass="vorschlag"):
                                    with tag ('th', klass="vorschlag"):
                                        text('Vorschlag anzeigen')
                                        with tag('td', klass="vorschlag", onclick="jump(event)"):
                                            for entry in data_ger[d][3:]:
                                                with tag('p', klass="vorschlag"):
                                                    if (len(entry.split())==1):
                                                        text(entry)
            with tag ('table', klass="table_lux"):
                doc.asis('<tr><td></td></tr>')          #first row always sticks, so placeholder row here
                for d in sorted(data_lux):
                    with tag ('tr'):
                        with tag('td', klass="key_lux", onclick="mark(event)"):
                            with tag('p', klass="key_lux key_lux_lemma"):
                                text(d)
                        with tag('td', klass="value_lux"):
                            with tag('table'):
                                with tag('tr', klass="vorkommen_lux"):
                                    with tag('th', klass="vorkommen_lux"):
                                        text("Vorkommen anzeigen")
                                        with tag('td', klass="vorkommen_lux"):
                                            with tag('p', klass="fdist_lux"):
                                                text("Kommt "+str(data_lux[d][0])+" Mal vor im Text")
                                            for entry in data_lux[d][1:]:
                                                with tag('p', klass="occur_lux"):
                                                    if (len(entry.split())>1):
                                                        text(entry)
            doc.asis('<script src="de_lu.js"></script>')
    return indent(doc.getvalue())

print("Programm startet...")

## Erstellt globale Variablen
german_dict=collections.defaultdict(list)
lux_dict=collections.defaultdict(list)
ger_tokens_lower=[]
lux_tokens_lower=[]
words=[]
pattern=re.compile(",|“|”|„|'|’|``|!|;|\.|:|-|–|«|»|\?")

print("...füllt luxemburgisches Wörterbuch")

lux_text=open("mml.txt", encoding='latin-1').read()
lux_text=lux_text.replace("-","")
lux_sent=nltk.sent_tokenize(lux_text)                                   ## alle Sätze
lux_tokens=nltk.word_tokenize(lux_text)                                 ## alle Tokens
for word in lux_tokens:
    lux_tokens_lower.append(word.lower())
lux_fdist=FreqDist(lux_tokens_lower)                                    ## alle Häufigkeiten pro Wort
for word in lux_tokens:                                                 ## Iteration ueber jedes lux. Wort
    if pattern.match(word):
            continue;
    word=word.lower()
    lux_dict_value_list=[]                                              ## Eigenschaftsliste
    lux_dict_value_list.append(lux_fdist[word])
    search_regex_lux = r"\b" + re.escape(word) + r"\b"
    for entry in lux_sent:                                              ## Iteration ueber jeden lux. Satz
        if re.search(search_regex_lux, entry,re.IGNORECASE):            ## Sucht alle Satze in denen das Wort vor kommt
            lux_dict_value_list.append(entry)
    lux_dict[word]=lux_dict_value_list                                  ## Eigenschaftsliste wird dem Wort zugewiesen

with open('lu_dict.pickle', 'wb') as handle:
    pickle.dump(lux_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("...füllt deutsches Wörterbuch")

##create german_dict with format key:Wort,value:list[POS-Tag,index_occurences]
ger_text=open("mmd.txt", encoding='utf-8').read()
ger_text=ger_text.replace("-","")
ger_sent=nltk.sent_tokenize(ger_text)                                   ## alle Tokens
ger_tokens=nltk.word_tokenize(ger_text)                                 ## alle Sätze
for word in ger_tokens:
    ger_tokens_lower.append(word.lower())
ger_fdist=FreqDist(ger_tokens_lower)                                    ## alle Häufigkeiten pro Wort
with open('mmd_tagged.txt', encoding='utf-8') as fp:                    ## Ausgabe vom TreeTagger im Format [Wort,POS-Tag,Lemma]
    for line in fp:                                                     ## Iteration ueber jedes de. Wort
        words=line.split()
        if pattern.match(words[2]):
            continue;
        words[2]=words[2].lower()
        german_dict_value_list=[words[0]]                               ## Eigenschaftsliste (mit allen POS-Tags, werden  aber nicht verwendet)
        german_dict_value_list.append(ger_fdist[words[0].lower()])
        german_dict_value_list.append(words[1])
        search_regex_ger=r"\b"+re.escape(words[0])+r"\b"
        for d in sorted(lux_dict):                                      ## Levensthein-Distanz Abfragen
            if(len(words[2]) <=2):
                if (nltk.edit_distance(words[2],d)<=0):
                    german_dict_value_list.append(d)
            elif(3 <= len(words[2]) <=4):
                 if (nltk.edit_distance(words[2],d)<=1):
                    german_dict_value_list.append(d)
            elif(4 < len(words[2]) <= 6 ):
                if (nltk.edit_distance(words[2],d)<=2):
                    german_dict_value_list.append(d)
            elif(6 < len(words[2]) <=20 ):
                if (nltk.edit_distance(words[2],d)<=3):
                    german_dict_value_list.append(d)
        for entry in ger_sent:                                          ## Iteration ueber jeden de. Satz
            if re.search(search_regex_ger, entry, re.IGNORECASE):                      ## Sucht alle Satze in denen das Wort vor kommt
                german_dict_value_list.append(entry)
        german_dict[words[2]]=german_dict_value_list                    ## Eigenschaftsliste wird dem Wort zugewiesen

with open('de_dict.pickle', 'wb') as handle:
    pickle.dump(german_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("...generiert html Ausgabe")

f=open('de_lu3.html','x', encoding='utf-8')                              ## Erstellt HTML Datei
f.write(display_article(german_dict,lux_dict))                          ## Schreibt HTML Inhalt

print("...Programm ist beendet")
