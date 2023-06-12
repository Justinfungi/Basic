### list all the memort usage
    du -h --max-depth=1

### Auto run program
    # list all content
    crontab -l

    # edit crontab file
    crontab -e

    crontab -l * * * * * python3 cron_test.py(absolute path)

    crontab -r

    *    *    *    *    *
    -    -    -    -    -
    |    |    |    |    |
    |    |    |    |    +----- 星期中星期几 (0 - 6) (星期天 为0)
    |    |    |    +---------- 月份 (1 - 12)
    |    |    +--------------- 一个月中的第几天 (1 - 31)
    |    +-------------------- 小时 (0 - 23)
    +------------------------- 分钟 (0 - 59)

    每分钟定时执行一次	* * * * *
    每小时定时执行一次	0 * * * *
    每天定时执行一次	0 0 * * *
    每周定时执行一次	0 0 * * 0
    每月定时执行一次	0 0 1 * *
    每月最后一天定时执行一次	0 0 L * *
    每年定时执行一次	0 0 1 1 *

    service cron status/start

### Colab to remote server

    !tar -czvf files.tar.gz /path/to/your/file

    scp files.tar.gz <REMOTE_USER>@<REMOTE_HOST>:<REMOTE_DIRECTORY>
    
    tar -xzvf /path/to/files.tar.gz
