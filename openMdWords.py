# open md words

a = ["trite",
"hegemony",
"ravenous",
"arcane",
"munificent",
"garrulous",
"prolific",
"taciturn",
"sycophant",
"sporadic",
"subversive"]

import webbrowser, time

pre = "https://mnemonicdictionary.com/word/"

for w in a:
    print "opening " + pre + w
    webbrowser.open(pre + w)
    time.sleep(1)
