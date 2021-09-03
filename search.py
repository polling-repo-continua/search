import requests
import argparse

def main():

    parser = argparse.ArgumentParser(description='search a source discovery script')
    parser.add_argument('-l', '--list', help='Domain list', required=True)
    parser.add_argument('-q', '--query', help='query', required=True)
    args = parser.parse_args()

    _domains = open(str(args.list), 'r').read().splitlines()

    for domain in _domains:

        try:

            if 'https' not in domain and 'http' not in domain:

                source = str(requests.get(f'https://{domain.strip()}').content)

                if str(args.query) in source:print(domain.strip())
                else:continue

            else:

                source = str(requests.get(domain.strip()).content)

                if str(args.query) in source:print(domain.strip())
                else:continue

        except:continue

if __name__ == '__main__':main()
