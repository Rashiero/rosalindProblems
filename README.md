# Rosalind.info

(rosalind.info)[https://www.rosalind.info/about/] is a project aiming to aid the learning bioinformatics via problem solving. In its plataform there are several classical computational problems that arise in modern biology. This repo is a collection of solves for the problems in the website.

There are five groups of problems, Python Village, Bioinformatics Stronghold, Bioinformatics Textbook Track, Bioinformatics Armory and Algorithmic Heights. 

* Python Village:
 Relates a few simple concepts of data types and operations in Python. 
 
* Bioinformatics Stronghold:
 Possess classical problems on biological sequence handling, such as translating genes, finidng complementary strands, calculating GC content, etc.

* Bioinformatics Armory:
 Has a greater focus on tools developed, so it focuses on Biopython packages for problem solving, for example.

* Bioinformatics Textbook Track: 
 Has a greater focus on modern bioinformatics problems, such as graph algorithms and hidden markov models.

* Algorithmic Heights:
 Has classical computational problems such as sorting algorithms, graph algorithms (e.g. Dijkstra) and data structures (e.g. Heap)

The overall idea of the project is to construct a Python library with the algoriths and data structures that solve these computational challenges. For instance, pattern finding algorithms of strings can be solved by a simple linear search, or utilize more complex approaches such as rolling hashes or suffix trees. While the exercises are being solved simply, what I aim for this project is to program these heavy operations and data structures in C and expand Python in a library that can be used to do the same operations in a more refined way.

## What has been done

The problems of Python Village are a good introduction for very beginners in Python and are present for the sake of completness. The problems currently being solved are from the Bioinformatics Stronghold. There are also basic problems, but interesting questions arise from their solutions, and their logic can be utilized in more complex programs.

# TODO

Start creating the C data structures and the library to handle computation.
Bioinformatics Armory, Bioinformatics Textbook Track and Algorithmic Heights' challenges are still open. Due to the nature of Algorithmic Heights's problems, their solution if very compatible with a C library and might help jumpstart that part of the project. Bioinformatics Armory has interesting complex problems that much of the solution will be either handled under the hood by the libraries or pieced together from previous logic, which means it either can be done independently from the others or only after the Python library is well developed.