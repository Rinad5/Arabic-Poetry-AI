from keras import Sequential
from keras.layers import LSTM, Dropout, Flatten, Dense
from keras.models import load_model
import numpy as np



'''
V 3.0
['\n', ' ', 'ء', 'آ', 'أ', 'ؤ', 'إ', 'ئ', 'ا', 'ب', 'ة', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ى', 'ي']
{'\n': 0, ' ': 1, 'ء': 2, 'آ': 3, 'أ': 4, 'ؤ': 5, 'إ': 6, 'ئ': 7, 'ا': 8, 'ب': 9, 'ة': 10, 'ت': 11, 'ث': 12, 'ج': 13, 'ح': 14, 'خ': 15, 'د': 16, 'ذ': 17, 'ر': 18, 'ز': 19, 'س': 20, 'ش': 21, 'ص': 22, 'ض': 23, 'ط': 24, 'ظ': 25, 'ع': 26, 'غ': 27, 'ف': 28, 'ق': 29, 'ك': 30, 'ل': 31, 'م': 32, 'ن': 33, 'ه': 34, 'و': 35, 'ى': 36, 'ي': 37}
{0: '\n', 1: ' ', 2: 'ء', 3: 'آ', 4: 'أ', 5: 'ؤ', 6: 'إ', 7: 'ئ', 8: 'ا', 9: 'ب', 10: 'ة', 11: 'ت', 12: 'ث', 13: 'ج', 14: 'ح', 15: 'خ', 16: 'د', 17: 'ذ', 18: 'ر', 19: 'ز', 20: 'س', 21: 'ش', 22: 'ص', 23: 'ض', 24: 'ط', 25: 'ظ', 26: 'ع', 27: 'غ', 28: 'ف', 29: 'ق', 30: 'ك', 31: 'ل', 32: 'م', 33: 'ن', 34: 'ه', 35: 'و', 36: 'ى', 37: 'ي'}



characters = [' ', 'ء', 'آ', 'أ', 'ؤ', 'إ', 'ئ', 'ا', 'ب', 'ة', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ى', 'ي']
chars_to_n = {' ': 0, 'ء': 1, 'آ': 2, 'أ': 3, 'ؤ': 4, 'إ': 5, 'ئ': 6, 'ا': 7, 'ب': 8, 'ة': 9, 'ت': 10, 'ث': 11, 'ج': 12, 'ح': 13, 'خ': 14, 'د': 15, 'ذ': 16, 'ر': 17, 'ز': 18, 'س': 19, 'ش': 20, 'ص': 21, 'ض': 22, 'ط': 23, 'ظ': 24, 'ع': 25, 'غ': 26, 'ف': 27, 'ق': 28, 'ك': 29, 'ل': 30, 'م': 31, 'ن': 32, 'ه': 33, 'و': 34, 'ى': 35, 'ي': 36}
n_to_chars = {0: ' ', 1: 'ء', 2: 'آ', 3: 'أ', 4: 'ؤ', 5: 'إ', 6: 'ئ', 7: 'ا', 8: 'ب', 9: 'ة', 10: 'ت', 11: 'ث', 12: 'ج', 13: 'ح', 14: 'خ', 15: 'د', 16: 'ذ', 17: 'ر', 18: 'ز', 19: 'س', 20: 'ش', 21: 'ص', 22: 'ض', 23: 'ط', 24: 'ظ', 25: 'ع', 26: 'غ', 27: 'ف', 28: 'ق', 29: 'ك', 30: 'ل', 31: 'م', 32: 'ن', 33: 'ه', 34: 'و', 35: 'ى', 36: 'ي'}
'''

