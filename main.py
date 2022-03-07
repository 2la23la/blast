
import re
Blosum = {
    ('W', 'F'): 1, ('L', 'R'): -2, ('S', 'P'): -1, ('V', 'T'): 0,
    ('Q', 'Q'): 5, ('N', 'A'): -2, ('Z', 'Y'): -2, ('W', 'R'): -3,
    ('Q', 'A'): -1, ('S', 'D'): 0, ('H', 'H'): 8, ('S', 'H'): -1,
    ('H', 'D'): -1, ('L', 'N'): -3, ('W', 'A'): -3, ('Y', 'M'): -1,
    ('G', 'R'): -2, ('Y', 'I'): -1, ('Y', 'E'): -2, ('B', 'Y'): -3,
    ('Y', 'A'): -2, ('V', 'D'): -3, ('B', 'S'): 0, ('Y', 'Y'): 7,
    ('G', 'N'): 0, ('E', 'C'): -4, ('Y', 'Q'): -1, ('Z', 'Z'): 4,
    ('V', 'A'): 0, ('C', 'C'): 9, ('M', 'R'): -1, ('V', 'E'): -2,
    ('T', 'N'): 0, ('P', 'P'): 7, ('V', 'I'): 3, ('V', 'S'): -2,
    ('Z', 'P'): -1, ('V', 'M'): 1, ('T', 'F'): -2, ('V', 'Q'): -2,
    ('K', 'K'): 5, ('P', 'D'): -1, ('I', 'H'): -3, ('I', 'D'): -3,
    ('T', 'R'): -1, ('P', 'L'): -3, ('K', 'G'): -2, ('M', 'N'): -2,
    ('P', 'H'): -2, ('F', 'Q'): -3, ('Z', 'G'): -2, ('X', 'L'): -1,
    ('T', 'M'): -1, ('Z', 'C'): -3, ('X', 'H'): -1, ('D', 'R'): -2,
    ('B', 'W'): -4, ('X', 'D'): -1, ('Z', 'K'): 1, ('F', 'A'): -2,
    ('Z', 'W'): -3, ('F', 'E'): -3, ('D', 'N'): 1, ('B', 'K'): 0,
    ('X', 'X'): -1, ('F', 'I'): 0, ('B', 'G'): -1, ('X', 'T'): 0,
    ('F', 'M'): 0, ('B', 'C'): -3, ('Z', 'I'): -3, ('Z', 'V'): -2,
    ('S', 'S'): 4, ('L', 'Q'): -2, ('W', 'E'): -3, ('Q', 'R'): 1,
    ('N', 'N'): 6, ('W', 'M'): -1, ('Q', 'C'): -3, ('W', 'I'): -3,
    ('S', 'C'): -1, ('L', 'A'): -1, ('S', 'G'): 0, ('L', 'E'): -3,
    ('W', 'Q'): -2, ('H', 'G'): -2, ('S', 'K'): 0, ('Q', 'N'): 0,
    ('N', 'R'): 0, ('H', 'C'): -3, ('Y', 'N'): -2, ('G', 'Q'): -2,
    ('Y', 'F'): 3, ('C', 'A'): 0, ('V', 'L'): 1, ('G', 'E'): -2,
    ('G', 'A'): 0, ('K', 'R'): 2, ('E', 'D'): 2, ('Y', 'R'): -2,
    ('M', 'Q'): 0, ('T', 'I'): -1, ('C', 'D'): -3, ('V', 'F'): -1,
    ('T', 'A'): 0, ('T', 'P'): -1, ('B', 'P'): -2, ('T', 'E'): -1,
    ('V', 'N'): -3, ('P', 'G'): -2, ('M', 'A'): -1, ('K', 'H'): -1,
    ('V', 'R'): -3, ('P', 'C'): -3, ('M', 'E'): -2, ('K', 'L'): -2,
    ('V', 'V'): 4, ('M', 'I'): 1, ('T', 'Q'): -1, ('I', 'G'): -4,
    ('P', 'K'): -1, ('M', 'M'): 5, ('K', 'D'): -1, ('I', 'C'): -1,
    ('Z', 'D'): 1, ('F', 'R'): -3, ('X', 'K'): -1, ('Q', 'D'): 0,
    ('X', 'G'): -1, ('Z', 'L'): -3, ('X', 'C'): -2, ('Z', 'H'): 0,
    ('B', 'L'): -4, ('B', 'H'): 0, ('F', 'F'): 6, ('X', 'W'): -2,
    ('B', 'D'): 4, ('D', 'A'): -2, ('S', 'L'): -2, ('X', 'S'): 0,
    ('F', 'N'): -3, ('S', 'R'): -1, ('W', 'D'): -4, ('V', 'Y'): -1,
    ('W', 'L'): -2, ('H', 'R'): 0, ('W', 'H'): -2, ('H', 'N'): 1,
    ('W', 'T'): -2, ('T', 'T'): 5, ('S', 'F'): -2, ('W', 'P'): -4,
    ('L', 'D'): -4, ('B', 'I'): -3, ('L', 'H'): -3, ('S', 'N'): 1,
    ('B', 'T'): -1, ('L', 'L'): 4, ('Y', 'K'): -2, ('E', 'Q'): 2,
    ('Y', 'G'): -3, ('Z', 'S'): 0, ('Y', 'C'): -2, ('G', 'D'): -1,
    ('B', 'V'): -3, ('E', 'A'): -1, ('Y', 'W'): 2, ('E', 'E'): 5,
    ('Y', 'S'): -2, ('C', 'N'): -3, ('V', 'C'): -1, ('T', 'H'): -2,
    ('P', 'R'): -2, ('V', 'G'): -3, ('T', 'L'): -1, ('V', 'K'): -2,
    ('K', 'Q'): 1, ('R', 'A'): -1, ('I', 'R'): -3, ('T', 'D'): -1,
    ('P', 'F'): -4, ('I', 'N'): -3, ('K', 'I'): -3, ('M', 'D'): -3,
    ('V', 'W'): -3, ('W', 'W'): 11, ('M', 'H'): -2, ('P', 'N'): -2,
    ('K', 'A'): -1, ('M', 'L'): 2, ('K', 'E'): 1, ('Z', 'E'): 4,
    ('X', 'N'): -1, ('Z', 'A'): -1, ('Z', 'M'): -1, ('X', 'F'): -1,
    ('K', 'C'): -3, ('B', 'Q'): 0, ('X', 'B'): -1, ('B', 'M'): -3,
    ('F', 'C'): -2, ('Z', 'Q'): 3, ('X', 'Z'): -1, ('F', 'G'): -3,
    ('B', 'E'): 1, ('X', 'V'): -1, ('F', 'K'): -3, ('B', 'A'): -2,
    ('X', 'R'): -1, ('D', 'D'): 6, ('W', 'G'): -2, ('Z', 'F'): -3,
    ('S', 'Q'): 0, ('W', 'C'): -2, ('W', 'K'): -3, ('H', 'Q'): 0,
    ('L', 'C'): -1, ('W', 'N'): -4, ('S', 'A'): 1, ('L', 'G'): -4,
    ('W', 'S'): -3, ('S', 'E'): 0, ('H', 'E'): 0, ('S', 'I'): -2,
    ('H', 'A'): -2, ('S', 'M'): -1, ('Y', 'L'): -1, ('Y', 'H'): 2,
    ('Y', 'D'): -3, ('E', 'R'): 0, ('X', 'P'): -2, ('G', 'G'): 6,
    ('G', 'C'): -3, ('E', 'N'): 0, ('Y', 'T'): -2, ('Y', 'P'): -3,
    ('T', 'K'): -1, ('A', 'A'): 4, ('P', 'Q'): -1, ('T', 'C'): -1,
    ('V', 'H'): -3, ('T', 'G'): -2, ('I', 'Q'): -3, ('Z', 'T'): -1,
    ('C', 'R'): -3, ('V', 'P'): -2, ('P', 'E'): -1, ('M', 'C'): -1,
    ('K', 'N'): 0, ('I', 'I'): 4, ('P', 'A'): -1, ('M', 'G'): -3,
    ('T', 'S'): 1, ('I', 'E'): -3, ('P', 'M'): -2, ('M', 'K'): -1,
    ('I', 'A'): -1, ('P', 'I'): -3, ('R', 'R'): 5, ('X', 'M'): -1,
    ('L', 'I'): 2, ('X', 'I'): -1, ('Z', 'B'): 1, ('X', 'E'): -1,
    ('Z', 'N'): 0, ('X', 'A'): 0, ('B', 'R'): -1, ('B', 'N'): 3,
    ('F', 'D'): -3, ('X', 'Y'): -1, ('Z', 'R'): 0, ('F', 'H'): -1,
    ('B', 'F'): -3, ('F', 'L'): 0, ('X', 'Q'): -1, ('B', 'B'): 4
}
wordList = []

