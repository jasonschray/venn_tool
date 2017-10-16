import getopt,sys,logging
import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles
from matplotlib_venn_wordcloud import venn2_wordcloud, venn3_wordcloud

def read_file():
    return True

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:v", ["help", "input=", "verbose"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    verbose = False
    fileName = None
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-i", "--input"):
            fileName = a
        else:
            assert False, "unhandled option"

    if verbose:
        logging.basicConfig(level=logging.INFO)
    if not fileName:
        logging.error('You must feed a valid input file. Example:\n'+
                        '   python main.py -i test.csv\n\n') 
        sys.exit()
    
    try:
        raw_data = pd.read_csv(fileName)
    except:
        logging.error('improper file format. File must be valid csv format.')
        sys.exit()   

    
    if len(raw_data.columns) != 3:
        logging.error('csv must have 3 datasets. This file is in improper format.')
        sys.exit()

    
    colA = raw_data[raw_data.columns[0]].dropna()
    colB = raw_data[raw_data.columns[1]].dropna()
    colC = raw_data[raw_data.columns[2]].dropna()


    logging.info('Data Set Parsed: '+str(colA.name))
    logging.info('Data Set Parsed: '+str(colB.name))
    logging.info('Data Set Parsed: '+str(colC.name)+'\n')

    group_110 = list((set(colA.tolist()).intersection(colB.tolist())).difference(set(colC.tolist())))
    group_011 = list((set(colC.tolist()).intersection(colB.tolist())).difference(set(colA.tolist())))
    group_101 = list((set(colA.tolist()).intersection(colC.tolist())).difference(set(colB.tolist())))
    group_111 = list((set(colA.tolist()).intersection(colB.tolist())).intersection(colC.tolist()))
    group_100 = (set(colA.tolist()).difference(set(group_110))).difference(set(group_101)).difference(set(group_111)) 
    group_010 = (set(colB.tolist()).difference(set(group_110))).difference(set(group_011)).difference(set(group_111))
    group_001 = (set(colC.tolist()).difference(set(group_011))).difference(set(group_101)).difference(set(group_111))

    logging.info('Sharted Items between '+str(colA.name)+
                 ' and '+str(colB.name)+':\n'+str(group_110)+'\n')
    logging.info('Sharted Items  between '+str(colB.name)+
                 ' and '+str(colC.name)+':\n'+str(group_011)+'\n')
    logging.info('Sharted Items  between '+str(colA.name)+
                 ' and '+str(colC.name)+':\n'+str(group_101)+'\n')
    logging.info('Sharted Items  between '+str(colA.name)+', '+str(colB.name)+', '+
                 ' and '+str(colC.name)+':\n'+str(group_111)+'\n')
    logging.info('Unique Items  of '+str(colA.name)+':\n'+ str(group_100)+'\n')
    logging.info('Unique Items  of '+str(colB.name)+':\n'+ str(group_010)+'\n')
    logging.info('Unique Items  of '+str(colC.name)+':\n'+ str(group_001)+'\n')
    basic_data = {colA.name:colA.tolist(),
                  colB.name:colB.tolist(),
                  colC.name:colC.tolist(),
                  }
    intersectioned_data = {'100':group_100,
                           '010':group_010,
                           '001':group_001,
                           '110':group_110,
                           '101':group_101,
                           '011':group_011,
                           '111':group_111,
                            }
    data_and_labels = {'data':intersectioned_data,
                       'lables':(colA.name,colB.name,colC.name)}
#    plot_simple_3venn_diagram(basic_data)
    plot_basic_venn_diagram(data_and_labels)
    
def plot_simple_3venn_diagram(data):
    set1 = set(['A', 'B', 'C', 'D'])
    set2 = set(['B', 'C', 'D', 'E'])
    set3 = set(['C', 'D',' E', 'F', 'G'])
    
    venn3([set1, set2, set3], ('Set1', 'Set2', 'Set3'))
    plt.show()

def convert_list_to_double_word(word_list):
    return True


def plot_basic_venn_diagram(data_and_labels):
    # Subset sizes
    data = data_and_labels['data']
    s = (
        len(data['100']),    # Abc
        len(data['010']),    # aBc
        len(data['110']),    # ABc
        len(data['001']),    # abC
        len(data['101']),    # AbC
        len(data['011']),    # aBC
        len(data['111']),    # ABC
    )

    v = venn3(subsets=s, set_labels=data_and_labels['lables'])
    
    # Subset labels
    v.get_label_by_id('100').set_text('\n'.join(data['100']))
    v.get_label_by_id('100').set_size(5)

    v.get_label_by_id('010').set_text('\n'.join(data['010']))
    v.get_label_by_id('010').set_size(5)

    v.get_label_by_id('110').set_text('\n'.join(data['110']))
    v.get_label_by_id('110').set_size(5)

    v.get_label_by_id('001').set_text('\n'.join(data['001']))
    v.get_label_by_id('001').set_size(5)

    v.get_label_by_id('101').set_text('\n'.join(data['101']))
    v.get_label_by_id('101').set_size(5)

    v.get_label_by_id('011').set_text('\n'.join(data['011']))
    v.get_label_by_id('011').set_size(5)

    v.get_label_by_id('111').set_text('\n'.join(data['111']))
    v.get_label_by_id('111').set_size(5)


    # Subset colors
    v.get_patch_by_id('100').set_color('#ADFF2F')
    v.get_patch_by_id('010').set_color('#993333')
    v.get_patch_by_id('110').set_color('blue')

    # Subset alphas
    v.get_patch_by_id('101').set_alpha(0.4)
    v.get_patch_by_id('011').set_alpha(1.0)
    v.get_patch_by_id('111').set_alpha(0.7)

    # Border styles
    c = venn3_circles(subsets=s, linestyle='None')
    c[0].set_lw(0) 
    c[1].set_lw(0)
    c[2].set_lw(0)     
    c[0].set_alpha(0)    
    c[1].set_alpha(0)
    c[2].set_alpha(0)


    plt.show()    


def usage():
    print('The following input arguments are supported:\n'+
          ' -h, --help\n'+
          '     This outputs a help menu describing all of the input arguments\n'+
          ' -i [input file], --input [input file]\n'+
          '     This is a required input argument that specifices the path of input data\n'+
          ' -v, --verbose\n'+
          '     This makes the script more verbose in its logging'
          )


if __name__ == "__main__":
    main()
else:
    print 'I think you might be running other scripts in this folder other than main...'
