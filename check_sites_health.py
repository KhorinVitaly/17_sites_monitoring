import whois
import requests
from datetime import datetime
import argparse
from os.path import exists


def load_urls4check(path):
    if not exists(path):
        return None
    with open(path, "r") as urls_file:
        return urls_file.read().split('\n')


def is_server_respond_with_200(url):
    try:
        OK_status_code = 200
        responce = requests.get(url)
        if responce.status_code == OK_status_code:
            return True
        else:
            return False
    except:
        return False


def get_domain_expiration_date(domain_name):
    domain = whois.whois(domain_name)
    if type(domain.expiration_date) == list:
        return domain.expiration_date[0].date()
    else:
        return domain.expiration_date.date()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", action="store",
                        help="file with url for check")
    return parser.parse_args()


def print_urls_information(urls):
    for url in urls:
        print(url)
        if is_server_respond_with_200(url):
            print('Server responded with HTTP 200 status')
        else:
            print('Server did NOT respond with HTTP 200 status')

        current_date = datetime.today()
        next_month = current_date.replace(month=current_date.month+1).date()
        expiration_date = get_domain_expiration_date(url)
        if next_month < expiration_date:
            print('Domain is available for one month at least')
        else:
            print('Domain is available until ' + expiration_date)

if __name__ == '__main__':
    args = parse_arguments()
    if not args.path:
        print('File with url for check is not specified!')
        exit()
    urls = load_urls4check(args.path)
    print_urls_information(urls)

