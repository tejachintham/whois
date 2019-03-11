import whois
import argparse
parser = argparse.ArgumentParser()
parser.add_argument( '-s',"--site",type=str)
args = parser.parse_args()
w = whois.whois(args.site)
print(w)
