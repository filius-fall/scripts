import click
import csv
import time
from tabulate import tabulate
import os


@click.group(invoke_without_command = True)
def timer():
    click.echo('Pomodora time Starts Now............')

@timer.command()
@click.argument('duration',default=2)
@click.option('--message','-m',default = "Success",type = str)
def start(duration,message):
    
    start_counter = int(time.time())
    start_time = str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec)

    print(start_time)

    while True:
        end_counter = int(time.time())
        

        if end_counter - start_counter == duration * 60 :
            passed_time = end_counter - start_counter    
            click.echo("End of timer")
            break
        
        passed_time = str(end_counter - start_counter) + 'Min'

    if os.path.isfile('data.csv'):
        with open('data.csv','a+',newline='') as file:
            end_time = str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec)  
            row = csv.writer(file)
            row.writerow([start_time,end_time,passed_time,message])
    else:
        if os.path.isfile('data.csv'):
            with open('data.csv','a',newline='') as file:
                end_time = str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec)  
                row = csv.writer(file)
                row.writerow(['start_time','end_time','duration','comments'])
                row.writerow([start_time,end_time,passed_time,message])


@timer.command()
def stats():
    with open('data.csv','r+',newline='') as file:
        row = csv.reader(file)


        print(tabulate([r  for r in row if 'start_time' not in r],headers = ['Start-Time','End-time','Duration','Comments']))