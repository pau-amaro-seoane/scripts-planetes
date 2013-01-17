import argparse

def parse_args():
    desc="Pau's Plot"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-r', '--range',  nargs=2, type=int, help='File numbers range')
    parser.add_argument('-s', '--single', nargs=1, type=int, help='Single file number to plot')
    args = parser.parse_args()

    # Empty dictionary with options
    options = dict()

    # Select only one option, or single, or range.
    if args.range != None and args.single != None:
        parser.print_help()
        sys.exit(0)

    # The mode of the reading will be store in the options['mode'] variable
    #   0 : default mode, read all the files
    #   1 : single mode, read only one file
    #   2 : range mode, read a range of files
    if args.range == None and args.single == None:
        options['mode'] = 0
    elif args.single != None and args.range == None:
        options['mode'] = 1
    elif args.single == None and args.range != None:
        options['mode'] = 2
    else:
        parser.print_help()
        sys.exit(0)

    # Adding the values on the two arguments of the parser
    options['single'] = args.single
    options['range']  = args.range

    return options
