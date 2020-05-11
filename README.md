# Coding challange from d4l 

## Task desc
Please write a program in your prefered language that will send out emails to recipients from a huge list (1 Mio entries) in a performant way. You do not need to send real emails but just fake the email sending by waiting for half a second.

## Approach

To solve this problem i'm going to use Python.
Because python is single threaded I'm using multiprocessing library to paralize the task of sending out emails. I'm also using a queue from which the workers take email adresses. 




