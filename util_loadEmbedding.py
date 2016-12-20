def load_embedding(emb_path):
    file = open(emb_path)
    words_num, emb_size = [int(x) for x in next(file).split()]

    w2vovcab = {}
    v2wvocab = {}

    M = []

    for i in range(0, words_num):
    #for i in range(0, 3):
        temp_line = next(file).split()
        temp_word = temp_line[0]
        temp_embdata = temp_line[1:]
        M.append(temp_embdata)
        w2vovcab[temp_word] = i
        v2wvocab[i] = temp_word

    #print temp_word, temp_embdata
    return M, w2vovcab
