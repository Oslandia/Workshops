#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

home_directory = os.path.expanduser('~') # '~' est un raccourci pour désigner le répertoire utilisateur.
file_list = os.listdir(home_directory)

count_dir = 0
count_file = 0
count_hidden = 0
count_others = 0
count = 0

for node in file_list:
    count = count + 1
    if node[0] == '.':
        count_hidden = count_hidden + 1
    if os.path.isfile(home_directory + '/' + node):
        count_file = count_file + 1
    elif os.path.isdir(home_directory + '/' + node):
        count_dir = count_dir + 1
    else:
        count_others = count_others + 1

print 'Le répertoire utilisateur contient :'
print '    - ' + str(count_file) + ' fichiers réguliers'
print '    - ' + str(count_dir) + ' répertoires'
print '    - ' + str(count_others) + ' autres fichiers'
print 'Notez que ' + str(count_hidden / float(count) * 100) + '% des fichiers sont masqués'

