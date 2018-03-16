#! python3
#Output: readNRCLexiconExcel.txt - Read the NRC lexicon. Return the English
#and Dutch words with their positve/negative value in a list

import openpyxl, pprint

print('Opening workbook...')

wb = openpyxl.load_workbook('lexi.xlsx')

sheet = wb.active

lexiconData = {}

en_words = {}

nl_words = {}

#TODO: Fill in lexiconData with each English and Dutch words from
#the NRC lexicon with their values

'Read rows'

for row in range(2, sheet.max_row + 1):
    #Each row has a word, label and value
    ENword = sheet['A' + str(row)].value
    NLword = sheet['I' + str(row)].value
    neg_label = sheet['AQ' + str(row)].value
    pos_label = sheet['AP' + str(row)].value

    'Fill in labeled words by language'
    en_words.setdefault(ENword,{'positive': pos_label, 'negative': neg_label})
    nl_words.setdefault(NLword,{'positive': pos_label, 'negative': neg_label})

    'Add the EN and NL words to the lexicon dictonary'
    lexiconData.update(en_words)
    lexiconData.update(nl_words)

print('Done.')

#TODO: Open a new file text and write the contents of
#lexiconData to it

print('Writing results...')

##'This part prints output of the data in python'
##for x in lexiconData:
##    for y in lexiconData[x]:
##            print(x, y, lexiconData[x][y])

'Write the output of the labels in a text file'
resultFile = open('lexicon.txt', 'w')

for x in lexiconData:
    for y in lexiconData[x]:
        z = "{} {} {}\n".format(x, y, str(lexiconData[x][y]))
        try:
            resultFile.write(z)
        except Exception as e:
            continue

resultFile.close()


print('Done.')

