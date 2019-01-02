def readfile():

        f = open('blogdata.txt')
        colline = f.readline()
        lines = f.readlines()
        blognames = []
        word = []

        colnames = colline.strip().split('\t')[1:]
        length = len(lines) - 1
        line = 1
        while line < length:
            part = lines[line].strip().split('\t')
            blognames.append(part[0])
            word.append([float(x) for x in part[1:]])
            line = line+1;
        return blognames, colnames, word