""" anydbm tutorial """

import anydbm
db = anydbm.open('captions.db', 'c')

#db['gom.png'] = 'A face of a bear'

print db['gom.png']

db.close()
