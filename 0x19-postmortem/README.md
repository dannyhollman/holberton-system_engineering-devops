# Wordpress Site Outtage (2/22/20)
![alt text](https://memecrunch.com/meme/1OQY7/typo-meme/image.jpg?w=640&c=1 "Logo Title Text 1")
## Issue Summary
Early on February 22 2020 our developers pushed an update to the wordpress site that included a typo in a  file extension (`.phpp` instead of `.php`). This typo caused all site traffic to receive a 500 Internal Server Error.  After testing to find the typo, a puppet script was deployed to restore access to wordpress site.

## Timeline
> 2/22/20
* 07:00 - Developers push an update to the wordpress site
* 07:01 - All trffic to wordpress site receiving a 500 Internal Server Error
* 07:03 - The Apache2 and MySql processes are checked to ensure they are running
* 07:06 - All processes found to be running, strace used to check system call status
* 07:10 - System calls reveal a call to a file that doesn't exist, caused by a typo
* 07:12 - Puppet script created and tested to fix typo
* 07:15 - Puppet script deployed and site functionality returned to normal

## Root Cause
The root cause of the outage was due to a typo in the `wp-settings.php` file.  The typo was in the name of a required file, creating a call to a file that didnd't actually exist. This call resulted in a 500 Internal Server Error, causing a full website outage.
## Resolution and recovery
The developers first checked to make sure that the Apache2 and MySql processes were running.  After finding that the expected processes were in fact running, the developers moved on to testing the system calls the processes were making with strace.  By using strace on the Apache2 process, the call to a non existant file was found, revealing the typo.  A puppet script was created and tested to fix the typo on all servers.  After successful tests the puppet script was deployed to all servers, fixing the problem and restoring site access.
## Corrective and Preventative Measures
The main cause of this outage was lack of testing before pushing code to live servers.  These type of issues can easily be avoiding in the future by toroughly testing to make sure everything works correctly before pushing code to the website.
