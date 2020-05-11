import multiprocessing
import time
#import Faker
import argparse

class Consumer(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Poison pill means shutdown
                #print ('%s: Exiting' % proc_name)
                self.task_queue.task_done()
                break
            print ('%s: sending email to  %s' % (proc_name, next_task))
            answer = next_task()
            if answer:
                self.task_queue.task_done()
                self.result_queue.put(answer)

        return


class Task(object):
    def __init__(self, email):
        self.email = email

    def __call__(self):
        time.sleep(0.5) # pretend to take some time to do the work
        return 'Email successfully sent to : %s ' % (self.email)
    def __str__(self):
        return '%s ' % (self.email)



if __name__ == '__main__':
    #read arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("num_jobs", help="Count of emails to send ")
    args = parser.parse_args()
    print(args.num_jobs)

    #Number of emails to send ...
    if args.num_jobs:
        num_jobs = int(args.num_jobs)

    start_time = time.time()

    # Establish communication queues
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    # Start consumers
    num_consumers = multiprocessing.cpu_count() * 2
    print("# Count of CPUs: %d" % multiprocessing.cpu_count())
    print ('Creating %d consumers' % num_consumers)
    consumers = [ Consumer(tasks, results)
                  for i in range(num_consumers) ]
    for w in consumers:
        w.start()

    # Enqueue jobs
    for i in range(num_jobs):
        tasks.put(Task(str(i)+"_email@em.com"))

    # Add a poison pill for each consumer to close them while the
    for i in range(num_consumers):
        tasks.put(None)

    # Wait for all of the tasks to finish
    tasks.join()




    # Start printing results
    while num_jobs:
        result = results.get()
        print ('Result:', result)
        num_jobs -= 1


    print("--- %s seconds ---" % (time.time() - start_time))
