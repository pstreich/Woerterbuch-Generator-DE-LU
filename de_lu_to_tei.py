import pickle
import collections
import yattag
from yattag import Doc, indent

def de_dict_to_tei(data_ger,data_lux):
    counter_entry_de = 0
    doc, tag, text = Doc().tagtext()
    doc.asis('<?xml version="1.0" encoding="UTF-8"?>')
    doc.asis('<?xml-model href="de_lu.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>')
    doc.asis('<TEI xmlns="http://www.tei-c.org/ns/1.0">')
    with tag('teiHeader'):
        with tag('fileDesc'):
            with tag('titleStmt'):
                with tag('title'):
                    text("TEI Version of DE-LU dictionary")
            with tag('publicationStmt'):
                with tag('p'):
                    text("Original Data: Pierre Streicher")
            with tag('sourceDesc'):
                with tag('p'):
                    text("DE-LU - TEI Version")
    with tag('text'):
        with tag('body'):
            for d in sorted(data_ger):
                counter_entry_de +=1
                with tag('entry',('xml:id','entry'+str(counter_entry_de))):
                    with tag('form',('type','lemma')):
                        with tag('orth',('xml:lang','de')):
                            text(d)
                    with tag('form',('type','variant')):
                        with tag('orth',('xml:lang','de')):
                            text(data_ger[d][0])
                        with tag('measure',('type','frequency')):
                            with tag('num'):
                                text(data_ger[d][1])
                                counter_note_de=0
                        for entry in data_ger[d][3:]:
                            if (len(entry.split()) > 1):
                                counter_note_de+=1
                                with tag('note',('xml:id','entry'+str(counter_entry_de)+'_note'+str(counter_note_de))):
                                    text(entry)
                    with tag('gramGrp'):
                        with tag('pos'):
                            text(data_ger[d][2])
                            counter_sense_lu=0
                    for entry in data_ger[d][3:]:
                        if (len(entry.split()) == 1):
                            counter_sense_lu+=1
                            with tag('sense',('xml:id','entry'+str(counter_entry_de)+'_sense'+str(counter_sense_lu)),('xml:lang','lu')):
                                with tag('def'):
                                    text(entry)
                                with tag('measure',('type','frequency')):
                                    with tag('num'):
                                        try:
                                            text(data_lux[entry][0])
                                        except:
                                            text("n.a.")
                                        counter_note_lu=0
                                for entry_note in data_lux[entry][1:]:
                                    if (len(entry_note.split()) > 1):
                                        counter_note_lu+=1
                                        with tag('note',('xml:id','entry'+str(counter_entry_de)+'_sense'+str(counter_sense_lu)+'_note'+str(counter_note_lu))):
                                            text(entry_note)
    doc.asis('</TEI>')
    return indent(doc.getvalue())

def lu_dict_to_tei(data_ger,data_lux):
    counter_entry_lu = 0
    doc, tag, text = Doc().tagtext()
    doc.asis('<?xml version="1.0" encoding="UTF-8"?>')
    doc.asis('<?xml-model href="de_lu.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>')
    doc.asis('<TEI xmlns="http://www.tei-c.org/ns/1.0">')
    with tag('teiHeader'):
        with tag('fileDesc'):
            with tag('titleStmt'):
                with tag('title'):
                    text("TEI Version of LU-DE dictionary")
            with tag('publicationStmt'):
                with tag('p'):
                    text("Original Data: Pierre Streicher")
            with tag('sourceDesc'):
                with tag('p'):
                    text("LU-DE - TEI Version")
    with tag('text'):
        with tag('body'):
            for d in sorted(data_lux):
                counter_entry_lu+=1
                with tag('entry',('xml:id','entry'+str(counter_entry_lu))):
                    with tag('form',('type','variant')):
                        with tag('orth',('xml:lang','lu')):
                            text(d)
                        with tag('measure',('type','frequency')):
                            with tag('num'):
                                try:
                                    text(data_lux[d][0])
                                except:
                                    text("n.a.")
                        counter_note_o_lu = 0
                        for entry in data_lux[d][1:]:
                            if (len(entry.split()) > 1):
                                counter_note_o_lu+=1
                                with tag('note',('xml:id','entry'+str(counter_entry_lu)+'_note'+str(counter_note_o_lu))):
                                    text(entry)
    doc.asis('</TEI>')
    return indent(doc.getvalue())

german_dict=collections.defaultdict(list)
lux_dict=collections.defaultdict(list)

with open('de_dict.pickle', 'rb') as handle:
    german_dict = pickle.load(handle)

with open('lu_dict.pickle', 'rb') as handle:
    lux_dict = pickle.load(handle)

f=open('data_to_publish/de_dict_tei.xml','x', encoding='utf-8')
f.write(de_dict_to_tei(german_dict,lux_dict))

f=open('data_to_publish/lu_dict_tei.xml','x', encoding='utf-8')
f.write(lu_dict_to_tei(german_dict,lux_dict))