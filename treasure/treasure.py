import requests
import json
import os
import click

from get_token import ENCODED_MESSAGE,HEADERS

token = ENCODED_MESSAGE
headers = HEADERS

LINK = "http://127.0.0.1:5000/api/v2/til_page"
 

@click.command()
@click.option('--title','-t',type=str)
@click.option('--url','-u',type=str)
@click.option('--descryption','-d',type=str,default="No Descryption added")
def treasure(title,url,descryption):
    data = {}
    data['title'] = title
    data['url'] = url
    data['descryption'] = descryption

    # click.echo(token)
    # click.echo(headers)
    # click.echo(data)


    requests.post(LINK,headers=headers,json=data)



