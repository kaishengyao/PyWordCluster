__author__ = 'kaisheny'

from Clustering import Clustering

class smtWordClustering(object):
    def __init__(self):
        self.word2cls = {}

    def generateClustering(self, doc, ncls, tofile):
        '''
        generate clustering from doc
        :param doc: document file name
        :param ncls: number of clusters
        :param tofile: file name to save cluster
        :return: save to a file
        '''
        wordFreq = Clustering.freq_dict_from_doc(doc)
        self.word2cls = Clustering.freq_to_cluster(wordFreq, ncls)
        Clustering.write_dict_to_file(self.word2cls, tofile)

if __name__ == "__main__":
    sln = smtWordClustering()
    #    doc = 'd:/data/smt/debug/bitext_voc160000.en'
    #    tofile = 'd:/data/smt/debug/bitext_voc160000.en.100.word.cls'
    doc = 'd:/data/smt/bitext_voc160000.en'
    tofile = 'd:/data/smt/bitext_voc160000.en.100.word.cls'
    sln.generateClustering(doc, 100, tofile)





