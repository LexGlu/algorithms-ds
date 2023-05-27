# Algorithms and Data Structures
Practice for implementing algorithms and data structures in Python.

## Algorithms
### Sorting
1) [Bubble Sort](./sorting/bubble_sort.py)
- Worst-case time complexity: `O(n^2)`
- Best-case time complexity: `O(n)` 
- Average-case time complexity: `O(n^2)`
- Worst space complexity: `O(1)`
- ![bubble-sort](./gifs/bubble-sort.gif)
2) [Reverse Bubble Sort](./sorting/desc_bubble_sort.py)
- The same as bubble sort, but traverses the list in reverse order and moves the smallest element to the start of the list.
3) [Shaker (Cocktail) Sort](./sorting/shaker_sort.py)
- Bidirectional bubble sort, that performs a bubble sort in both directions
- Performs better than bubble sort, but still has the same worst-case time complexity
- Worst-case time complexity: `O(n^2)`
- Best-case time complexity: `O(n)`
- Average-case time complexity: `O(n^2)`
- Worst space complexity: `O(1)`
- ![shaker-sort](./gifs/shaker-sort.gif)
4) [Insertion Sort](./sorting/insertion_sort.py)
- Worst-case time complexity: `O(n^2)`
- Best-case time complexity: `O(n)`
- Average-case time complexity: `O(n^2)`
- Worst space complexity: `O(1)`
- ![insertion-sort](./gifs/insertion-sort.gif)
5) [Selection Sort](./sorting/selection_sort.py)
- Worst-case time complexity: `O(n^2)`
- Best-case time complexity: `O(n^2)`
- Average-case time complexity: `O(n^2)`
- Worst space complexity: `O(1)`
- ![selection-sort](./gifs/selection-sort.gif)
6) [Merge Sort](./sorting/merge_sort.py)
- Worst-case time complexity: `O(nlogn)`
- Best-case time complexity: `O(nlogn)`
- Average-case time complexity: `O(nlogn)`
- Worst space complexity: `O(n)`
- ![merge-sort](./gifs/merge-sort.gif)
7) [Quick Sort](./sorting/quick_sort.py)
- Worst-case time complexity: `O(n^2)`
- Best-case time complexity: `O(nlogn)`
- Average-case time complexity: `O(nlogn)`
- Worst space complexity: `O(logn)`
- ![quick-sort](./gifs/quick-sort.gif)


## Setup
1) Clone the repository with `git clone https://github.com/LexGlu/algorithms-ds.git`
2) Navigate to the root directory of the project with `cd algorithms-ds`
3) Create a virtual environment with `python -m venv venv`
4) Activate the virtual environment with `source venv/bin/activate`
5) Install the dependencies with `pip install -r requirements.txt`

## Testing
Pytest is used for automated testing of each algorithm. To run the tests, run `pytest` in the root directory of the project.