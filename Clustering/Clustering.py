__author__ = 'kaisheny'

def freq_dict_from_txt(txt, d):

    txt = txt.strip()
    words = txt.split(' ')
    for w in words:
        w = w.strip()
        if len(w) == 0:
            continue
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    return d

def write_dict_to_file(d, file_name):
    with open(file_name, 'w') as f:
        for k, v in sorted(d.items()):
            f.write('%s %d\n' % (k, v))

def freq_dict_from_doc(doc):
    wordFreq = {}
    with open (doc) as f:
        for line in f:
            freq_dict_from_txt(line, wordFreq)
    return wordFreq

def freq_to_cluster(wordFreq, ncls):
    '''
    sort words in descending order according to their frequency
    wordFreq: a dictionary of {word, counts} pair
    ncls : number of clusters
    '''
    totalCnt = 0
    for k, v in wordFreq.items():
        totalCnt += v
    binSize = totalCnt / ncls
    word2cls = {}
    classId = 0
    classCnt = 0
    for w in sorted(wordFreq, key=wordFreq.get, reverse=True):
        cnt = wordFreq[w]
        classCnt += cnt
        word2cls[w] = classId
        if classCnt > binSize:
            classId += 1
            classCnt = 0

    return word2cls


