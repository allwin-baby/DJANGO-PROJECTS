
from apscheduler.schedulers.blocking import BlockingScheduler
from motoonefusion import  motoOneFusion
sched = BlockingScheduler()
sched2 = BlockingScheduler()
# Schedule job_function to be called every two hours
sched.add_job(motoOneFusion, 'interval', seconds=4)
#2 cron jobs dont allow to work sconcurrently
sched.start()

