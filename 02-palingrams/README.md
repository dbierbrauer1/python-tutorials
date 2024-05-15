# Palingrams
This tutorial shows a basic example of loading a local custom module (`load_dictionary`) to another program. It also shows some basic usage of slicing strings in a list; here, we use slicing to find palingrams (phrases spelled the same forward and backward). The `palingrams_optimized.py` modifies the `palingrams.py` to conduct the search over a set as opposed to the original list, which reduces runtime significantly. Although sets do not preserve order and duplicates are not allowed, this does not matter here.

Within this folder, we also introduce `cProfile` which is part of the Python standard library. This outputs some basic statistics including how long the program took to run. Here, `cprofile_test.py` imports the `palingrams_optimized` module and runs on the `find_palingrams()` function.

## References
- Vaughan, Lee. *Impractical Python Projects: Playful Programming Activities to Make You Smarter* First edition., No Starch Press, Inc., 2019. [GitHub](https://github.com/rlvaugh/Impractical_Python_Projects/tree/master)

- [Dictionary Link](https://greenteapress.com/thinkpython/code/words.txt)