querySeq = input("Please Enter the protein sequence ").upper()
WordThreshold = int(input("Please Enter the word threshold "))
WordLength = int(input("Please Enter the word length "))
HSPThreshold = int(input("Please Enter the HSP threshold "))
querySeqScores = []
#getting the score for each character and itself
for i in range (0, len(querySeq)):
    score = Blosum[(querySeq[i],querySeq[i])]
    querySeqScores.append(score)
print(querySeqScores)
#remove low complexity
queryseq = list(querySeq)
for i in range (0,len(querySeqScores)):
    if (len(querySeqScores)-i)>=len(querySeqScores)-2:
        if (querySeqScores[i] == querySeqScores[i + 2]) and (querySeqScores[i + 1] == querySeqScores[i + 3]):
            queryseq[i] = 'X'
            queryseq[i + 1] = 'X'
            queryseq[i + 2] = 'X'
            queryseq[i + 3] = 'X'
print(queryseq)

#dividing our query to seeds
for i in range(0, len(querySeq)):
    word = querySeq[i: (i + WordLength)].upper()
    if len(word) == WordLength:
        wordList.append(word)

print(wordList)

aminoAcids = ['W', 'F', 'L', 'R', 'S', 'P', 'V', 'T', 'Q', 'N', 'A', 'Z', 'Y', 'D', 'H', 'M', 'G', 'I', 'E', 'B']
newWordList = []
# generating mutation for the first letter of each seed
for i in range(0, len(wordList)):
    for j in aminoAcids:
        for x in range(0, WordLength):
            sum = 0
            mutation = list(wordList[i])
            mutation[x] = j
            mutationStr = ""
            if Blosum.get((wordList[i][x], mutation[x])) is None:
                mutatedLetter = Blosum.get((mutation[x], wordList[i][x]))
            else:
                mutatedLetter = Blosum.get((wordList[i][x], mutation[x]))
            sum += mutatedLetter
            for y in range(0, WordLength):
                mutationStr = mutationStr + (mutation[y])
                if (y != x):
                    sum += Blosum[(wordList[i][y], mutation[y])]

            if sum > WordThreshold and (wordList[i][x] != mutationStr[x] or x == 0):
                z = {"seed": mutationStr,
                     "start": i,
                     "score": sum}
                newWordList.append(z)
