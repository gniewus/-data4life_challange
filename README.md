# Coding challange from d4l 

## Task desc
Please write a program in your prefered language that will send out emails to recipients from a huge list (1 Mio entries) in a performant way. You do not need to send real emails but just fake the email sending by waiting for half a second.

## Approach

To solve this problem i'm going to use Python.
Because python is single threaded I'm using multiprocessing library to paralize the task of sending out emails. I'm also using a queue from which the workers take email adresses. 



### Testing:

I've tested the program on my 2018 Macbook Pro with 2.9 GHz 6-Core Intel Core i9 and 32GB RAM. 
In practice ``` multiprocessing.cpu_count() ``` showed 12 available CPU cores.

- 10 emails : 0.5264360 second
- 100 emails : 2.5321319103240967 seconds
- 1000 emails : 21.09543490409851 seconds
- 10000 emails : 209.1258671283722 seconds
- 100000 emails : ca. 2000 seconds ~ 1h 6 min 
- 1000000 emails : ca. 20 000 seconds ~ 5h 30 minutes


