#+TITLE:  Solving the Traveling Salesman Problem using Self-Organizing Maps
#+AUTHOR: Diego Vicente Martín
#+EMAIL:  mail@diego.codes

This repository contains an implementation of a Self Organizing Map that can be
used to find sub-optimal solutions for the Traveling Salesman Problem. The
instances of the problems that the program supports are =.tsp= files, which is
a widespread format in this problem. All the source code can be found in the
=src= directory, while a report and brief presentation slides (in Spanish) can
be found in the =report= folder. However, for a complete read on the topic, you
can read [[https://diego.codes/post/som-tsp/][my blog post explaining this implementation and its evaluation]].

[[file:diagrams/uruguay.gif]]

To run the code, only Python 3 and the dependencies (=matplotlib=, =numpy= and =pandas=,
which are included in the Anaconda distribution by default) are needed. In case
you are not using Anaconda, you can install all the dependencies with:

#+BEGIN_SRC sh
pip install -r requirements.txt
#+END_SRC

To run the code, simply execute:

#+BEGIN_SRC sh
cd som-tsp
python src/main.py assets/<instance>.tsp
#+END_SRC

The images generated will be stored in the =diagrams= folder. Using a tool like
=convert=, you can easily generate an animation like the one in this file by
running:

#+BEGIN_SRC sh
convert -delay 10 -loop 0 *.png animation.gif
#+END_SRC

This code is licensed under MIT License, so feel free to modify and/or use it
in your projects. If you have any doubts, feel free to contact me or contribute
to this repository by creating an issue.

-----

This code was presented for the Bio-Inspired Artificial Intelligence course in
the Computer Science & Technology master's degree @ UC3M. A previous version of
this code can be found in [[https://github.com/DiegoVicen/ntnu-som][this repository]]. Special thanks to [[https://github.com/leo-labs][Leonard Kleinans]],
who worked with me in that previous version.
