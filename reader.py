from xml.etree import ElementTree


class DatasetReader:
    def __init__(self, filename):
        self.__dataset = open(filename, 'r')
        self.__parsed_dataset = None

    def __parse(self):
        self.__parsed_dataset = list()
        for line in self.__dataset.readlines():
            sentence = list()
            line = line.replace(';', ' ')
            for word in line.split(' '):
                word = word.strip('\n')
                sentence.append(word)
            tag = sentence[-1]
            sentence.pop(-1)
            self.__parsed_dataset.append([tag, sentence])

    def read(self):
        if self.__parsed_dataset is None:
            self.__parse()
        return self.__parsed_dataset


class KorpusReader:
    def __init__(self, filename):
        self.__korpus = ElementTree.parse(filename)
        self.__parsed_korpus = None

    def __parse(self):
        self.__parsed_korpus = dict()
        root = self.__korpus.getroot()
        for child in root:
            lemma = child.attrib['lemma']
            lemma = lemma.replace('+', '')
            for variant in child:
                for form in variant:
                    word_form = form.text
                    word_form.replace('+', '')
                    self.__parsed_korpus[word_form] = lemma

    def read(self):
        if self.__parsed_korpus is None:
            self.__parse()
        return self.__parsed_korpus
