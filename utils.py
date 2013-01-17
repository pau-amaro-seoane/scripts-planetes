#!/usr/bin/env python

from math import sqrt
import subprocess
import shlex
import sys

def get_filenames(options):

    # Default, all the files
    cmd = "find . -maxdepth 1 -regex './ascii_[0-9][0-9][0-9]' -type f -exec ls -1rt '{}' +"
    files = []
    if options['mode'] == 0:
        # All the files using "ascii_XXX" with 3 numbers
        out = subprocess.Popen(shlex.split(cmd), stdout = subprocess.PIPE)
        files = [i.rstrip() for i in out.stdout]

    elif options['mode'] == 1:
        files.append('ascii_'+str(options['single'][0]).zfill(3))
        try:
            with open(files[0]) as f: pass
        except IOError as e:
            print('File not found')
            sys.exit(0)

    elif options['mode'] == 2:
        # Get all the files
        out = subprocess.Popen(shlex.split(cmd), stdout = subprocess.PIPE)
        files = [i.rstrip() for i in out.stdout]
        # Create subset
        ini_file = 'ascii_'+str(options['range'][0]).zfill(3)
        end_file = 'ascii_'+str(options['range'][1]).zfill(3)
        print(ini_file)
        print(end_file)

        # The files included are RANGE_INI <= i <= RANGE_END
        files = [i for i in files if i.replace('./','') <= end_file and i.replace('./','') >= ini_file]

    #print(files)
    #sys.exit(0)
    return files

def get_particle_colors_id(ID, x, y, z):
    # Data split by R
    id_red    = []
    id_blue   = []
    id_white  = []

    # Change this values !!!!
    Rred   = 1
    Rblue  = 20
    Rwhite = 60

    # Going through the IDs
    for ii in range(len(ID)):
        xx = x[ii]
        yy = y[ii]
        zz = z[ii]
        id = int(ID[ii])
        r = sqrt(xx**2 + yy**2 + zz**2)
        # Find the points smaller than Rred
        if r < Rred:
            id_red.append(id)

        # Find the points smaller than Rblue
        elif r < Rblue:
            id_blue.append(id)

        # Find the points smaller than Rwhite
        elif r < Rwhite:
            id_white.append(id)

        else:
            print("Out of bounds!")

    # Now, red, blue and white are lists with
    # the IDs of the particles.

    return frozenset(id_red), frozenset(id_blue), frozenset(id_white)

def get_particle_colors(ID, x, y, z, id_red, id_blue, id_white):

    red   = [[],[],[]]
    blue  = [[],[],[]]
    white = [[],[],[]]

    for i, xx, yy, zz in zip(ID, x, y, z):
        if i in id_red:
            red[0].append(xx)
            red[1].append(yy)
            red[2].append(zz)

        elif i in id_blue:
            blue[0].append(xx)
            blue[1].append(yy)
            blue[2].append(zz)

        elif i in id_white:
            white[0].append(xx)
            white[1].append(yy)
            white[2].append(zz)

    return red, blue, white
