# class SingletonGovt:
#    __instance__ = None
#    def __init__(self):
#        """ Constructor.
#        """
#        if SingletonGovt.__instance__ is None:
#            SingletonGovt.__instance__ = self
#        else:
#             # SingletonGovt.__instance__ = SingletonGovt.__instance__
#            raise Exception("You cannot create another SingletonGovt class")
#
#    @staticmethod
#    def get_instance():
#        """ Static method to fetch the current instance.
#        """
#        if not SingletonGovt.__instance__:
#            SingletonGovt()
#        return SingletonGovt.__instance__
#
# government = SingletonGovt()
# print(id(government))
# same_government = SingletonGovt.get_instance()
# print(id(same_government))
# another_government = SingletonGovt.get_instance()
# print(id(another_government))
# new_government = SingletonGovt()
# print(id(new_government))
#
#
# # class Singleton:
# #    __instance = None
# #    @staticmethod
# #    def getInstance():
# #       """ Static access method. """
# #       if Singleton.__instance == None:
# #          Singleton()
# #       return Singleton.__instance
# #    def __init__(self):
# #       """ Virtually private constructor. """
# #       if Singleton.__instance != None:
# #           raise Exception("This class is a singleton!")
# #       else:
# #          Singleton.__instance = self
# # s = Singleton()
# # print(s)
# #
# # s = Singleton.getInstance()
# # print(s)
# #
# # s = Singleton.getInstance()
# # print(s)
# #
# # s1 = Singleton()
# # print(s1)



import operator

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        # print(word)
        num_vowels = 0
        for letter in word:
            # print(letter)
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score +=1
    return score


n = int(input())
words = input().split()
print(words)
print(score_words(words))