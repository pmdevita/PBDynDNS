# Porkbun Dynamic DNS

Simple Porkbun Dynamic DNS implementation

## Installation

Install to your system packages

```python3 -m pip install git+https://github.com/pmdevita/pbdyndns```

Create a config file at `/etc/pbdyndns.conf`

```ini
[general]
api_key = your api key
secret_api_key = your secret key
domain = domain to edit
subdomain = optional subdomain to change
id = id for record to edit
```

You can find the ID from the Porkbun website by inspecting the network requests it makes when you click "edit" under 
DNS Records in the interface. In the given JSON, look under `dnsRecords` for the record that matches the one you want 
to update and grab it's `id` property.

Finally, make a cron job, you might need to use the full path to Python depending on your cron environment

```21 */2 * * * python3 -m pbdyndns -c /etc/pbdyndns.conf```