'''
[' ', 'ء', 'آ', 'أ', 'ؤ', 'إ', 'ئ', 'ا', 'ب', 'ة', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ى', 'ي']
{' ': 0, 'ء': 1, 'آ': 2, 'أ': 3, 'ؤ': 4, 'إ': 5, 'ئ': 6, 'ا': 7, 'ب': 8, 'ة': 9, 'ت': 10, 'ث': 11, 'ج': 12, 'ح': 13, 'خ': 14, 'د': 15, 'ذ': 16, 'ر': 17, 'ز': 18, 'س': 19, 'ش': 20, 'ص': 21, 'ض': 22, 'ط': 23, 'ظ': 24, 'ع': 25, 'غ': 26, 'ف': 27, 'ق': 28, 'ك': 29, 'ل': 30, 'م': 31, 'ن': 32, 'ه': 33, 'و': 34, 'ى': 35, 'ي': 36}
{0: ' ', 1: 'ء', 2: 'آ', 3: 'أ', 4: 'ؤ', 5: 'إ', 6: 'ئ', 7: 'ا', 8: 'ب', 9: 'ة', 10: 'ت', 11: 'ث', 12: 'ج', 13: 'ح', 14: 'خ', 15: 'د', 16: 'ذ', 17: 'ر', 18: 'ز', 19: 'س', 20: 'ش', 21: 'ص', 22: 'ض', 23: 'ط', 24: 'ظ', 25: 'ع', 26: 'غ', 27: 'ف', 28: 'ق', 29: 'ك', 30: 'ل', 31: 'م', 32: 'ن', 33: 'ه', 34: 'و', 35: 'ى', 36: 'ي'}

'''



characters = ['\n', ' ', 'ء', 'آ', 'أ', 'ؤ', 'إ', 'ئ', 'ا', 'ب', 'ة', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ى', 'ي']
chars_to_n = {'\n': 0, ' ': 1, 'ء': 2, 'آ': 3, 'أ': 4, 'ؤ': 5, 'إ': 6, 'ئ': 7, 'ا': 8, 'ب': 9, 'ة': 10, 'ت': 11, 'ث': 12, 'ج': 13, 'ح': 14, 'خ': 15, 'د': 16, 'ذ': 17, 'ر': 18, 'ز': 19, 'س': 20, 'ش': 21, 'ص': 22, 'ض': 23, 'ط': 24, 'ظ': 25, 'ع': 26, 'غ': 27, 'ف': 28, 'ق': 29, 'ك': 30, 'ل': 31, 'م': 32, 'ن': 33, 'ه': 34, 'و': 35, 'ى': 36, 'ي': 37}
n_to_chars = {0: '\n', 1: ' ', 2: 'ء', 3: 'آ', 4: 'أ', 5: 'ؤ', 6: 'إ', 7: 'ئ', 8: 'ا', 9: 'ب', 10: 'ة', 11: 'ت', 12: 'ث', 13: 'ج', 14: 'ح', 15: 'خ', 16: 'د', 17: 'ذ', 18: 'ر', 19: 'ز', 20: 'س', 21: 'ش', 22: 'ص', 23: 'ض', 24: 'ط', 25: 'ظ', 26: 'ع', 27: 'غ', 28: 'ف', 29: 'ق', 30: 'ك', 31: 'ل', 32: 'م', 33: 'ن', 34: 'ه', 35: 'و', 36: 'ى', 37: 'ي'}


'''دنا البين من أروى فزالت حمولها
لتشغل أروى عن هواها شغولها

وما خفت منها البين حتى تزعزعت
هماليجها وازور عني دليلها'''

unparsedInput = input("Your input text for the prediction: ")
textLen = int(input("Number of chars to predict: "))

X = []

for char in unparsedInput[0:30]:
    X.append(chars_to_n[char])

modelP = load_model('Best_motanaby4.h5')
predTxt = []
for i in range(textLen):
    fitTestCase = np.reshape(X, (1, len(X), 1))
    fitTestCase = fitTestCase / float(len(characters))
    #print(modelP.predict(fitTestCase, verbose=1))
    prediction = np.argmax(modelP.predict(fitTestCase, verbose=0))
    #print(prediction)
    seq = [n_to_chars[n] for n in X]
    X.append(prediction)
    predTxt.append(prediction)
    X = X[1:len(X)]

unparsedTxt = [n_to_chars[val] for val in predTxt]
txt = ''
for char in unparsedTxt:
    txt += char
print(txt)
print(unparsedTxt)

