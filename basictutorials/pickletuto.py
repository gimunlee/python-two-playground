""" Pickling tutorial """
import pickle
import cPickle

def main():
    """Test code"""

    temp_list = [1, 2, 3]
    repr_temp_list = pickle.dumps(temp_list)
    temp_list2 = pickle.loads(repr_temp_list)
    print temp_list2

    print temp_list == temp_list2
    print temp_list is temp_list2

    grades = [3, 2, 1]
    grades_file = open('grades.dat', 'wb')
    pickle.dump(grades, grades_file, -1)
    grades_file.close()

    new_grades_file = open('grades.dat', 'rb')
    new_grades = pickle.load(new_grades_file)
    new_grades_file.close()
    print new_grades

    repr_temp_list = cPickle.dumps(temp_list)
    temp_list2 = cPickle.loads(repr_temp_list)
    print temp_list2

if __name__ == '__main__':
    main()
