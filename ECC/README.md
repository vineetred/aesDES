## Elliptical Curves
1. Language = Python 3.6.4
2. To run the program, one needs to run the command "python3 ec.py".
3. After this, all the placeholder commands inside the program testing out every operation and function will run.
4. The format of the points is as follows - [x,y]. The arguments need to passed into this format for the program to run properly.
5. The EC Domain parameters will be found in the file called 'variables.txt'. Changes to the curve must be made here.
6. The outputs will be saved in the file named 'output.txt'.
### Function definitions
* **read_Parameters()** - Reads the parameters from the variables.txt file
* **read_Point()** - Reads the points from user input through the terminal
* **write_Point_terminal()** - Prints given points onto the terminal
* **addition()** - Adds two points. Accepted format of points is [x1,y1],[x2,y2]
* **pointDoubing()** - Doubles the given point. Accepted format of points is [x,y]
* **negationPoint()** - Returns the negation of a given point
* **subtractionPoint()** - Returns the different between two points.
* **mutliplePoint()** - Returns the scalar multiplitcation of a point, P. Accepted format of points is [x,y],k.
* **find_Y()** - Returns either y or an exception. Accepted format of points is (x).
