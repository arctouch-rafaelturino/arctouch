I choose to use Python with Flask and Vue, for a quick prototipation while still maintaining the option to scale the system up.
That said, the architecture is pretty bare bones. Some parts of the code were written with the possibility of big changes happening in the future.
For example, the search listing and the front page are two different components. With that, it is easy to change either one of them without having to touch on the other.

To run it locally, you have to put you api key in the key.py file.

On the server side, I used `requests`, the almost standard Python requests framework and `json`, the standard Json lib for Python.
Alongside Vue, I used `VueRouter`, a router api developed by the same people that maintain Vue itself.
I tried my best to use as few libraries as possible, as a personal challenge and also to make it easier to judge the quality of the code. 
