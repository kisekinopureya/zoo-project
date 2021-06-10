# Zoo Simulation Case Study

On 500 to 500 field,

Amount of Species:
- 30 Sheep (15 Male, 15 Female)
- 10 Cow (5 Male, 5 Female)
- 10 Hen
- 10 Rooster
- 10 Wolf (5 Male, 5 Female)
- 8 Lion (4 Male, 4 Female)
- 1 Hunter

How Many Units Does Each Species Move:
- Sheep: 2 Unit
- Cow: 2 Unit
- Hen And Rooster: 1 Unit
- Wolf: 3 Unit
- Lion: 4 Unit
- Hunter: 1 Unit

Rules:
- Species move randomly
- Species cannot leave the area
- Wolf hunts Sheep, Hen and Rooster in 4 Unit
- Lion hunts Sheep and Cow in 5 Unit
- Hunter hunts any animal in 8 Unit
- The same kind of animal with random gender reproduces when the same kind of animals with different gender close up each other in 3 Unit

After 1000 Unit, it prints count of animals.

## Running

Clone the repository or download tarball from releases and extract, then simply run

`$ ./zoo.py`

To print detailed output:

`$ ./zoo.py --debug`




