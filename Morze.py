md = {
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z'
}

MHz = {
    'shell': '3.505MHz',
    'halls': '3.515MHz',
    'slick': '3.522MHz',
    'trick': '3.532MHz',
    'boxes': '3.535MHz',
    'leaks': '3.542MHz',
    'strobe': '3.545MHz',
    'bistro': '3.552MHz',
    'flick': '3.555MHz',
    'bombs': '3.565MHz',
    'break': '3.572MHz',
    'brick': '3.575MHz',
    'steak': '3.582MHz',
    'sting': '3.592MHz',
    'vector': '3.595MHz',
    'beats': '3.600MHz'
}

text = input().split(" ")
word = []
for i in text:
    word.append(md[i])
if ''.join(word) in MHz:
    print(MHz[''.join(word)])
else:
    print("I didn't find anything")
