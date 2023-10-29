# Cron Jobs
[Geef een korte beschrijving van het onderwerp]

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht
### Gebruikte bronnen
- [Cron Jobs For Beginners | Linux Task Scheduling](https://www.youtube.com/watch?v=v952m13p-b4)
- [How to Run a Crontab Job Every Week on Sunday](https://www.geeksforgeeks.org/how-to-run-a-crontab-job-every-week-on-sunday/)

### Ervaren problemen

### Resultaat
1. Script om de huidige datum en tijd te schrijven naar een bestand in mijn home directory.
```
#!/bin/bash
/usr/bin/date >> ~/datetime.txt
```

![datetime.sh maken](images/10_cron-jobs1-1.png)<br><br>

![execute datetime.sh](images/10_cron-jobs1-2.png)<br><br>

2. Script in crontab zodat het elke minuut ge-execute wordt.
```
# m h  dom mon dow   command
* * * * * /usr/bin/date >> ~/datetime.txt
```

![script in crontab](images/10_cron-jobs2-1.png)<br><br>

![execute script](images/10_cron-jobs2-2.png)<br><br>

3. Script in crontab dat wekelijks de beschikbare disk space schrijft naar een bestand in /var/logs. Met `@weekly` wordt de script elke zondag om 12:00 AM ge-execute.
```
# m h  dom mon dow   command
@weekly /usr/bin/df -H >> /var/logs/available_space.txt
```

![execute script](images/10_cron-jobs3.png)<br><br>