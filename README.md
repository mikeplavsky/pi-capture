# pi-capture

Run every 1 minute:
```
*/1 * * * * sudo -H -u pi bash -c "/home/pi/monitor/run.sh BUCKET_NAME"
```

sudo is needed for getting aws configuration from the user profile

Idea has been taken from this:
https://www.raspberrypi.org/documentation/usage/webcams/ 
