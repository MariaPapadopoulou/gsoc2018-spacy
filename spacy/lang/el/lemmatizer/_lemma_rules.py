# coding: utf8
from __future__ import unicode_literals


ADJECTIVE_RULES = [
    ["οί","ός"], # καρδιακοί
    ["ές","ός"], # επιφανειακές
    ["ές","ος"],
    ["οι","ος"],
    ["α","ης"], # αγαθοβιόλα
    ["ωδη","ες"], # δασώδη
    ["ώδη","ες"], 
    ["ότερη","ός"],
    ["ότερος","ός"],
    ["ότεροι", "ός"],
    ["ότερων","ός"],
    ["ότερες", "ός"],
]


NOUN_RULES = [
    ["ιά","ί"], # παιδιά
    ["ια","ι"], # ποτήρια
    ["ες","α"], # κεραμίδες
    ["ές","ά"],
    ["ές","ά"],
    ["ες","α"], # εσπερινές 
    ["ες","η"], # ζάχαρη
    ["ές","ή"], # φυλακές
    ["ές","ής"], # καθηγητής
    ["α","ο"], # πρόβατα
    ["ατα","α"], # στόματα
    ["άτα","άτα"], # ντομάτα
    ["άτες","άτα"], # πατάτες
    ["ία","ία"],
    ["ιά","ιά"],
    ["οί","ός"], # υπουργοί
]


VERB_RULES = [
    ["εις", "ω"],
    ["εις","ώ"],
    ["ει","ω"],
    ["ει","ώ"],
    ["ουμε","ω"],
    ["ουμε","ώ"],
    ["ετε","ω"],
    ["ετε","ώ"],
    ["ουν","ω"],
    ["ουν","ώ"],
    ["είς","ώ"],
    ["εί","ώ"],
    ["ούν","ώ"],
    ["εσαι","ομαι"], #αισθάνεσαι
    ["εσαι","όμαι"],
    ["έσαι","ομαι"],
    ["έσαι","όμαι"],
    ["εται","ομαι"], 
    ["εται","όμαι"],
    ["έται","ομαι"],
    ["έται","όμαι"],
    ["όμαστε","όμαι"],
    ["όμαστε","ομαι"],
    ["έσθε","όμαι"],
    ["εσθε","όμαι"],

]


PUNCT_RULES = [
    ["“", "\""],
    ["”", "\""],
    ["\u2018", "'"],
    ["\u2019", "'"]
]
