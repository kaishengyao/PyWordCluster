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

def write_dict_of_list_to_file(d, file_name):
    with open(file_name, 'w') as f:
        for k, v in sorted(d.items()):
            for t in v:
                f.write('%s %d\n' % (t, k))

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
    cls2wrd = {}
    classId = 0
    classCnt = 0
    cls2wrd[classId] = []
    for w in sorted(wordFreq, key=wordFreq.get, reverse=True):
        cnt = wordFreq[w]
        classCnt += cnt
        word2cls[w] = classId
        cls2wrd[classId].append(w)
        if classCnt > binSize:
            classId += 1
            classCnt = 0
            cls2wrd[classId] = []

    return word2cls, cls2wrd


