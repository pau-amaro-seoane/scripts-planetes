#!/usr/bin/env python

"""
#################################
Generic multiplot script for    #
matplotlib, with reminder for   #
styles                          #
                                #
Date, Berlin                    #
Pau Amaro Seoane                #
#################################
"""

"""
Generate images without having a window popup:
  matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
  or matplotlib.backends is imported for the first time.
"""
# Uncomment these to save directly to eps and look at the bottom
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Uncomment these to play around with ticks and look ahead
#from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from pylab import *

# LaTeX
from matplotlib import rc # needs dvipng
rc('text', usetex=True)
rc('font',**{'family':'serif','serif':['Palatino']})

# Black background
import matplotlib as mpl
mpl.rcParams['axes.facecolor']='black'

######## Create arrays from the data #####

# If there is no input parameters, the script will read all the files
# in the same directory.
# The parameters could be only "one" or "two" numbers, that will mean
# plot "one file" or plot "a range of files".
from parser import parse_args
from utils  import get_particle_colors_id, get_particle_colors, get_filenames

options = parse_args()

files = get_filenames(options)
first = True
for file in files:
    data = loadtxt(file)

    ID   = data[:, 0]  # Column 1
    mass = data[:, 1]  # Column 2
    x    = data[:, 2]  # Column 3
    y    = data[:, 3]  # Column 4
    z    = data[:, 4]  # Column 5

    # Sun
    xs = data[0,2]
    ys = data[0,3]
    zs = data[0,4]

    # Planet
    xp = data[1,2]  # Row 2, column 3
    yp = data[1,3]
    zp = data[1,4]


    ######################## Here starts the plot ##########################
                                                                           #
    # The upper subplot; 3 rows , 1 column , subplot #1                    #
    #--------------------------------------------------                    #
    #subplot (111)                                                          #
    #ay = subplot(111)                                                      #
    axis('equal') # Do you need a square box?                              #
    #ay.set_xscale('log')                                                   #
    #ay.set_yscale('log')                                                   #
    #grid(True, color = 'lightgrey', linewidth=0.75, linestyle=':')         #

    # Only T=0 and we save the index of the particles with colors
    if first:
        id_red, id_blue, id_white = get_particle_colors_id(ID,x,y,z)
        first = False
    red, blue, white = get_particle_colors(ID, x, y, z, id_red, id_blue, id_white)

    ylabel ('Y (AU)', size=18)                                  #
    plot(red[0], red[1], \
                              marker='o', markevery=1, ms=1,\
                              mec='black', mew=0, mfc='red',\
                              ls='', lw=1.0, color='red',\
                              antialiased=True)                            #
    plot(blue[0], blue[1], \
                              marker='o', markevery=1, ms=1,\
                              mec='black', mew=0, mfc='blue',\
                              ls='', lw=1.0, color='blue',\
                              antialiased=True)                            #
    plot(white[0], white[1], \
                              marker='o', markevery=1, ms=1,\
                              mec='black', mew=0, mfc='white',\
                              ls='', lw=1.0, color='white',\
                              antialiased=True)                            #
    plot(xp, yp, \
                              marker='o', ms=3,\
                              mec='black', mew=0.5, mfc='wheat',\
                              ls='', lw=1.0, color='red',\
                              antialiased=True)
    plot(xs, ys, \
                              marker='o', ms=3,\
                              mec='black', mew=0.5, mfc='yellow',\
                              ls='', lw=1.0, color='red',\
                              antialiased=True)

    # xlabel only here if common to all subplots                           #
    xlabel ('X (AU)', size=18)                #
                                                                           #
    ########################################################################


    ###### Limits #######
    #                   #
    xlim(-10,10)
    ylim(-10,10)
    #                   #
    #####################

    #xticks([-50, -40, -30, -20, -10, 0, +10, +20, +30, +40, +50])
    #yticks([-50, -40, -30, -20, -10, 0, +10, +20, +30, +40, +50])

    ##################### Ticks (needs uncommented import in preamble) ##################
    #                                                                                   #
    # majorLocator   = MultipleLocator(0.14)   # only multiples of 0.14 for major ticks #
    # majorFormatter = FormatStrFormatter('%1.1f') # format of these                    #
    # minorLocator   = MultipleLocator(0.005)  # as before but for minor ticks          #
    #                                                                                   #
    # subplot (311)                            # specify for which subplot              #
    # ax = subplot(311)                        # and define again axis                  #
    #                                                                                   #
    # ax.xaxis.set_major_locator(majorLocator) # set it                                 #
    # ax.xaxis.set_major_formatter(majorFormatter)                                      #
    ##for the minor ticks, use no labels; default NullFormatter                         #
    # ax.xaxis.set_minor_locator(minorLocator)                                          #
    #                                                                                   #
    #####################################################################################


    ######### Choose between pop-up window and eps output ######
                                                               #
    # Draw the thing with a window pop-up:                     #
    #plt.show()                                                     #
                                                               #
    # Generate images without having a window popup:           #
    # (have a look at the top)                                 #
    plt.savefig(file+'.png')                            #
                                                               #
    # When using within a shell script over a number of files  #
    # which use the $1 (sys.argv[1])                           #
    #name, ext = sys.argv[1].split('.')                        #
    #plt.savefig('%s.eps' % name)                              #
                                                               #
    ############################################################