print(newWordList)

#splitting our db into lines
database = open("datebase.txt")
databaseSeq = database.read().splitlines()
foundMatches=[]

#finding the matcheing hits btw each line in db & our wordtuple
for i in range(0,len(databaseSeq)):
    for wordTuple in newWordList:
        seed = wordTuple["seed"]
        matched = re.search(seed,databaseSeq[i])
        if(matched is not None):
            print(matched)
            x= {"seqIndex":i,
                "span":matched.span(),
                "WordTuple": wordTuple}
            foundMatches.append(x)

# extension part
extended_qr = []
extended_db = []
extension_info = []
for i in foundMatches:
    index = 0
    sen_db = databaseSeq[i["seqIndex"]]
    ext_db = i["WordTuple"]["seed"]
    ext_qr = i["WordTuple"]["seed"]
    totalsc = i["WordTuple"]["score"]
    maxScr = totalsc
    a = True
    b = True
    stopcondition_a = True
    stopcondition_b = True
    while a or b:
        a = False
        b = False
        # appending the letters to the right
        if stopcondition_a:
            if ((i["span"][1] + index) < len(sen_db)) and (
                    (i["WordTuple"]["start"] + WordLength + index) < len(queryseq)):
                ch_dbr = sen_db[i["span"][1] + index]
                ch_qrr = queryseq[i["WordTuple"]["start"] + WordLength + index]
                if Blosum.get((ch_dbr, ch_qrr)) is None:
                    scr = Blosum.get((ch_qrr, ch_dbr))
                else:
                    scr = Blosum.get((ch_dbr, ch_qrr))
                currentScrr = totalsc + scr
                if (maxScr - currentScrr) <= 3:
                    ext_qr += ch_qrr
                    ext_db += ch_dbr
                    totalsc = currentScrr
                    if totalsc > maxScr:
                        maxScr = totalsc
                    a = True
                else:
                    stopcondition_a = False

        # appending the letters to the left
        if stopcondition_b:
            if ((i["span"][0] - index - 1) >= 0 and ((i["WordTuple"]["start"] - index - 1) >= 0)):
                ch_dbl = sen_db[i["span"][0] - index - 1]
                ch_qrl = queryseq[i["WordTuple"]["start"] - index - 1]
                if Blosum.get((ch_dbl, ch_qrl)) is None:
                    scl = Blosum.get((ch_qrl, ch_dbl))
                else:
                    scl = Blosum.get((ch_dbl, ch_qrl))
                currentScrl = totalsc + scl
                if (maxScr - currentScrr) <= 3:
                    ext_qr = ch_qrl + ext_qr
                    ext_db = ch_dbl + ext_db
                    totalsc = currentScrl
                    if totalsc > maxScr:
                        maxScr = totalsc
                    b = True
                else:
                    stopcondition_b = False

        index += 1
    if totalsc > HSPThreshold:
        x = {"Found sequence": ext_db,
             "Score": totalsc,
             "database index": i["seqIndex"]}
        extension_info.append(x)
        extended_qr.append(ext_qr)

if len(extended_qr) == 0:
    print("query not found")
else:
    print(extension_info)
    print(extended_qr)
