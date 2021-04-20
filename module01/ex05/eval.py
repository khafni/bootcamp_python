class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(words) != len(coefs):
            return -1
        e = 0
        for e1, e2 in zip(words, coefs):
            e += len(e1) * e2
        return e
    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(words) != len(coefs):
            return -1
        e = 0
        for index, elem in enumerate(words):
            e += len(elem) * coefs[index]
        return e