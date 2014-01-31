import argparse


def parse_args():
    parser = argparse.ArgumentParser(usage='%(prog)s [options]',
                                     prog='twphotos')
    parser.add_argument('-u', '--user',
                        help="user account")
    parser.add_argument('-l', '--list', dest='list_slug',
                        help='list slug with --user as list owner')
    parser.add_argument('-o', '--outdir',
                        help='output directory')
    print_help = 'print media urls and tweet ids instead of download'
    parser.add_argument('-p', '--print', action='store_true',
                        help=print_help)
    parser.add_argument('-r', '--parallel', action='store_true',
                        help='enable parallel download')
    count_help = 'number of most recent photos to download'
    parser.add_argument('-n', '--num', type=int,
                        help=count_help)
    parser.add_argument('-i', '--increment', action='store_true',
                        help='download only new photos since last download')
    args = parser.parse_args()
    return args
