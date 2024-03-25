# DataStructure

A simple BinarySearchTree implementation on Python

# Description

Initial simple implementation of BinarySearchTree.

Applied using iterative instead of recursive.


### Added extra methods:
NA

### Notes:

README still in draft.

### Applied Methods:
- Insert: Iterative method
- Read: DFS recursive method, will return an ordered list
- Delete:
  - Find the target node to delete
  - Check if target is not found
  - Check if target is root node
    - If leaf node -> delete
    - Elif right child -> replace target with right child
    - Elif left child -> replace target with left child
    - Else find min from right root, recursive delete on that min, then set target value to min
  - If leaf node -> delete
  - Elif right child -> replace target with right child
  - Elif left child -> replace target with left child
  - Else find min from right root, recursive delete on that min, then set target value to min

---------------------------------

[//]: # (# Documentation)

[//]: # ()
[//]: # (## Constructor)

[//]: # (- [DataStructure&#40;&#41;]&#40;#DataStructure&#41;)

[//]: # ()
[//]: # (## Attributes)

[//]: # ()
[//]: # (- **head**: _The first node of the DataStructure_)

[//]: # ()
[//]: # (## Methods)

[//]: # ()
[//]: # (- [insertAtIndex&#40;&#41;]&#40;#insertAtIndex&#41;)

[//]: # ()
[//]: # ()
[//]: # (## Referenced Classes)

[//]: # ()
[//]: # (- [Node]&#40;#Node&#41;)

[//]: # ()
[//]: # (---------------------------------)

[//]: # ()
[//]: # (### DataStructure&#40;&#41;)

[//]: # ()
[//]: # (Constructor for DataStructure class.)

[//]: # ()
[//]: # (```python)

[//]: # (class DataStructure&#40;node=None&#41;)

[//]: # (```)

[//]: # ()
[//]: # (###### Time Complexity)

[//]: # ()
[//]: # (O&#40;n&#41;)

[//]: # ()
[//]: # (###### Parameters)

[//]: # ()
[//]: # (- **node : Node**)

[//]: # (    - Node representing the head of the constructed DataStructure. If existing DataStructure data structure is to be imported)

[//]: # (      to this data structure, pass in the head of existing head of DataStructure here.)

[//]: # ()
[//]: # (###### Returns)

[//]: # ()
[//]: # (- **DataStructure**)

[//]: # (    - A generated DataStructure object.)

[//]: # ()
[//]: # (###### Examples)

[//]: # ()
[//]: # (```)

[//]: # (>>> existing_ll = Node&#40;1, Node&#40;2, Node&#40;3&#41;&#41;&#41;)

[//]: # (>>> ll = DataStructure&#40;existing_ll&#41;)

[//]: # (>>> print&#40;ll&#41;)

[//]: # (DataStructure&#40;)

[//]: # ([1, next=<DataStructure.Node object at 0x000001B1210BE350>],)

[//]: # ([2, next=<DataStructure.Node object at 0x000001B1210BC790>],)

[//]: # ([3, next=None]&#41;)

[//]: # (```)

[//]: # ()
[//]: # (--------)
