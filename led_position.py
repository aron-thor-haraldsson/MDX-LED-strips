"""

To determine the position and facing a strip of LEDs has,
These six equations describe the shape of the graph they form.
This represents one unit of 'length' and the equation can be scaled up/down
to fit the actual size of the LED strips by changing the value of 'a'.

y=(e^a)*(ln(x)+2)       {y>e}{0>x>2e^a}
y=(e^a)*(ln(-x)+2)      {y>0}{-2e^a>x>0}
y=(e^a)*(ln(x^(-1)+2)   {y>0}{0>x>2e^a}
y=(e^a)*(ln(-x^(-1))+2) {y>0}{-2e^a>x>0}
x=(e^a)*(ln(y)+2)       {x>0}{0>y>2e^a}
x=(e^a)*(ln(-y)+2)      {x>0}{-2e^a>y>0}
x=(e^a)*(ln(y^(-1))+2)  {x>0}{0>y>2e^a}
x=(e^a)*(ln(-y^(-1))+2) {x>0}{-2e^a>y>0}
