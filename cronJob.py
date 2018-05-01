from crontab import CronTab
my_cron = CronTab(user='jim')
for job in my_cron:
    print(job)
    
    /LaptopPriceComparison/apiCall.py