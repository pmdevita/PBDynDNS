import configparser
import urllib.request
import urllib.parse
import json

def execute_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    api_key = config["general"]["api_key"]
    secret_api_key = config["general"]["secret_api_key"]
    domain = config["general"]["domain"]
    subdomain = config["general"].get("subdomain", "")
    type = config["general"].get("type", "A")
    id = config["general"]["id"]
    content = get_current_ip(api_key, secret_api_key)
    edit_record(api_key, secret_api_key, domain, id, content, subdomain, type)


def json_request(url, data):
    data = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(url, data)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    req.add_header('Content-Length', str(len(data)))
    return req


def get_current_ip(api_key, secret_api_key):
    req = json_request("https://api-ipv4.porkbun.com/api/json/v3/ping", {"secretapikey": secret_api_key, "apikey": api_key})
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read().decode())
        return data["yourIp"]


def edit_record(api_key, secret_api_key, domain, id, content, subdomain="", type="A"):
    data = {
        "secretapikey": secret_api_key,
        "apikey": api_key,
        "name": subdomain,
        "type": type,
        "content": content
    }
    req = json_request(f"https://api.porkbun.com/api/json/v3/dns/edit/{domain}/{id}", data)
    try:
        r = urllib.request.urlopen(req)
    except Exception as e:
        print(e, e.read())
        raise e
    r.close()


import argparse

parser = argparse.ArgumentParser(description="Update a Porkbun domain with a new IP")
parser.add_argument("--config", "-c", help="Path to configuration file")


def __main__():
    args = parser.parse_args()
    if args.config:
        execute_config(args.config)

