def make_training_set(training_file_name):
    '''Reads a training set from the specified file.
       return list of tuples in format: id, diagnosis, 9 attributes.'''
    training_set_list = []
    # open file
    training_file = open(training_file_name)
    # read each line in the file
    for line_str in training_file:
        line_str = line_str.strip() # strip off EOF character '\n'
        # parse the line into its 11 parts
        id_str,a1,a2,a3,a4,a5,a6,a7,a8,a9,diagnosis_str = line_str.split(',')
        if diagnosis_str == '4': # diagnosis is 'malignant'
            diagnosis_str = 'm'
        else:
            diagnosis_str = 'b' # diagnosis is 'benign'
        # create a tuple for the patient
        patient_tuple = id_str, diagnosis_str,int(a1),int(a2),int(a3),int(a4),\
            int(a5),int(a6),int(a7),int(a8),int(a9)
        # append to the end of the training_set list
        training_set_list.append(patient_tuple)
    # close file
    training_file.close()
    return training_set_list # return the training set

def train_classifier(training_set_list):
    return []

def make_test_set(test_file_name):
    return []

def classify_test_set_list(test_set_list, classifier_list):
    return []

def report_results(reslt_list):
    print('Reposted the results')

def main():
    
    print('Reading in training data...')
    training_dile_name = 'breast-cancer-training.data'
    training_set_list = make_training_set(training_dile_name)
    print('Done reading training data.\n')

    print('Training classifier...')
    classifier_list = train_classifier(training_set_list)
    print('Done training classifier.\n')

    print('Reading in test data...')
    test_file_name = 'breast-cancer-test.data'
    test_set_list = make_test_set(test_file_name)
    print('Done reading test data.\n')

    print('Classifying records...')
    result_list = classify_test_set_list(training_set_list, classifier_list)
    print('Done classifying.\n')

    report_results(result_list)

    print('Program finished.')

if __name__ == '__main__':
    main()