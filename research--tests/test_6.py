import argparse


parser = argparse.ArgumentParser(
    prog='PROG',
    description='''this description
        was indented weird
            but that is okay''',
    epilog='''
            likewise for this epilog whose whitespace will
        be cleaned up and whose words will be wrapped
        across a couple lines''')

parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")

args = parser.parse_args()

if args.verbose: print("Verbose")