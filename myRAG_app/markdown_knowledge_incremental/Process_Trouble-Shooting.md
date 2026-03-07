# Process_Trouble-Shooting

- generated_at: 2026-03-07T11:21:39.147032+00:00
- knowledge_root: /home/gabri/udemy/llm_engineering/myRAG_knowledge

## Summary
- sources: 3
- segments: 505
- characters: 862235
- failed_files: 0

## Source: eBOOK Kulkarni Robust Process Development and Scientific Molding 2E.pdf
- source_path: /home/gabri/udemy/llm_engineering/myRAG_knowledge/Process_Trouble-Shooting/eBOOK Kulkarni Robust Process Development and Scientific Molding 2E.pdf
- source_ext: .pdf
- parser_used: PyPDFLoader
- fallback_used: False
- parse_status: success
- extracted_chars: 753335

### Segment 1 (page 1)

Suhas Kulkarni
Robust Process Development
and Scientific Molding
Theory and Practice
2nd Edition
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 2 (page 2)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 3 (page 3)

Kulkarni
Robust Process Development
and Scientific Molding
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 4 (page 4)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 5 (page 5)

Robust Process
Development and
Scientific Molding
Theory and Practice
Suhas Kulkarni
2nd Edition
Hanser Publishers, Munich Hanser Publications, Cincinnati
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 6 (page 6)

Distributed in the Americas by:
Hanser Publications
6915 Valley Avenue, Cincinnati, Ohio 45244-3029, USA
Fax: (513) 527-8801
Phone: (513) 527-8977
www.hanserpublications.com
Distributed in all other countries by:
Carl Hanser Verlag
Postfach 86 04 20, 81631 München, Germany
Fax: +49 (89) 98 48 09
www.hanser-fachbuch.de
The use of general descriptive names, trademarks, etc., in this publication, even if the former are not especially
identified, is not to be taken as a sign that such names, as understood by the Trade Marks and Merchandise Marks
Act, may accordingly be used freely by anyone. While the advice and information in this book are believed to be true
and accurate at the date of going to press, neither the authors nor the editors nor the publisher can accept any legal
responsibility for any errors or omissions that may be made. The publisher makes no warranty, express or implied,
with respect to the material contained herein.
The final determination of the suitability of any information for the use contemplated for a given application
r
emains the sole responsibility of the user.
Cataloging-in-Publication Data is on file with the Library of Congress
All rights reserved. No part of this book may be reproduced or transmitted in any form or by any means, electronic
or mechanical, including photocopying or by any information storage and retrieval system, without permission in
writing from the publisher.
© Carl Hanser Verlag, Munich 2017
Editor: Cheryl Hamilton
Production Management: Jörg Strohbach
Coverconcept: Marc Müller-Bremer, www.rebranding.de, München
Coverdesign: Stephan Rönigk
Printed and bound by Kösel, Krugzell
Printed in Germany
ISBN: 978-1-56990-586-9
E-Book ISBN: 978-1-56990-587-6
The Author:
Suhas Kulkarni, 2097 Courage Street, Vista, CA 92081, USA
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 7 (page 7)

Dedicated to my Parents
Dr. Mohan P Kulkarni
Jayashree M Kulkarni
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 8 (page 8)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 9 (page 9)

Preface to the
Second Edition
As the saying goes “the only thing that is constant is change.” It has been six years
since the first edition of this book was published, and it has been very well
r
eceived.
Thank you to all its readers. Since then, I have continued my research to further
understand the process of injection molding with the final goal of robust process
development. As I kept publishing and teaching this new material, it became time
to revise the book.
This second edition has new material in almost all the chapters. Some concepts,
which were explained in the first edition, have been expanded upon and rewritten
for better understanding. Several figures have been added to complement the
e
xplanations. Some of the chapters and text have been split up and rearranged
to have a better flow of understanding. A complete chapter on “Basic Quality Con-
cepts” has also been added.
The topic of process development is a complex one, but once the concepts are
under
stood, implementation is easy. The key is to understand the basics first. Over
the years, in my consulting business, I often get called on by companies to ‘fix’
their processes. I always go back to the basics and ask them several simple ques-
tions about their molds, machines, and processes to which they sometimes have no
answer, or when they do answer my questions, they figure out the solution to the
problem on their own. Their process development was probably done by throwing
darts on a dartboard and hence the issues. This book is attempting to change that.
By using the techniques described in this book, one can establish what I call cruise
control processes: set the process, start molding, and never touch a setting until the
run is done.
The topic of “Design of Experiments” (DOE) has great importance in injection
molding. Many companies employ this technique, but not effectively. The reason is
not because of their lack of knowledge of DOE, but because of their lack of under -
standing of the basics of molding, along with their choice of factors and levels for
the DOE. This topic has been expanded in the new edition.
I would like to thank Hanser Publications and their staff for this opportunity to
write the second edition. Mark Smith and Cheryl Hamilton have been very helpful
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 10 (page 10)

VIII Pr eface to the Second Edition
with the proofing and, moreover, very patient with all the delays from my side.
I would also like to thank several other people who have helped me with the sec-
ond edition. Lorena Castro who took all the bits and pieces of my writing and trans-
formed it into readable flow needs a special mention and acknowledgement.
In the preface to the first edition, I failed to mention a very important place that
also helped shape my career and my life. The National Chemical Laboratory (NCL),
Pune, India, is where my dad worked all his life as a research scientist. I lived in the
shadows of this great institution and its several researchers. My dad would often
take me to his lab when he conducted his research, and that is where the seeds of
my future were laid. I worked on a couple of projects during my college days in its
Polymer Engineering Department, and that was my first personal exposure and
in
volvement with research. It was my experience at NCL, which was one of the
contributing factors that pushed me to study further.
My constant sources of inspiration and help include Tim and Violeta of Distinctive
Plastics, who have opened their company for my research and seminars, my profes-
sor from college, Dr. Basargekar, my colleagues in the industry, Ravi Khare, Atul
Khandekar, Vishu Shah, Vikram Bhargava, Randy Phillips, and my family.
To my mom, dad, and siblings, I will be forever indebted to you for all the support
and inspiration you have given me over the years.
Suhas Kulkarni

Oct
ober 2016
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 11 (page 11)

Preface to
First Edition
When I interviewed for my second job after I graduated, I was told that if the posi-
tion was offered to me, I would have to spend my first three days at a seminar on
Scientific Molding and Design of Experiments. It was all new to me then. My job
was to implement this new technology as a standard across the company. The job
was offered to me; I accepted and attended the seminar. Implementing the tech-
niques on the first couple molds was a refreshing change from how I did it before.
The scientific method of developing the process left no room for any guess work by
applying the theories of polymer science and injection molding. Scientific evidence
proved why parts could be or could not be molded consistently within the required
specifications. My enthusiasm for the use of these techniques grew as I found
more and more evidence of success. Over the next few years, I gave presentations
at the local SPE chapter and the attendees wanted to learn more to make their
oper
ations efficient. In 2004 I decided to start consulting in the area of Scientific
Processing, a term I coined to include all the processes that are involved in the
transformation of the pellet to the final product that is shipped out to the customer.
My research work on the ‘overdrying’ of PBT and Nylon was the main driving force
to think of the process as being outside of the molding machine and not just what
happens in the mold. As my consulting and teaching career expanded, I found
many people looking for a resource to learn the basic underlying principles of
pol
ymers and plastics and apply them to injection molding. They wanted to
under
stand the why, and then how of Scientific Processing. ‘Where can I find this
information?’ was always a question that was asked. This book is the answer to
their question.
Understanding the molding process from the scientific perspective helps in mak -
ing better decisions to establish the parameters that are involved in controlling the
journey of the pellet; from the warehouse to the molding machine and then to its
conversion as a molded product. All the parameters are set on the basis of scien-
tific knowledge and experience making the process efficient in terms of produc
-
tivity
. Higher yield, reduced scrap, robust processes, reduced quality inspection,
reduced number of process changes leading to less human intervention are some
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 12 (page 12)

X Pr eface to First Edition
of the benefits of Scientific Processing. This book details the theory and practice of
Scientific Processing. There are a lot of ‘rules of thumb’ in injection molding. My
mission is to eliminate them and present a scientific solution. A good example is
the size of vents in the mold.
I hope my commitment to researching and understanding of the molding process
will continue to give a better insight to the process. I hope to share those with you
in the future editions of this book. There are a number of people who are part of
the success of writing this book. Some gave me the knowledge, some inspired me
to learn more while others gave me unconditional support in this endeavor. It is
impossible to thank all of them individually but without all of them this project
would not have been accomplished. First and foremost, special mention must be
made of my father who introduced me to the fascinating world of chemical re-
search. It is from here that I get my curiosity, creativity and my analytical abilities
of problem solving. Thanks to my teachers and professors who not only imparted
the knowledge but also instilled in me the value of education through the dedica-
tion to their students. It is from here that I get my inspiration to teach and spread
my knowledge. Thanks to my family and friends who have supported me and be-
lieved in me. It is from them that I get my will power and courage to get past the
current frontiers and take a step into an unknown future.
In the production of this book I would like to thank Christine Strohm and the man-
agement of Hanser Publications for publishing the book. The sections on cavity
pressure sensing and the chapter on rheology were reviewed by Mike Groleau of
RJG and John Beaumont of Beaumont Technologies respectively. Thanks to them
for their valuable comments. Thanks also to Dave Hart for proofreading the text
and making the matter an interesting technical read. Valuable comments from
Ravi Khare of Symphony Technologies were included on the DOE chapter. Without
the unconditional help of Tim and Violeta Curnutt of Distinctive Plastics I would
have not had the chance to experiment with many of the theories and applications
put forward in this book. Special thanks to them for letting me make Distinctive
Plastics my home during the book writing process. I am often told I am an effective
teacher with clear concepts in polymer science and rheology – I have picked the
teaching skills and the knowledge from Prof. Basargekar – my sincere acknowl-
edgements to him. Under the leadership of Vishu Shah I conducted a few success-
ful seminars with the Society of Plastics Engineers. These seminars gave me the
fuel and material for this book. Thanks to Vishu not only for the opportunities of
the seminars but also for being a professional guide and a personal friend. I would
also like to acknowledge the efforts of John Bozzelli and Rod Groleau for their
pioneer
ing work in Scientific Molding and raising its awareness in the molding
community.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 13 (page 13)

XIPreface to First Edition
To my alma maters, Maharashtra Institute of Technology, Pune, India and Univer -
sity of Massachusetts, Lowell, USA: Hidden in one of your foundations’ bricks are
the enriching roots to my success. Thank You.
Suhas Kulkarni

FIMMTEC
H Inc.

V
ista, CA.

Januar
y 2010
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 14 (page 14)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 15 (page 15)

Contents
Preface to the Second Edition ................................... VII
Preface to First Edition .......................................... IX
1
Intr
oduction to Scientific Processing ........................ 1
1.1 The Ev olution and Progress of Injection Molding .................. 1
1.2
The Molding Pr
ocess
..........................................
2
1.3
The Thr
ee Types of Consistencies
R
equired in Injection Molding .....
2
1.4
Scientific Pr
ocessing
..........................................
6
1.5
The F
ive Critical Factors of Molding
.............................
7
1.5.1
P
art Design
...........................................
8
1.5.2
Mat
erial Selection
.....................................
8
1.5.3
Mold Design and Cons
truction
...........................
9
1.5.4
Mac
hine Selection ......................................
9
1.5.5
Molding Pr
ocess
.......................................
9
1.6
Concur
rent Engineering
.......................................
10
1.7

Variation ....................................................
10
2 Pr operties of Polymers and Plastics That Influence
Injection Molding ........................................... 13
2.1 Polymers .................................................... 13
2.2
Molecular W
eight and Molecular Weight Distribution
..............
15
2.3
P
olymer Morphology (Crystalline and Amorphous Polymers)
........
17
2.4
R
ole of Morphology in Injection Molding
.........................
22
2.4.1
Differ
ences in Shrinkage between Amorphous and

Cr
ystalline Materials
...................................
22
2.4.2
Melt Pr
ocessing Range ..................................
22
2.4.3
Mold F
illing Speed
.....................................
23
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 16 (page 16)

XIV Cont ents
2.4.4 Mold T emperatures .................................... 24
2.4.5
Bar
rel Heat Profile
.....................................
24
2.4.6
Scr
ew Recovery Speeds
.................................
25
2.4.7
N
ozzle Temperature Control
.............................
25
2.4.8
Cooling T
imes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
2.4.9
Mec
hanical Properties
..................................
26
2.4.10
Op
tical Clarity .........................................
26
2.5
Ex
ceptions of Morphology Rules to
P
olyolefins .....................
27
2.6
Ther
mal Transitions in Polymers ................................
28
2.6.1
R
elationship between the Glass Transition Temperature
and Post Mold Shrinkage ................................
32
2.7
Shr
inkage of Polymers in
Injection
Molding .......................
36
2.8
The Plas
tic Pressure–Volume–
T
emperature (PVT) Relationship
......
39
2.8.1
Im
portance of Plastic Density in Injection Molding
..........
40
2.8.2
R
esidence Time and Maximum Residence Time of a Plastic . . .
41
2.8.3
Plas
tic Datasheets ......................................
43
2.9
R
eferences
..................................................
45
3 P olymer Rheology ........................................... 47
3.1 Viscosity .................................................... 47
3.2
N
ewtonian and Non-Newtonian
Mat
erials .........................
49
3.3
V
iscosity in Polymer Melts .....................................
50
3.4
Effect of T
emperature on Viscosity ...............................
54
3.5
V
elocity and Shear Rate Profiles .................................
55
3.6
Application t
o Injection Molding ................................
56
3.6.1
Flo
w Imbalance in an 8-Cavity Mold
......................
57
3.6.2
R
acetrack Effect in a Part with Constant Thickness
.........
59
3.6.3
S
tress Build-Up in Molded Parts
.........................
59
3.6.4
W
arpage Difference between Cavities
.....................
60
3.7
Sol
ving Flow Imbalances Using Melt Rotation Techniques
..........
60
3.8
F
ountain Flow ................................................
62
3.9
Effect of F
ountain Flow on Crystallinity, Molecular Orientation,
and Fiber
Or
ientation ..........................................
65
3.10
Char
acterization of Polymer Viscosity
...........................
66
3.11

References ...................................................
67
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 17 (page 17)

XVContents
4 Plas tic Drying ............................................... 69
4.1 Pr oblems in Melt Processing Related to the Presence of Moisture .... 71
4.1.1
Deg
radation of Plastic
..................................
71
4.1.2
Pr
esence of Surface Defects ..............................
71
4.2
Hy
groscopic Polymers
........................................
75
4.3
Dr
ying of Plastics .............................................
77
4.3.1
Dr
ying Temperatures and Times
.........................
77
4.3.2
R
elative Humidity and Dew Point
........................
79
4.3.3
Air Flo
w Rate
.........................................
80
4.4
Eq
uipment for Drying Plastics ..................................
80
4.4.1
Ov
en Dryers
..........................................
80
4.4.2
Ho
t Air Dryers
........................................
81
4.4.3
Desiccant Dr
yers
......................................
81
4.4.4
Classifications Based on t
he Location of the Dryer
..........
81
4.5
De
termination of the Amount of
Mois
ture
........................
82
4.5.1
The Glass Slide T
echnique (TVI Test)
.....................
82
4.5.2
The Kar
l-Fischer Titration Method ........................
83
4.5.3
Electr
onic Moisture Analyzer ............................
83
4.5.4
Measur
ement of the Dew Point
..........................
84
4.6
‘Ov
erdrying’ or Overexposure to Drying Temperatures ..............
85
4.7
Cautions ....................................................
92
4.8
Pr
evention of Overexposure to
Long
er

Drying Times . . . . . . . . . . . . . . .
92
4.9
Ov
erdrying Controller .........................................
93
4.10

References ...................................................
94
5 Common Plas tic Materials and Additives ..................... 95
5.1 Classification of P olymers ...................................... 95
5.2
Commer
cially Important Plastics ................................
97
5.2.1

Polyolefins ............................................
97
5.2.2
P
olymers from Acrylonitrile, Butadiene, Styrene, and Acrylate
98
5.2.3
P
olyamides (PA)
.......................................
99
5.2.4
P
olystyrenes (PS)
......................................
100
5.2.5

Acrylics ..............................................
101
5.2.6
P
olycarbonates (PC)
....................................
101
5.2.7

Polyesters .............................................
101
5.2.8
P
olyvinyl Chloride (PVC)
................................
101
5.2.9
P
olyoxymethylene (POM or Acetal) ........................
102
5.2.10

Fluoropolymers ........................................
103
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 18 (page 18)

XVI Cont ents
5.3 Additives .................................................... 103
5.3.1

Fillers ................................................
104
5.3.2

Plasticizers ...........................................
104
5.3.3
Flame R
etardants
......................................
104
5.3.4
Anti-aging A
dditives, UV Stabilizers
......................
105
5.3.5
N
ucleating Agents
.....................................
105
5.3.6

Lubricants ............................................
106
5.3.7
Pr
ocessing Aids ........................................
106
5.3.8

Colorants .............................................
106
5.3.9
Blo
wing Agents ........................................
106
5.3.10
Ot
her Polymers ........................................
107
5.4
Closing R
emarks
.............................................
108
5.5
R
eference
...................................................
108
6 Injection Molding and Molding Mac hines .................... 109
6.1 The His tory of Injection Molding ................................ 109
6.2
Injection Molding Mac
hines and Their Classifications ..............
110
6.3
Mac
hine Specifications
........................................
112
6.3.1
Clam
p Force (Tonnage)
.................................
113
6.3.2
Sho
t Size .............................................
113
6.3.3
Scr
ew Diameter and L/D Ratio ...........................
113
6.3.4
Plas
ticating Capacity ...................................
114
6.3.5
Maximum Plas
tic Pressure ..............................
114
6.4
The Injection Molding Scr
ew
...................................
114
6.5
Scr
ew Designs ...............................................
117
6.6
The Chec
k Ring Assembly ......................................
118
6.7
Int
ensification Ratio (IR)
......................................
119
6.8
Obt
aining Intensification Ratios .................................
121
6.9
Selecting t
he Right Machine for the Mold .........................
122
6.9.1
Ph
ysical Size of the Mold
...............................
122
6.9.2
Calculating t
he Required Machine Tonnage for a Mold
.......
124
6.10
The R
ule of Thumb for Tonnage Is Only an Estimate ................
126
6.10.1
P
ercentage Shot Size Used and Number of Shots in the Barrel
127
6.10.2
R
esidence Time of the Material in the Barrel
...............
130
6.10.3
Pr
actical Methods to Find Percentage Shot Size, Shots in
a
Bar
rel, and Residence Time
............................
130
6.10.4
R
esidence Time Distribution .............................
131
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 19 (page 19)

XVIIContents
7 Scientific Pr ocessing, Scientific Molding, and
Molding Parameters ......................................... 133
7.1 Intr oduction ................................................. 133
7.1.1
Pr
ocess Robustness ....................................
135
7.1.2
Pr
ocess Consistency
...................................
135
7.2
The 11 + 2 Plas
tic Injection Molding Machine Parameters
............
138
7.3
Pr
ocess Outputs
..............................................
141
7.4
What Scientific Molding and Scientific Pr
ocessing Are Not
..........
142
7.5
The Injection Molding Cy
cle ....................................
143
7.5.1
Injection, P
ack, and Hold ................................
143
7.5.2
Speed and Pr
essure
....................................
145
7.5.3
Pr
essure Limited Process
...............................
146
7.5.4
Decoupled MoldingSM ................................... 146
7.5.5
Int
ensification Ratio (IR)
................................
147
7.5.6
Scr
ew Speed
..........................................
148
7.5.7
Bac
k Pressure
.........................................
150
7.5.8
Cy
cle Time ............................................
151
7.6

References ...................................................
152
8 Pr ocess Development Part 1: the 6-Step Study –
Exploring the Cosmetic Process ............................. 153
8.1 Intr oduction ................................................. 153
8.2
Intr
oduction to Process Development
............................
153
8.3
Pr
emolding Setup
............................................
156
8.4
S
torage and Drying of Resin
....................................
156
8.4.1
Plas
tic Drying .........................................
157
8.5
Mac
hine Selection
............................................
159
8.6
Im
portance of Adding Charge Delay Time
........................
160
8.7
F
illing in Injection: Weight or Volume? ...........................
161
8.8
Se
tting of the Melt Temperatures ................................
162
8.9
Se
tting Mold Temperatures .....................................
165
8.10
Pr
ocess Optimization – the 6-Step Study
.........................
165
8.10.1
S
tep 1: Optimization of the Injection Phase–Rheology Study ...
165
8.10.2
Pr
ocedure to Determine the Viscosity Curve at the
Molding Mac
hine ......................................
169
8.10.3
Ho
w to Use this Information
.............................
171
8.10.4
Cautions and Ex
ceptions
................................
173
8.10.5
Pr
ofiling of Injection Speeds
.............................
173
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 20 (page 20)

XVIII Cont ents
8.10.6 When a Shor t Shot Sticks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
8.10.7
Selecting Melt T
emperature for Viscosity Graphs ............
176
8.10.8
S
tep 2: Determining the Cavity Balance –
Cavity Balance Study
...................................
177
8.11
R
easons for Cavity Imbalance ...................................
180
8.11.1
De
termining the Cause of Cavity Imbalances
...............
184
8.11.2
Calculating Ca
vity Imbalance
............................
184
8.11.3
A
cceptable Level of Cavity Imbalance
.....................
185
8.11.4
S
tep 3: Determining the Pressure Drop –
Pressure Drop Studies
..................................
187
8.12
Effect of Pr
essure Drop on the Pack and Hold Phase ................
194
8.12.1
S
tep 4: Determining the Cosmetic Process Window –

Pr
ocess Window Study ..................................
195
8.13
R
elationship between Cavity Balance and Process Windows
.........
202
8.14
The P
ack and Hold Pressure Rule Not to Be Used
..................
202
8.14.1
S
tep 5: Determining the Gate Seal Time – Gate Seal Study
....
203
8.15
Differ
entiating between the Pack and the Hold Phase
..............
206
8.16
Ho
t Runner and Valve Gated Molds
..............................
210
8.16.1
S
tep 6: Determining the Cooling Time – Cooling Time Study
..
210
8.16.2
Op
timization of Screw Rotation Speed .....................
213
8.16.3
Wh
y to Not Use the Rule of Thumb ........................
214
8.17
Op
timization of Back Pressures
.................................
215
8.18
The Cosme
tic Scientific Process .................................
216
8.18.1
P
ost Mold Shrinkage Studies .............................
216
8.18.2
Pr
ocedure to Measure Shrinkage
.........................
219
8.19
R
ecommended Mold Function
Qualification Pr
ocedure ..............
220
8.20
R
ecommended Adjustments to
Maint
ain Process Consistency
and Robustness
..............................................
221
8.21
Pr
ocess Documentation
.......................................
222
8.22

References ...................................................
223
9 Pr ocess Development Part 2:
Exploring the Dimensional Process via the DOE .............. 225
9.1 P arameters in Injection Molding ................................ 226
9.1.1
Design of Exper
iments: Definition
........................
228
9.2
T
erminology .................................................
230
9.2.1
F
actor
...............................................
230
9.2.2

Response .............................................
231
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 21 (page 21)

XIXContents
9.2.3 Level ................................................. 231
9.2.4
Designed Exper
iment ...................................
231
9.3
R
elationships between the Number of Factors, Levels,
and Experiments
.............................................
232
9.4
Balanced Ar
rays ..............................................
234
9.5
Int
eractions
.................................................
235
9.6
Conf
ounding or Aliasing
.......................................
238
9.7
R
andomization ...............................................
240
9.8
F
actorial Experiments .........................................
241
9.9
Dat
a Analysis
................................................
241
9.9.1
T
ornado Charts
........................................
243
9.9.2
Cont
our Plots ..........................................
244
9.9.3
Pr
ediction Equation
....................................
245
9.9.4
Pr
ocess Sensitivity Charts ...............................
246
9.10
Using t
he Results from DOE
....................................
247
9.10.1
Pr
ocess Selection
......................................
247
9.10.2
Ca
vity Steel Adjustment .................................
248
9.10.3
Pr
ocess Adjustment Tool
................................
249
9.10.4
Se
tting Process Change Tolerances ........................
249
9.10.5
R
educing Inspection ....................................
249
9.11
The Dimensional Pr
ocess Window (DPW) .........................
250
9.12
Selections of F
actors for DOEs
..................................
252
9.13
Anal
ysis of Variance (ANOVA)
..................................
257
9.14
Collecting Sho
ts for a Quality Check
.............................
258
9.15
Choosing t
he Highs and Lows for DOEs from the Process Window
....
259
9.16
DOE Application t
o Optimize Pack and Hold Times .................
260
9.17
Se
tting Acceptable Machine Tolerances and Alarms during
Production
..................................................
265
9.18

Summary ....................................................
266
10 Mold Qualification Flo wchart, Production Release,
and Troubleshooting ........................................ 269
10.1 Mold Qualification Flo wchart ................................... 269
10.1.1
Mold F
unction Qualification Procedure ....................
271
10.1.2
Mold and P
art Quality Qualification Procedure ..............
271
10.2
Mold Qualification Chec
klist ....................................
271
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 22 (page 22)

XX Cont ents
10.3 Pr ocess Documentation ........................................ 272
10.3.1
Pr
ocess Sheet
.........................................
272
10.3.2
W
aterline Diagrams
....................................
273
10.3.3
Mold T
emperature Maps
................................
274
10.3.4
Se
tup Instructions
.....................................
275
10.3.5
Oper
ator Instructions ...................................
275
10.4
Document
ation Books .........................................
276
10.5
Qualification Pr
oduction Runs ..................................
277
10.6
Mold Specific T
roubleshooting Guide ............................
277
10.7
Molding S
tartup and Shutdown
.................................
278
10.7.1

Purging ..............................................
278
10.7.2
S
tartup of a Molding Machine ............................
279
10.7.3
Shutdo
wn of a Molding Machine
.........................
280
10.8

Troubleshooting ..............................................
280
10.9
Im
portant Equipment and Tools for Qualifications and
Troubleshooting
..............................................
283
10.10

Common Defects, Their Causes, and Prevention
...................
284
10.10.1
Spla
y: What is it? How to get rid of it? .....................
285
10.10.2
Def
ects in Molding
.....................................
287
11 R ole of Mold Cooling, Venting, and Regrind in Process
Development ............................................... 293
11.1 Mold Cooling ................................................. 293
11.1.1
N
umber of Cooling Channels
............................
294
11.1.2
R
eynolds Number of the Coolant Flow
....................
294
11.1.3
T
ype of Coolant
.......................................
295
11.1.4
Ser
ies and Parallel Cooling
..............................
296
11.2
V
enting .....................................................
297
11.2.1
Dimensions of t
he Vent
.................................
298
11.2.2
Pr
imary Vent Depths
...................................
299
11.2.3
Location of V
ents
......................................
302
11.2.4
F
orced Venting or Vacuum Venting .......................
304
11.3
R
egrind .....................................................
305
11.3.1
Effect of t
he Molding Process on the Part Properties
........
305
11.3.2
Using R
egrind
........................................
307
11.3.3
Batc
h and Continuous Processes of Incorporating Regrind ....
307
11.3.4
Es
timating the Amount of Regrind from
Different Generations
..................................
308
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 23 (page 23)

XXIContents
11.3.5 Effect of R egrind on Processing ........................... 311
11.3.6
Closing R
emarks .......................................
311
12 R elated Technologies and Topics ............................ 313
12.1 Ca vity Pressure Sensing Technology ............................. 313
12.1.1
Sensor
s and Output graphs ..............................
314
12.1.2
T
ypes and Classification of Pressure Sensors ...............
315
12.1.3
Use of Inf
ormation from the Pressure Graphs ...............
317
12.1.4
Contr
olling the Process with Cavity Pressure Sensors ........
319
12.1.5
Sensor Locations
......................................
321
12.2
Building a Kno
wledge Base
....................................
322
12.3
Concur
rent Engineering in
Injection Molding
.....................
324
12.3.1
The Pr
oduct Designer ...................................
326
12.3.2
The T
ooling Engineer
...................................
326
12.3.3
The Mold Designer and Mold Mak
er ......................
327
12.3.4
The Mat
erial Supplier
..................................
327
12.3.5
The Pr
ocess Engineer ...................................
328
12.3.6
The Quality Engineer
...................................
329
12.3.7
The Sales T
eam at the Molder ............................
329
12.3.8
Mandat
ory for All Departments
..........................
330
12.3.9
Im
plementing Concurrent Engineering ....................
330
13 Quality Concep ts ............................................ 333
13.1 Basic Concep ts ............................................... 333
13.2

Histogram ...................................................
334
13.3
N
ormal Distribution ...........................................
335
13.4
S
tandard Deviation ............................................
336
13.5
Specification Limits and
S
tandard Deviation ...................... 337
13.6
Capability Inde
x ..............................................
339
13.7
Pr
ocess Capability
............................................
340
13.8
S
tatistical Quality Control (SQC) and Statistical Process Control (SPC)
342
13.9

References ...................................................
342
Appendix A Mat erials Data Sheet .............................. 343
Appendix B
Con
version Tables for Commonly Used
Process Parameters ............................... 349
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 24 (page 24)

XXII Cont ents
Appendix C W ater Flow Tables ................................. 351
Appendix D
P
art Design Checklist .............................. 353
Appendix E
Mold Design Chec
klist ............................. 355
Appendix F
Mold Qualification Chec
klist ...................... 357
Appendix G
R
egrind Tables – Percentage of Regrind
in Total Shot ....................................... 359
Index ........................................................... 361
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 25 (page 25)

Introduction to
Scientific Processing
 1.1  The Ev olution and Progress
of

Injection

Molding
Injection molding and extrusion are the most common techniques employed in the
manufacture of plastic products. Injection molding of plastics began as an idea by
the Hyatt brothers for the manufacture of billiard balls. The idea was borrowed
based on a patent by John Smith to inject metal castings. Since then, injection
molding of plastics has come a long way. The technique became a popular way to
fabricate plastic parts because of the simplicity of the concept, efficiency of pro-
duction, and the possibility of producing intricate parts with fine details.
The art of injection molding evolved to its present state due to a few key reasons.
The requirements of the molded parts became more stringent because of the ad-
vances in the fields of science and technology. The demand for tighter tolerances
and more complex parts increased and is ever increasing. A required tolerance of
a couple thousandths of an inch on a one inch dimension is not uncommon these
days. Parts requiring innovative designs, especially designed for assembly (DFA)
or parts molded from different materials in the same mold (multi-material mold-
ing) are now commonplace. As polymer materials were developed for injection
molding, the requirements of processing changed. The discovery of the different
morphologies of polymers and the need for better melt homogeneity in molding led
to the introduction of the injection screw. Various designs for material-specific
screws have followed since. The use of high temperature materials that have high
melting points and need high mold temperatures have led to the use of high-tem-
perature ceramic heaters and mold temperature controllers providing higher heat
capability. Innovations in electrical and electronic technologies paved the road for
machines that could be better controlled, accurate, and efficient. Response times
for hydraulic valves can be in milliseconds. All electric machines and hybrid
mac
hines are gaining popularity because of their consistency and accuracy. The
real time processing parameters of a molding machine can now be viewed from
1
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 26 (page 26)

2 1  Introduction to Scientific Processing
any part of the world via an internet connection and therefore machine production
can be monitored or machines can be debugged online. All these features are be-
coming a common practice among manufacturers. Even some auxiliary equipment
can now be debugged and programmed by the suppliers via an internet connec-
tion. For the machines tied into the company ERP system, automated messages can
be sent to the managers and supervisors about the machine status and quality
issues.
The need for efficiency and the requirements for advanced product features
have dictated the need for innovations in injection molding over the years.
 1.2  The Molding Process
The actual molding process has been traditionally defined as the inputs to the
molding machine. These are the settings of speeds, pressures, temperatures and
times such as injection speeds, holding pressure, melt temperature and cooling
time. These are inputs one would set at the molding machine and record on a
sheet, commonly called the Process Sheet. However, the word process now needs to
be redefined as the complete operation that encompasses all the activities the plas-
tic is subjected to inside a molding facility−from when the plastic enters the mold-
ing facility as a pellet to when it leaves the facility as a molded part. For example,
the storage of the plastic, the control of the drying of the plastic, and the post mold
shrinkage of the part can have a significant influence on the quality of the part.
During this journey of the pellet, every stage can have a significant effect on the
final quality of the part or assembly. Naturally, understanding every stage now
becomes imperative if we would like to control the quality of the molded part.
Molding a part that meets the quality requirements is not the real challenge. The
real challenge is molding parts consistently; cavity to cavity, shot after shot, and
from one production run to another meeting all the quality requirements and with
the least amount of effort and maximum efficiency.
 1.3  The Thr ee Types of Consistencies
R
equired in Injection Molding
The aim of developing a molding process should be to develop robust processes
that would not need any process modifications once the processes are set. Process
consistency leads to quality consistency, see Figure 1.1. We look for three different
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 27 (page 27)

31.3 The Three Types of Consistencies R equired in Injection Molding
types of consistencies: cavity-to-cavity consistency (Figure 1.1(a)), shot-to-shot con-
sistency (Figure 1.1(b)), and run-to-run consistency (Figure 1.1(c)). Cavity-to-cav -
ity consistency is required in multicavity molds so that each cavity is of the same
quality level as the other cavities. Shot-to-shot consistency implies that every con-
secutive shot would be identical to the previous shot, or the first shot is identical to
the last shot of the production run with the process parameters remaining the
same during the entire production run. When the process parameters from two
different runs are identical and they produce the same quality parts, then this is
called run-to-run consistency. Robust and stable processes always yield consistent
quality parts with one established process.
There can be several reasons for the three types of consistencies. A cavity-to-cavity
inconsistency could be caused because of an error when cutting the steel in one of
the cavities or by making one of the gates too large. A shot-to-shot inconsistency
could be caused because of a damaged leaking check ring at the end of the molding
screw. A run-to-run inconsistency can be caused because of a lack of a robust pro-
cess or simply because the process was not accurately or completely documented
in the previous run. The run to run consistency is the one that most companies
struggle with. This book is deals in depth with process development of robust,
r
epeatable and reproducible processes.
Figure 1.1 The three types of consistencies required in injection molding
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 28 (page 28)

4 1  Introduction to Scientific Processing
Figure 1.1 The three types of consistencies required in injection molding (continued)
Another reason for inconsistencies and variations in the molded product is the
nature of the shrinkage of plastics. When molten plastic is injected inside a mold it
cools and freezes to form the product. There is a reduction in the volume of the
melt when it cools inside the mold. This is called shrinkage. The magnitude of
shrinkage determines the final dimensions of the part. However, this shrinkage is
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 29 (page 29)

51.3 The Three Types of Consistencies R equired in Injection Molding
not easily predictable and depends on a number of factors. There is a range of
shrinkage values available and that makes it difficult for a mold maker to select a
shrinkage value. For example, the shrinkage value for a low density polyethylene
is between 1.3 to 3.1 %, which is a wide range. Shrinkage also depends upon the
processing conditions. For example, higher the melt temperature, the higher the
shrinkage. Almost every processing parameter can affect the shrinkage to varying
degrees. Refer to Figure 1.2, which shows the effect of the molding parameter on
the length of the part. To increase or decrease the length of the part, several
par
ameters can be increased or decreased.
MELT
(MORE VOLUME)
MOLDED PART
(LESS VOLUME)
Length
 Low Melt Temp
 Low Mold Temp
 High Pack Pressures
 High Pack Times
 High cooling Times
Length
 High Melt Temp
 High Mold Temp
 Low Pack Pressures
 Low Pack Times
 Low cooling Times
Increase the length
Decrease the length
Figure 1.2 Effect of molding parameters on shrinkage and dimension of a part
As seen in the figure, several parameters can have effect on the part dimension
and quality. To increase the length of the part, some parameters need to be in-
creased whereas some need to be decreased. Further, the magnitudes of change in
length with change in the parameter varies from parameter to parameter. If the
molding processes are not developed with these understandings, and in case the
dimensions get out of specifications, each processor can work with any one of the
parameters. The net result being that processes that were supposedly approved
end up having completely different values in a matter of a few runs. When process
sheets are compared, for example, from two years ago, there are hardly any num-
bers that match the current settings.
It should be the goal of every molder to develop an understanding of the molding
process for the given mold. A systematic process development approach must be
followed. The result of such an approach is a robust, repeatable and reproducible
process: the 3 R’s.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 30 (page 30)

6 1  Introduction to Scientific Processing
A process shown in Figure 1.3 is not acceptable because there is a lot of ineffi-
ciency in the system. Such processes result in defective parts, loss of material, loss
of time, and not to mention the time and effort put in by the molding personnel.
The parts can be remolded and shipped to the customer, however, the time and
effor
ts lost cannot be recovered. The reputation of the molder is something that
can also be permanently affected.
> Parts out of Spec > QA needs to be involved > Tech needs to be involved
> Time Loss > Material Loss > Possible Customer Returns
Figure 1.3 Example of an inefficient process
 1.4  Scientific Processing
Scientific Processing is the process of achieving consistency in part quality via the
application of the underlying scientific principles that control the parameters of
the molding process. To achieve this consistency, we must be able to control every
activity that is taking place in the process and to control every activity, we must
understand the underlying scientific principles. The goal of scientific processing
should be to achieve a robust process. Achieving robustness in each of the stages
that the pellet travels through automatically translates to an overall robust pro-
cess. The term consistency must not be confused with the parts being within the
required specifications. A consistent process will produce parts that will reflect
the consistency but the parts may be out of specifications. In this case, the mold
steel must be adjusted to bring the parts within the required specifications and the
process must not be altered.
The term Scientific Molding was coined and promoted by a two pioneers in the field
of injection molding, John Bozzelli and Rod Groleau. Their principles are widely
used today and are industry standards. Scientific molding deals with the actual
plastic that enters the mold during the molding operation at the molding press.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 31 (page 31)

71.5 The Five Critical Factors of Molding
Scientific processing is the complete process from when the pellet enters the
f
acility and leaves the facility as a finished product. Figure 1.4 shows the journey
of the pellet.
Figure 1.4 The journey of the pellet and the critical factors that need to be controlled
 1.5  The Five Critical Factors of Molding
The final molded part is a result of five critical factors, which need to be carefully
selected, as shown in Figure 1.5:
1.
P
art design
2.
Mat
erial selection
3.
Mold design and cons
truction
4.
Molding mac
hine
5.
Molding pr
ocess
Each of these factors plays a very important role in the production of the molded
part and therefore every one of them has to be optimized for producing the molded
part. It is not just the performance of the part but also the consistent molding of
the part in production.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 32 (page 32)

8 1  Introduction to Scientific Processing
1.5.1Part Design
The concept of the part starts with the engineer designing it. The part must be de-
signed for molding and all the design rules for plastics must be considered. Rules
for plastic part design are considerably different than those used for metal part
design because of the inherent nature of the plastic. For example, to avoid sink
defects in the plastic part, thick sections cannot be present. Additionally, all cor -
ners must have a radius to avoid stress concentration and premature failure. With
the growing cost of labor and the need for efficiency in the manufacturing process,
the part designers now face the added challenges of designing parts for assembly
along with those molded parts that utilize multiple materials, commonly referred
to as multicomponent molding or multimaterial molding.
Mold Design
& Build
Molding
Machine
Process
Part Design
Material
Part
Quality
Figure 1.5 The five factors influencing part quality consistency and process robustness
1.5.2Material Selection
Based on the part design and the part performance requirements, the plastic mate-
rial must be selected. In addition, the part design may require a special plastic
material or a special additive to be added to the base plastic for performance. If a
thick section must be present, a filled material may need to be selected or if there
is a sliding surface, then an additive reducing the coefficient of friction may need
to be added to the plastic. Material selection should typically be done when the
basic part design is done. Additional smaller changes can be done concurrently.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 33 (page 33)

91.5 The Five Critical Factors of Molding
1.5.3Mold Design and Construction
Once the part design and material selection is complete, the mold must be de-
signed and constructed such that it is robust enough to withstand the molding
process and the plastic material. For example, during the molding process, the
mold can be subjected to high mechanical stresses, especially during the plastic
injection and the packing phases. The gates are high-wear areas and there are sev-
eral places where the air needs to vent out for the plastic to enter the mold. Some
plastic materials will require special attention and the mold must be specifically
designed with the material in mind. Shrinkage may vary considerably from mate-
rial to material. All these material specific factors must be considered. The re-
quired number of parts over the life of the mold is another factor that will dictate
the actual materials of construction. Wear on the mold components must be con-
sidered, as the materials chosen to build the injection mold and mold cavities will
impact the overall life of the mold and associated amount of maintenance required
to keep it production worthy.
1.5.4Machine Selection
Selecting the right machine for the mold should be done once the mold design is
complete. It can be done concurrently during the mold construction stage. The
machine plays a very important role in the stability of the molding process. For
example, machines with large shot sizes must not be used to mold small shots be-
cause the part quality consistency will suffer. Vice versa, using a large percentage
of the shot size can give rise to problems with melt homogeneity and therefore
issues wit
h fill and dimensions. Small molds must also not be mounted in large
machines for fear of mold damage due to excessive clamp tonnage being applied.
1.5.5Molding Process
Process optimization is the last step before the mold is released into production.
This book will cover this topic in detail. If the above four factors and activities are
not properly selected or performed, process optimization can be a challenge, if not
impossible, without incurring significant cost and delay to the project. At this
stage, it is usually very late in the project timeline to make any changes to the part
design or mold design, especially because of the cost and time involved. An im-
properly constructed mold can have a very narrow process window leading to a
process that will tend to be unstable. If the material selected is not capable of hold-
ing the tolerances, no process will be able to produce satisfactory parts. Molding
processes should be robust, repeatable, and reproducable.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 34 (page 34)

10 1  Introduction to Scientific Processing
 1.6  Concurrent Engineering
There are various departments involved in the production of the molded part and
therefore regular meetings between the different departments must be held. Each
department will have specific knowledge of the selection process and can contrib-
ute not just to the process but more importantly predict issues once the mold
comes over to their department. For example, getting the process engineer involved
in a mold design can help in part orientation in the mold for easy removal, or the
mold maker can get help with vent locations based on the process engineer’s expe-
rience. Involving the quality engineer can help the process engineer understand
the required tolerances in the design stage. If the tolerances seem to be unrealistic,
they can go back to the product designer for wider tolerances or a material change.
There are a lot of benefits associated with implementing concurrent engineering in
injection molding. A section is devoted to this topic in this book. In the chapters
that follow, the reader will be introduced to the underlying scientific principles to
achieve a robust molding process. This understanding will then help in the appli-
cation of these principles, to develop a robust process and to troubleshoot prob-
lems that occur in production. The chapters have been written in a logical sequence
to build the readers’ knowledge as one would require it or should learn it. However,
if the reader is familiar with the topic, he or she can bypass some in favor of other
chapters containing the desired information.
 1.7  Variation
Variation is a natural phenomenon that is present in every process and activity.
For example, the time it takes to drive to work has a number, but it can be an aver-
age number that is collected over a certain period of time. There will be times that
are lower than the average and there are times that are above the average. In in
-
jection molding, if t
he lengths of 100 parts are measured, then one could get an
average number, but there will be parts below and above this number. Variation
can never be eliminated, so the goal should be to minimize it. Variation should be
measured in order to predict the quality of the molded parts. As shown in Figure
1.6, a molder could measure the part marked as A and decide that all the molded
parts are within specification. However, only when the variation is measured can
it be seen that there will be some parts, such as the one marked B, which are out
of specification.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 35 (page 35)

111.7 Variation
LSL USL
PART A
PART B
NOM
Distribution of
inherent variation
X
X
Figure 1.6 Reason to measure variation
Variation in injection molding can come from a number of sources as shown in
Figure 1.7. The variation in the molded product is the collective variation from
each of these sources, plus many more. Controlling the variation in each source
will help the reduction of the overall variation in the final product.
PROCESS PERSONNEL MACHINE
ENVIRONMENT MATERIALS MEASUREMENT
Figure 1.7 Some of the sources of variation in a molded part
Suggested Reading
Osswald, T. A., Turng, L., Gramann, P. J. (Eds.), Injection Molding Handbook (2007) Hanser, Munich
Kulkarni, S. M., Injection Molding Magazine (June 2008) Cannon Publications, Los Angeles, USA
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 36 (page 36)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 37 (page 37)

Properties of Polymers
and Plastics That
Influence Injection
Molding
The term plastic is most commonly used when referring to injection molding mate-
rials. Plastics are a class of long-chain molecules called polymers. When polymers
have certain properties they are called plastics. Since most of the commercially
molded polymers fall under the classifications of plastics, we shall refer to these
materials as plastics in this book. The other most commonly molded polymers are
thermoplastic elastomers (TPEs) that have the same molding characteristics as
plastics but different properties when molded. When referring to these materials,
these will be mentioned as TPEs. To understand the concept of injection molding of
plastics, a basic understanding about polymers, their properties, and the additives
that are incorporated into them is required. This chapter will discuss the topic of
polymers and their application to the injection molding process.
 2.1  Polymers
Every particle in the universe is composed of atoms. Atoms in turn combine to
form molecules. A molecule of water is made up of two atoms of hydrogen and one
atom of oxygen. Polymers are very large molecules that have several identical
molecules joined t
ogether. An ethylene molecule attaches itself to another ethylene
molecule and when several thousands or millions of such molecules join with each
other, a polyethylene molecule is formed. ‘Poly’ means many and ‘mer’ means part.
A polymer is many parts chemically joined together. The basic single unit from
which it is synthesized is called a monomer, ‘mono’ meaning one. Polymers are
also called macromolecules. The process of converting monomers to polymers is
called polymerization. Polymers can also be synthesized from multiple monomers.
For example, ABS is synthesized from three different monomers, acrylonitrile,
butadiene, and styrene.
2
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 38 (page 38)

14 2  Properties of Polymers and Plastics That Influence Injection Molding
Polymers have been around since the beginning of time. DNA, the basic unit of life,
is a polymer found in all plants and animals and is a naturally occurring polymer.
Today, almost all commercially available polymers are synthesized from natural
ingredients. The first commercially synthesized polymers were materials such as
ebonite in the late 1800s. Interestingly, the widely used polyolefins gained com-
mercial importance only in the late 1950s, almost couple decades after the intro-
duction of polyvinyl chlorides, nylons, and polyesters. Recently introduced poly -
mers are based on biomaterials and nanotechnology.
Polymers are synthesized from monomers via a chemical process. There are mainly
two types of polymerization processes, the addition polymerization process and the
condensation polymerization process. In the addition polymerization process, a
cat
alyst initiates the polymerization reaction and each monomer adds onto the
next monomer until all the monomers are polymerized. A common example of an
addition polymer is polyethylene. Poly
e
thylene is polymerized from ethylene mon-
omer, which is a gas at room temperature. The double bond in the ethylene mole-
cule breaks and a bond with an adjacent ethylene molecule is formed. The process
continues and the result is a large molecule with high molecular weight. The
pol
ymerization process is shown in Figure 2.1.
Monomer
Ethylene
Polymer
Polyethylene
Polymerization
Polymerization
Figure 2.1 The process of polymerization and formation of polyethylene
In condensation polymerization too, each monomer adds on to the next monomer,
but this chemical reaction also produces a low molecular weight byproduct that
has to be continuously removed out of the system for the polymerization to con-
tinue. Condensation polymers are usually polymerized from two or more families
of monomers. Nylons and polyesters are examples of condensation polymers. A
nylon (chemical name: polyamide) is polymerized from the monomer families of
diamines and diacids, as shown in the chemical reaction.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 39 (page 39)

152.2 Molecular Weight and Molecular Weight Distribution
nH2N – R – NH 2 + nHO2C – R’ – CO 2H →
H – (– NH – R – NHC
O – R’ – CO –) n – OH + (2n–1)H 2O
R and R’ ar
e the characteristic groups that are present in the monomer. In this
case, water is the byproduct. Based on these groups, different types of nylons can
be produced. The unit in parenthesis repeats itself to form the polymer. If R is
(Ch
2)6, then the first monomer is hexa me thylene diamine and if R’ is (CH 2)4, the
second monomer is adipic acid. The polymer that is synthesized from these two
monomers is poly(hexamethylene adipamide), commonly called Nylon 6,6.
 2.2  Molecular W eight and Molecular
Weight Distribution
The repetition of the monomer units causes the molecular weight to increase. The
number average molecular weight is the addition of the molecular weights of
each of the molecules divided by the number of molecules. Most commercial poly -
mers have a number average molecular weight between 40,000 and 200,000, with
some having extremely high numbers. Ultra-high molecular weight polyethylene
(
UHMWPE) is an e
xample for a molecular weight in the range of 1–6 million.
Molecular w
eights for greases and soft waxes range between 500 and about 3000,
whereas some tough and brittle waxes have molecular weights between 3000 and
10,000 [1]. When the attraction between the molecules (intermolecular forces) is
high, the materials can gain sufficient mechanical properties at lower molecular
weights. Polyamides and polyesters are examples of polymers with strong inter
-
molecular f
orces. In materials such as polyethylene, where intermolecular forces
are low, high molecular weights are required to achieve acceptable mechanical
properties. In general terms, molecular weights for polyethylenes are higher those
that for nylons or polyesters. UHMWPE was developed for applications in which
polyethylenes were the right choice except for their mechanical properties. In most
cases, the mechanical properties reach a plateau with increasing molecular
weights. Other properties are also affected by molecular weight. Of particular inter-
est to molders is the viscosity of the polymer where an increase in molecular
weight results in the increase in viscosity. For melt processing, a certain minimum
viscosity is essential for the formation of a processable and homogeneous melt.
Processability increases with molecular weight but due to the increase in viscosity,
the energy required to process also increases and reaches a point where the in-
crease is not practical for melt processing, see Figure 2.2.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 40 (page 40)

16 2  Properties of Polymers and Plastics That Influence Injection Molding
Figure 2.2 Effect of molecular weight on mechanical properties and the viscosity of polymers
n
MW
Figure 2.3 Molecular weight distribution for injection molding and extrusion grades
The addition of the monomers during the polymerization process (both addition
and condensation) is completely random. It is difficult to control the growth of the
molecules which results in molecules of various lengths and therefore varying
molecular w
eights. This in turn leads to a distribution of the molecular weight in
the polymer called the molecular weight distribution (MWD) of a polymer. The
MWD is an important factor in processing. The lower molecular weight units melt
faster than the high molecular weight units. In injection molding, the plastic needs
to be injected into the mold as fast as possible to make sure the molecules do not
freeze off in the cold mold during injection. If this happens, the part will not fill
completely and/or will have built up internal stresses when ejected out of the mold.
A narrow MWD ensures that all the molecules are molten during approximately
the same period of time. When the residence time in the barrel of the injection
molding machine reaches the upper limit, the possibility of molecular breakdown
or degradation, resulting in the loss of properties in the final product, increases.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 41 (page 41)

172.3 Polymer Morphology (Crystalline and Amorphous Polymers)
This is another reason why a low MWD is desired. However, in the case of extru-
sion, melt strength is an important element of the process. In this case, the higher
molecular weight units have higher viscosity and help to carry the molten lower
molecular weight units to form the extrudate. Therefore, a broader MWD is pre-
ferred. A narrow MWD would result in the loss of melt strength, therefore, also in
the loss of the shape and characteristics of the extrudate profile. The residence
time inside the barrel of an extruder is short because extrusion is a continuous
process and therefore the risk of degradation is low. This difference in MWD is the
decisive factor whether a resin is an injection molding grade or an extrusion grade.
Sometimes, extrusion grades are used in injection molding because the viscosity
can be low enough to fill the cavities effectively and consistently. The opposite
would be less likely, where injection molding grades are used in extrusion. Figure
2.3 shows the difference in the MWD for injection molding and extrusion grades.
 2.3  P olymer Morphology (Crystalline
and Amorphous Polymers)
Polymer morphology is the type of arrangement of the molecules in a polymer
sample. Based on the different ways the molecules can be arranged, there are two
types of polymers: amorphous and crystalline polymers. In amorphous polymers,
the molecules are randomly present without any structure or arrangement. Under
a high-power microscope, this sample would look like a big bowl of cooked spa-
ghetti. In the case of crystalline polymers, there are certain regions of the sample
where the molecules are present in a highly ordered and structured manner.
Each of these regions is called a crystallite. The difference between the two mor -
phologies is shown in Figure 2.4, and the difference in the properties is mentioned
in Table 2.1.
Amorphous Crystalline
Figure 2.4 Arrangement of molecules in amorphous and (semi)crystalline polymers
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 42 (page 42)

18 2  Properties of Polymers and Plastics That Influence Injection Molding
No polymer can be completely crystalline and there are always areas in the poly -
mer where the molecules are present in a random manner. A polymer is therefore
truly semicrystalline in nature, where crystallites are present in the midst of amor-
phous regions. Part of a molecule can be present in an amorphous region and part
of it can be present in a crystallite, as shown in Figure 2.5. The degree of crystallin-
ity refers to the amount of crystallites present in the sample. Table 2.2 shows the
degree of crystallinity for some common polymers.
Crystallite
Amorphous Matrix
Figure 2.5 Crystallites are present in an amorphous matrix
Table 2.1 Difference between the Properties of Amorphous and Crystalline Polymers
Amorphous Crystalline
Random Structure Ordered Structure
Broad ‘Melting’ Range Narrow Melting Range
Low Volumetric Shrinkage Higher Volumetric Shrinkage
Lower Mech. Properties Higher Mech. Properties
Transparent/Translucent Opaque
e. g., ABS, PS e. g., Nylons, Polyesters
Table 2.2 Degree of Crystallinity for Common Polymers [2]
Polymer Degree of Crystallinity
High density polyethylene 0.80
Isotactic polypropylene 0.63
Poly(ethylene terephthalate) 0.50
Nylon 66 0.70
Nylon 6 0.50
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 43 (page 43)

192.3 Polymer Morphology (Crystalline and Amorphous Polymers)
There are two main reasons why a polymer can be amorphous or crystalline: the
geometric regularity of the polymers and the strength of the intermolecular forces
between them. Geometric regularity is the arrangement of the groups on the main
chain. Stereoregular polymers are those where the monomer segments on the
main chain are in the same regular configuration. This regularity helps the chains
to pack closer and easier together, just as the blocks in the game of Tetris. In the
case of atactic polymers, where the monomer segments are randomly oriented, the
chance for packing of the molecules is reduced, leading to an amorphous polymer.
During the polymerization process of some polymers, it is possible to control the
orientation of the monomers and produce stereoregular polymers. Polystyrene is
an example of such a controlled polymerization. Regular polystyrene is atactic and
therefore amorphous. However, it can be polymerized by using certain metallocene
catalysts to form a stereoregular polymer that makes the polystyrene semicrystal-
line. The properties of crystalline polystyrene are far superior and their mechani-
cal and chemical properties excel. The molecular structures of atactic and syndio-
tactic polystyrene are shown in Figure 2.6.
Figure 2.6 Atactic and syndiotactic polystyrene
Another common example is linear polyethylene, which is a highly crystalline and
branched polyethylene that is amorphous. Intermolecular forces also play a role in
determining crystallinity. The stronger the attraction between the groups of mole-
cules, the higher is the crystallinity. Nylon is an example where the intermolecular
forces are high, see Figure 2.7. The hydrogen atom of one molecule has a strong
affinity to the oxygen atom of the adjacent molecule, causing the chains to get
closer and pack better. This effect can also be observed in the case of polyesters.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 44 (page 44)

20 2  Properties of Polymers and Plastics That Influence Injection Molding
Figure 2.7 Intermolecular attraction resulting in an increase in polymer crystallinity
Table 2.3 lists the morphologies of some common polymers. However, it must be
noted that morphologies can be altered during their manufacture and the melt
processing of the polymer. For example, mold temperature plays a very important
role in the development of crystallinity. Low mold temperatures do not favor the
development of crystallites. This is described later in the chapter.
Table 2.3 List of Amorphous and Crystalline Polymers
Polymer Chemical Name Amorphous Semicrystalline
ABS Acrylonitrile butadiene styrene Y
ASA Acrylonitrile styrene acrylate Y
GPPS General purpose polystyrene Y
HDPE High-density polyethylene Y
HIPS High-impact polystyrene Y
LCP Liquid crystalline polymers Y
LDPE Low-density polyethylene Y
PA Polyamide (nylons) Y
PAI Polyamide imides Y
PBT Polybutylene terephthalate Y
PC Polycarbonate Y
PEEK Polyether ether ketone Y
PET Polybutylene terephthalate Y
POM Polyoxymethylene (acetal) Y
PP Polypropylene Y
PPS Polyphenylene sulfide Y
PSU Polysulfone Y
PVC Polyvinyl chloride Y
SAN Styrene acrylonitrile Y
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 45 (page 45)

212.3 Polymer Morphology (Crystalline and Amorphous Polymers)
The relationship between the percentage crystallinity and molecular weight de-
fines the use of the polymer, which defines the use of polyethylene based on this
relationship, see Figure 2.8. Low molecular weight and low crystallinity polyethyl-
ene is typically used more in soft waxes and greases, whereas high molecular
weight and highly crystalline materials tend to be hard plastics.
% Crystallinity
Figure 2.8 Effect of molecular weight and crystallinity on the mechanical properties of
pol
yethylene [1]
Morphology of a Melt
As mentioned in Section 2.3, morphology is the type of arrangement of the mole-
cules. Polypropylenes (PP) are crystalline materials. If a piece of PP is melted, the
molecules move away from each other and all the crystallites disappear. There is
no systematic arrangement of the molecules placing them in a random arrange-
ment. Since they are random, the PP in its melt form is in an amorphous state. The
melt of a crystalline polymer is therefore always in an amorphous state. An excep-
tion to this are liquid crystalline polymers (LCP).
Opaque when solidT ransparent when molten
Figure 2.9 The melt of crystalline plastics is always in an amorphous state (except LCPs)
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 46 (page 46)

22 2  Properties of Polymers and Plastics That Influence Injection Molding
 2.4  Role of Morphology in Injection Molding
The molding characteristics of crystalline and amorphous polymers are different.
Crystallites are formed because of high molecular attraction and because of the
possibility of the chains being unhindered to form the bond. Sometimes just the
presence of another molecule or a side chain prevents crystallization. For melt
processing, the crystallites must be dissolved and the chains separated from each
other in order to reduce the viscosity and inject the melt into the mold. It is this
basic nature of forming and dissolving of the crystallites that dictates various
differ
ences in processing and melt behavior.
2.4.1 Differences in Shr inkage between Amorphous
and

Crystalline Materials
Shrinkage is the volumetric change between the melt phase and the glassy or
r
ubbery phase. As the temperature increases, the molecules gain more and more
energy, become mobile, and move away from each other. This results in an increase
in the volume of the polymer. The intermolecular volume is called free volume. As
the polymer cools, the opposite takes place and the free volume reduces, a process
known as shrinkage. In crystalline polymers, the movement of the molecules away
from each other is much greater compared to amorphous polymers. As the mole-
cules cool, they settle back into a highly structured and closely packed array, which
is another contributing reason for their high shrinkage. The absence of such a
structure in amorphous polymers negates the need for the molecules to find a defi-
nite resting place during the cooling process, resulting in a lower shrinkage value
compared to crystalline plastics. Shrinkage values for ABS, an amorphous poly -
mer, are approx. 0.5–0.8 % compared to some nylons or acetals that can exhibit
shrinkage values of up to 2.5 %.
2.4.2Melt Processing Range
Similar to an ice crystal, the polymer crystallite needs a specific and definite
amount of energy to melt. This is called the crystalline melting point and at this
particular temperature the crystallite melts. In crystalline plastics, melting occurs
over a fairly narrow range of temperatures; this melting range typically covers
appr
ox. 20 °C (30 to 35 °F), see Figure 2.10. For example, PBT (Valox 420 from
Sabic Inno
vative Plastics) needs to be processed between 248 and 265 °C (480 to
510 °F), i. e., within a range of 18 °C. The temperature is not as specific and sharp
as in the case of simple molecules because of the presence of the amorphous
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 47 (page 47)

232.4 Role of Morphology in Injection Molding
regions and other attraction forces. The lower the percentage of crystallinity, the
broader is the processing range.
In the case of amorphous plastics, there is no melting point but the molecules sof-
ten over a range of temperatures. There is a recommended processing temperature
range for amorphous plastics. In this range, the viscosity of the plastic is low
enough to flow and fill the cavities. For example, ABS (Cycolac from Sabic Innova-
tive Plastics) can be processed from 218 to 260 °C (425 to 500 °F), a range of 42 °C.
Tg Tm
Figure 2.10 Thermal transitions and melt processing ranges for amorphous and crystalline
plastics
2.4.3Mold Filling Speed
Viscosity of the plastic and melt temperature are inversely related. As the plastic
temperature increases, the viscosity decreases. As the plastic flows through the
cold mold, the temperature of the plastic drops and the viscosity increases. Since
for crystalline plastics, the processing range is narrow, the temperature of the flow
front must always be higher than the minimum required melt temperature. In the
above example of the PBT, the flow front temperature must never drop below
248 °C (480 °F) before the cavity is completely filled. This narrow processing range
of crystalline polymers therefore dictates the fact that the plastic must be injected
as fast as possible into the mold.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 48 (page 48)

24 2  Properties of Polymers and Plastics That Influence Injection Molding
In the case of amorphous plastics, because the plastic stays viscous over a broader
range of temperatures, slow injection speeds are permissible, as long as the flow
front stays above the minimum processing temperature. This is typical in the
molding of lenses and other optical parts.
2.4.4Mold Temperatures
Similar to the melting of the crystallites at a particular temperature, the crystal-
lites also start to form at a particular temperature, a temperature lower than the
melt temperature. This is called the crystallization temperature. This temperature
supplies the necessary energy for the formation of the crystallites. If the mold is
too cold, the polymer will not be able to receive this energy, preventing the forma-
tion of the crystallites. This leads to the loss of the properties in the molded part.
Material suppliers conduct extensive research to determine suggested operating
mold temperatures. Therefore, it is highly recommended to stay within the recom-
mended specifications for crystalline materials. This concept is further explained
in Section 2.5 on thermal transitions.
Since crystallites are absent in amorphous plastics, the mold temperature range
can be broader and can be especially extended towards the lower temperatures.
Because crystallites do not need to be formed, the molecules are not looking for
any particular amount of energy; therefore, lower temperatures are acceptable.
However, care has to be taken to prevent molded-in stresses when parts are pro-
duced using extremely cold molds.
2.4.5Barrel Heat Profile
In the injection molding barrel, the screw performs the function of conveying and
melting the polymer. The base of the screw is where the polymer pellets first come
in contact with the screw. This section is designed to convey and then soften the
pellets. In case of crystalline polymers, the crystallites need a lot of energy to melt,
so this section, which is usually the second heating zone from the back of the
screw, is set at a higher temperature than the next zones in order to initiate the
softening of the molecules. But because crystalline plastics can also be heat sensi-
tive or cannot stand high temperatures for long periods of time, the temperature in
next heating zone is reduced. This leads to a heating profile that has a hump in the
middle, which is typical for crystalline plastics. In case of amorphous plastics,
such a profile is not necessary because they need less energy to soften and can
tolerate longer residence times in a heated barrel, as is shown in Figure 2.11.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 49 (page 49)

252.4 Role of Morphology in Injection Molding
Nozzle Zone 1 Zone 2 Feed throat
Amorphous
Crystalline
(Reverse profile)
Figure 2.11 Barrel heat profiles for amorphous and crystalline plastics
2.4.6Screw Recovery Speeds
The barrel heaters provide heat on the outside of the cylinder. Because plastics are
bad conductors of heat, the plastic closer to the screw and furthest from the wall of
the barrel requires additional heat to become plasticized. This additional effective
melting energy comes from the shear friction caused by the rotating screw. High
screw speeds generate high amounts of shear, helping the crystallites melt and
ensuring melt homogeneity. For amorphous plastics, due to the low energy re-
quired to melt the plastic, high screw speeds are not critical. In fact, high screw
speeds can degrade the material and cause defects such as splay.
2.4.7Nozzle Temperature Control
Nozzle temperature control is critical while processing crystalline polymers. Not
only must the temperature of the nozzle be maintained within the processing
range, it should be maintained within a temperature range that is much narrower
than the processing range. This is especially important during the static phases of
the plastic flow, which follows the holding phase of one cycle and precedes the
injection phase of t
he next cycle. Lower temperatures tend to freeze off the plastic
in the nozzle tip making it impossible to inject the next shot. At higher tempera-
tures, all the crystallites will have disappeared making the viscosity very low and
causing what is commonly called nozzle drooling. There are some innovative de-
signs for nozzle tips available in the market to help prevent this problem. With
amorphous plastics, the broad processing range helps maintain the viscosity in
the nozzle and prevents freeze off or drool.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 50 (page 50)

26 2  Properties of Polymers and Plastics That Influence Injection Molding
2.4.8Cooling Times
Once the crystallites are formed, the molded part gains sufficient strength and
only needs a small drop in temperature to be ejected out of the mold. Therefore, in
the case of crystalline materials, the cooling times are shorter compared to amor -
phous plastics (for the same part thickness). Nucleating agents are added to some
crystalline plastics to accelerate crystallization, thus reducing the cooling time
even further. Nucleating agents have no effect on amorphous materials because
there are no crystallites to be formed.
2.4.9Mechanical Properties
The crystallites provide mechanical strength to the polymer. They are like a rope,
rather than a bundle of grass, providing strength. Generally speaking, crystalline
plastics have higher mechanical properties than amorphous plastics. Therefore,
most are referred to as engineering resins. However, with the advent of new tech-
nologies and the discovery of new additives, the properties of amorphous materials
can be easily modified to match those of crystalline materials.
2.4.10Optical Clarity
Most amorphous polymers in their natural and unmodified state are optically clear.
The distance between the molecules is large, allowing the wavelengths of light
to pass through and making them transparent: polystyrene is an example of this.
For crystalline polymers, the packing of the molecules does not allow the passage
of light and therefore they are usually opaque. As the degree of crystallinity de-
creases, the materials tend be translucent. As will be discussed in the next section,
melts of any polymer, crystalline or amorphous, are always amorphous and there-
fore a purge of an unfilled melt will always look clear. Polyethylene, a crystalline
plastic, is opaque but a small amount of melt drool out of the nozzle tip will always
be transparent.
A summary of the processing differences between amorphous and crystalline ma-
terials is summarized in Table 2.4. These are only broad comparisons because part
and mold design can affect every one of these parameters.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 51 (page 51)

272.5 Exceptions of Morphology Rules to P olyolefins
Table 2.4 Summary of the Processing Differences between Amorphous and Crystalline
Mat
erials*
Process Amorphous (Semi) Crystalline
Mold Fill Rates Slower rates are acceptable Fast rates are required
Importance of Mold
T
emperatures
Mainly for improved cosmetics
and stress relief
For mechanical properties,
cosme
tics and stress relief
Molding Barrel Settings Regular profile May require a reverse profile
Melt Heat Stability Fair Low
Molding Screw Rotation Speeds Lower are acceptable Require high
Nozzle Tip Temperature Control Easy Difficult because of
Freeze off/drool
Cooling times Higher Lower
* These are broad comparisons only. Part and mold design can affect every one of these parameters.
 2.5  Ex ceptions of Morphology Rules
to

Polyolefins
Polyolefins are mostly crystalline materials. It would therefore be logical to follow
the processing guidelines that are mentioned in Section 2.3. However, there are
some properties that these crystalline materials possess that belong to the amor -
phous category:
 The
y have sharp melting points but by nature they are soft and can therefore be
processed for a small range below their melting temperatures. These materials
are also thermally stable for a wide range above the melt temperature, and in
some cases, even up to 200 °F above the melt temperatures. Therefore, the over-
all processing range for these materials is very wide although they are crystal-
line materials.
 Because t
hey have a wide processing range, slower injection speeds can be used
to inject the material into the mold.
 Cr
ystallization temperatures dictate mold temperatures, therefore, mold temper-
atures would have to be set between 70–110 °C for polyethylenes and much
higher in case of polypropylene. However, in most cases, it is perfectly acceptable
to deviate from this range and mold parts are lower mold temperatures or even
using chilled water as the cooling medium. The reason for this is twofold. First,
since the T
g of olefins is lower than room temperature, complete crystallization
can happen as a post molded phenomenon. Therefore, ultimately the molded
part will achieve the required properties. The associated danger is the presence
of molded in stresses, dimensional variation, and warpage in the parts. The
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 52 (page 52)

28 2  Properties of Polymers and Plastics That Influence Injection Molding
majority of the parts molded with olefins are commodity products, therefore, the
drawbacks are usually overlooked. As an example, a trash can molded from poly-
propylene does not have tight tolerances that have to be maintained. In most
cases it is mostly cosmetic with some load testing. The end user could use it for a
few years during which if it get defective it is thrown away. In some cases these
drawbacks are remedied by using fillers and additives. Depending on the quality
requirements, the mold temperatures must be set appropriately.
 Scr
ew speeds need not be on the higher end since the crystallites are soft and
will ultimately melt because of the smearing action. Screw speeds must be opti-
mized to create a good homogeneous melt. If there are colorants or other addi-
tives that may burn and degrade at the higher screw speeds, then it is acceptable
to reduce the screw speeds.
Because of the soft nature of the plastic, ejection temperatures are closer to room
temperatures. This increases the cooling time and therefore cycle times are usu-
ally long. As a related side note, part design can play an important role and reduce
cycle times significantly.
 2.6  Thermal Transitions in Polymers
Although there are no polymers that are completely crystalline, for the sake of the
following discussion, let us assume that they do exist. Therefore in the following
discussion, a crystalline polymer would mean a polymer that is 100 % crystalline,
an amorphous polymer would mean a polymer that is 100 % amorphous, and a
semicrystalline polymer would be a polymer that is partially crystalline with the
crystallites present in the amorphous regions.
First consider an amorphous polymer submerged in a very cold liquid such as liquid
nitrogen. The temperature of liquid nitrogen is anywhere between –210 to –195 °C
(–345 to –320 °F). At this temperature, the different molecular energies are almost
nonexistent and therefore the molecules are not free to move, resulting in a brittle
polymer. A sheet of flexible plastic, when quenched into liquid nitrogen, becomes
brittle. If dropped on a concrete floor, it would sound like glass and shatter into bits
and pieces. However, if the temperature of the sheet is gradually increased, the
thermal energy from the increasing temperature provides energy to the molecules.
Depending on the polymer the sheet is made of, at a given temperature, the sheet
becomes flexible. This is called the glass transition temperature or the T
g of the
pol
ymer. At Tg, the molecules have sufficient energy to move and the polymer is
flexible. A further increase in the temperature provides more energy, the flexibility
increases, and eventually the molecules become soft enough to form a viscous mass
suitable for melt processing. An increase in the energy of the molecules results in
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 53 (page 53)

292.6 Thermal Transitions in Polymers
the increase in the specific volume of the polymer. Specific volume is the volume
per gram of the polymer. A plot of specific volume versus temperature, like the one
shown in Figure 2.10, shows a linear increase in the volume until an inflection point
is reached, where the slope of the line changes. The inflection point reflects the glass
transition temperature of the amorphous polymer. Further increase after the glass
transition shows a steady increase in the specific volume.
Next, let us look at a crystalline polymer and perform the same experiment. In
crystalline polymers, the intermolecular forces are very high and therefore a con-
siderable amount of energy is required to move the molecules away from each
other. As the temperature increases, the molecules gain more and more energy but
the intermolecular forces prevent any movement. At the temperature where the
molecules move away from each other and become mobile, the molecules are very
flexible and the polymer is now a molten mass. The crystallites need a definite
amount of energy to melt. When they receive this in the form of thermal energy
they melt all at once. The phenomenon is similar to the melting of low molecular
molecules, such as water where ice turns into water at 0 °C. For this reason, crys-
talline materials show a sharp melting point. Because the transition from a solid to
a liquid is sudden, the transition is referred to as melting and the transition tem-
perature is called the melt temperature or T
m. These polymers do not go through a
glass transition temperature. A plot of specific volume versus temperature shows
an inflection point at the T
m, as can be seen in Figure 2.12.
Crystalline
Amorphous
Semicrystalline
Specific
Volume
(cm³/gm)
- Semicrystalline Polymers- Semicrystalline Polymers
T T
Figure 2.12 Specific volume versus temperature for polymers
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 54 (page 54)

30 2  Properties of Polymers and Plastics That Influence Injection Molding
Based on the thermal responses of amorphous and crystalline polymers, it is now
easy to predict the response of a semicrystalline polymer. As state previously, a
semicrystalline polymer can be thought of as crystallites present in an amorphous
matrix of molecules. This sample will exhibit the properties of the crystalline and
the amorphous polymer and will therefore have a glass transition temperature and
a melting point temperature. On the specific volume plot, there will be two inflec-
tion points representing each of the transitions, as shown in Figure 2.11. However,
in case of semicrystalline polymers, the inflection point is not as sharp as one
would see in the amorphous or crystalline samples. Rather, there is a range where
the inflection starts and ends. This happens because of the different sizes of the
crystallites and differences in molecular lengths. Once the molecules of a semi
-
cr
ystalline material have melted, they now have a lot of thermal energy and any
additional energy can start breaking down the molecules causing degradation of
the polymer.
This difference between the crystalline and amorphous materials leads to the fact
that semicrystalline materials have a much narrower melt processing window
compared to amorphous materials. For example, nylon (a semicrystalline material)
will have a melt processing window between 248 and 265 °C (480 to 510 °F), while
an ABS (amorphous material) has a window between 218 and 260 °C (425 to
500 °F). The processing window is 17 °C for nylon, compared to 42 °C for ABS.
Specific
heat
Temperature →
Second run
First run
Tg Tc Tm
Figure 2.13 Typical representation of a DSC plot for polymers
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 55 (page 55)

312.6 Thermal Transitions in Polymers
Now, let us consider the reverse process of phase transitions. When the tempera-
ture of a melt of a crystalline polymer is gradually reduced, the molecular energy
starts to reduce. The viscosity of the melt starts to increase and the crystallites
begin to reappear. The temperature at which the crystallites occur is called the
crystallization temperature or the T
c. For crystallization to occur, the melt must be
subjected to the crystallization temperature for a finite amount of time. If the melt
of a crystalline polymer is rapidly quenched below the glass transition tempera-
ture, the solidified polymer will not exhibit any crystallites and will be completely
amorphous. It is for this reason that mold temperature is of greater importance
when molding semicrystalline polymers as compared to amorphous polymers.
The above discussed temperatures affect the properties of the polymers and there-
fore decide the final applications of the polymers. For example, for the product de-
signer, the T
g is one of the important factors of consideration. For a product to be
flexible at room temperature, its T g must be below room temperature, such as for
elastomers. For a product to be rigid at room temperature, the Tg must be above the
room temperature. For the molder, the knowledge about the crystallization and
melting temperatures is important because these dictate the processing condi-
tions. The T
c is used to determine the mold temperature range to start and promote
the crystallization of the molecules. The Tm is used to determine the melt tempera-
ture ranges. A processing data sheet does not provide these as typical values but
they are reflected under the processing conditions. The material manufacturer per-
forms the analysis and uses the results as one of the many tests to recommend the
processing conditions.
The differential scanning calorimeter (DSC) is an instrument used to determine
the thermal transitions in polymers. A typical graph generated by a DSC was
shown in Figure 2.13. For crystalline polymers, two scans are performed. During
the first scan, the polymer is taken from a low set temperature all the way past the
melting temperature, and the transitions are recorded. The sample, which is now
in the molten form, is immediately quenched in liquid nitrogen. Most polymers are
below the T
g at this temperature. Since the melt is amorphous and is immediately
quenched, all the energy is taken away and the frozen polymer is also completely
amorphous. The DSC scan is repeated. As the temperature increases, the mole-
cules gain more and more energy. The glass transition is noticed and when the
crystallization temperature is reached the crystallites begin to form. Crystalliza-
tion temperatures are recorded on the second scan. For amorphous polymers, a
second scan is not necessary.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 56 (page 56)

32 2  Properties of Polymers and Plastics That Influence Injection Molding
Tg
Tc
Tm
Tc
Figure 2.14 Resulting morphologies depending on polymer conditioning
The relationship of mold temperature and crystallinity is explained in Section 2.3.4
using the DSC graph, see also Figure 2.14. The figure shows the difference in the
resulting morphologies when a polymer sample is quenched below the T
g and
when a polymer sample is subjected to the crystallization temperatures for a given
time.
2.6.1 R elationship between the Glass Transition Temperature
and Post Mold Shrinkage
Below the T g, the molecules have no energy and are therefore are not capable of
any movement. The plastic is brittle at temperatures below the Tg. Above the Tg, the
plastic molecules have the energy to be mobile and the plastic is therefore flexible.
Referring to Figure 2.15, consider the room temperature at 25 °C. At room temper-
ature, the polycarbonate (PC) disc breaks when one tries to bend it because the T
g
of PC is about 150 °C. However, the polypropylene (PP) ruler flexes but does not
break because, depending on the grade of the PP used, the T
g of PP can be any -
where between 0 to –30 °C.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 57 (page 57)

332.6 Thermal Transitions in Polymers
Room Temperature
25 100
Tg of
Polystyrene
0 -25
Tg of
Polypropylene
Temperature (°C)
50 75
Polystyrene is
brittle at room
temperature
Polypropylene is
flexible at room
temperature
Figure 2.15 PC breaks but PP flexes at room temperature because of the position of their
melting temperatures, with respect to room temperature
Consider a molding process with the following conditions:
 Ambient t
emperature is 25 °C.
 T
emperature of the molded part when ejected out of the mold is 65 °C.
 The time t
hat the part takes to cool from 65 °C to the ambient temperature of
25 °C is 7 minutes (see Figure 2.20).
 A cr
itical dimension is the length of the part.
65
52
43
35
30 27 26 25 25 25 25 25 25 25 25 25
10
20
30
40
50
60
70
0123456789 10 11 12 13 14 15 16
Part Temp vs Time Part Temp
Time (minute)
Temperature (° C)
Figure 2.16 Change in part temperature with time
Two materials, Plastic A and Plastic B, were molded. Plastic A has a Tg of 35 °C.
This means that above 35 °C, the molecules are mobile and have the energy to
move, and below 35 °C, the molecules do not have sufficient energy to move. Plas-
tic B has a T
g of 10 °C. This means that above 10 °C, the molecules are mobile and
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 58 (page 58)

34 2  Properties of Polymers and Plastics That Influence Injection Molding
have the energy to move, and below 10 °C, the molecules do not have sufficient
energy to move.
Plastic A: refer to Figure 2.17. The part that is molded with Plastic A has a Tg of
60 °C. From the graph, we can observe that the time the part takes to reach 60 °C
is 3 minutes. Because molecules are mobile above the T g, the material will con-
tinue to shrink until they reach the T g. Therefore, in this case, the length of the
part will keep changing until the temperature of 60 °C is reached, or in other
words, the length will keep changing for the first 3 minutes and it will then will
stay constant. Therefore, post molding shrinkage after the part has reached its T
g is
nonexistent, and the dimensions do not change once the parts have been molded
and are always subjected to temperatures below the T
g. In the this example, the
length of the part stays constant over time.
5.15
5.13
5.12
5.11 5.11 5.11 5.11 5.11 5.11 5.11
5.1
5.11
5.12
5.13
5.14
5.15
5.16
01 2 3456789 10 11 12 13 14 15
16
v Part Temp
Time (minute)
MaterialA with Tg = 35 °C
Length (cm)
Figure 2.17 Change in part length with time for Plastic A with a Tg of 35 °C
Plastic B: Refer to Figure 2.18. The part that is molded with Plastic B has a Tg of
10 °C. Because the ambient temperature is above the T g of the plastic, the mole-
cules in the molded part will never reach the T g. Therefore, in this case, the mole-
cules will always have enough energy to keep moving and reach their equilibrium
positions in ambient temperature. This movement causes shrinkage, leading to a
continuous change in part length until an equilibrium is reached. This shrinkage
can occur over a longer period of time, which could be in hours or even days. In the
this example, the length of the part molded from this Part B with a T
g of 10 °C will
continue to change over time until it reaches the final equilibrium.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 59 (page 59)

352.6 Thermal Transitions in Polymers
5.15
5.14
5.13
5.12
5.115
5.11
5.105
5.1 5.1 5.15 .1 5.1
5.095
5.105
5.115
5.125
5.135
5.145
5.155
01 02 03 04 05 06 07 08 09
01 00
Part Length vs Time Part Temp
Time (hour)
Material with Tg = 10 °C
Length (cm)
Figure 2.18 Change in part length with time for Plastic B with a Tg of 10 °C
Commodity plastics, such as polyethylenes and polypropylenes, have Tg values that
are lower than room temperatures and, therefore, they are susceptible to higher
degrees of post mold shrinkage. Often one notices that over time, lids of plastic
containers do not fit well and become warped. This is the result of post mold
shrinkage. CD discs and DVD discs are molded from polycarbonate, which has a T
g
value of about 150 °C. Therefore, one will probably never come across a CD or a
DVD that is warped. The T
g is reached very quickly as the disc gets ejected from
the mold. It also helps that CDs and DVDs are even-walled and thin.
The Tg is what is called as an alpha transition, and it has the most effect on the post
mold shrinkage phenomenon. Every polymer also has other similar transitions be-
low the alpha transitions called the beta and gamma transitions. In reality, there is
still a very small movement of the molecules below T g, but is not as significant as
compared to the movement above the T g. Therefore, a small amount of post mold
shrinkage will always continue to happen even below the T g. Sometimes, this can
be confused with and/or added to the stress relief that could be also occurring at
the same time. Stress relief can happen below or above the T
g.
The common stress relief technique of annealing is based on the concept of T g.
During the injection molding process, because of the high melt pressures, stresses
can develop in the part. If the part is taken slightly above the T
g, these stresses can
be relaxed. There can be a dimensional change associated with the annealing pro-
cess for the reasons previously described in this section.
Refer to Figure 2.19, which shows a music cassette that was processed under con-
ditions that led to in-molded stress. The cassette was lost in the interior of the car
and was found several months later after a hot summer. The heat from inside a
parked car relieved the in-molded stress and caused the warpage.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 60 (page 60)

36 2  Properties of Polymers and Plastics That Influence Injection Molding
Figure 2.19 Warpage due to release of in-molded stress
Table 2.5 Glass Transition and Melting Temperatures*
Polymer Tg (°C) Tm (°C)
Natural rubber  –73  36
Nylon 6   50 250
Polybutadiene (trans-)  –54  47
High density polyethylene (HDPE) –125 146
Polypropylene (syndiotactic)   –8 204
Polystyrene (PS)  100 250
Polyvinyl chloride (PVC)  –18 191
Polycarbonate (PC)  150 243
Acrylonitrile butadiene styrene (ABS)  104 –
*  Because t here are several grades of the same base polymers, and moreover, because the plastic purchased
from suppliers always has additives blended in, the values here should be used for reference only. As in the
case of ABS, which is a ter-polymer, the Tg will drop with increasing amounts of the butadiene content.
 2.7  Shr inkage of Polymers in
Injection

Molding
Shrinkage occurs when the melt begins to cool and the molecules start to return to
their desired equilibrium states. The distance between the molecules is higher in
the melt than when they are cooled. As the melt cools, the molecular distance de-
creases, reducing the free volume and causing shrinkage. The higher the increase
in volume during the melting phase, the higher is the shrinkage. The shrinkage of
the plastic during the injection molding process can be easily affected by the vari-
ous molding parameters. This poses the biggest challenge to mold makers when
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 61 (page 61)

372.7 Shrinkage of Polymers in Injection Molding
sizing the core and cavity steel and to the processors in order to maintain the part
quality during production. It is therefore important to develop a robust and stable
process that will produce parts with consistent shrinkage and that is least affected
by natural variations. The shrinkage of injection molded parts also depends on the
direction of plastic flow, see Figure 2.20. The plastic is injected through the gate
and the molecules get oriented in the direction of flow. Given a chance to relax and
with sufficient available energy the molecules will get back to their original
non-oriented equilibrium state. But this is not always the case, because molding
cycles need to be fast and wall thicknesses are small, inhibiting relaxation. In addi-
tion, typically the molecules are under mechanical stress from the injection, pack
and hold forces. This causes a variation in shrinkage between the direction of flow
and the direction perpendicular to flow. The effect is more pronounced for crystal-
line materials because they have a high shrink value caused by the formation of
the crystallites. Amorphous materials too exhibit a difference in shrinkage de-
pending on flow direction, but the difference is not as pronounced. Materials ex-
hibiting varying shrinkage values in the cross and parallel flow directions are
known as anisotropic materials; materials with identical shrinkage values are
called isotropic materials. For example, polyesters are anisotropic materials while
ABS is an isotropic material. For Valox 357, a polyester manufactured by Sabic
Inno
vative Plastics, the parallel flow shrinkage values range from 1.0 to 1.4 % and
the cross flow values range from 1.2 to 1.6 %. Although there is an overlap, the
a
verage values for the cross flow are higher. For Starex AB-0760, an ABS manu
-
f
actured by Samsung, the shrinkage values in the cross and parallel flows are both
0.30 to 0.60 %.
Exact shrinkage values can never be predicted because shrinkage is a function of
various parameters. Some manufacturers publish the shrinkage values for differ -
ent sample thicknesses because, as stated earlier, in thicker parts heat can be re-
tained for a longer time allowing the molecules to relax and causing more shrink -
age. For this reason it is difficult to determine the exact mold cavity dimensions
that will yield a molded part with the exact finished dimensions. It is very rare to
build an injection mold cavity and cores that are the exact size of the desired fin-
ished part or CAD model. Mold makers will typically build the mold ‘steel safe’ and
adjust the steel after the initial sampling of the mold. Another factor that compli-
cates this situation is the fact that final shrinkage is a function of both the cross
and parallel flow shrinkages. Rarely will a required dimension be perfectly parallel
or perfectly perpendicular to the melt flow. The final shrinkage value is a combina-
tion of the two numbers. In this case, leaving the mold cavity and cores steel safe
is always a good idea. It is not possible to do so in all cases and the tooling engineer
must rely on past experience and make the best decision.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 62 (page 62)

38 2  Properties of Polymers and Plastics That Influence Injection Molding
Figure 2.20 Parallel flow and cross flow shrinkage
The term shrinkage in injection molding always compares the part dimensions to
the dimensions of the mold. Shrinkage of the melt in a free state is always positive.
This means that the volume will always decrease and the part dimension will
therefore always become smaller. The term free state is used to describe a non
-
inhibit
ed state of movement where the molecules are not held by any other forces.
However, in some parts, such as long tubular parts, we find that as the part shrinks
the length will decrease, forcing the diameter to increase, see Figure 2.21. This can
be visualized similar to Poisson’s effect where contraction due to external force in
one direction leads to the expansion in the perpendicular direction. This negative
shrinkage in the diameter of the part is due to the force that is exerted because of
the overall reduction in the length of the part which can be significant. Stress can
easily build up in such parts and cause premature product failure.
Figure 2.21 Positive and negative shrinkage in molded parts
The phenomenon does not necessarily lead to a negative shrinkage value, and can
also result in a reduced shrinkage value, depending on the amount of mechanical
stress in the part. This poses another challenge for the mold maker in sizing of the
cavities. Mechanical stresses can cause a change in dimension in parts with other
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 63 (page 63)

392.8 The Plastic Pressure–Volume– T emperature (PVT) Relationship
geometries, such as square boxes with deep pockets. The deep pockets create un-
supported walls. Sometimes reduction in the distance between the walls causes an
increase in the distance in the other direction. This is represented in Figure 2.22.
As molded
Post molded
Figure 2.22 Mechanical stresses affecting part dimensions
 2.8  The Plas tic Pressure–Volume–
T
emperature (PVT) Relationship
COOL HOLD PACK INJECTION
INCREASING
PRESSURE
0 MPa
50 MPa
100 MPa
150 MPa
200 MPa
SABIC Innovative Plastics
Grade: Xenoy 1102
Figure 2.23 Pressure-volume-temperature relationship in injection molding
Figure 2.23 shows that at 0 MPa of pressure, as the temperature of the plastic is
increased, the specific volume also increases. This increase is the result of the in-
crease in the intermolecular distance and the free volume. At any given tempera-
ture, if an external pressure is applied, the melt gets compressed and the specific
volume decreases. Specific volume is directly proportional to temperature but is
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 64 (page 64)

40 2  Properties of Polymers and Plastics That Influence Injection Molding
indirectly proportional to the pressure. In injection molding, there is a combina-
tion of factors involved as the melt is transformed into the product. The melt is
collected as a shot (see Section 2.8.1) in front of the molding screw. There is some
compression of the melt because of the pressure (back pressure) during the shot
build up process. The molten plastic is then injected with high pressure into a cold
mold. During this process, and after the plastic is inside the mold, the melt is
cooling do
wn. As the melt is being transformed to the final molded product, the
pressure, volume, and temperature of the melt are all continuously changing, and
the final contour in the graph is a combination of the curves in the Figure 2.23.
Cavity pressure sensing equipment can track these curves and predict shot to shot
part quality and consistency.
As a processor, one of the most important concepts to keep in mind is that plastic
melt is compressible and elastic, which can be visualized in the example of a rub-
ber band ball (Figure 2.24). It can sometimes be seen that in the molding process,
at the end of the second stage pressures and just before the screw recovery pro-
cess, the screw bounces back. This happens as the melt decompresses when the
pressure is released. As will be discussed in Chapter 7, cushion values must also
be kept at a minimum in order to avoid shot to shot variations.
Force
Figure 2.24 Plastic melt is compressible similar to a ball of rubber bands
2.8.1Importance of Plastic Density in Injection Molding
Density is defined as the weight of unit volume of a cube of a given material and is
expressed as grams per centimeter cube (g/cc or g/cm
3) in the metric system. For
example, the density of polystyrene (PS) is 1.06
g/cc. This means t
hat a 1 centi
-
me
ter PS cube will weigh 1.06 grams or a volume of 1 cubic centimeter (cc); if filled
with PS, will weigh 1.06 grams. If the same volume is filled with lead, it will weigh
11.36 grams because the density of lead is higher than PS. It will weigh 0.789
grams if 1 cc is filled ethanol because the density is lower than PS.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 65 (page 65)

412.8 The Plastic Pressure–Volume– T emperature (PVT) Relationship
By definition, the shot capacity of a molding machine is defined as the maximum
amount of PS that can be held in front of the screw. For example, if the shot ca
-
pacity is specified t
o be 100 grams, then the barrel will hold 100 grams when the
screw is completely in its retracted position. The density of PS is 1.06
g/cc. If t
he
same volume in front of the screw that holds 100 grams is now filled with a plastic
with a higher density, such as a 30 % glass filled PBT with a density of 1.53
g/cc,
t
he shot capacity will now be 144
g. On t
he other hand, if the PS is replaced by
polypropylene (PP), which has a density of 0.90
g/cc,
the shot capacity will now be
only be 85
g. This im
plies that even though the barrel is rated for 100
g, it will be
im
possible to mold a 100 g PP part on the machine. Refer to Figure 2.24.
Machine shot sizes are frequently used in injection molding calculations. It is im-
portant that the shot sizes are therefore always recalculated for the material being
molded. The formula is: Normalized shot size = (published shot size in GPPS/1.06)
× density of the material under consideration. GPPS is a general purpose poly
-
s
tyrene.
To avoid confusion, several manufacturers have started specifying the machine shot
sizes in volumetric units. In such cases, all part weights and runner weights will
also have to get converted into volumes to perform the appropriate calculations.
No Material SpecificG ravity Shot Capacity (g)
1P olystyrene 1.06 100
2N ylon 61 .15 108
3A cetal 1.42 134
4 30% GF PBT1 .53 144
5L DPE0 .928 7
6P olypropylene 0.90 85
MAXIMUM VOLUME OF
THE BARREL = V
Figure 2.25 Max shot weight dependence on material densities
2.8.2Residence Time and Maximum Residence Time of a Plastic
At a given melt temperature, a polymer can be held without degradation only for a
finite amount of time. If the polymer is subjected to longer lengths of time, the
polymer chains break and start to degrade. This time is defined as the maximum
residence time. Figure 2.26 is a residence time graph for ULTEM 1000, a polyether
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 66 (page 66)

42 2  Properties of Polymers and Plastics That Influence Injection Molding
imide from Sabic. If the melt temperature is set to approximately 700 °F (371 °C),
the plastic can be held in the barrel for a maximum of about 12 minutes. As the
melt temperature increases, the maximum residence time number decreases.
From the same graph, if the melt temperature is 770 °F (410 °C), then the maxi-
mum residence time is 6 minutes.
Figure 2.26 Maximum residence time for Ultem 1000 (PEI from SABIC Innovative Plastics)
In the molding process, the plastic enters the feed throat, gets conveyed over the
screw, collects in front of the screw, and is then injected through the nozzle into
the mold. The section of the barrel that houses the screw is heated with the
assis
tance of the heater bands, which help to melt the plastic. The shear from the
rotating screw also contributes to the heat and aids the melting. The plastic enters
into the barrel as pellets and leaves as a melt. The amount of time the plastic takes
to travel from the feed throat to the nozzle tip is called the residence time of the
plastic in the barrel. Because injection molding is a batch process, depending on
the shot weight of the mold, the cycle time of the mold, and the maximum shot size
of the machine, the residence time of the plastic will change.
During the injection molding operation, the melt should always have a residence
time that is less than the maximum residence time for the given material. If the
mold is a hot runner mold, then the residence time of the melt in the hot runner
system must be added to the residence time in the barrel to give the total residence
time. See Section 6.8.4 for calculations and more information.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 67 (page 67)

432.8 The Plastic Pressure–Volume– T emperature (PVT) Relationship
2.8.3Plastic Datasheets
Datasheets for plastics provide detailed information about them. There are differ -
ent types of datasheets. The most common datasheets, which the material manu-
facturers provide, are the property data sheets, the processing datasheets, and the
material safety datasheets (MSDS).
TYPICAL PROPERTIES
MECHANICAL Value Unit Standard
Tensile Stress, yld, Type I, 0.2 in/min 7500 psi ASTM D 638
Tensile Modulus, 0.2 in/min 450000 psi ASTM D 638
Flexural Stress, yld, 0.05 in/min, 2 in span 17600 psi ASTM D 790
Flexural Modulus, 0.05 in/min, 2 in span 325000 psi ASTM D 790
Hardness, Rockwell R 90 - ASTM D 785
IMPACT Value Unit Standard
Izod Impact, notched, 73°F 4.1 ft-lb/in ASTM D 256
Izod Impact, notched, -40°F 1.2 ft-lb/in ASTM D 256
Gardner Impact, 73°F 8 ft-lb ASTM D 3029
THERMAL Value Unit Standard
HDT, 264 psi, 0.250", unannealed 220 °F ASTM D 648
CTE, flow, -40°Ft o 100°F 4.21E-05 1/°F ASTM E 831
Relative Temp Index, Elec 60 °C UL 746B
Relative Temp Index, Mech w/impact 60 °C UL 746B
Relative Temp Index, Mech w/o impact 60 °C UL 746B
PHYSICAL Value Unit Standard
Specific Gravity 1.05 - ASTM D 792
Mold Shrinkage, flow, 0.125" 0.5 -0 .8 % GE Method
Melt Flow Rate, 230°C/3.8 kgf 5 g/10 min ASTM D 1238
OPTICAL Value Unit Standard
Gloss, untextured, 60 degrees 88 - ASTM D 523
ELECTRICAL Value Unit Standard
Dielectric Strength, in air, 62 mils 952 V/mil ASTM D 149
Arc Resistance, Tungsten {PLC} 6 PLC Code ASTM D 495
Hot Wire Ignition {PLC) 3 PLC Code UL 746A
High Voltage Arc Track Rate {PLC} 1 PLC Code UL 746A
High Ampere Arc Ign, surface {PLC} 0 PLC Code UL 746A
Comparative Tracking Index (UL) {PLC} 0 PLC Code UL 746A
FLAME CHARACTERISTICS Value Unit Standard
UL Recognized, 94HB Flame Class Rating (3) 0.060 in UL 94
Figure 2.27 Example of a properties datasheet
The property datasheets provide information about the properties of the plastics.
These properties can be physical, mechanical, electrical, and so on. The categories
of the properties will depend on the intended end use of the material. An example
of the properties datasheet is shown in Figure 2.27 for a generic ABS. This data-
sheet provides the properties of the plastic under the guidance of organizations
such as the ASTM, ISO, DIN, and JIS. These organizations provide specifications of
the test sample, the conditions, and the procedure of testing. These values should
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 68 (page 68)

44 2  Properties of Polymers and Plastics That Influence Injection Molding
be used as guidelines. When comparing two materials, care should be taken that
the test method used for both is the same because there are no conversion factors
available between the test methods, for example, between an ASTM test and a ISO
test. The final manufactured product is almost certainly of another geometry and
therefore the numbers on the datasheet should only be a guide. Generic datasheets
contain only a single point data. Processing parameters can have a substantial
im
pact on the properties. As was shown in this article, the impact of the resistance
for a given ABS ranges from less than 2 N-m (1.4 ft-lb) to almost 50 N-m (36.5
ft-lb),
as a r
esult of changing melt temperatures between 218 and 271 °C, and mold tem-
peratures between 29 and 85 °C.
An example of a processing datasheet is shown in Figure 2.28. Resin manufactur -
ers conduct tests on the materials to arrive at the values on the datasheet. There
are no standards available for these tests. For the most part, the mold tempera-
tures, the melt temperatures, the drying times, and other temperatures can be re-
lied upon. However, the injection pressure, the injection speed, the back pressure,
the screw rotation speeds in revolutions per minute (rpm), and the shot to cylinder
size cannot be relied upon because these are always a function of the part design
and the mold design. A part that is about 10
mm t
hick and 50
mm long will r
e-
quire a lot less pressure and speed to fill as compared to a part that is 3
mm t
hick
and 200
mm long. A 30
r
pm on a 20
mm molding scr
ew is not the same as a
30
r
pm on a 50
mm molding scr
ew because the circumferential speed on a 50
mm
will be higher
, therefore, it will generate more shear heat. There have been no stud-
ies done to prove that a 50 to 70 % value of shot to cylinder size provides the best
quality parts. A general rule in industry is a 20 to 80 % size, but that can also be
challenged based on the part and material that is under consideration for molding.
The cycle time should also figure into the calculation.
Injection Molding Parameter Value Unit
Drying Temperature 200–210 °F
Drying Time 2–4 hr
Drying Time (Cumulative) 8 hr
Maximum Moisture Content 0.01 %
Melt Temperature 450–500 °F
Nozzle Temperature 450–520 °F
Front -Z one 3 Temperature 450–470 °F
Middle -Z one 2 Temperature 420–440 °F
Rear -Z one 1 Temperature 370–390 °F
Mold Temperature 120–180 °F
Back Pressure 50–100 psi
Screw Speed 30–60 rpm
Shot to Cylinder Size 50–70 %
Vent Depth 0.0015–0.002 in
Figure 2.28 Example of a processing datasheet
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 69 (page 69)

452.9 References
 2.9  References
[1] T urner, A. and Gurnee, E. F., Organic Polymers, Prentice-Hall, 1967, p. 51
[2]
Zw
eifel, H., Maier, R., Schiller, M., Plastics Additives Handbook (2009) Hanser, Munich
[3]
R
ef: http://www.ptonline.com/columns/the-importance-of-melt-mold-temperature
Suggested Reading
Deanin, R. D., Polymer Structure, Properties and Applications (1972) Cahners, Boston, MA
Tager, A. A., Physical Chemistry of Polymers (1978) Mir Publishers, Moscow
Odian, G., Principles of Polymerization (1991) Wiley Interscience, USA
Gowariker, V. R., Viswanathan, N. V., Sreedhar, J., Polymer Science (1996) New Age International (P)
Limited, Delhi
Billmeyer, F. W., Textbook of Polymer Science (1984) Wiley Interscience, NY
Brydson, J. A., Plastics Materials (195) Butterworth-Heinemann Ltd, Oxford, UK
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 70 (page 70)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 71 (page 71)

Polymer Rheology
Polymer rheology is the science of flow of polymers. The study of polymer flow is
essential to understand the melt processing of plastics. In any melt processing
technique, the plastic has to be melted and then deformed to conform to the final
product specifications. In injection molding, the melt must be injected into a mold
and then cooled to get the final part. In extrusion, the melt is shaped through a die
and then cooled down to get the required profile. During the injection of the melt
into the mold and until it reaches its final form, the melt is subjected to various
forces including mechanical and thermodynamic forces. In this chapter, some of
these concepts are explained in brief to give the reader an understanding sufficient
enough to help apply them to injection molding. The concepts also have been sim-
plified and the general mathematical details have been left out. For those readers,
who would like to get an in depth understanding on this topic, a number of books
are mentioned in the references at the end of the chapter.
 3.1  Viscosity
Viscosity is the resistance to flow. The higher the resistance to flow, the higher is
the viscosity. Honey or corn syrup do not flow easily and therefore have high vis-
cosities. On the other hand, water flows very easily and therefore has low viscosity.
Gasses have even lower viscosities as compared to water and therefore flow easier.
Viscosity depends on a number of factors and is an inherent property of the fluid
but can be influenced by external forces. Based on the types of forces the polymer
is subjected to and/or on the type of medium the polymer is present, various types
of viscosities are defined. Of particular interest in injection molding is the viscos-
ity of the melt as defined by the apparent viscosity. As will be discussed later in the
chapter, the viscosity of the melt is dependent on the applied force and therefore is
not constant. Hence the adjective ‘apparent’ is used to describe the viscosity at a
particular given shear rate.
3
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 72 (page 72)

48 3  Polymer Rheology
Consider a liquid sandwiched between two metal plates as shown in Figure 3.1.
The distance between the plates is H. The area of the plates is A. The bottom plate
is held stationary and the top plate is displaced in the X direction with a force F
and a velocity V = V
H, see Figure 3.2.
F
Y
H
X
A
V
Figure 3.1 Experimental setup to determine the velocity profile
V
V
V
F
H
Figure 3.2 Velocity profile for a liquid under shear force
The layer of liquid just below the top plate will also move with the plate at a velo -
city VH and the layer just above the bottom plate will be stationary with a velocity
equal to V = V0 = 0. At any layer between the two plates, at a distance of x, the velo-
city is
Vx and is proportional to the distance from the bottom plate. The shear rate
is the differential velocity between the layers. Since each of the layers is moving at
different velocities, the shear rate is also a function of the distance x. The shear
rate of the top layer is given by the equation
g∙
H=VH /H (3.1)
and at an
y given layer at a distance x is given by
g∙
x=Vx /x (3.2)
The units of shear r
ate are reciprocal seconds or s–1.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 73 (page 73)

493.2 Newtonian and Non-Newtonian Mat erials
Each layer is subjected to shear forces as it is being pulled in the direction of the
applied force. Since stress is force divided by area, the shear force τ at the top layer
can be defined as
τ=F/A

(3.3)
Any layer at a distance x from the bottom layer will be subjected to a force Fx, which
is between zero and F. The area on which the force is applied stays the same.
Therefore the shear stress for this layer will be
τ
x=Fx /A (3.4)
Fx and Vx are both proportional to the distance of the layer from the bottom plate.
That means the greater the distance, the higher the velocity and the higher is the
shear force. The increase in shear stress is directly related to the increase in shear
rate. The two are governed by the equation
τ=ηg∙

(3.5)
where η is the constant of proportionality called the viscosity of the liquid. The
viscosity is the slope of the line when the shear stress is plotted versus shear rate.
 3.2  N ewtonian and Non-Newtonian
Mat
erials
In the above discussion, the shear stress was linearly proportional to the shear rate
with viscosity being the constant of proportionality, see Figure 3.3. In some fluids,
the relationship between the shear stress and the shear rate is not linear. The vis-
cosity is not a constant and is dependent on the shear rate or the time the fluid is
subjected to the shear. Such fluids are not non-Newtonian fluids. Based on the re-
sponse to shear, non-Newtonian fluids can be classified into two types, dilatant and
shear thinning fluids. In dilatant fluids, the viscosity increases with increasing
shear rate and in shear thinning fluids, the viscosity decreases with increasing
shear rates, see Figure 3.4(a). Based on the response to the time of shear at con-
stant shear rate, non-Newtonian fluids are classified into rheopectic and thixo-
tropic fluids (see Figure 3.4(b)). All plastics show shear thinning behavior.
Rheology is the science of the flow of non-Newtonian materials. All polymers are
non-Newtonian, specifically shear thinning, as the shear rate increases, the visco
-
sity dr
ops.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 74 (page 74)

50 3  Polymer Rheology
-
-
Figure 3.3 Shear stress versus shear rate for Newtonian and non-Newtonian liquids
Figure 3.4 Change in viscosity as a function of (a) shear rate and (b) time for Newtonian and
non-Newtonian liquids
 3.3  Viscosity in Polymer Melts
Polymer melts are non-Newtonian. Research has shown that the velocity profile,
which is the line that joins the velocities of each layer, is never a straight line as
shown in Figure 3.2. A typical velocity profile for a polymer melt, called fountain
flow, is shown in Figure 3.5. The parabolic velocity profile is a result of a pressure
driven flow through a closed channel. The drag from the channel walls slow the
material, resulting in a higher velocity in the center. At the flow front, this condi-
tion causes the faster flowing material in the center of the channel to “fountain” to
the slower flowing regions. Fountain flow conditions only exist at the flow front
and cannot occur behind the flow front. However, the velocity profile conditions
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 75 (page 75)

513.3 Viscosity in Polymer Melts
exist throughout the flow, at the flow front and behind the flow front., i. e., the
center is always flowing faster than the perimeter. Hot runners, where the channel
is already full, will not experience fountain flow, except when they are first filled.
Fountain flow will exist in the cavities and in cold runners. An incompletely filled
runner or a short shot will always exhibit their flow front velocity profiles as shown
in Figure 3.5.
Because the profile is not linear, the shear rate equation in Eq. 3.1 now needs to be
rewritten as
g∙ = (x/h)(dx/dt)

(3.6)
Where t is time, h is the thickness or diameter of the flow channel, and x is the
distance along the flow channel. The units do not change and are reciprocal sec-
onds or s
–1.
The relationship between viscosity and shear rate is described by various mathe-
matical models. The most popular model, the Power Law Viscosity Model proposed
by Ostwald and de Waele, is widely applicable to injection molding. This equation
accurately represents the shear thinning region found at the high shear rates in
injection molding. The power law viscosity model is given by the equation
η = mg∙
n–1 (3.7)
wher
e m is a constant called the consistency index and n is the power law index.
A representation of a typical graph of viscosity versus shear rate is shown in Fig-
ure 3.6 for a polyester. Note that the shear rates represented here are of the order
of those that are experienced in injection molding.
Wall
Wall
Figure 3.5 Velocity profile of plastic flow
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 76 (page 76)

52 3  Polymer Rheology
800
600
400
200
0
0 2000 4000 6000 8000
Apparent Shear Rate
App. Shear Viscosity (Pa-s)
Figure 3.6 Effect of shear rate on viscosity represented on the linear scale
For polymer melts subjected to very low shear rates, the viscosity is essentially
unchanged. There is very little or no effect of the shear rate. However, these shear
rates are not encountered in injection molding. This is the reason why there are
different viscosity models to represent viscosity.
Equation 3.7, η = mg∙
n–1, can be rewritten as
logη = logm + (n – 1)logg∙
(3.8)
This equation now becomes a linear equation and if a graph of log η versus log is
plotted, we get a straight line as shown in Figure 3.7. This is the typical graph that
is obtained from a melt rheometer test. The graph in Figure 3.7 is generated from
the same data used for the PBT graph in Figure 3.6. The slope of the line is (n – 1).
Polymer melts are shear thinning and therefore the viscosity drops, resulting in a
negative slope of the line. Therefore, the value of n is always less than 1 but greater
than zero.
In polymer melts, as the shear rate is applied, the molecules start to align them-
selves in the direction of flow, moving away from their equilibrium intertwined
states. Increasing shear rates stretch and align more and more molecules in the
direction of flow. This alignment facilitates the easy movement of the flow layers
past each other, thus reducing the resistance to flow or viscosity. At a certain point,
all the molecules become aligned in the flow direction and increasing the shear
rate further has little or no further effect on the viscosity.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 77 (page 77)

533.3 Viscosity in Polymer Melts
1000
100
10
1001 000
Apparent Shear Rate (1/s)
App. Shear Viscosity (Pa-s)
10000
PBT-4
Figure 3.7 Effect of shear rate on viscosity represented on the logarithmic scale
0
200
400
600
800
02 000 4000 6000 8000
Apparent Shear Rate (1/s)
App. Shear Viscosity (Pa-s)

Non-Newtonian
Tending towards
Newtonian
Figure 3.8 Effect of apparent shear rate (injection speed) on the viscosity of the polymer
For the sake of practical injection molding, we could consider the region of higher
shear rates as a Newtonian region where the viscosities become consistent. Since
the viscosities are a result of the fill speeds, the corresponding regions of fill
speeds are now treated as the consistent region. Injection speed is synonymous to
shear rate and an in-mold viscosity curve appears similar to the one shown in Fig-
ure 3.8. Shear rate can be calculated as the reciprocal of the fill time, where fill
time is the time the screw takes to travel from the set shot size to the holding phase
transfer position of the screw on the molding machine. Simply put, it is the time for
which the screw moves in the injection phase.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 78 (page 78)

54 3  Polymer Rheology
 3.4  Effect of Temperature on Viscosity
In the solid state the molecules have very little thermal energy and therefore are
almost immobile. Depending on the ambient temperature and the glass transition
temperature (T
g) of the polymer, the polymer can be either brittle or soft and tough.
The thermal regions are explained in Chapter 2. Below the T g, the plastic is very
brittle and is said to be in the glassy state. Above the T g the plastic is soft and is
said to be in the rubbery or viscoelastic state. Above the melting temperature (Tm),
for crystalline plastics, the plastic is in the melt form. In general, as the tempera-
ture is increased, the thermal energy reduces the weak intermolecular attraction
that holds the molecules together, making them more mobile. Amorphous poly-
mers continue to soften and crystalline polymers show a sharp melting point. In-
crease in temperature increases the mobility of the molecules, thereby reducing
the viscosity of the polymer. Temperature and viscosity are inversely related. Fig-
ure 3.9 shows the effect of temperature on the viscosity of the melt. It is also clear
that the effect of shear rate is higher than the effect of temperature.
Figure 3.9 Effect of temperature on the viscosity of the melt (Source: Sabic Innovative
Plas
tics)
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 79 (page 79)

553.5 Velocity and Shear Rate Profiles
In injection molding, it is common practice to increase the melt temperature to
make the plastic flow easier. However, Figure 3.9 demonstrates that increasing the
injection speed will have a greater effect on part fill. This advantage is discussed in
Chapter 7 and a procedure to generate the in-mold rheology curve is also discussed.
 3.5  Velocity and Shear Rate Profiles
The velocity profile shows the relative velocities of the different layers in the poly-
mer melt as it flows through a channel. The length of the arrows in the velocity
profile represents the velocity of each of the layers. The velocity at the wall is zero
and therefore the shear rates are very low near the wall. The velocity increases to-
wards the center of the channel, following a parabolic profile and it is highest at
the center. As discussed earlier, shear rate is the difference in the velocities of the
adjacent layers. In Figure 3.10, the difference in the velocities in the first two lay-
ers near the wall is very high compared to two layers near the center of the chan-
nel. Therefore, the shear rate is higher near the wall, compared to the center of the
channel. The shear rate profile, which is a derivative of the velocity profile, is plot-
ted below the velocity profile in Figure 3.10. These studies are relatively recent [1].
Wall
Wall
Velocity = 0
Velocity = max
Shear rate = 0
Shear rate = max
Shear rate profileCenter line
Velocity profileCenter Line
V
V
Figure 3.10 Velocity and shear rate profiles in polymer melts
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 80 (page 80)

56 3  Polymer Rheology
.8
.6
.4
.2
.0
0 1 2 0 5000 10000
0 500 1000 50 100 150 200 250
.8
.6
.4
.2
.0
.8
.6
.4
.2
.0
.8
.6
.4
.2
.0
Fig.A Fig. B
Fig. CFig.D
Figure 3.11 Outputs from a finite element, finite difference flow analysis program providing
information on the melt conditions through the cross-section of a cold runner; y-axis is
from the center line of the channel to the channel wall: (A) velocity; (B) shear rate; (C) melt
temperature; (D) viscosity [1]
Figure 3.11 [1] shows the outputs from a finite difference flow analysis program. It
shows the velocity, shear rate, melt temperature, and viscosity of the cross section
of the melt. The y-axis represents the direction perpendicular to flow.
 3.6  Application to Injection Molding
The direct effect of the shear rate distribution discussed above is visually evident
in injection molding, particularly in the filling pattern of multicavity molds. As the
plastic begins to flow in the runner, the shear layers are formed as shown in Figure
3.10. Since the melt flow is always laminar, these layers split and/or flow into the
various flow channels in laminas. Each of these laminas has their own characteris-
tic properties, such as shear rates and temperatures. The high shear laminas just
below the wall of the flow channel create a low viscosity region changing the velo
-
city of flo
w in some cavities and causing cavity-to-cavity flow imbalances. Some of
the typical and common characteristics of such flows and their effect on the parts
are described in the following.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 81 (page 81)

573.6 Application to Injection Molding
3.6.1Flow Imbalance in an 8-Cavity Mold
Consider an 8-cavity mold as shown in Figure 3.12. As the plastic flows through
the primary runner, the shear layers are developed.
If we disregard the frozen layer (in a cold runner mold), we can distinguish be-
tween two distinct layers. The outside layer is the high-shear layer and the inside
layer is the low-shear layer. In the diagram, the high shear layer is the shaded area.
Section A-A is the cross section of the primary runner and shows the two layers
concentric to each other. Since the flow through the mold is laminar, the variations
in shear, temperature, and viscosity across the runner proceed into the secondary
runner. The inner low-shear laminas hit the far wall of the secondary runner and
the high-shear laminas on the outer perimeter continue to flow along the near wall
of the branching secondary runner. The cross section shown in Section B-B illus-
trates this distribution of high- and low-sheared material in the branching second-
ary runner.
A - A
A
A
Primary Runner
High Shear Region
Low Shear Region
High Shear Region
B B
Secondary
Runner
Secondary
Runner
B - B
Figure 3.12 Split of different shear rate regions in an 8-cavity mold [2]
CA V 1 CA V 2
CA V 4CA V 3
Figure 3.13 Flow imbalance between the inside and outside cavities. The photo on the right is
an actual short shot of a polycarbonate material molded at optimal process conditions [3]
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 82 (page 82)

58 3  Polymer Rheology
The laminar flow continues through the secondary runner, the tertiary runner, and
then into the cavities. The result is that inside cavities (those close to the sprue)
are filled first, as they are fed by the hotter, high-sheared, lower viscosity material
developed earlier in the runner. This is shown in Figure 3.13. A visual proof of the
high-shear lamina is shown in Figure 3.14.
Here, a runner used in the molding of a PVC part clearly showed degradation
caused by the high shear. The black streak on the inside is the high-shear lamina
in the figure. Note that the burning/streaking of the material develops prior to the
actual corner. We point this out in particular, because shear induced imbalances
are sometime misrepresented as being caused by a sharp corner in a runner. Here,
the evidence dispels this theory as the runner is not only radiused (no sharp cor -
ners) but the burning begins before the corner.
Burn before the
radiused corner
Degraded
material flowing
into the parts
Figure 3.14 Visual evidence of the high-shear lamina [3]
The cavity-to-cavity imbalance described above is called a rheological imbalance.
The runner is said to be rheologically imbalanced despite the fact it is geometri-
cally balanced. When the distance from the sprue to the gate is the same for each
cavity, the mold is said to be geometrically balanced. This geometrical balance in a
runner is still commonly incorrectly referenced as a “naturally balanced” runner.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 83 (page 83)

593.6 Application to Injection Molding
3.6.2Racetrack Effect in a Part with Constant Thickness
The part shown in Figure 3.15 is made with a single-cavity mold, producing a
100
mm
×
2 mm t
hick flat part with a constant wall thickness. The shear effect on
viscosity can be seen in the flow pattern developed in this cavity. The high-sheared
low-viscosity material developed in the perimeter of the runner splits and concen-
trates along the perimeter of the flat disc, causing the race tracking effect. Note
that the photo in the right shows that the effect is significant enough to create a
gas trap, opposite the gate, in this flat part.
Figure 3.15 Racetrack effect causing a gas trap in a part with uniform thickness [3]
3.6.3Stress Build-Up in Molded Parts
The part shown in Figure 3.16 is made from a transparent material in a two-cavity
mold. The parts are packed out and examined with a polarizing lens after molding.
The build-up of stress can be seen on the inside of the parts. This is the area where
the hotter laminas flow, causing differential cooling and therefore stress.
Stress
Figure 3.16 Stress build-up observed under a polarizing lens [3]
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 84 (page 84)

60 3  Polymer Rheology
3.6.4Warpage Difference between Cavities
Figure 3.17 shows parts molded in a 4-cavity mold. Because the location of the hot
laminas in the cavities is different, two of the cavities are warped while the other
cavities are perfectly flat.
Warp in Cavities 2 & 3 No Warp in Cavities 1 & 4
Figure 3.17 Warpage differences between cavities from the same mold caused by a melt
imbalance [3]
 3.7  Sol ving Flow Imbalances Using
Melt Rotation Techniques
The solution for balancing the flow and creating rheologically balanced molds was
developed and patented by John Beaumont of Beaumont Technologies in Erie,
Pennsylvania (please note that the use of this technology requires a licensing
agreement from Beaumont Technologies Inc.) Beaumont’s varied methods of melt
management, commonly known as Melt

Flipper® technology, can be used in appli-
cations that include the rheological balance of mold and part filling, control of
intr
a-cavity filling, warpage, part property, and cosmetic manipulation. One of the
more common applications is shown for an 8-cavity mold in Figure 3.18(a). This is
a conventional H-shaped runner with eight cavities. The cross sections of the flows
are also shown. In the primary runner, the high shear and the low shear areas are
concentric to each other. As the flow splits at the secondary runner, the high-
sheared material stays on the inside. At the split at the tertiary runner, the high-
shear material ends up in the inside cavities, causing these cavities to fill before
the outside cavities. Inside and outside cavities exhibit different melt conditions.
The result is that the parts formed in these two cavity groups will be different in
size, weight, and properties.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 85 (page 85)

613.7 Solving Flow Imbalances Using Melt Rotation Techniques
Figure 3.18 Before and after examples using the melt rotation technology [3]
Beaumont’s patented melt rotations technologies use a variety of methods to
manag
e the position of the high- and low-sheared laminates to achieve the desired
balancing effects. In this 8-cavity example, the melt would be “flipped” or rotated,
90 degrees prior to entering the tertiary runner to the position shown in Figure
3.18(b). This rotation is commonly created at the intersection of the primary and
the secondary runner. When this melt exits the secondary runner, the high-shear
area is now on the top rather than on the inside, as is shown in Figure 3.18(a) with-
out the flip. When this reoriented material enters the split of the tertiary runner,
the high- and low-sheared melt splits up evenly into the two branches and each of
the cavities receives melt with equal amounts of high-shear and low-shear mate-
rial. This creates a fill and rheological balance between all cavities in the mold.
In the above case, the melt was rotated at one location, the intersection of the pri-
mary and the secondary runner. In case of a 16-cavity mold, the concept can be
extended and the melt will need to be rotated at two locations for balancing all
sixteen cavities. In addition, by applying similar melt rotation techniques, some of
the other problems in the parts can be solved. An excellent treatise on this subject
with detailed explanation is provided in [1]. Some of the ‘before and after’ exam-
ples are shown in Figure 3.18. Figure 3.18(a) shows the filling pattern resulting in
a conventional geometrically balanced runner. Filling is not only unbalanced from
cavity to cavity, but each side of the Flow #1 cavities (inside four cavities) is differ-
ent. Figure 3.18(b) shows the filling pattern after melt rotation was applied. Note
that a balanced filling results not only between cavities but also within cavities.
Not only will all eight parts be almost similar, but the use of pressure transducers
(or thermocouples) for controlling and monitoring the process can be significantly
improved. Figure 3.18(c) shows the filling pattern resulting in a simple flat disk,
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 86 (page 86)

62 3  Polymer Rheology
where the high-sheared material from the runner is causing a race track effect
around the perimeter. Figure 3.18(d) is the same disk, except the melt has been
conditioned using Beaumont’s multi-axis rotation technology (MAX
TM technology).
Here, the majority of the high-sheared laminates have been repositioned to flow
across the center region of the cavity.
Figure 3.19 shows the temperature distribution before and after the use of melt
rotation technology. The photos of these parts were taken with an infrared camera
immediately after molding. The left hand side part is the inside cavity fed by the
high-sheared lamina. In the conventional runner there is clear evidence that the
inside cavity is fed with hotter material (white). Note that this evidence of thermal
variation exists even after the parts were partially cooled in the mold.
Conventional Runner MeltFlipper® Runner
Figure 3.19 Temperature distribution before and after using melt rotation technologies [3]
 3.8  Fountain Flow
In thermoplastic injection molding the mold temperature is set lower than the melt
temperature because the melt needs to cool down to at least the ejection tempera-
ture. To the touch of the human hand, the mold may be hot but the mold is always
considered to be cold. For example, the mold temperature for a polyetherimide
(PEI) material is in the range of around 165 to 180 °C . Personnel are required to
wear safety gloves when working with these molds. In the following sections, a
cold mold therefore does not mean the mold is cold to human touch, but that it is
colder than the plastic.
Plastic flow is laminar. Refer to Figure 3.20. When the plastic injection starts and
the plastic first touches the cold mold, it freezes at the walls of the mold. The plas-
tic that is injected behind this melt pushes its way through the center, moves ahead
of the frozen layer, and ends up against the mold wall just ahead of it. The result is
an inside-out flow, where the flow front looks similar to a water fountain, and
therefore is called fountain flow.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 87 (page 87)

633.8 Fountain Flow
Mold Steel
Start of Injection
Progress of Melt Flow
Figure 3.20 Depiction of fountain flow and the formation of the frozen layer with melt
pr
ogression
If we divide the plastic melt that is ready to be injected into the mold into various
sections, it is interesting to see where each of these sections end up. The plastic
that is in the nozzle tip forms the skin of the sprue whereas the center of the sprue
contains the plastic from the very back of the melt that was in front of the check
ring. Refer to Figure 3.21, which shows a schematic cross section a mold with the
progression of the melt marked by the numbers. For example, in the barrel, Sec-
tion 1 is in the nozzle tip. When this gets injected into the mold, it will end up on
the skin of the part that is closest to the machine nozzle. Section 2 will get pushed
further and will form the skin on the part that is ahead of Section 1.
1 2 3 4 5 6 7 8 9 10
1
1
7 6 5 4 3 2
7 6 5 4 3 2
8
8
8 9 9 9 10 10 10
Molten Plastic in Barrel
Numbers indicate Sections 1 to 10Location of where the plastic from
each section of the barrel end up
after injection into a mold cavity
Molded Part
(Schematic representation)
Figure 3.21 Relationship between position of the molecules in the barrel and their position in
the final molded part
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 88 (page 88)

64 3  Polymer Rheology
Fountain flow can be seen during color changes. If a molder is molding parts in
blue and then switches to yellow, and then the yellow shows up at the end of fill,
and the blue shows up in the sprue or the gate area of the part. Refer to Figure
3.22, which shows the molded part and the runner at a color change from a clear
plastic to a yellow plastic. The skin of the sprue and the part are both formed with
clear plastic and the inside of the part is formed with the yellow plastic. The cold
slug well at the end of the sprue is also filled with clear plastic since that is the
first plastic that enters the mold. The gate area of the part is filled with the yellow
plastic where as the end of fill and the skin of the part are filled with the clear
plastic.
Figure 3.22 Evidence of fountain flow during color change
Understanding fountain flow can help in troubleshooting defects in molded parts.
If a cosmetic defect is always located in the same spot on the part, one could back-
track the possible location of the melt to figure out the source of the problem. For
example, a molder had a part that failed in one particular section. The problem was
tracked down to a long nozzle body with the thermocouple at one end and the
heater band at the other. The plastic was getting degraded and during the injection
ended up in the section of the failure. Changing the nozzle body to a shorter one
helped solve the problem.
The concept of fountain flow is used in the technique of co-injection molding. Refer
to Figure 3.23. In the process of co-injection, parts are molded with one material
forming the skin and the second material forming the core of the part. The skin
material is selected for cosmetic reasons and/or other reasons such as environ-
mental protection. The core material is used as a filler to drop the cost or to use as
regrind material or just as a foaming matrix to reduce weight and prevent sink. In
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 89 (page 89)

653.9 Effect of Fountain Flow on Crystallinity, Molecular Orientation, and Fiber Or ientation
this technique, the skin plastic is injected first immediately followed by the core
plastic. When the required amount of skin plastic is injected, the mold is only
par
tially filled, but since the core material immediately follows, it pushes the melt
of the skin plastic further to the walls, and the core plastic fills the part from the
inside.
Skin Material Core Material
First
Injection
Second
Injection
Molten Skin gets
pushed by Core
Material
Continued
Injection
Mold Fill
Complete
Figure 3.23 Co-injection Molding; an application of fountain flow
 3.9  Effect of F ountain Flow on Crystallinity,
Molecular Orientation, and Fiber
Or
ientation
Consider the flow of a crystalline material into a mold. During the formation of the
skin, the plastic touches the cold mold and forms the skin almost instantaneously.
Therefore, the molecules in the skin layer have no time nor the energy to crystal-
lize completely. The layers underneath this skin are insulated from the mold
sur
face and have a little more time before they cool down to a no flow condition.
Therefore, the layers progressively have more time and energy to complete the
crystallization process. If a cross section of a molded product is examined for crys-
tallinity, it can be found that the center of the part has the most crystallinity and
that the skin has the least.
For these same reasons mentioned in the previous paragraph, and because the
skin layers freeze off almost immediately, the molecules and the fibers that are
oriented in the direction of the plastic flow freeze off in the same orientation. With
the progressive layers, the heat lets the molecules and fibers relax, and reach an
equilibrium position. Therefore, the molecules on the surface have the most orien-
tation but the ones on the inside have the least orientation. Refer to Figure 3.24.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 90 (page 90)

66 3  Polymer Rheology
Surface:
 More Orientation
 Less Crystallinity
Inside:
 Less Orientation
 More Crystallinity
SECTION A-A
Gate
A
A
Figure 3.24 Molecular orientation, fiber orientation, and crystallinity in injection molded parts
 3.10  Characterization of Polymer Viscosity
Polymers are found in a variety of applications ranging from their use in a solution
(as in the case of paints) to being processed as melts. In this range of applications,
the shear rates range from very low to very high. There is a need to employ various
techniques to characterize the viscosity for a couple of reasons. First, there is no
one viscosity model that fits the wide range of shear rates. A low shear model will
not fit the viscosity-shear rate relationship at a high shear rate and vice versa.
Second, t
he presence of another medium, such as a solvent or a plasticizer, alters
the models and the properties of these mediums have characteristic effects on the
viscosity. Based on these different characterization methods, various viscosities
are also defined. Solution rheology is the study of polymers in solvents and melt
rheology is the study of rheology of melts. Of particular interest related to injection
molding is melt rheology at high shear rates. This is done with the help of the
capillary rheometer. The shear rates that are observed in the machine nozzle, sprue,
runner, gates, and the part can all be duplicated in this rheometer. Typical shear
rates can range from 100 s
–1 to almost 100,000 s –1, with the shear rates in the
gates potentially going into the millions per second. Figure 3.24 shows a schematic
of a basic rheometer. It consists of a barrel and plunger arrangement. On the bot-
tom end of the barrel is a die. The barrel is heated to a desired temperature based
on the material being tested and is then filled with the plastic to be tested. Once
molten, the plunger travels at various shear rates and the plastic is extruded
through the die. The geometry of the die is very important and is used in the calcu-
lations of the shear rates. The plastic is extruded at various shear rates and the
viscosity is measured. Typically, the viscosity is measured at three different tem-
peratures. These data are is sometimes made available by the material suppliers
for mold design and flow simulation purposes.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 91 (page 91)

673.11 References
Another common test is called the melt flow test. This test is carried out using a melt
flow indexer that has a basic arrangement similar to the capillary rheometer. The
difference is that this is a low shear test, with shear rates not commonly seen in
injection molding. The adv
antage of simplicity and a general correlation with the
high shear viscosity makes this popular. The output number is called the melt flow
index (MFI) or the melt flow rate (MFR). The melt flow indexer is similar to the cap-
illary rheometer, except that instead of the load cell, a known weight is placed on the
plunger. The arrangement consists of a plunger, barrel, and a die. The barrel is set to
a desired temperature, then loaded with the plastic. Once a predetermined time has
lapsed, the weight is placed on top of the plunger. The weight forces the plastic to be
extruded. The weight of the plastic extruded in 10 minutes (in grams) is called the
MFI or simply the melt index of the plastic. For example, if 25
g of plas
tic was
e
xtruded from the die, the MFI is 25. In the industry, it is common to say that the
material is a 25 melt material. The units for MFI are always grams
r
egardless of the
measurement system. The MFI number is commonly found on material certifica-
tions as an incoming quality control parameter. A number of companies perform
their own test to confirm these numbers and to keep a log of the incoming lots of
material. This is an easy and inexpensive way of quality control, though care must
be taken with filled compounds. In this case, the fillers do not melt and can cause an
obstruction to flow and bias the results making them inconsistent.
The procedures for the capillary rheometer and the melt flow indexer tests are both
defined by ASTM or other test organizations. They also define the various temper-
atures, weights, times, and other test conditions that may vary based on the type of
plastic being tested.
 3.11  References
[1] Beaumont, J., Runner and Gating Design Handbook (2007) Hanser, Munich
[2]
Beaumont,
J. et al., Solving Mold Filling Imbalances in Multicavity Injection Molds, Journal of
Injection Molding T
echnology (June 1998) Vol 2, No. 2, p. 47
[3]
Beaumont Inc.,
Technical Presentation (2009)
Suggested Reading
Beaumont, J., Nagel, R., and Sherman, R., Successful Injection Molding (2002), Hanser Publishers,
Munic
h
Aklonis, J. J., Introduction to Polymer Viscoelasticity (1983) Wiley Interscience, NY
Billmeyer, F. W., Textbook of Polymer Science (1984) Wiley Interscience, NY
Cogswell, F., Polymer Melt Rheology (1981) John Wiley, NY
Dealy, J. and Wissbun, K., Melt Rheology and its Role in Plastic Processing Theory and Applications (1990)
Van Nostrand Reinhold, NY
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 92 (page 92)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 93 (page 93)

Plastic Drying
Most plastics tend to absorb moisture when exposed to humidity. This is true with
plastic in any form, whether in pellet form before processing or in a finished prod-
uct, such as an injection molded product. Such plastics are called hygroscopic or
hydrophilic plastics. Plastics that do not absorb moisture are called hydrophobic
plastics. Nylons are common examples of hygroscopic plastics. Nylon parts will
absorb moisture and alter the dimensions of the molded part, depending on the
humidity. As a nylon part absorbs moisture, it can swell in physical size, causing
dimensions to change beyond the required specification limits. Although moisture
absorption is inevitable in the molded part, excess moisture should be removed
from the plastic resin to an acceptable level before molding in order to produce an
acceptable part. Every plastic has an acceptable maximum moisture level above
which melt processing problems can occur. Moisture levels must be below this
recommended value before processing. A list of maximum moisture levels for vari-
ous materials is provided in Table 4.1. The numbers mentioned are for nonfilled
plastics. Most fillers are nonhygroscopic and therefore do not absorb any moisture.
Consider as an example nonfilled nylon. Nylons typically need to have a moisture
level of less than 0.20 % before they are processed. If a particular nylon resin is
50 % glass filled, then the amount of nylon is 50 %. Therefore, the amount of allow-
able moisture will also be 50 % of 0.20 or 0.10 %. The amount of filler must always
be taken into consideration when conducting a moisture test. Most material manu-
facturers overlook this when providing the datasheets.
4
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 94 (page 94)

70 4  Plastic Drying
Table 4.1 Unfilled Materials and the Recommended Maximum Moisture (Courtesy: IDES.com)
Long name Short name Suggested maximum moisture ( %)
Acetal (POM) copolymer Acetal copolymer 0.15–0.20
Acetal (POM) Homopolymer Acetal Homopolymer 0.2
Acrylic, polymethyl methacrylate PMMA 0.097–0.10
Acrylonitrile butadiene styrene ABS 0.010–0.15
Polyamide 6 Nylon 6 0.095–0.20
Polyamide 66 Nylon 66 0.15–0.20
Polyamide 66/6 copolymer Nylon 66/6 0.099–0.20
Polyphthalamide PPA 0.045–0.15
Polycarbonate PC 0.019–0.020
Polybutylene terephthalate PBT 0.020–0.043
Polyethylene terephthalate PET 0.0030–0.20
Polyether imide PEI 0.020–0.021
Polyethylene, high density HDPE NA
Polyethylene, low density LDPE NA
Polyethylene, linear low density LLDPE NA
Polyphenylene sulfide PPS 0.015–0.20
Polypropylene homopolymer PP homopolymer 0.050–0.20
Polystyrene, general purpose PS (GPPS) 0.02
Polystyrene, high impact HIPS 0.1
Polyvinyl chloride PVC NA
Styrene acrylonitrile SAN 0.020–0.20
In materials such as nylon, moisture plays an extremely important role during
processing by acting as a viscosity regulator for the melt. Therefore, there is also a
minimum required level of moisture for such materials. This topic will be dis-
cussed further later on in this chapter. Drying plastic resins before processing is a
critical step. Plastic resins that are hydroscopic must be subjected to elevated dry-
ing temperatures for a specified time, in order to effectively remove excess mois-
ture. However, excessive drying of the plastic resin, beyond the manufacturer’s
recommended times and temperatures, can also create problems. Until recently,
this has been an overlooked condition although it can have a very negative poten-
tial impact on the mechanical properties and appearance of the finished molded
part. Exposure of plastic resins to drying temperatures above the manufacturer’s
recommended levels for excessive periods of time is typically referred to as “over
-
dr
ying.”
If the process of drying is not done correctly, it can result in losses in production in
the form of scrap parts and also lost production time that cannot be recovered.
Drying is accomplished with the help of dryers in the molding facility. Some plas-
tics come pre-packaged in vacuum sealed bags and do not need to be dried as long
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 95 (page 95)

714.1 Problems in Melt Processing Related to the Presence of Moisture
as they are processed immediately after being removed from their packaging. Any
opened and unused portion must be dried before it is processed, if later stored in
an open environment.
 4.1  Pr oblems in Melt Processing Related
to the Presence of Moisture
There are several problems that can result due to the presence of moisture during
the melt processing of the plastic.
4.1.1Degradation of Plastic
In the presence of moisture, the plastic can degrade in the injection molding bar -
rel. A chemical reaction called hydrolytic degradation can take place at molding
temperatures and attack the long-chain molecules. The water molecule acts as a
catalyst and initiates the degradation. The degradation can itself produce more
water and increase the rate of the degradation reaction. This breakdown of the
molecules causes the loss of properties in the final product. There are two types of
hydrolytic degradations that can occur: If the chain ends are broken, the loss in
molecular weight is not significant and the effect on the end product is negligible.
This type of degradation is called end-chain degradation. In random degradation,
the polymer molecules are broken at random bonds along the molecule’s length
and this can cause a significant drop in molecular weight, leading to a decrease in
properties. Typically, parts molded from degraded materials tend to become brittle
and show a reduction in their mechanical properties. There can also be a loss in
appearance ranging from a shiny finish to a dull finish. Other surface defects, such
as splay, are also common. Hydrolytic degradation is a common problem with
condensation
polymers, such as polyesters, nylons, polycarbonates, and polyure-
thanes.
4.1.2Presence of Surface Defects
A number of surface defects can be attributed to the presence of moisture during
processing.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 96 (page 96)

72 4  Plastic Drying
Splay
Any moisture that gets carried by the melt during injection of the melt into the
mold stream gets released and then tends to form a film between the melt and the
mold surface. The presence of this film prevents the melt from coming in contact
with the mold surface and picking up the texture of the cavity surfaces. The film
creates a smooth surface and once cooled down, the plastic shows shiny streaks in
this area, see Figure 4.1. This phenomenon is called splay or sliver streaks.
Figure 4.1 Splay on the surface of a part
Bubbles
If the moisture stays inside the melt and does not come out to the surface, internal
defects, such as voids or bubbles, can form in the part. In some cases, if the bubble
is too close to the surface, the moisture inside is still hot and pressurized when the
part is ejected from the mold. This can show up as an external defect such as a
bump or bubble on the part. These defects can either be microscopic or in some
cases show up as large deformations common in large and thick parts. Figure 4.2
shows internal voids and external defects due to excessive moisture.
Figure 4.2 Internal voids and external defects on a part due to excessive moisture
Burn Marks
High injection speeds cause the plastic to be subjected to high shear rates. At these
shear rates and in the presence of moisture some plastics can undergo degradation
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 97 (page 97)

734.1 Problems in Melt Processing Related to the Presence of Moisture
and burning of the molecules. This can show up as dark streaks or discoloration in
the part. Sometimes, the burning can be seen at the end of fill. Vents are designed to
help remove the displaced air in the cavity and runner system as the plastic fills the
mold during the mold filling process. If moisture is present in the melt, the plastic
can degrade, which causes an excess amount of gas that needs to be evacuated from
the mold cavity. Once the moisture vapor gets to the front of the melt stream, it does
not mix with the melt and always stays in front of the melt stream. If sufficient vent-
ing is not provided to allow the moisture vapor or gas to escape, it will get trapped
and compressed under the high injection, pack, and hold pressures, resulting in a
diesel effect that causes burning of the plastic. This burning can be seen as a black
or a white mark at the end of fill location, depending on the type of plastic.
Plugging up of the Vents
The excessive moisture or the volatiles from the degraded polymer and its addi-
tives can overload the venting system of the mold. This degradation generates
by-products that are low-molecular weight compounds. These compounds begin to
collect in the vents, plugging them up. As production continues, the part quality
starts deteriorating because of reduced venting capacity. Burn marks on the parts
near the end of fill are common and frequent when this occurs. Cleaning of the
vents is required to eliminate the burn marks. Figure 4.3 shows residue built up on
the mold surface.
Dimensional Variation
Plugging of the vents can cause dimensional changes in the part. Part dimensions
are directly related to plastic pressure in the cavity. Therefore, to obtain consistent
quality, the cavity pressure must be consistent during every injection molding
cy
cle. However, if the vents are clogged, the air and gasses cannot escape and the
internal pressure of the cavity increases, producing a part of varying dimensions.
Parts with tight tolerances can easily drift out of specification limits.
Figure 4.3 Residue built up on the secondary vents
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 98 (page 98)

74 4  Plastic Drying
Loss in Properties at the Weld Line
When resins are not properly dried, moisture will be present at the flow front;
when two flow fronts meet, the moisture interferes and does not allow weld
strength to develop to its full potential. This causes reduced weld line strength.
Sometimes the weld line is also more noticeable in such cases. This loss in weld
line strength can also be a result of insufficient venting due to plugged vents as
described earlier.
Nozzle Drool
This is a common phenomenon in crystalline plastics such as nylons. Under nor -
mal circumstances, plastic does not leak from the nozzle tip after the screw recov-
ers and fills the barrel with resin. There are two main factors that prevent nozzle
drool: First, at the end of the screw recovery process the screw is sucked back
without rotation for a short distance. This reduces the internal plastic pressure and
gets the molten plastic away from the nozzle tip. Second, the tip is controlled at a
temperature that keeps the viscosity of the plastic high enough to prevent it from
flowing out of the nozzle but low enough to allow plastic flow through the nozzle at
the start of the next injection cycle. This control is extremely important and the
presence of any moisture in the plastic can reduce the viscosity to an extent that
the plastic will continually drool out of the nozzle tip. No amount of reduction of
nozzle temperature or increase in suck-back can help because the plastic flow rate
is high, preventing sufficient time for the plastic to cool down through the short
nozzle tip. Drying of these resins to control the drool is therefore important. Since
crystalline plastics have a narrow processing range, they tend to have lower visco
-
sities com
pared to amorphous plastics. Drying of such resins to control the drool
becomes important. When the material is first loaded into the dryer and is stag-
nant in the dryer for the required amount of time, the material near the outlet of
the dryer is usually not exposed to the dry air. This is due to the design of the
hopper where the cone that supplies the dry air sits above a certain level. Only
plastic that is above this cone is subjected to the dry air and gets dried. It is advis-
able to drain out the plastic until dry plastic is encountered and then start the
molding. In some cases, when the moisture content is very high, it is not uncom-
mon to see sputtering of the melt out of the nozzle. Once the molding process is
started, materiel is continuously flowing from the top to the bottom of the hopper
and dry material is constantly supplied to the molding machine.
Inconsistency in Shot Control
The presence of moisture can mask the true volume of the plastic during the shot
build up and therefore cause a reduction in the amount of the required plastic.
Alt
hough the screw will always reach the shot size or build the required volume for
injection, it may not always be equal to the volume of the shot that is essential to
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 99 (page 99)

754.2 Hygroscopic Polymers
make a good quality part. Every shot will therefore be of a different weight, causing
inconsistency from shot to shot.
Examples of hygroscopic materials that do not degrade in the presence of moisture
are ABS, SAN, and acrylics. Nylons and polyesters are examples of materials that
will degrade in the presence of moisture. Examples of nonhygroscopic materials
are polyethylenes, polypropylenes, and polystyrenes. These materials do not ab-
sorb moisture; however, in humid environments moisture can settle on the surface
of the un-molded pellet, resulting in cosmetic defects, such as splay if the material
is not first dried to remove the surface moisture.
 4.2  Hygroscopic Polymers
Polymers that absorb moisture are called hygroscopic. Whether a polymer absorbs
moisture depends on its chemical structure, see Figure 4.4. The water molecule
shown here is made up of two atoms of hydrogen and one atom of oxygen. Because
the two hydrogen atoms and the oxygen atom tend to share electrons, the hydrogen
atoms are usually on one side of the molecule, which results in the molecule being
positively charged on one side and negatively charged on the other. A molecule
with this kind of charge distribution is called a polar molecule.
Negative charge
Hydrogen atom
Polar molecule
Hydrogen atom
Oxygen atom
Figure 4.4 Chemical structure of the water molecule
Similar to water, certain groups on the main chain of a polymer can also form polar
groups. For example, the carbonyl group (–C=O–) found in polyamides and poly
-
es
ters is a polar group (see Figure 4.5). These polar groups on the polymer chains
attract the polar water molecules like magnets to form weak secondary bonds re-
sulting in the hygroscopic nature of the polymer (Figure 4.6). These secondary
bonds are also called hydrogen bonds.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 100 (page 100)

76 4  Plastic Drying
Hydroxyl group
Carbonyl group
Carboxyl group
Amines & Amides
Figure 4.5 Examples of polar groups
Some polymers, for example polyethylenes, are polymerized from nonpolar mono-
mers such as ethanes. In an ethane molecule, the charges are balanced around the
carbon atoms and hence the polymer is nonpolar. The polar water molecule is
therefore not attracted to the nonpolar polyethylene molecule. Polyethylene is
therefore nonhygroscopic (see Figure 4.7).
Polar water molecules
Hydrogen bond
Polar groups on
polymer molecule
Figure 4.6 Polar water molecules forming hydrogen bonds with polar groups on the polymer
molecule making the polymer hygroscopic
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 101 (page 101)

774.3 Drying of Plastics
Polar water molecules
Non polar groups on
polymer molecule
Figure 4.7 Absence of hydrogen bonding between water molecules and polymers with non -
polar g
roups making the polymer nonhygroscopic
 4.3  Drying of Plastics
There are some important considerations that need to be taken into account for
effective plastic drying before the melt processing stage.
4.3.1Drying Temperatures and Times
The nature of each polar group for every plastic is different and the strength of the
bond between the water molecule and the plastic varies. For example, in polyure-
thanes the bond strength is very high compared to the bond strength in ABS. For
this reason, the drying times and temperatures for individual plastics are different.
Depending on the specific grade, polyurethane is typically dried 4 to 6 hours at
132 °C (270 °F), whereas an ABS needs to be dried for 2 to 4 hours at around 75 °C
(165 °F). The range in drying times is due to the fact that initial moisture content
can vary depending on the humidity the polymer material is exposed to. If mois-
ture content is higher, the drying time required to remove the moisture will be
longer, while the rate per unit time of moisture removal stays the same. Only a
given amount of moisture can leave the plastic in a given amount of time. The size
and the shape of the pellet can also affect the drying times. The drying tempera-
tures and times for some common plastics are listed in Table 4.2. Note that some of
these materials may not be injection molding materials.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 102 (page 102)

78 4  Plastic Drying
With some plastics, various combinations of drying times and temperatures can be
used to dry the material. For example, polyphthalamide (PPA) can be dried at 79 °C
(175 °F) for 8 hours or at 212 °C (250 °F) for 2 hours. The choice of recommended
combination depends on the optimal residence time of the plastic in the dryer.
Sometimes the dryers can be large compared to the material used per hour. Care
must be taken because certain resins can be very sensitive to higher drying tem-
peratures, especially if subjected to longer times in the dryer than suggested by
the manufacturer. Prolonged drying times can harm the plastic. In some cases
discoloration can be seen in the plastic pellets. It is also possible that the plastic
pellets may soften and stick together in the dryer. The pellets affected the most are
those near the exit, or bottom, of the hopper, which take the weight of the pellets
above them, causing bridging and making the situation worse. Higher tempera-
tures can also lead to the loss of the low molecular weight additives in the base
polymer.
Table 4.2 Drying Temperatures and Times for Common plastics (Courtesy: IDES.com)
Name Drying temp (°C) Drying time (h)
ABS 175–190 2.0–4.0
ACETAL HOMOPOLYMER 175–195 2.0–4.0
ACRYLIC (PMMA) 180 3.0–6.0
ASA 180–190 2.0–4.0
NYLON 6 160–180 2.0–4.0
NYLON 66 175 2.0–4.0
PBT 250–280 3.0–4.0
PC 250 3.0–4.0
PEEK 176 3
PEI 300 4.0–6.0
PLA 212 4
PPS 275 3.0–6.0
PS-GPPS 180 2.0–4.0
PS-HIPS 160–180 2.0–4.0
PSU 275 4
PUR N/A N/A
PVC 150 2.0–4.0
PVDF 302 1
SAN 160–180 2.0–4.0
SPS 176 2.0–4.0
In case of both hygroscopic and nonhygroscopic polymers, there can be water
condensation
on the pellet surface. If the pellet is transported from a relatively
cold environment, such as a silo on the outside of the building, into a warmer and
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 103 (page 103)

794.3 Drying of Plastics
possibly more humid molding environment, water can condense on the surface of
the pellets. This is similar to the water condensation we see on the outside of the
glass of a cold drink on humid days. Condensation can also occur at the feed throat
of the molding machine which is typically kept cool by cold water circulation in
order to avoid bridging at the feed throat. If the area is not cooled, the plastic that
is
s
tationary between the end of screw recovery and before the mold opens melts
to form a solid mass and prevents the plastic from being conveyed into the molding
barrel. Nonhygroscopic materials are therefore surface dried at low temperatures
to remove this moisture before processing. Exposing the plastic to room tempera-
ture or low temperature dry air for a short period of time is sufficient to dry off the
moisture. The drying time can be as low as half an hour on low humidity days.
Additives can also be hygroscopic in nature. For example, certain calcium-based
fillers can absorb moisture. Any plastics filled with these compounds must there-
fore be dried before processing regardless whether the base plastic is hygroscopic
or not.
4.3.2Relative Humidity and Dew Point
To extract the moisture out of the plastic, the air used for drying should be as dry
as possible. When the plastic with moisture is exposed to the dry air, the system is
looking to achieve equilibrium and therefore the moisture is continually extracted.
The dryness of the air can be expressed with the help of two terms: the relative
humidity and the dew point. Relative humidity is the percentage of moisture the
sample of air holds compared to the amount of moisture it could hold when it is
saturated. The saturation level changes with temperature. The lower the tempera-
ture, the lower is the maximum amount of moisture it can hold.
Dew point indicates the amount of moisture in the sample of air. The higher the
dew point, the higher is the amount of moisture in the air. The dew point is defined
as the temperature to which the given air sample will have to cool in order to reach
100 % relative humidity or complete saturation. Therefore, a lower dew point indi-
cates a lower amount of moisture in the air. A temperature of –40 °C (–40 °F)
equates to very low amount of moisture (less then 0.4 %) in the sample of the air.
This temperature is therefore taken as the target dew point temperature to be
achieved for the air that is supplied to the dryers.
Let us put this into perspective by considering an example. The dryer temperature
is set to 100 °C. This means that the air being supplied to the dryer is at 100 °C.
At this temperature, the air may still contain moisture, depending on its relative
humidity. This moisture will prevent the drying of the plastic to the required
le
vels. To reduce this moisture, the air must be dried. This is usually done by using
desiccant beds that absorb the moisture from the air as it is passed through the
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 104 (page 104)

80 4  Plastic Drying
desiccant. As the amount of moisture in the air is reduced, the temperature at
which it will condense, or its dew point, also reduces. Lower dew point tempera-
tures indicate that the amount of moisture being supplied to the dryer is also lower.
Therefore, measuring the dew point will indicate the dryness of the air. If the dew
point is around –40 °C, the quality of the air is acceptable to dry the plastic. The
final moisture level in the air is a result of the temperature, relative humidity, and
the dew point of the air.
4.3.3Air Flow Rate
The hopper used to dry the material is supplied with air that has a low dew point,
is dry, and has been heated to the recommended temperature. As the plastic dries,
the moisture migrates to the surface and should be continuously carried out of the
system. This requires a sufficient amount of flow of the air through the system.
Therefore the flow rate of the air through the system is important.
 4.4  Equipment for Drying Plastics
Several types of dryers are available for drying plastics. The classification is based
on the technology or other features, such as location of the dryer.
4.4.1Oven Dryers
During the early years of molding, when processors realized the need for drying,
ovens similar to baking ovens were used. The plastic was spread out on large trays
and put into the ovens to dry. The large trays helped to spread out the plastic and
increased the area of exposure to the heat. The plastic would not dry evenly if the
layer of plastic was too thick. Handling of the hot trays and transporting the mate-
rial to the hopper of the machine was not easy and often required two people.
Smaller ovens are still in use in some R & D facilities and production facilities that
process small amounts of material. One of the additions to these ovens is the use of
a vacuum pump. The vacuum decreases the boiling point of any liquids and at the
same time facilitates the removal of the moisture from the chamber speeding the
drying process.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 105 (page 105)

814.4 Equipment for Drying Plastics
4.4.2Hot Air Dryers
Hot air dryers supply hot air to the plastic at the bottom of the dryer and as the air
passes through the plastic, it picks up the moisture from the surface of the pellets
and transports it out of the system. The heat also helps to drive the moisture to the
surface of the pellet. The supplied air is picked up from the atmosphere, heated
and pumped into the dryer. These systems are best suited for surface drying of
nonhygroscopic materials such as olefins or for materials that do not require mois-
ture levels to be very low before processing.
4.4.3Desiccant Dryers
These dryers are similar to hot air dryers except for the fact that the air first passes
over a desiccant bed that adsorbs almost all of the moisture from the air. This dry
air is then heated and supplied to the hopper. Since the relative humidity is now
low, the air can pick up more of the moisture from the plastic, helping to achieve
the lower moisture levels desired for materials such as nylons. As the moisture is
adsorbed by the desiccant bed, the desiccant will eventually become saturated
with the absorbed moisture. As the saturation level of the desiccant increases, its
ability to absorb moisture decreases, making the drying process less efficient. To
correct this, there is a regeneration cycle during which the desiccant is dried and
then recycled back into the system. Desiccant dryers are widely used in most mod-
ern-day facilities because of their versatility.
4.4.4Classifications Based on the Location of the Dryer
Dryers can be located next to the molding machine and a hose can be used to sup-
ply dried material from the dryer to the molding machine. These are conventional
dryers that are most commonly used in small to medium size companies in which
a variety of materials are processed and mold changes are frequent. The dryers are
mobile and can be moved from one machine to another. In companies processing a
mix of hygroscopic and nonhygroscopic materials it is not required to invest in the
same number of dryers as the number of molding machines. The dryers can be
moved where needed. Hopper dryers on the other hand are dryers that are mounted
directly on the molding machine such that the dry material is fed straight into the
feed throat of the molding machine. This is a good solution for extremely hygro-
scopic materials such as some polyurethanes that can pick up moisture during the
transportation from the conventional dryer to the molding machine through the
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 106 (page 106)

82 4  Plastic Drying
transport hose. The disadvantage is that these dryers are attached directly to the
molding machine and are not easily moved to different molding machines on short
notice. This type of dryer, for all practical purposes, is considered dedicated to the
machine.
Central dryers are very large dryers that can be installed in companies that pro-
cess large quantities of the same material. The material is dried at a central loca-
tion and is then transported to the molding machine for processing.
 4.5  De termination of the Amount
of

Moisture
It is critical to be able to accurately determine the amount of moisture in the plas-
tic to be melt processed. Therefore, an accurate measurement system is necessary.
There are various direct and indirect measurement methods, most of which suffer
from a basic problem. When trying to extract the moisture for analysis and meas-
urement, other volatiles, additives, and residual polymerization compounds in-
cluding monomers are released. These can therefore mask the actual amount of
moisture in the plastic and give false readings. There are ways to prevent this but
they would not be practical in a production environment. Some moisture analysis
methods are discussed in the following.
4.5.1The Glass Slide Technique (TVI Test)
This test was developed by GE Plastics (now Sabic Innovative Plastics) and is called
the Thomasetti volatile Indicator Test or the TVI test. It involves placing four to five
plastic pellets on a glass slide that is heated on a hot plate. With the help of another
slide, the pellets are pressed together and sandwiched between the two slides.
Once the pellets are flattened out, the slides are removed and allowed to cool. Any
moisture in the pellets shows up as bubbles in the slide. Sometimes it is helpful to
use a microscope to view the bubbles. This is an easy way to determine the pres-
ence of moisture in the sample, although the slides and the hot plate must be han-
dled very carefully to avoid safety issues. This test does not provide a numeric
value of the amount of moisture present in the plastic and, as in other tests, vola-
tiles from degradation or an additive cannot be identified. The TVI Test is not a
commonly used test in industry.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 107 (page 107)

834.5 Determination of the Amount of Mois ture
4.5.2The Karl-Fischer Titration Method
This type of analysis will produce the most accurate results. However, because of
the time required to conduct this test, the additional materials and equipment re-
quired, the test is also not commonly used. The basic underlying principle of this
method is that a small amount of electricity will be generated with the chemicals
involved in the test due to the reaction of the moisture in the plastic. The plastic is
heated to a higher temperature to release the moisture. The amount of electricity
generated is directly related to the amount of moisture present in the system.
A
ccurate measurement of the electricity generated provides the amount of mois-
ture present in the plastic. Figure 4.8 shows a setup for a Karl Fisher titration sys-
tem. A disadvantage of this system is that at elevated temperatures, water can be
produced in some plastics. This may be caused by degradation or by melt polymer-
ization, a phenomenon explained in Section 4.1.1. Therefore, for these plastics the
newly formed water can skew the results and provide false readings.
Figure 4.8 A Karl Fischer setup to measure moisture in a sample (Courtesy: Denver
Ins
truments)
4.5.3Electronic Moisture Analyzer
With the advances in technologies and with better understanding of the moisture
absorption process, electronic moisture analyzers have become common in many
production facilities. The biggest advantage they provide is their simplicity of use
without any prior knowledge or experience in plastics or moisture determination.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 108 (page 108)

84 4  Plastic Drying
The test takes less than approximately ten minutes and provides a print out of the
moisture level in the plastic. The instrument can also be hooked up to a PC to col-
lect and record test data over time. These analyzers work on the principle of weight
loss when the plastic is heated and the water leaves the system. In this test, a small
amount of plastic is placed on a pan that is attached to a micro-scale. The weight of
the sample is recorded and the sample is heated to a desired predetermined tem-
perature for each plastic. As the water leaves the plastic, the weight drops and once
the weight stays constant, it is assumed that the plastic has lost all its moisture.
The final weight is recorded and the percentage weight loss is calculated, provid-
ing the moisture content of the plastic. The disadvantage of this system is that it
does not take any other volatiles that may be lost during the heating process into
consideration, which could influence the moisture content results. Figure 4.9
shows a picture of a moisture analyzer. These types of analyzers are widely used
because of the simplicity of use and the sufficiently reliable data they produce.
Figure 4.9 Electronic moisture analyzer (Courtesy: Denver Instruments)
4.5.4Measurement of the Dew Point
A dew point meter helps to measure the dew point of the air that is supplied to
the dryer. Although this method does not actually measure the dryness of the
resin, it helps in assuring that the dryer is fed with dry air. A dew point of –40 °C
(–40 °F) is a good indication that the amount of moisture in the air is at very low
acceptable levels.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 109 (page 109)

854.6 ‘Overdrying’ or Overexposure to Drying Temperatures
 4.6  ‘Overdrying’ or Overexposure to Drying
Temperatures
Most polymers and plastics are blended with low molecular weight additives, such
as heat stabilizers, processing aids, and other specialty additives. The additives are
used to enhance the plastics’ properties for specific applications and/or to reduce
their cost. Such a blended polymer is called a resin. All plastics used for melt
pr
ocessing are considered resins because of these essential additives. Additives
include plasticizers, lubricants, flame retardants, heat stabilizers, colorants, blow-
ing agents, and biocides among others. Most of them are added to the polymers in
small percentages and are low molecular weight compounds or oligomers.
The drying of the plastic must be controlled in order to not exceed the maximum
recommended drying times. On the production floor this important rule is very
easily overlooked. It is typical in the molding industry to first load the resin into
the dryer and then to complete the mold change in order to ensure that the resin is
being dried during the setup operation and no time is being wasted. This is a very
efficient procedure. However, if the mold setup was not completed in time or the
first shots from the mold were not acceptable and the mold had to be pulled out for
maintenance, the plastic that is left in the dryer is now being subjected to addi-
tional drying time at elevated temperatures. The overexposure may lead to a poten-
tial loss of the low molecular weight additives in the plastic. These additives are
usually not as heat resistant as the polymers, especially after prolonged drying
times. Another scenario in which overdrying can be a potential problem is when
the dryer is oversized for the mold in the machine. In an oversized dryer the resi-
dence time of the plastic is longer than the recommended maximum drying time of
the plastic. For example, if the hourly usage of material is 10

lb and the maximum
recommended drying time is 8
h, t
hen, if the capacity of the dryer is more than
80
lb, t
he plastic that is on top or that is loaded last, will be subjected to a drying
time of more than 8 hours before it is actually used. This must be avoided.
Case Study
A study [1] exemplifies this for two particular materials, a polyester and a nylon.
Here, the polyester was a 30 % glass filled polybutylene therpthalate (PBT) and the
nylon was a 15 % glass filled nylon 66. Both resins were dried for varying times and
the impact of the overdrying was studied. Parts were molded from an existing pro-
duction mold. For each material, the process was kept unchanged during the mold-
ing of the resins dried for the various times. The results were material specific and
the effect of overdrying was different for both materials, as was confirmed by ther-
mal analysis and mechanical tests. In a thermogravimetric analysis (TGA) the plas-
tic sample is continuously heated, which causes the polymer to burn off at a given
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 110 (page 110)

86 4  Plastic Drying
temperature which depends on the base plastic and its additives. Rheology studies
are performed to study the viscosity of the plastic and to determine the effect of
drying. The shear sweep study provided the viscosity versus shear rate plot and
the thermal degradation study was done by plotting the viscosity versus time at a
given shear rate. As the plastic stayed in the barrel, the plastic degraded and a
change in the viscosity was recorded. The observations and the results are dis-
cussed in the following.
Results for PBT
The resin and the molded parts were tested using the procedures mentioned above.
During the molding process it was seen that as the drying time increased, flash on
the parts increased, indicating a drop in melt viscosity. However, there was no sig-
nificant change in the actual characteristic values, such as fill time, cushion value,
screw recovery time, and others. The TGA data is shown in Figure 4.10.
0
10
20
30
40
50
60
70
80
90
100
110
0 100 200 300 4005 00 6007 00 80 0
Weight %
Temperature °C
PBT– 4
PBT–12
PBT– 48
Figure 4.10 TGA graphs of PBT dried for 4, 12, and 48 hours [1]
The final residue left behind was about 33 % of the initial weight. Because the resin
was a 30 % glass filled material, most of this residue must have been the glass. To
better understand the results, T
1/2 is defined as the temperature at which 50 % of
the weight loss occurs. Considering the percentage of the residue remaining, 50 %
of the weight loss occurs at approximately 420 °C for PBT-4 and at approximately
475 °C for the PBT-48. This indicates that for the shorter drying times, a weight
loss occurred at lower temperatures suggesting there must be a component in the
resin that decomposed at lower temperature leading to an earlier loss in weight.
This additive was probably decomposed and was taken out of the dryer during the
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 111 (page 111)

874.6 ‘Overdrying’ or Overexposure to Drying Temperatures
lengthy drying process and therefore the PBT-48 had a T 1/2 that was almost 55 °C
higher than the T1/2 for PBT-4. Looking closely at the numerical data and analyzing
the initial weight loss in the PBT, it can be seen that the slope of the curve is higher
for the PBT-4, indicating sudden weight loss similar to those seen in low molecular
weight compounds and oligomers. After the initial differences in the slopes of the
curves, the lines then seem to run parallel, suggesting the decomposition of the
base resin.
Shear sweep data obtained by capillary rheometry is shown in Figure 4.11. The
data did not show any difference in melt rheology. This could suggest that the addi-
tive lost during the drying process was not a processing aid intended to lower vis-
cosity for ease of processing. No other conclusions could be drawn.
Thermal degradation data also obtained using capillary rheometry is shown in Fig-
ure 4.12. The data showed a difference between the two resins only at residence
times of 9 minutes and above. PBT-48 showed a lower viscosity compared to PBT-4.
This could have been caused by the degradation of the base resin, lowering its
molecular w
eight and thereby lowering its viscosity. It could also be an indication
that the component lost during the excessive drying process was a heat stabilizer.
It is also interesting to note that the viscosity curve almost flattens out past 9 min-
utes, possibly suggesting that the polymer is completely degraded and that it is the
glass fibers now being carried by the degraded resin and contributing to the
viscosity
.
10
100
1000
100 1000 10000
App. Shear Viscosity (Pa-s)
Apparent Shear Rate (1/s)
PBT-4
PBT-48
Figure 4.11 Capillary rheometry data (shear sweep) for PBT dried for 4 and 48 h [1]
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 112 (page 112)

88 4  Plastic Drying
1
10
100
1000
05 10 15 20 25 30 35
Time (min)
App. Shear Viscosity (Pa-s)
PBT-4
PBT-48
Figure 4.12 Capillary rheometry data (time sweep) for PBT dried for 4 and 48 h [1]
PBT parts molded from this resin after excessive residence times in the dryer
crumbled into pieces when a small amount of force was applied. The drop impact
testing of the parts demonstrated a clear difference between PBT-4 and PBT-48.
This data is shown in Figure 4.13. As can be seen, the mean failure energy de-
creased with the increase in drying time. The parts tended to become more brittle.
This could be the effect of either the loss of an additive, such as an impact modifier,
and/or the degradation of the resin. There was a sharp drop in the mean failure
energy between 12 and 36 hours of drying time. Before and after these times the
curve stayed relatively flat. Looking at this data, drying times should be limited to
12 hours to retain the material properties.
0.75
0.80
0.85
0.90
0.95
1.00
1.05
1.10
0481 21 62 02 42 83 23 64 04 44 85 2
Mean Failure Energy (Joules )
Drying Time (Hours)
PBT
NYLON
Figure 4.13 Mean failure energy of parts molded with PBT and nylon dried for varying drying
times [1]
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 113 (page 113)

894.6 ‘Overdrying’ or Overexposure to Drying Temperatures
Results for Nylon
In the case of nylon, studies were conducted for drying times of 4 hours and 48
hours. The resin and the molded parts were tested with the procedures mentioned
earlier and the TGA data is shown in Figure 4.14. Here, a 15 % glass filled resin was
used. The residue left behind was approximately 17 % of the original weight. We
can again be certain that most of the residue was the glass left behind. The T
1/2
values for both nylon-4 and nylon-48 seemed to be approximately 470 °C. The
weight loss also started around the same time and imitated each other. We can
therefore infer that there was no significant difference between the TGA curves for
the regularly dried and the overdried resin. There was no noticeable loss of any
additive.
0
10
20
30
40
50
60
70
80
90
100
110
01 00 2003 00 400 500 600 700 800
Temperature °C
NYLON-4
NYLON-48
Figure 4.14 TGA graph for nylon dried for 4 and 48 h [1]
10
100
1000
100 1000 10000
Apparent Shear Rate (1/s )
App. Shear Viscosity (Pa-s)
NYLON-4
NYLON-48
Figure 4.15 Capillary rheometry data (shear sweep) for nylon dried for 4 and 48 h [1]
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 114 (page 114)

90 4  Plastic Drying
The capillary rheometry-shear sweep data is shown in Figure 4.15. It is interesting
to note that the viscosity for the nylon-48 was higher than that for nylon-4. Khanna,
et al. [2] have noticed a similar increase in the viscosity of nylons with increase in
drying temperature and time held constant. Similar studies by Pezzin and Gechele
[3] showed that the melt viscosity increased with time for lower moisture contents.
Khanna hypothesizes that the increase in the viscosity could be explained by the
following two reasons:
 The mois
ture in the nylon acts as a plasticizer for the melt, reducing its viscosity.
With higher drying temperatures, loss of moisture leads to an increase in visco
-
sity
.
 The melt eq
uilibrium is represented by a characteristic equilibrium constant,
Kcond. If excess water is added to the melt in equilibrium, the reaction will go in
the direction of the reactants (i. e., degradation), while the reverse (i. e., polycon-
densation) should occur if water is removed from the equilibrium melt.
In the present study, the drying temperature was held constant and the drying
time was varied. Considering the theories put forth by Khanna, and the similar
results obtained here, the net result of the increase in drying time must be the
same as the increase in drying temperature. The loss of moisture between drying
times of 4 hours and 48 hours must have contributed to the increase in viscosity of
the melt. Evidence of this was also seen during the molding of the parts. A feature
that was 48 mm long with an average height of 3.5
mm and a widt
h of 6
mm w
as
almost completely filled (99 %) during the injection phase of the molding cycle
when molding with nylon-4. When nylon-48 was used, this feature was only filled
to approximately 62 % of the original flow length. Photographs of this are shown in
Figure 4.16.
Figure 4.16 Complete parts and ‘injection only’ parts molded with nylon dried for 4 and 48 h [1]
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 115 (page 115)

914.6 ‘Overdrying’ or Overexposure to Drying Temperatures
1
10
100
1000
05 10 15 20 25 30 35
NYLON-4
NYLON-48
Time (min)
App. Shear Viscosity (Pa-s)
Figure 4.17 Capillary rheometry data (time sweep) for nylon dried for 4 and 48 h [1]
Thermal degradation data using capillary rheometry are shown in Figure 4.17. The
two resins do not seem to differ in viscosity for residence times of 12 minutes and
beyond. With a residence time of 6 minutes, nylon-48 has a higher viscosity com-
pared to nylon-4. The same reasoning as in the above section can be applied here.
Once past the 6 minute interval, the resin probably begins to degrade and the final
viscosity of the two resins matches.
Drop impact testing of the parts demonstrated no significant difference between
nylon-4 and nylon-48, as shown as a dotted line in Figure 4.13. The average mean
failure energy for the two samples was 0.774 Joules. Long drying times did not
seem to affect the drop impact strength of the resin. It is evident from the above
discussion that it is important to control the drying process of the resin. Overdry -
ing can result in a loss of physical properties as seen in the case of PBT, or lead to
the increase in the viscosity as in the case of nylon. For nylons, because the water
in the plastic has an effect on the viscosity of the plastic, the water can be thought
of as a viscosity regulator. The viscosity changes will have an impact on the flow
properties and the associated features, such as the weld line strength of parts.
Other properties affected by flow, such as surface finish and polymer/filler ratio
could also be impacted by long drying times. Secondary operations, such as ultra-
sonic welding and joining, require a certain amount of polymer to be present on
the surface in order to achieve successful bonding. Therefore, a minimum level of
moisture is required for nylons because water is a viscosity regulator. This level is
usually around 0.015 %. However, this is something each molder must determine
and maintain individually.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 116 (page 116)

92 4  Plastic Drying
 4.7  Cautions
Drying of some resins such as PBT has a cumulative effect. The drying process
r
emoves the low molecular weight additives for good and they do not return if the
drying is stopped and the resin returned to the shelf for the next run. However, in
the case of nylons, the moisture can be absorbed back and the viscosity can be
re-regulated. Since each resin and its additives is unique, customized experimen
-
t
ation is best suited to determine the type of control required for each individual
process. The results above must not be taken as any sort of standard results. Ex
-
per
imentation is time consuming and expensive and therefore it is best to keep it
simple and avoid overdrying.
 4.8  Pr evention of Overexposure to
Long
er

Drying Times
On the shop floor there are a couple of efficient ways to prevent overdrying:
Turning down the dryer temperature: If molding is not ready to be started after the
material is dry, turn down the dryer temperature to about 25 °C (80 °F), but keep
the dryer running. Supplying the hopper with low temperature dry air will keep
the moisture out and will not have detrimental effects on the resin.
Sizing the hopper: Size the hopper dryer such that the residence time of the plastic
stays between the minimum and maximum recommended drying times of the
plastic. When the hopper is larger than required this may be difficult. In this case,
retrofit the dryers with a level sensor and adjust the level to maintain the required
amount of material.
The material required for the run must be calculated and only the required amount
of material should be dried. If the machine is going to be down for an extended
period of time after the drying has taken place, the dryer must be shut off as soon
as possible.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 117 (page 117)

934.9 Overdrying Controller
 4.9  Overdrying Controller
Figure 4.18 shows this logic applied to a design of a controller, while Figure 4.19
depicts a concept for a programmable controller that would control the drying pro-
cess of the resin.
Set Level Sensor
Set Drying Temperature = T
Set Drying Time = H
Set Run Time = 0
Continue Drying
Is run time >H
Start Molding
Continue Molding
Has the machine been
operational in last 10 min?
Drop Dryer Temperature by 50 °
Is Hopper Temperature = 100 °
Maintain Hopper Temperature to 100°
Flow Chart for the logic behind controller
NO
NO
YES
YES
YES
NO
Figure 4.18 Controller logic to control residence time in the dryer [1]
Initially, the controller would set the drying time and temperature. Based on shot
weight of the mold, a resin level sensor would be set such that the residence time
of the resin in the hopper exceeds the recommended drying time by an hour to two
hours. Once the set drying time has elapsed, the controller looks for a signal from
the machine indicating that the machine is operational and molding parts. Such a
signal can be picked up from screw rotation or mold open/close. If the controller
receives this signal it will maintain the dryer temperature. If it does not receive the
signal, indicating that the machine is not operational, the controller will start to
drop the drying temperature by a preset value, for example 10 °C. If in a preset
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 118 (page 118)

94 4  Plastic Drying
time, for example 15 minutes, the controller does not get the machine operation
signal, it will further drop the temperature down by another step. It will do so until
it reaches a temperature of 25 °C. At this time, dry air will be circulating in the
hopper and keep the resin dry. As soon as the machine is ready for operation and
the controller gets this signal, the temperature of the hopper will begin to rise to
the desired drying temperature in preset steps of temperature and time. If normal
molding operation is interrupted, the controller will follow the same logic de-
scribed above and drop the dryer temperature. Such a control mechanism will
ensur
e that the resin will never experience excessive drying times and prevent
overdrying.
Undried resin
Dry airAdjustable level sensor
Figure 4.19 Flowchart for the logic behind controlling the drying process [1]
 4.10  References
[1] K ulkarni, S. M., SPE ANTEC Tech Papers (2003) p. 736
[2]
Khanna Y
. et al., Polymer Engineering and Science, Vol. 36 (13), p. 1745, (July 15, 1996)
[3]
P
ezzin G., and Gechele G., J. Appl. Polymer Sci., Vol 8, p. 2195, (1964)
Suggested Reading
Brydson, J. A., Plastics Materials (1999) Butterworth Heinemann Ltd, Oxford
Harper, C. A., Modern Plastics Handbook (2000) McGraw Hill, New York, NY
Deanin, R. D., Polymer Structure, Properties and Applications (1972) Cahners, Boston, MA
Odian, G., Principles of Polymerization (1991) Wiley Interscience, NY
Shah, V., Handbook of Plastics Testing and Failure Analysis (2007) Wiley Interscience, NY
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 119 (page 119)

Common Plastic
Materials and Additives
Injection molding processors are mainly concerned with the way the plastic flows
and with the temperature at which the plastic can be processed. Flow characteris-
tics of all plastics are very similar. They all follow non-Newtonian behavior and
therefore exhibit shear thinning effects. A pattern from a flow simulation program
for two different plastics will look very similar, because plastic flow is always lam-
inar. The pressures and temperature distributions may be different, but the flow
patterns are similar. All plastics have their unique processing temperature range,
both for the mold temperature and the melt temperature. Even with these com-
monalities, it is still important to understand the different types of plastics and the
additives that are incorporated into them. With this knowledge processors will be
able to better understand the materials they work with and to take the necessary
precautions during their processing. For example, while polyethylenes can be in-
jected at very high speeds, one must be very careful with PVC, because it tends to
degrade at higher speeds. This chapter will introduce the base materials, the addi-
tives, and the reason for their incorporation. Only the most common polymers by
volume and the additives used in injection molding will be discussed.
 5.1  Classification of Polymers
Polymers can be classified in a number of ways. In the field of molding the term
plastic is most commonly used. We use the term polymer when we describe the
basic nature of the molecules and their properties. Plastics are those polymers that
can withstand a moderate to significant amount of force before showing any signif-
icant deformation. Polymers that are deformed under light loads are called elasto-
mers. Technically, the difference can be seen clearly in the stress-strain graphs in
Figure 5.1. In the following, the term plastic will be used to describe all molding
materials and the term polymer will be used when an intrinsic property needs to
be referenced.
5
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 120 (page 120)

96 5  Common Plastic Materials and Additives
The following classifications of polymers are also used:
Thermoplastics: They can be repeatedly heated, melted, and processed into useful
products. Example: ABS
Thermosets: Once these polymers are processed, they form a chemical network and
all the molecules now are crosslinked. It is impossible to re-melt the polymer in
this state because there is more energy required to separate the crosslinked bonds
than the energy required to break the main chains. This results in a total destruc-
tion of the polymer. Example: Liquid silicone rubbers (LSRs)
Organic Polymers: These contain carbon atoms in their backbone and are derived
mainly from organic materials from nature. Example: Polyethylene
Inorganic Polymers: These contain atoms other than carbon in their backbone.
Example: Polysilanes
Stress
Brittle
Strain
Tough with break
Tensile strength
Tough and plastic
Elastomers
Figure 5.1 Tensile properties for different types of plastics
Elastomers (TPE): These are similar to thermoplastics except they are soft and
r
ubbery at room temperature. Their glass transition temperatures are below room
temperature.
Homopolymers: These are polymerized from only one type of monomer. Example:
Polyethylene
Copolymers: These are manufactured from two or more monomers. Example: ABS –
polymerized from acrylonitrile, butadiene, styrene
Alloys: These are polymers physically mixed with each other and there is no
c
hemical interaction between the different polymers. Example: PC-ABS alloys are
common in the appliance industry.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 121 (page 121)

975.2 Commercially Important Plastics
 5.2  Commercially Important Plastics
Some of the commercially important plastics that are injection molded are de-
scribed in the following. All descriptions relate to unfilled plastics without any
additiv
es.
5.2.1Polyolefins
Polyolefins are the most basic hydrocarbons and contain carbon and hydrogen
at
oms only. Polyethylenes and polypropylenes are the most widely injection molded
polyolefins.
Polyethylene: Polyethylene is one of the widest used materials because of its excel-
lent electrical insulation properties, good chemical resistance, impact properties,
and low cost. The properties of polyethylene (also known as polyethene) can be
tailored to meet certain application requirements. The tailoring changes the den-
sity of the polymer which allows to classify the different polyethylenes. Low den-
sity polyethylene (LDPE) has a density of 0.91–0.92g/cm
3, medium density poly-
ethylene (MDPE) has a density of 0.93–0.94g/cm 3 and high density polyethylene
(HDPE) has a density of 0.95–0.96g/cm3. Linear low density polyethylene (LLDPE)
is technically a copolymer and is designed for better impact properties and
im
proved flexibility. It is mainly used for films. The density of LLDPE is around
0.91g/cm3. To improve some of the mechanical properties and still retain the other
pr
operties of polyethylene, its molecular weight is increased. This product is
called ultra high molecular weight polyethylene (UHMWPE) with a density of
0.92–0.93g/cm
3. UHMWPE is difficult to mold because of its high melt viscosity.
The weight average molecular weight of UHMWPE can be in the range of 1–6 × 106,
whereas for other ethylenes it is around 50,000 to 300,000. The disadvantage of
polyethylenes is that they exhibit high thermal expansion, poor weathering resist-
ance, and low heat deflection temperatures. Although the mechanical properties of
polyethylene are low, with the use of reinforcing fillers such as glass fibers these
properties can be enhanced. Polyethylenes can also be crosslinked to improve their
properties.
Polypropylene: Both polypropylene and polyethylene have similar structures and
similar properties. Most commercially available polypropylenes are isotactic poly-
propylenes with densities of 0.90g/cm
3. They exhibit good electrical properties,
good environmental stress cracking resistance, and good heat resistance. Poly -
pr
opylene dominates in the area of thin-wall molding which requires good flex
properties. CD covers with living hinges are examples of these applications that
can stand continued flexing. The biggest disadvantage of polypropylene is its low
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 122 (page 122)

98 5  Common Plastic Materials and Additives
temperature flexibility or impact resistance. As the temperature reaches 0 °C, the
polymer becomes brittle and often cracks. This issue is often resolved by either
incorporating additives or copolymerizing polypropylene with a small percentage
of poly
e
thylene.
Other olefins such as cyclic olefins are used in molding but not to the extent as
polyethylenes and polypropylenes.
5.2.2Polymers from Acrylonitrile, Butadiene, Styrene, and Acrylate
Monomers and polymers of acrylonitrile, butadiene, styrene and acrylates are
compatible with each other and produce a variety of useful polymers and plastics.
Each of these can be polymerized by themselves or with other monomers. Each of
the monomers provides a unique property to the final polymer. For example, buta-
diene is a polymer with a low T
g value and therefore provides impact resistance;
styrene adds luster to the product and helps to improve the processability; acry -
lonitrile adds heat and chemical resistance; acrylic adds weathering resistance.
ABS is one of the most commonly used materials. Depending on the end use re-
quirement, it can be produced with varying percentages of the monomers. An
absence of s
tyrene produces nitrile rubber, an absence of butadiene will produce
styrene acrylate resins (SAN), and an absence of acrylate will produce styrene
butadiene rubber (SBR) or impact modified styrene (HIPS). SBR is butadiene with
a small percentage of polystyrene and HIPS is polystyrene with a small amount of
butadiene. By themselves, the polymerization products are polyacrylonitrile, poly-
butadiene, and polystyrene. Similar combinations with acrylate monomer yield
different polymers as was shown in Figure 5.2. Because of the endless possible
combinations of the monomers, the properties of the end polymer can be tailored.
Not only the percentages of the monomers play an important role, but the method
of preparation can also affect the properties. The polymers can be copolymerized
from the monomers, grafted onto a base polymer, or the individual polymers can
be physically blended with each other. These polymers can be further blended with
other polymers to create other customized polymers. A blend of polycarbonate (PC)
and ABS called PC/ABS is widely used in thin-wall molding, such as cell phone cases.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 123 (page 123)

995.2 Commercially Important Plastics
Heat res
Acrylonitrile
Butadiene Styrene
Acrylate
Acrylic
Polybutadiene
Weather res
UV res
Low temp res
Impact
Luster strength
moldability
Chemical res
Figure 5.2 Polymers produced from acrylonitrile, butadiene, styrene, and acrylates
5.2.3Polyamides (PA)
Most polyamides used for molding are commonly called nylons, although not all
PAs are nylons. Nylons are crystalline materials; they are manufactured by poly -
condensation reactions usually producing water as the byproduct. Nylons pro-
duced from dibasic acids and diamines are identified by a numbering system that
indicates the number of carbon atoms in the base monomers. A nylon 6/6 has six
carbon atoms in the dibasic acid and six carbon atoms in the diamine. A nylon
4/12 has four carbon atoms in the dibasic acid and twelve carbon atoms in the di-
amine. For example, nylon 6/6 is made from hexamethylene diamine and adipic
acid that each contain six carbon atoms. Nylons made from a single monomer are
identified by just one number. For example nylon 6 is made by the ring opening
polymerization of caprolactam that contains six carbon atoms. Commercially,
n
ylon 6 and nylon 6/6 are widely used in injection molding. Nylons are tough and
offer good impact and chemical resistance even at moderately elevated tempera-
tures. This is the reason they are used in a lot of automotive applicatioons, such as
under the hood. Gears, cams, and bearings are also products made from nylons.
The biggest disadvantage of nylons is due to the fact that they are strong hydro-
philic materials, i. e., they absorb a lot of moisture. The presence of moisture dras-
tically affects their properties, such as dimensional stability and electrical proper-
ties. Most data sheets for nylons are therefore available for ‘dry’ and ‘conditioned’
nylons. The properties of nylons are also affected by the crystallinity of the poly -
mers. Table 5.1 shows the relative difference in properties between nylon 6 and
nylon 6/6.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 124 (page 124)

100 5  Common Plastic Materials and Additives
Table 5.1 Relative Differences in Properties of Nylon 6 and Nylon 6/6
Property Nylon 6 Nylon 6/6
Crystallinity Lower Higher
Heat resistance Lower Higher
Chemical resistance Same Same
Impact strength Higher Lower
Wear resistance Lower Higher
Processibility Lower melt and wider window Higher melt and narrower window
Processing of nylon if fairly simple because of its favorable flow properties. Nylon
must be dried to the right moisture level before processing. Some amount of mois-
ture in the plastic acts as a viscosity reducer and regulator and therefore exposure
of nylon to excessive drying times should be avoided. Drying of nylon is discussed
on Chapter 4. If nylon is not dried prior to molding, it can degrade in the barrel due
to hydrolysis causing a drop in properties. Surface defects such as splay is com-
mon with undried resin. Drooling from the nozzle tip between mold open and mold
close is another issue because the water reduces the viscosity of the plastic and
makes it drool out of the nozzle tip after the shot builds up. Because of the high T
m
and Tg, cycle times can be short.
5.2.4Polystyrenes (PS)
Polystyrene is polymerized from styrene and is also called poly(vinyl benzene). It
can be either atactic or syndiotactic, as described on Chapter 2. Most commercially
used poly
s
tyrene is atactic with good optical clarity because of its amorphous na-
ture. The Tg of the polymer is high, resulting in good dimensional stability. Solvent
resistance, weathering resistance, and impact strength of polystyrenes are low.
Impact strength can be improved by incorporating a small amount of rubber, such
as butadiene, creating a high impact polystyrene, commercially called HIPS; how -
ever, this affects the clarity of the final product. Another useful property of poly
-
s
tyrene is its ease to be processed into foam. Commercially available styrofoam is
polystyrene mixed with a blowing agent during the melt processing to produce the
foamed product. It has extensive use and in fact dominates the packaging industry.
Because of its low cost, ease of molding and availability in FDA approved grades,
polystyrene finds its way into many household and kitchen products.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 125 (page 125)

1015.2 Commercially Important Plastics
5.2.5Acrylics
Commercial acrylic is mainly polymethyl methacrylate (PMMA). It is an amor -
phous polymer and has excellent clarity. Because of its high resistance to UV light
and good weathering property, it is widely used to make lighted sign boards and
outdoor lighting articles. It is a good substitute for glass, except for its low scratch
resistance. The disadvantage of acrylics is their poor resistance to organic solvents
and low stress cracking resistance.
5.2.6Polycarbonates (PC)
PCs are almost considered engineering materials because of their high impact
strength. Their high transparency and high impact strength make them an ideal
choice for automotive exterior lighting parts, helmet visors, and safety goggles.
Processing of PC is fairly easy, although the presence of moisture can cause a lot of
problems in the molding of PC. Cosmetic issues, such as splay, are common. A va-
riety of PCs are available on the market and care must be taken to study the data
sheet before molding a new grade of PC. The processing may be so widely different
that the processing temperatures of two PCs may not even overlap. PCs have low
stress cracking resistance and their chemical resistance is fair.
5.2.7Polyesters
Polyethylene terephthalate (PET) and polybutylene terephthalate (PBT) are the
most common injection molded polyesters. They exhibit excellent mechanical
properties and are easy to process. By volume, PET is more commonly used in blow
molding to produce containers and bottles. Because of their high chemical resist-
ance to automotive fluids, PBT is used in under-the-hood applications. PBT is prone
to be attacked by certain solvents.
5.2.8Polyvinyl Chloride (PVC)
PVC is one of the least stable polymers, but is processed successfully with the
appr
opriate additives and stabilizers. It is probably the material that has had the
worst reputation over the years because of safety concerns. However, PVC is one of
the most versatile polymers. It can be easily modified to achieve a wide range of
flexibility. PVC by itself is very rigid and is marketed under the name rigid PVC or
UPVC. PVC has excellent chemical and weathering resistance and is therefore
widely used in pool and garden equipment. PVC has excellent electrical properties
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 126 (page 126)

102 5  Common Plastic Materials and Additives
and is also used as cable insulators. The addition of plasticizers softens rigid PVC.
With the addition of a large amount of plasticizer PVC can be processed into films
by nonmelt processing techniques. To make PVC more chemical resistant, it is
chemically modified to incorporate chlorine in the molecule. This PVC is called
chlorinated PVC. Heat resistance and weatherability decrease with the addition of
the chlorine. Melt processing of PVC requires extreme care and caution. Decompo-
sition of PVC produces hydro
c
hloric acid which is an irritant to humans. Therefore,
the residence time in the molding barrel must be controlled and limited. Once the
production run is over, all the PVC in the barrel must be thoroughly purged. All
related equipment must also be cleaned to avoid any of the PVC from getting to the
barrel with the next material. This is especially true if the next material to be
molded is an acetal. Acetal and PVC are known to be an explosive combination in
their melt form and therefore any chance of them being mixed must be avoided.
5.2.9Polyoxymethylene (POM or Acetal)
Although acetal is the commonly used term (sometimes polyformaldehyde is also
used), this material is actually polyoxymethylene. It is a crystalline polymer and is
considered an engineering plastic. It has excellent stiffness, fatigue endurance,
resistance to creep, and low coefficient of friction. POM also exhibits excellent
chemical resistance below 70 °C to all organic solvents. Above this temperature,
some phenolic materials can react with the polymer. Resistance to inorganic poly-
mers is low. Gears, bearings, conveyor parts, or any moving parts in assemblies are
good application candidates for acetals because of their unique properties. The
cost of acetal is fairly high. The density of the unfilled polymer is 1.42
g/cm3,
which is very high compared to olefins or nylons. This makes it less attractive
when it competes with other materials because the part will weigh more and there-
fore cost more, if molded in acetal. Melt processing of acetals is fairly easy. Over -
heating of processing barrels and large residence times must be avoided. Degrada-
tion produces formaldehyde gas which is an irritant. Acetals are non-hygroscopic
and therefore do not require drying. Surface drying is helpful in humid environ-
ments. A typical problem occurring when molding acetal is that the parts show
unusual shrinkage values, far different from the published values. The main rea-
son is usually due to the gate freezing off before the part is packed out with the
required amount of plastic. Enlarging the gate size helps.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 127 (page 127)

1035.3 Additives
5.2.10Fluoropolymers
Fluoropolymers are polymers containing fluorine. Polytetrafluoroethylene (PTFE),
also called Teflon, is the most commonly used fluoropolymer. However, because of
its high melt viscosity it is almost impossible to be injection molded. It has excel-
lent mechanical properties over a wide range of temperatures. It does not dissolve
in any acids, alkalis, or organic solvents. It also has a low dielectric constant. Be-
cause PTFE cannot be melt processed, the sintering technique is used to produce
PTFE components, such as pump valves. PTFE tape commonly used before install-
ing a water pipe on to a mold is produced by the process of skiving. Polyvinylidene
fluoride (PVDF) is a fluoropolymer that can be injection molded. PVDF also offers
good chemical resistance although it is not as high as that of PTFE. PVDF has been
successfully used in chemical and electrical equipment and even in the manufac-
ture of internal battery components. Perfluoroalkoxy copolymer (PFA), fluorinated
ethy
lene pr
opylene (FEP), and ethylene-tetrafluoroethylene (ETFE) are other fluoro-
polymers that offer similar properties as PTFE, but they are modified to be injec-
tion moldable. Molds that need to be designed for molding fluoropolymers need to
have wide runners and gates to reduce the pressure drop through the mold. Spe-
cial screws with generous section dimensions, large feed sections, and smaller
me
tering sections can be helpful in the processing of these polymer.
 5.3  Additives
Today, all polymers that are supplied by the manufacturer have additives blended
into them. Additives can change the properties of the polymers substantially. PVC
is the best example of this. As mentioned earlier, PVC by itself is rigid but with the
addition of a plasticizer it can become extremely flexible. All additives must be
compatible with the base polymer and must not bleed out or plate out under ex-
tended service conditions. Some PVC films get tacky with increase in temperature.
This is the bleeding out of some of the plasticizers contained in it. They must also
be able to withstand the processing conditions such as melt temperature and shear
rates. These additives can be solids, liquids, gases, or other polymers. Some of the
important additives based on their use are described in the following.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 128 (page 128)

104 5  Common Plastic Materials and Additives
5.3.1Fillers
Fillers are added to polymers either to improve the properties or to reduce the cost.
Glass fiber is an example of a filler used to increase the stiffness or creep resist-
ance of the base plastic, it is also called a reinforcing filler. Other examples of re
-
inf
orcing fillers are wood flour, carbon fibers, and nylon fibers used to increase the
impact strength and rigidity of the base plastic. Glass beads are usually added to
plastics to reduce the shrinkage or sometimes (depending on the base polymer
density and the glass bead density) the weight of the polymer. These are called
iner
t fillers. Talc and calcium carbonate are other examples of inert fillers. In the-
ory, any material that is compatible and can be blended into the polymer matrix
can be used as a filler. Over the years, experiments have been conducted with a
large number of fillers, especially when a particular material was easily available
in the local geographic area. For example, fibers from the coconut tree or from the
coconut ha
ve been successfully used in some applications in some South Asian
countries. In some cases, coupling agents are used to form a bond between the
filler and the polymer since the two are not always compatible, typically with in
-
org
anic fillers.
5.3.2Plasticizers
Plasticizers are added to provide flexibility and softness to a material. Because of
their compatibility, they get in between the polymer molecule, increasing the inter-
molecular distance. They also help in reducing the melt viscosity for improved
processing properties. PVC is the biggest consumer of plasticizer by volume. Plas-
ticizers are usually low molecular weight compounds, usually oligomers. If the
plasticizers are not compatible, they tend to migrate to the surface of the polymer.
Phthalates such as di(isooctyl) phthalate (DIOP) are commonly used as plasticizers
in PVC. Concerns regarding safety have led researchers to more natural products
and in recent years epoxidized soybean oil (ESO) has gained popularity.
5.3.3Flame Retardants
For most products that are in direct contact or in close proximity with humans,
such as furniture, toys, televisions, and computers, flame retardants are added to
prevent the spread of fire. Although the plastics used in these products will burn
in the presence of a fire, they must not continue to do so when the source of the fire
is removed. Most consumer materials, such as olefins and polystyrenes, will con-
tinue to burn even if the source is extinguished. Flame retardants are added to
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 129 (page 129)

1055.3 Additives
plastics to inhibit this continued burning. This is achieved by one of several
mec
hanisms, such as forming an incombustible gas and cutting of the supply of
oxygen required for the burning. Halogen-containing compounds, such as chlor -
inat
ed paraffins, and phosphates, such as trixylyl phosphate, are used as flame re-
tardants. Testing is done using various methods and the rate of burn, time of burn
once the flame is removed, and the amount of burn of the sample are all recorded
as vital data.
5.3.4Anti-aging Additives, UV Stabilizers
Over time, polymers tend to lose some of their properties because of a variety of
changes in the polymer: The molecular weight can drop as a result of chain scis-
sion or certain additives can degrade or bleed out. Some of these can cause chain
reactions because the reaction products can help in the propagation of the reac-
tion. Antioxidants and UV stabilizers are commonly added to plastics as anti-aging
additives. The antioxidants react with any free radicals that are formed and pre-
vent the propagation of the chain scission. UV light can cause a change in the
physical properties of the polymer, e. g., causing it to become hard leading to sur-
face cracking. They may also discolor. Automotive head lamp covers tend to be-
come yellow over time because of their extended exposure to the UV light present
in sunlight. UV stabilizers absorb the UV light and prevent it from affecting the
plastic. Certain amines are examples of UV stabilizers. All products that are ex-
posed to sunlight must have a UV stabilizer incorporated.
5.3.5Nucleating Agents
Nucleating agents are used in crystalline polymers to help speed up the nucleation
process and lower molding cycle times. When the melt enters the mold, it is com-
pletely amorphous and as it starts to cool down, the crystallization process starts.
Mold temperatures are maintained high enough to supply the energy for crystal
-
lization. Cr
ystallization provides the required properties to the end product and
therefore it must be completed before the plastic temperature falls below the glass
transition temperature (T
g). Below the T g, no meaningful crystallization can take
place. Nucleating agents help to increase the onset and rate of nucleation. They are
commonly incorporated in olefins, polyesters, and nylons that form the majority of
the injection molded crystalline polymers. Talc is a good example of a nucleating
agent for polypropylenes.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 130 (page 130)

106 5  Common Plastic Materials and Additives
5.3.6Lubricants
Lubricants are added to reduce the coefficient of friction in the final products. In
many assemblies, moving parts slide against each other (cams) or drive another
part by an applied mechanical force (gears). In such cases, a low coefficient of fric-
tion is desired for two reasons:
1.
t
he energy required to move the parts is reduced, and
2.
a
lower coefficient of friction translates to less heat buildup in the part. Heat
buildup can cause thermal expansion of the component changing its dimen-
sions and leading to the failure of the assembly.
Graphite and PTFE are added to plastics in small quantities to act as lubricants.
5.3.7Processing Aids
Some texts classify lubricants and processing aids in one category. Processing aids
act as melt viscosity reducers that help in the melt processing of the plastic. They
are also called flow promoters. Amine waxes are examples of these. Processing
aids do not alter the final property of the plastic and their primary function is to
ease the processing.
5.3.8Colorants
Colorants are blended into the base polymer to impart the destined color. Compat-
ibility is no doubt important, but in injection molding, where color pellets are
mixed with the plastic, the carrier resin for the colorant also needs to be compati-
ble. Colors can also be added as liquids directly into the barrel of the injection
molding machine, although this can get messy. The advantage here is that the
control of the amount of liquid can be very accurate. Mixing color powders with
the resin must be done immediately prior to processing because the powder tends
to separate during transport. The powder also tends to stick to the walls of the mix-
ing equipment and hoppers.
5.3.9Blowing Agents
Blowing agents are used to mold plastic parts with a cellular structure. In thick
parts this helps reduce the overall weight of the part and it also improves the
s
tructural strength of the part. Defects related to thick sections, such as sink
marks, are eliminated. The blowing agent mixes with the plastic and creates internal
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 131 (page 131)

1075.3 Additives
pressure to push the plastic towards the walls of the mold. The molded parts are
therefore dimensionally more consistent as compared to conventional parts. The
disadvantage of using a blowing agent is the additional cost and effort of mixing.
Parts molded with a blowing agent do not have good surface finishes. Large hop-
pers or containers are examples of parts molded using blowing agents. When the
process is used to improve the structural properties, it is also called structural
foam molding. Styrofoam cups are molded using a blowing agent. Blowing agents
can be chemicals that decompose in the injection barrel to form a gas and help
foam the plastic (e. g., sodium bicarbonate) or they can also be gases, such as nitro-
gen and air.
5.3.10Other Polymers
Technically, when polymer blends are produced, one polymer is added to another
polymer. Therefore these polymers may also be considered as additives. For exam-
ple, in a PC/ABS blend, PC can be considered an additive to ABS or vice versa.
Thermal properties of a blend of polyhydroxybutarate and polyvinyl acetate are
shown in Figure 5.3.
-153 58 5 135 185
TT
Figure 5.3 Thermal properties of blends of PHB/PVAc
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 132 (page 132)

108 5  Common Plastic Materials and Additives
 5.4  Closing Remarks
In Chapters 2 and 3, the morphology and the rheology of the polymers were dis-
cussed. Additives can have a profound influence on both these properties. A poly -
mer that is naturally crystalline can be made completely amorphous by incorporat-
ing additives. Figure 5.3 shows the thermal properties of a PHB/PVAc blend. The
PVAc was blended in various proportions into the PHB starting with 10 %. As the
amount of PVAc increased, the glass transition temperature and the crystallization
temperature of the PHB phase increased. Polymer properties can be tailored by
blending techniques and by the addition of additives. However, there may not
alw
ays be a win-win situation for all the properties. Some of them may have to be
compromised.
 5.5  Reference
[1] Alfr ey, Turner, and Gurnee, E. F., Organic Polymers, Prentice-Hall (1967) p. 51
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 133 (page 133)

Injection Molding and
Molding Machines
 6.1  The History of Injection Molding
The concept of injection molding for plastics was adopted from the metal die cast
industry, which began to develop in the early to mid-1800s. Plastics were not
known for their useful properties at this time. All polymers were naturally occur -
ring materials and did not have much industrial value. In 1869, John Hyatt devel-
oped a concept to make billiard balls from cellulose nitrate, also known as cellu-
loid. His machine consisted of a cylinder heated by steam to melt the celluloid and
a hydraulic plunger to inject the plastic into the mold. Developments continued
and several inventors produced several designs of molding machines and their
components. Over the years, molding machines advanced from their manual oper-
ations to automatic operations with electrical controls. Almost seventy years after
the first injection molding machine was developed, a major milestone was achieved.
In 1948, for the first time, the two-stage screw was introduced in the injection
molding industry. Until then melt homogeneity was achieved with the help of
t
orpedoes in the injection barrel. The use of the two-stage screw provided the re-
quired homogeneity and allowed better control of the plastic shot size injected into
the mold. As a result of the improved melt efficiency and better melt homogeneity
provided by the two-stage screw, a larger volume of plastic could now be melted,
leading to the possibility of molding larger parts. As molding machine control sys-
tems improved with the advent of advanced electronics engineering, the molding
machines became more sophisticated, providing better control of the injection
molding process. Multishot molding machines, better screw designs, clamp posi-
tion versatility, and nonhydraulic all-electric machines were some of the many im-
proved features and products being introduced to the molding industry. Today’s
machines have become highly complex and are capable of molding almost any -
thing that a product designer would desire, from micromolded parts used in the
watch industry to large parts used in the automotive industry and everything in
between. The latest generation of machines can be connected to any computer in
the world via the Internet and monitored remotely. This helps with quick debugging
6
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 134 (page 134)

110 6  Injection Molding and Molding Machines
and problem solving of machine and molding problems without requiring an engi-
neer on site.
 6.2  Injection Molding Machines and
Their Classifications
A conventional injection molding machine is shown in Figure 6.1(a). Plastic pellets
are fed into the barrel of the injection molding machine where shear heat gener -
ated by the rotating screw and external heat provided by electric heaters around
the barrel melt the plastic, making it ready to be processed. As the screw rotates, it
augers the required amount of plastic for the shot to the front of the barrel. This
plastic is then injected into the mold by the forward movement of the screw. The
mold has a coolant flowing through it that helps maintain its temperature. Once
the part is cooled below its ejection temperature, it is ready to be ejected out of the
mold. Although the process of injection molding seems fairly simple, there are
multiple speeds, pressures, times, and temperatures that must be controlled in or-
der to produce quality products. It is the optimization of these processing parame-
ters necessary to run an efficient and successful molding operation that scientific
processing is all about.
(d)
Figure 6.1 Machine classifications based on clamp and nozzle positions (Courtesy: Arburg Inc.)
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 135 (page 135)

1116.2 Injection Molding Machines and Their Classifications
Injection molding machines are classified in a number of ways. Based on the move-
ment of their clamp, they are classified as horizontal clamp or vertical clamp mold-
ing machines (see Figure 6.1(a)–(d)). Horizontal clamp machines are suitable for
most applications where the parts are ejected out of the mold and fall onto a con-
veyor or into a box due to gravity. Molded parts may then go through a secondary
operation before being packed and sent to the customer. Horizontal clamp ma-
chines are the most versatile machine and are most common. Vertical clamp ma-
chines are suitable for producing insert molded parts, where a horizontal parting
line is an advantage to seating inserts into the mold. It is the vertical clamp orien-
tation of a vertical molding machine that allows the mold parting to remain paral-
lel with the floor. This arrangement allows gravity to hold inserts or other compo-
nents to be over-molded into position in the lower half of the mold. Once the inserts
are positioned, the top half of the mold can be clamped into position over the in-
serts that have been placed into the bottom half. Vertical molding machines com-
monly have a rotary or a shuttle mechanism that moves the bottom half of the mold
from underneath the clamping mechanism to an area easily accessible by either an
operator or a robot for unloading the parts and loading the inserts. In most cases
there are two or more moveable mold bases. While inserts are being loaded into
one of the exposed mold bases, another mold base is clamped shut and being
inject
ed with plastic. This parallel activity saves time and increases output of the
insert molding process. It also helps in reducing residence time of the plastic in
the barrel.
Injection molding machines may also be classified based on the direction of plastic
injection. Horizontal injection machines are most common. Here, the injection unit
is mounted parallel to the ground and plastic is injected through a sprue bushing
usually mounted in the center of the mold. Plastic flows into the mold via the sprue
bushing, flowing through the center of the mold half, perpendicular to the parting
line of the mold (i. e., the split line where both mold halves separate). The runner
system delivers plastic to the cavities and is cut into one or both sides of the mold.
The sprue intersects the path of the runner in the center of the mold, allowing
plastic melt to be distributed to the cavities. Upon mold open, the molded parts and
runners remain on the moving side of the mold half. In this scenario, the hardened
plastic sprue is pulled out of the stationary mold half, leaving a long appendage of
plastic that can be gripped by the jaws of a robotic sprue picker as part of the part
ejection cycle. This is the standard horizontal molding arrangement. On the other
hand, some molded components with part design and/or mold design restrictions,
cannot use a sprue and runner configuration for delivery of plastic through the
center of one mold half. Instead, the sprue is eliminated and the entire runner sys-
tem has to be at the parting line. This is typically referred to as a parting line shot,
since the plastic is injected into the mold where the mold halves meet, on the part-
ing line. In such cases vertical injection of the plastic is required and therefore the
injection barrel is rotated to a vertical position. There is a limitation on the size of
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 136 (page 136)

112 6  Injection Molding and Molding Machines
the vertical injection unit because it is usually supported on tie bars. In some
cases, a vertical injection unit will have its own independent support units, but
these still have to be versatile in their horizontal movement to allow adjustment for
the position of the parting line on the mold.
Figure 6.2 Two shot (material) machine (Courtesy: Arburg Inc.)
Multishot machines have two or more injection barrels and are capable of molding
parts that are comprised of two different materials. A toothbrush is a common ex-
ample of a part produced by a two shot process. With the first shot, the plastic
substrate is molded. The mold is then opened and the cavities with the first shot of
plastic are indexed to align with the second injection unit. When the mold closes,
the second shot is injected over the now hardened first shot or substrate, creating
a two shot component that is ejected from the mold. Typically, the second shot is a
soft elastomers-type material typical for the soft handle molded over the tooth-
brush substrate. A two-shot machine is shown in Figure 6.2.
 6.3  Machine Specifications
Molding machines are most commonly specified by their tonnage and shot size.
When selecting the molding machine, these two are the primary specifications
that are considered. Once these requirements are satisfied, other specifications are
considered.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 137 (page 137)

1136.3 Machine Specifications
6.3.1Clamp Force (Tonnage)
The plastic is injected into the mold under high pressure. This pressure generates
a force on the mold face that can very easily open the mold during injection. To
prevent the mold from opening, the clamp is kept locked down by a counterforce.
The maximum available force to keep the mold closed is called the clamp force of
the machine. It is usually specified in tons and is therefore also called the tonnage
of the machine. Appendix B lists the different units that are used to specify ma-
chine tonnage.
6.3.2Shot Size
Shot size is another important parameter to consider when selecting a molding
machine. The shot size of a molding machine is determined by the maximum
weight of general purpose polystyrene (GPPS) that can be molded with a single
stroke of the injection molding screw. A shot size of 100
g
would indicate that a
GPPS part weighing no more than 100
g can be molded on t
he machine. It is be-
coming more common to use the volume of the cylinder that comprises the barrel
of the molding machine rather than the GPPS part weight because the latter can be
misleading. The density of GPPS is 1.06
g/cm3 and therefore, for the given volume
of the cylinder/barrel of the molding machine, it can hold more or less weight of
another material, depending on its density. To make matters simple, consider the
shot size of the machine to be 106
g, whic
h equates to 100
cm3 of volume. There-
fore, it can hold 106
g of GPPS. If t
his GPPS was replaced with low density poly -
e
thylene (LDPE) with a density of 0.91
g/cm3, the maximum shot size now is 91 g
of
LDPE. For a 30 % glass filled nylon (density of 1.33
g/cm3), the shot size is 133 g.
It is t
herefore now becoming common to specify the shot size in terms of volume
rather than weight. The setting of the shot size on the machine is also taking this
approach because it helps when moving the mold from one machine to another
machine of a different screw diameter. It is easier to match the shot volume than
calculate the new shot size in linear dimensions.
6.3.3Screw Diameter and L/D Ratio
As the name suggests, the screw diameter is the diameter of the screw, either in
millimeters or in inches. The barrel diameter is only slightly bigger than the screw.
For example, for a 50
mm
screw, typical barrel clearance is 0.1
mm
(4 thousands of
an inch). Over time, screw wear can cause material leaking over the screw flights,
causing inconsistency from shot to shot.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 138 (page 138)

114 6  Injection Molding and Molding Machines
The ratio of the length of the screw to the diameter of the screw is called the L/D
ratio. The higher the L/D ratio, the better is the melt homogeneity.
6.3.4Plasticating Capacity
The plastic has to be melted and heated to its processing temperature. The melting
of the plastic is accomplished by the heater bands around the barrel and the shear
heat generated by the rotating screw. The screw is also transporting the plastic to
the front of the barrel, ready to be injected into the mold. Barrel temperature, expo-
sure time, and screw speeds are all important to get a good homogeneous melt. If
the material is moved too fast, the plastic pellets may not have enough time to melt,
and the melt can contain plastic pellets that are not or only partially melted. Dur -
ing the purging process, it is common to see unmelted pellets of polyethylene com-
ing out of the nozzle tip if high screw speeds were used. Plasticating capacity is the
maximum weight of GPPS that can be raised to the molding temperature and me-
tered in front of the screw. It is usually expressed in kilograms or pounds per hour.
6.3.5Maximum Plastic Pressure
Thin-walled parts require more pressure to fill than do thick-walled parts. There-
fore, depending on the application, the maximum available pressure needs to be
specified. For hydraulic machines, the maximum available plastic pressure de-
pends on the maximum available hydraulic pressure and the intensification ratio
of the screw. Plastic pressure is specified in pounds per square inch or bar or other
pressure units.
There are other parameters that are specified on machine data sheet. Discussions
of these are beyond the scope of this book. Suggested books on this topic are men-
tioned at the end of this chapter.
 6.4  The Injection Molding Screw
The injection molding screw and barrel assembly is responsible to help deliver the
right quality of melt to the mold. Electric heater bands are installed around the
barrel and supply radiant heat energy to melt the plastic. However, it is the screw
that plays the vital role in the process of achieving a homogeneous melt. The screw
provides shear heat to assist in the melting process along with the required mixing
and homogenizing of the melt. It also helps in accurately measuring the volume of
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 139 (page 139)

1156.4 The Injection Molding Screw
the shot to be injected into the mold. Several designs of screws have been devel-
oped based on different materials and their needs. The most common screw is
called a general purpose screw or the GP screw. The design of a GP screw is shown
in Figure 6.3.
Figure 6.3 The general purpose screw
The GP screw has three main sections (or zones), each of which serves a special
purpose. They are described in the following together with some other terms. The
screw construction can be described as a shank with flights that are wrapped
around it. In most cases, there is only one ribbon that creates the flights.
Outside Diameter: This is the diameter of an imaginary cylinder that is created by
joining the outside area of the flights. The outside diameter is constant and is
slightly smaller than the internal diameter of the barrel.
Root Diameter: This is the diameter of the shank. The root diameter changes from
the back to the front of the screw, depending on the section of the screw.
Channel Depth: The difference between the outside diameter, and the root diameter
is the feed depth. Since the root diameter changes, the feed depth also changes
from the back to the front of the screw.
Feed Zone: This is the section of the screw that picks up the material from the feed
opening (base of the hopper) and begins to soften the material as it is being con-
veyed. The root diameter is the smallest here and is constant. Since the root dia
-
me
ter is constant, the channel depths are also constant; they are also called the
feed depth. In the feed zone, the material is picked up and is softened as it is con-
veyed by the rotation of the screw. The material must never be completely molten
in this section because that would prohibit the picking up of additional material.
A term commonly used to describe this phenomenon is screw slipping, where the
melt rotates with the screw and prohibits the screw from moving back to pick up
more material and build the next injection shot.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 140 (page 140)

116 6  Injection Molding and Molding Machines
Transition Zone (Compression Zone): In this section, the root diameter increases
gradually, resulting in the decrease of the channel depth. At the start of this sec-
tion, the root diameter is the same as the root diameter of the feed section, where it
gradually increases until the section ends. This causes the feed depth to steadily
decrease. As the screw rotates, the softened pellets begin to get compressed and
the air and any other volatiles are forced out from between them because the feed
depth is decreasing and the plastic is being conveyed. With the help of heat from
the external heater bands and the shear from the rotation of the screw, the plastic
begins to melt. As the feed depth reduces because of dispersive and distributive
mixing, the plastic ends up as a homogeneous melt by the time it reaches the end
of the transition zone. Distributive mixing occurs when the melt streams distribute
and reconvene. On the other hand, dispersive mixing is similar to a smearing
action. Ther
e is a combination of distributive and dispersive mixing taking place in
the barrel.
Metering Zone: The metering zone is the last zone and is the closest to the nozzle of
the machine. The depth of the channels in this section is minimal compared to the
other two sections. The root diameter stays constant and therefore the channel
depth is also constant. Since the shot is built by moving the screw back until it
reaches a set linear position (shot size), the metering depth must be as minimum
as possible to reduce the variation in the amount of melt for each consecutive shot.
With a larger metering depth, the amount of material that is fed in front of the
screw can vary, leading to inconsistencies. However, as the depth reduces, the
shear increases and, therefore, the risk of material degradation is also increasing,
especially for shear sensitive materials such as PVC. A compromise must be found
and special screw designs are therefore necessary for certain types of materials.
Figure 6.4 shows the melting progression of the plastic as it travels through each
of these sections. In the feed zone, the pellets have softened and begin to adhere to
each other. When they travel to the transition zone, there is a combination of
melted and unmelted plastic. There is still evidence of plastic pellets that have
been compressed together. The metering and transition zones are the same, and
the feed zone is usually twice the length of any of one these sections. In custom
designed screws, these lengths can be altered. Longer feed zones increase the
throughputs, longer transitions decrease shear, and a longer metering section will
output a more homogeneous melt but will create more shear.
Compression Ratio: This is the ratio of the feed section channel depth to the meter-
ing section channel depth. It defines the amount of compression to which the ma-
terial has been subjected. The higher the compression ratio, the better is the melt
homogeneity, but also the higher is the shear. The depth of the channels also con-
tributes to the amount of shear heat, melt homogeneity, and the throughput.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 141 (page 141)

1176.5 Screw Designs
Figure 6.4 Melting progression of the plastic as it travels through the sections of the screw
Typical compression ratios are mentioned below:
 Lo
w compression ratio: 1.5 : 1 to 2.5 : 1 used for shear sensitive materials such as
PVC
 Medium com
pression ratio: 2.5 : 1 to 3.0 : 1 used in general purpose materials
 High
compression ratios: 3.0 : 1 to 5.0 : 1 used for crystalline materials such as
nylons
Helix Angle: This is the angle of the flight in relation with the plane perpendicular
to the screw axis.
L/D Ratio: The L/D ratio is the working length of the screw flight to the outside
diameter of the screw. Most injection molding screws have L/D ratios of 20 : 1.
Greater L/D ratios allow more exposure of the plastic to heat and shear, improving
the melt homogeneity and therefore increasing throughput at the desired process-
ing temperature.
 6.5  Screw Designs
The screw described in Figure 6.3 was a general purpose design that can be used
for most materials and in most situations. Screws have been designed for specific
requirements, such as for shear sensitive materials or to improve the throughput
to reduce cycle times. Screw designs also depend on the degree of crystallinity, the
viscosity, and the additives present in the plastic. In injection molding, mixing
screw designs and barrier screw designs are most common. Mixing screws, as the
name suggests, help to mix the additives such as colorants and also help to im-
prove melt homogeneity. There are certain sections incorporated into the screw
that create the mixing effect. Barrier screw designs have two screw channels in the
transition section of the screw separated by a barrier flight. The unmelted plastic
stays in the first channel until it is completely molten and then moves on to the
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 142 (page 142)

118 6  Injection Molding and Molding Machines
second channel. This ensures that the plastic is completely molten before it reaches
the metering section. Examples of screw designs are shown in Figure 6.5.
Figure 6.5 A mixing screw and a barrier screw (Courtesy: Westland Corporation)
 6.6  The Check Ring Assembly
The check ring assembly is essentially a nonreturn valve. The most popular design
is shown in Figure 6.6. During the shot build-up process, the screw is rotating to
pick up the material. During this time, the check ring is in the forward position
and allows the passage of the material to the front of the screw. During injection,
the check ring seats itself on the body and stops the plastic from being pushed
back over the flights, acting as a one-way nonreturn valve. Check rings wear over
time, and the plastic will begin to leak into the flights. This causes inconsistency in
the shot and therefore shot-to-shot variations. Check rings must be checked period-
ically and changed at the slightest sign of leakage. Various designs of check rings
are available on the market for specific materials and applications.
Figure 6.6 Working of a check ring
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 143 (page 143)

1196.7 Intensification Ratio (IR)
Other types of check rings include ball check valves that are suitable for unfilled,
nonshear sensitive materials such as polyolefins. Smear valves are used to process
highly viscous materials such as rigid PVC. There is no shut-off mechanism in a
smear valve. The high viscosity helps to prevent the back flow of the plastic during
injection.
 6.7  Intensification Ratio (IR)
To understand IR (intensification ratio), consider a hydraulic piston: a cylinder ar-
rangement as shown in the schematic (Figure 6.7) A pressure of 800
psi
is applied
on the larger cross section of 6
in2. Therefore the total force on the hydraulic oil
behind the piston is 800
×
6
=
4800 lb. Ther
e is a reduction of the cross section
area from 6
in2 to 2 in2. The force of 4800 lb is t herefore applied on the smaller
cross section of 2
in2. Therefore, the calculated pressure on other side of the
smaller piston is 4800/2
=
2400 psi. The r
eduction of the diameter from 6
in2 to
2

in2 increases the pressure from 800 psi t o 2400 psi, so t he pressure is intensified
3 times. This number is the ratio of the larger diameter to the smaller diameter and
is the intensification ratio.
PRESSURE
= 800 PSI
FORCE
= 800 x 6
= 4800 lb
C/S AREA = 6 SQ IN
C/S AREA = 2 SQ IN
PRESSURE
= 4800/2 PS
I
= 2400 PSI
FORCE = PRESSURE X AREA
OR
PRESSURE = FORCE / AREA
INTENSIFICATION RATIO = A1/A2= 6/2 = 3
4800
lbs
Figure 6.7 Schematic for intensification ratio
To drive a nail into a wall, the force is applied to the head of the nail. The cross
section of the area at the head of the nail is comparatively larger than the point.
Therefore, the applied force of the hammer at the head of the nail is intensified at
its point and this is what pushes the nail into the wall. This is only an analogy be-
cause in injection molding, we deal with fluids and not solids. The laws of physics
are different for fluids and solids. In injection molding, there is a hydraulic ram at
the back on the molding screw where hydraulic pressure is applied. This force is
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 144 (page 144)

120 6  Injection Molding and Molding Machines
intensified at the screw tip and converted to plastic pressure. The ratio of the cross
sectional area of the ram to the cross sectional area of the screw is called the inten-
sification ratio (IR), see Figure 6.8. Plastic pressure at the nozzle is equal to the
product of the applied hydraulic pressure and the IR. Intensification ratios range
from about 6 : 1 to as high as 23 : 1. Higher IRs are necessary to mold thin parts
with long flow lengths. In electric machines, there is no hydraulic ram and the
pressure applied to the back of the screw is what the plastic experiences so that
the IR for an electric machine is equal to 1.
Plastic Pressure = Hydraulic Pressure × Intensification Ratio
Figure 6.8 Intensification ratio
When a mold is moved from one molding machine to another, in order to mold
identical quality parts, the plastic molding process on both machines must be
identical. One of the factors that need to be matched is the plastic pressure. The
plastic pressure needs to be calculated with the formula above and then the hy -
draulic pressure on the 2nd machine needs to be back calculated from the same
formula. An example of this is shown in Table 6.1. If the packing pressure used
on Machine 1 is 800
psi and t
he intensification ratio is 10, the applied plastic
pr
essure is 8000
psi. If t
he mold is moved to Machine
2 wit
h an intensification
r
atio of 13.5 then to get a plastic pressure of 8000 on Machine 1
a pr
essure of
8000/13.5
= 593
psi mus
t be used. If the hydraulic pressures are matched then the
plastic pressure will equal to 800
×
13.5
=
10,800 plas
tic psi which could result in
flashed parts and/or dimensionally nonidentical parts.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 145 (page 145)

1216.8 Obtaining Intensification Ratios
Table 6.1 Process Transfer between Machines, Matching Plastic Pressures
Parameter Machine 1 Machine 2
Intensification Ratio 10 13.5
Case 1:
Holding Pressure –
Hydraulic
800 psi 8000 / 13.5 = 593 psi
Holding Pressure –
Plastic
800

×

10 = 8000 psi Required = 8000 psi
Case 2:
This could result
in flash and/or
dimensionally
un
-
accep
table parts
Holding Pressure –
Hydraulic
800 800 psi
Holding Pressure –
Plastic
800 × 10 = 8000 psi 800 × 13.5 = 10,800 psi
 6.8  Obtaining Intensification Ratios
Getting the IR number directly from the machine manufacturer can sometimes be
a challenge. However, there are couple ways that these can be obtained.
Some machines provide a graph like the one shown in Figure 6.9. The different
screws sizes that are compatible with the machine are mentioned. Based on the
screw size of the machine, one can calculate the IR by dividing the plastic pressure
value by the hydraulic pressure value. The graph can also be used to find the plas-
tic pressure at any given hydraulic pressure setting on the molding machine.
0
3000
6000
9000
12000
15000
18000
21000
24000
27000
30000
33000
02 00 4006 00 8001 0001 2001 4001 6001 8002 0002 2002 400
Plas/g415cPressure vs Hydraulic Pressure
Hydraulic Pressure
Plas/g415c Pressure
A Hydraulic Pressure of 2200 psi is equal to
a) Plas/g415c Pressure of 21000 psi on
a 40 mm screw
I R = 21000/2200 = 9.54
b) P las/g415c Pressure of 30000 psi on
a 30 mm screw
I R = 30000/2200 = 13.63
Figure 6.9 Calculation the IR from the graph provided by the machine manufacturer
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 146 (page 146)

122 6  Injection Molding and Molding Machines
If such a graph is not available, the machine specification sheet can be helpful. The
machine specification sheet should list the maximum plastic pressure. On the
molding machine, if the injection pressure setting is selected the machine usually
displays a range of pressures. The higher number is the maximum hydraulic pres-
sure of the machine. If the maximum plastic pressure from the specification sheet
is divided by the maximum hydraulic pressure of the machine, the resulting value
is the IR. In case the machine does not show the range of pressures an input of a
very high number in the field will alarm and provide the user with the maximum
hydraulic pressure value.
 6.9  Selecting the Right Machine for the Mold
The machine selection is one of the five important factors that will contribute to the
quality of the part. The mold and the machine must be compatible, and this is often
overlooked. Usually, only two factors are taken into consideration: whether the mold
physically fits in the machine and whether the clamp tonnage is sufficient. However,
one of the most important factors is what percentage of the machine shot size will
be used. The residence time of the material in the barrel and the lower limiting size
of the mold are other factors. Both are described in the following.
6.9.1Physical Size of the Mold
The mold size is defined by three variables (see Figure 6.10).
Figure 6.10 Mold size specifications
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 147 (page 147)

1236.9 Selecting the Right Machine for the Mold
Mold Stack Height (H): This is the distance between the sides of the mold in the
direction of the mold open and close when the mold is fully shut.
Mold Width (W): This is the distance between the vertical sides of the mold, looking
in the direction of injection of the plastic. This applies to molds mounted in hori-
zontal machines, but the definitions are extended to other molds also.
Mold Length (L): This is the distance between the top and bottom side of the mold,
looking in the direction of injection of the plastic. This again refers to horizontal
molds.
Naturally, the mold must fit in the machine such that at least two sides can be
bolted to the platen of the machine. The mold can hang off the platens on the other
two sides, but the molding area must not be outside the platen. The molding area
must always be supported by the platen, see also Figure 6.11. If the cavity is not
supported, the injection pressure can easily deflect the plates and cause flash in
the part. Injection pressures can be very high, applying tremendous force on the
mold base, and over time, can damage the mold components if the mold is not
properly supported by the mold platens. On the other hand, the mold must not be
considerably smaller than the platen. It must cover at least 70 to 75 % of the area
between the tie bars. This is especially true for toggle machines, where the clamp-
ing force is applied on the outside and not in the center of the platens. There is a
possibility of platen deflection, if the mold is too small, causing platen damage over
time. The toggle system also provides reduced support in the center of the mold
where the main injection pressure is applied. Even with adequate support pillars
in the mold, there still could be deflection because of the lack of support, causing
part defects.
Cavities
outside
the platen
area
Figure 6.11 Cavities outside the molding area
In regards to the mold height, every machine has a minimum and a maximum
mold height that it can accept. The moving platen closes the mold and applies the
set tonnage to the mold. Because of the limit on the travel distance during closing,
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 148 (page 148)

124 6  Injection Molding and Molding Machines
the mold height needs to be greater than this limit. If the mold is less than the
minimum mold height, the platen can never let the two halves of the mold touch
and apply the tonnage. Therefore minimum mold height is important. On the other
hand, the mold must be smaller than the maximum mold height in order to fit in
the machine.
The required mold open stroke will depend on the part, usually the part dimension
in the direction of ejection. The open stroke should be such that the mold halves
are far enough apart when fully opened so that the part falls out of the mold after
ejection. The mold open stroke must be greater than the longest dimension of the
part in the direction of ejection. For example, on a rectangular part as shown in
Figure 6.12, it should be the diagonal of the part. Even with this distance, there is
still a danger of damaging the part because it may still hit the side of the mold as it
falls off the ejectors. For this reason, the mold opening stroke must be set as wide
as possible to avoid damage, but not such that cycle time is lost due to unnecessary
movement of the mold.
Minimum mold open
distance > max length
of the part in any direction
Mold open
Figure 6.12 Minimum mold open distance
6.9.2Calculating the Required Machine Tonnage for a Mold
The injection pressure of the plastic applies an outward force on the mold cavities,
which works to separate the mold halves. This force must be counter balanced by
the machine in order to keep the mold halves closed. If the plastic pressure is higher
than the clamp force applied to keep the mold closed, the mold will open, and the
plastic will escape from the mold at the parting line where the mold splits open,
causing part defects, typically flash. The force that keeps the mold closed is called
the clamp tonnage of the machine. The applied clamp force is measured in tons.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 149 (page 149)

1256.9 Selecting the Right Machine for the Mold
The area of the mold that experiences the plastic injection pressure is perpendicu-
lar to the direction of mold open and close and is called the projected area. Refer to
Figure 6.13. The shaded area is the projected area. In some molds, slides are used
to create some of the features of the part. The slides move in and out as the mold
closes and opens because of an angled pin or a heel block. The plastic injection
pressure can exert a force on the slide and can in turn force the mold open action.
In such case, the area of the slide exposed to the plastic must be added on to the
projected area.
A
A
SPRUE
RUNNER
CAVITY
3.00
2.00
SECTION A –A
 Area of 1 Cavity = 2 x 3 = 6 Sq Inches
 Area of 4 Cavities = 6 x 4 = 24 Sq Inches
 Area of the Runner = 4 x 1 = 4 Sq Inches
Total Projected Area = 24 + 4 = 28 Sq Inches
Direction of
Mold Open –C lose
Figure 6.13 Projected area of a mold
The rule of thumb for calculating the tonnage required for the part is given in:
Required tonnage = (Projected area of the part × Number of cavities + Projected
area of the runner) × (Tons / in
2 required for the resin)
Depending on the plastic material properties, every material requires a certain
amount of force during the mold fill and then requires a certain amount of pres-
sure to pack the part out. Typically, crystalline materials require 3.5 to 4.5 tons of
clamp force per square inch of projected area, while amorphous materials require
anywhere between 2.5 to 4.0 tons of clamp tonnage per square inch of projected
area. The calculation is only a rule of thumb since there are several factors that
need to be considered.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 150 (page 150)

126 6  Injection Molding and Molding Machines
 6.10  The R ule of Thumb for Tonnage
Is Only an Estimate
The calculation mentioned in the previous section is a good estimation but by no
means a perfect calculation. Following are the factors that affect tonnage (Refer to
Figure 6.14):
More Tonnage to fill More Tonnage to pack
l l a W k c i h Tl l a W n i h T
4 Gates1 Gate
More Tonnage Less Tonnage
Edge Gate
More Tonnage Less Tonnage
Center Gate
All parts have
identical
projected area
values
Edge Gate
More Tonnage Less Tonnage
Sequential Gates
1 2 3
Figure 6.14 Factors affecting required tonnage on parts with identical projected areas
1. W all thickness: Thinner parts need more pressure to fill the cavity whereas
thicker parts will require more packing pressure to compensate for the shrink -
age. Two parts can have the same projected area but the thicker part will re-
quire more tonnage because it needs to get packed out more than the thinner
part. However, in a part such as in a laptop cover, a very thin wall with a long
flow length will also require more tonnage to withstand the high injection pres-
sures required to fill the part. Thin walls constitute parts as thin as 0.5
mm
(0.020
in) and t
hick walls are those above 7 to 8
mm (about 0.3
in). N
ominal
walls are usually between 2 and 5

mm (0.080 to 0.200

in) thick.
2.
N
umber of gates: The more the number of gates, the easier it is to fill the mold
and less pressure is required to pack the cavities out. Two parts can have the
same projected area but the one with more gates will require less tonnage.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 151 (page 151)

1276.10 The Rule of Thumb for Tonnage Is Only an Estimate
3. P osition of the gates: If the part edge is gated, it will require more tonnage com-
pared to as if it is gated in the center because the flow length is cut into half
when the part is gated in the center.
4.
Seq
uential valve gating: Molds that are sequentially gated require less tonnage
because the force is being applied only in the areas that are influenced by the
open gates.
5.
Or
ientation of the part in the mold: In Figure 6.15, the same part is shown to
have injection points from two different directions. Using the above formula, the
required tonnage when the plastic is injected from the side will be lower than
when injected from the front. This does not mean that the part can be run on a
lower tonnage press. The flow length would then play a role in the tonnage.
L
L
W H
Projected
area
Projected
area
Direction
of injection
Direction
of
injection
Figure 6.15 Part projected area in the direction of injection
Tonnage calculation is very complex and not easy to predict. Computer simulation
programs do an acceptable job in this calculation, but caution is warranted when
applying the results.
6.10.1Percentage Shot Size Used and Number of Shots in the Barrel
The percentage of the shot size used is the most important factor for molding con-
sistency and is often overlooked. The percentage of the shot size gives an idea of
the amount of plastic injected into the mold with respect to the maximum amount
of plastic the barrel can hold or the fraction of the shot size that is injected into the
mold. The formula for this calculation is given in:
% Shot Size used = ((((Part weight × Number of cavities) + Runner weight))
× (1.06/(Density of the plastic)))/(Shot size of the machine) × 100
The percentage of the shot size used must be always between 20 and 80 % of the
available shot size.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 152 (page 152)

128 6  Injection Molding and Molding Machines
A number below 20 % could result in the following problems:
 The mac
hine needs a finite amount of time to build and achieve the set pressures
and speeds. It is similar to listening to a commercial for a car that claim “0 to
60
m
ph in 5 seconds.” This tells us that the car will require 5 seconds to reach
60
m
ph and so at the end of 2 seconds, the speed is not yet what the driver has
set to achieve. Therefore if the molding shot is very small, the injection phase
can be inconsistent because not enough time is given for pressure and velocity to
reach required levels. Moreover, the plastic that has now built up the pressure is
suddenly stopped, and the momentum is unpredictable, leading to large varia-
tions in the fill.
 In case of cr
ystalline materials, the shear heat from the turning screw is an im-
portant factor for melting the crystallites and achieving a homogeneous melt. If
the shot is very small, then the screw may make very few revolutions to reach
the set shot size limit. This results in the loss of shear heat and therefore affect-
ing the melt homogeneity.
 W
ith smaller shots, the residence time of the plastic in the barrel increases. This
can lead to material degradation.
 Plas
tic melt is compressible. When pressure is applied to a small shot, some of
the applied pressure is lost in compressing the melt leading to the inconsistency
in fill. On larger shots sizes, there is a compression of the melt but the percent-
age compression is much smaller as compared to a smaller shot.
A number above 80 % could result in the following problems:
 As descr
ibed in Section 6.1, the material needs to spend the required amount of
time in order going through the melting and homogenization process. A large
shot size will transport the material quickly, and the material will not have a
chance to form a homogeneous melt for the injection shot. For example, during
the startup of a machine, when the machine is being purged using high screw
speed and back pressures, sometimes unmelted pellets can be seen coming out
of the nozzle tip. This is because the pellets did not have enough time to melt and
homogenize because of the higher percentage shot sizes used in purging (Figure
6.16). In the case of hot runner molds, there is an added challenge of transfer -
ring the pressure applied to the screw through the hot runner. When the shot is
large, the pressure applied has to first compress the plastic in the barrel, then in
the hot manifold, and then inject the plastic in the mold. The larger the shot, the
more inconsistency.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 153 (page 153)

1296.10 The Rule of Thumb for Tonnage Is Only an Estimate
Figure 6.16 Unmelted plastic pellets in the purge as a result of moving too fast through the
molding barrel
Deviation from the 20 to 80% rule:
It is no
t always possible to have a machine that fits the 20 to 80 % rule for the shot
size of a given mold. Almost every molder has such a mold and they can mold per-
fectly acceptable parts.
On the low end, the preferred number is 20 %. Following are the situations where
numbers less than 20 % could be acceptable:
 If t
he molded part has wide dimensional tolerances. In such cases, any variations
from the inconsistent fill that cause a variation in the dimensions can be ab-
sorbed by the tolerances.
 If
the molded part is being molded out of a heat stable material, such as a poly -
ethylene or a polypropylene. Chances of material degradation is low.
 R
ecent advances in machinery controls have improved the accuracy and control
of the injection phases of the molding cycle. In such cases, deviations from the
rule can be considered.
On the high end, the preferred number is 80 %. Unless the screw design is a spe-
cially optimized screw for efficient melting with large shot sizes, the rule should
never be deviated from. Larger L/D ratio screws help in efficient melting.
As the term suggests, the number of shots in the barrel would mean how many
shots are present in the barrel. As an example, if the machine shot size is 60 grams
and the injected shot weight is 5 grams, then there would be 4 shots in the barrel.
The barrel usage would be 25 %.
Cautionary Notes: Hot runner manufacturers can provide information on the vol-
ume of the hot manifold. This volume should not be used in the calculation of the
percentage of the shot size. The formula mentioned above is a good estimate be-
cause to get the exact percentage shot size number, one needs to add on the amount
of melt that is on the molding screw, and at the same time, subtract the material
that is not being used for the shot. Only the amount of plastic required for the shot
is melted and collected in front of the screw. The machine does not collect the com-
plete maximum shot and then inject what is required.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 154 (page 154)

130 6  Injection Molding and Molding Machines
6.10.2Residence Time of the Material in the Barrel
Residence time is related to the percentage of the shot size used and can be defined
as the total amount of time the plastic resides in the injection unit. The total time
from entering the feed throat to exiting the nozzle is called the residence time of the
plastic in the barrel. The calculation is shown in the following equation.
Residence time Shot capacity of the machine
Part weightN
=
×
()
uumber of cavitiesR unner weight1 .06/ Density of the p()() +× llastic
Cycle time
()()
×
In simple terms residence time can also be calculated as shown here:
Residence Time = Number of Shots in the barrel × Cycle Time.
Every material has a maximum recommended residence time in the barrel. Be-
cause plastics are heat sensitive, they will degrade when overexposed to molding
temperatures. PVC is a prime example of a material that cannot be left in the barrel
for long periods of time. It degrades quickly and releases hydrochloric acid, an
ir
ritant and hazard. Residence time numbers, typically in minutes, are provided by
the material manufacturers. Depending on the grade of PVC, the maximum resi-
dence time is between 4 to 7 minutes. Maximum acceptable residence time for the
same material can be different based on the molding temperature used. The higher
the molding temperature, the shorter is the recommended residence time. In the
case of Ultem, a polyetherimide from the Sabic company, the maximum residence
time at 365 °C is 14 minutes whereas at 410 °C it drops to 6 minutes.
Residence time depends upon the cycle time, the L/D ratio of the screw, and the
lengths of the metering and compression sections of the screw. In the case of a hot
runner mold, the residence time in the hot manifold must also be added to the time
in the barrel. Hot runner manufacturers can provide the volume of the hot mani-
fold and this can be used in the calculation.
6.10.3 Pr actical Methods to Find Percentage Shot Size,
Shots in a
Bar
rel, and Residence Time
Please note that extreme caution needs to be exercised during any tests at the
molding machine. Only those with sufficient experience with molding machines
should perform these tests. A simple and practical method can provide the number
of shots in the barrel: As the molding machine is in operation, the hopper system
can be pulled away, and a color pellet is dropped at the bottom of the feed throat
when the molding screw is visible. Next, push the hopper system back in place,
and starting from the next injection, count the number of shots until the color
shows up in the part. This will be the number of shots in the barrel.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 155 (page 155)

1316.10 The Rule of Thumb for Tonnage Is Only an Estimate
Calculate the residence time by multiplying the number of shots in the barrel with
the cycle time. Calculate the percentage of the shot size used by taking the reci
-
pr
ocal of the number of shots in the barrel and multiplying it by 100.
For example: Cycle Time = 15 sec
One Shot Weight = 5 grams
Number of Shots till color showed up in the parts = 3
Calculated Residence Time = 6 × 15 = 90 minutes = 1 min 30 sec
Calculated % Shot Size used = (1/6) × 100 = 33 %
6.10.4Residence Time Distribution
The screw is designed to mix the plastic and additives, such as color pellets. There-
fore the system is not truly a first in, first out system. There is no buildup of the
plastic in any part of the barrel or the screw, but because of the mixing, the mole-
cules could spend more or less time in the barrel. The more effective the screw
mixes in, the higher the distribution. Needless to say, the higher the number of
shots in the barrel, the larger the distribution seems to be, but this can get mis-
leading. For example, if there are 3 shots in the barrel, then the added color pellet
may get mixed in only one of the three shots where as if there are 12 shots in the
barrel then the added color will get disctributed in 4 shots. If any change is made
in the processing parameters involving times and temperatures, then the number
of shots in the barrel should be molded and discarded before collecting parts for a
quality check.
Suggested Reading
Chabot, J., The development of plastic processing machinery and methods, John Wiley and Sons, Inc.
(1992) New York
Osswald, T. A., Turng, L., and Gramann, P. J., Injection Molding Handbook (2007) Hanser Publishers,
Munich
Beaumont, J. P., Nagel, R., and Sherman, R., Successful Injection Molding (2002) Hanser Publishers,
Munich
Rosato, D. V. and Rosato, D. V, Injection Molding Handbook (2000) CBS, New Delhi, India
Dray, R., How to compare barrier screws, Plastics Technology (Dec. 2002), p. 46
Dealy, J. and Wissbun, K., Melt Rheology and its Role in Plastic Processing Theory and Applications (1990)
Van Nostrand Reinhold
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 156 (page 156)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 157 (page 157)

Scientific Processing,
Scientific Molding, and
Molding Parameters
 7.1  Introduction
Several parameters determine a successful molding process. There are various
speeds, pressures, times, and temperatures to be considered. Scientific processing
encompasses an understanding of the underlying scientific principles of each pa-
rameter and the application of these principles to achieve a robust process and
consistency in part quality. Scientific processing covers the complete molding pro-
cess, from the time the plastic enters the facility to when it leaves as a finished
product. A robust process is one that can accept reasonable natural variations or a
small purposeful change in an input but still delivers consistent output. The term
consistency means molding parts with the least variation in the quality of the part.
The quality of the part can mean its dimensions, appearance, part weight, or any
other aspect that is important to the form, fit, or function of the part. The variation
should be from special cause variations and not from any natural cause variations.
Special cause variations are variations that are caused by an external factor. For
example, if the chiller unit shuts down, the mold temperature will change causing
a change in the quality of the part. Natural cause variations are inherent to the
process. Their effect can be minimized but not eliminated. For example, if the plas-
tic used to mold the parts has 30 % of glass fiber mixed in it, in every molded shot
the amount of glass will not be exactly 30 %. It will be slightly more or less, for
e
xample, between 29.7 and 30.3 %. If one weighs 100 consecutive parts from the
molding process, each part will weigh differently although the process was not
changed. This variation cannot be eliminated, but the mixing process can be im-
proved, and the variation can be reduced.
Robustness and consistency should not be confused with parts being molded
within the required specifications. Parts can be out of specifications but the pro-
cess can be robust and the quality can be consistent. The goal of scientific process-
ing is to achieve a robust process at each stage of the molding process the pellet is
subjected to.
7
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 158 (page 158)

134 7  Scientific Processing, Scientific Molding, and Molding Parameters
The term scientific molding was coined by a two pioneers in the field of injection
molding, John Bozzelli and Rod Groleau. Their principles and procedures are
widely used today and are industry standards. Scientific molding deals with the
actual plastic that enters the mold during the molding operation at the molding
machine. The term introduced here is scientific processing, which is defined as the
complete activity the plastic is subjected to from the storage of the plastic as pellets
to the shipping of the plastic as molded parts. Scientific processing is applying
scientific principles to each of the steps involved in the conversion of the plastic to
the final product, see Figure 7.1. Chapters 8 and 9 will focus on the understanding
and the application of the theories to each of these steps and then optimizing them.
Successful process development results in a process that is robust, repeatable, and
reproducible.
Plastic Enters The Facility
Storage
Molding Process
Mold
Preconditioning
Ejection Out Of The Mold
Packaging
Shipping
Plastic Pellet
Plastic Part
Scientific
Molding
Scientific
Processing
Figure 7.1 The journey of the plastic pellet and the critical factors that need to be controlled
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 159 (page 159)

1357.1 Introduction
7.1.1Process Robustness
A process is considered robust when changes to the inputs have minimum effects
on the quality of the part. The changes here can be intentional or may be due to
natural variations. Naturally, intentional changes must be within reason. In gen-
eral, a process becomes more robust as larger input changes can be introduced
without adversely affecting the resulting output part quality. For example, after a
certain injection speed is reached, the viscosity of the plastic remains constant.
The viscosity curve is in a robust area and variations in injection speed have little
effect on the viscosity and therefore the amount of fill into the mold. At low in
-
jection speeds, a slight c
hange in the injection speed causes a large change in the
viscosity, resulting in shot-to-shot fill inconsistency. Therefore, this is not a robust
area of the process and should be avoided. In addition, it must be understood that
natural variations can never be eliminated. Taking these conditions into consider-
ation will help ensure building a robust and consistent process.
7.1.2Process Consistency
A process is considered consistent when it meets the following two requirements:
1.
All
variations in the outputs of the process are a result of only natural cause
variation.
2.
The s
tandard deviation of the variation is at a minimum value.
For example, the cushion value is an output of the injection, pack, and hold phases.
If the cushion value shows minimum variation, and a distribution curve of the
cushion value over time is normal, then the process is consistent. In this case, the
process under consideration would include only the injection, pack, and hold
phases.
A robust process will always produce parts of consistent quality because there is
little variation in the output. It also goes without saying that for the quality to be
consistent, the process must be robust. For injection molding, whenever there is an
inconsistency in part quality, the robustness of the process is usually suspect be-
cause the process is reflected in the part quality. In general, based on how robust
the process is and on the required tolerance limits, we consider four possible re-
sulting production process scenarios, as shown in Figure 7.2, which shows a rep-
resentation of a run chart for a particular dimension.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 160 (page 160)

136 7  Scientific Processing, Scientific Molding, and Molding Parameters
USL
(a) Non-robust process with special cause variation producing parts out of specificatons.
(b) Non-robust process with special cause variation producing parts within specificatons.
NOM
LSL
USL
NOM
LSL
(c) Robust process with common cause variation producing parts out of specificatons.
(d) Robust process with common cause variation producing parts within specificatons.
USL
NOM
LSL
USL
NOM
LSL
Figure 7.2 Types of processes based on variations and tolerances
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 161 (page 161)

1377.1 Introduction
Figure 7.2(a) shows a process that is not robust because of dimensional changes in
the part. The first four data points are closer to the upper specification limit, but
the next data point drops down towards the lower specification limit. There are
some parts being molded out of specifications. Figure 7.2(b) shows the same pro-
cess, however with increased tolerances; this process is producing parts within
specifications. In both these cases, a special cause variation seems to be contribut-
ing to the inconsistent part quality. An attempt must be made to eliminate this
variation even though in the second case, the parts are within the required speci-
fications. Figures 7.2(c) and (d) both represent a robust process, because the qual-
ity distribution is normal. In Figure 7.2(c), the tolerance limits are such that this
process although robust, produces parts out of specifications. In Figure 7.2(d), the
tolerances are wider than in Figure 7.2(c) and, therefore, the same process now
produces acceptable parts. Clearly, the process in Figure 7.2(d) is the most desira-
ble process. Setting of the tolerance limits is done by the product engineer. In some
cases, the engineer does have the flexibility to open up the tolerances based on the
form, fit and function of the part. If opening of the tolerances is not acceptable to
the product engineer and if it is not possible with the current process setup to re-
duce the variation, alternative solutions such as selecting another plastic, chang-
ing the amount of filler, or using cavity pressure control must be considered. As
mentioned earlier, an attempt must always be made to eliminate the special cause
variation, even if the parts are within the required specifications. This makes part
quality more predictable and the manufacturing process less vulnerable to mold-
ing defective parts. Another benefit of implementing the discipline of developing
robust processes is a reduction in part inspection frequency and sample sizes. The
goal of process development, using scientific principles and techniques, must be to
establish a process that is consistent and well within the specification limits simi-
lar to the one shown in Figure 7.2(d). Simply molding parts within the specifica-
tion limits does not necessarily mean that the process is robust and stable.
There are ways to improve the robustness of a process, reduce variation, and im-
prove consistency. The aim of process development should be to develop a stable
and robust process.
There are systematic steps that must be followed in order to achieve this goal. Un-
fortunately, these steps are often ignored because they are time consuming and
can increase the number of mold trial iterations. Often overlooked is the amount of
time, energy, and materials that are wasted and scrapped due to production of
nonq
uality parts: the mold needs constant attention of a technician to adjust the
process to produce the parts within specification; parts molded out of specification
must be scrapped and rerun. This is a waste of material, machine time, and human
resources. The time lost cannot be regained. Often, parts that are out of specifica-
tions are shipped to the customer where they will be discovered. This causes a
loss of reputation, return of parts for rework, time consuming corrective action
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 162 (page 162)

138 7  Scientific Processing, Scientific Molding, and Molding Parameters
investigations, and the cost to scrap and remake the parts that cannot be reworked.
With all the competition in a truly global market, efficiency in every area becomes
an essential requirement. Consistency in output cavity-to-cavity, shot-to-shot and
run-to-run are results of a robust process.
 7.2  The 11 + 2 Plas tic Injection Molding
Machine Parameters
There are 11 primary plastic molding parameters on the molding machine that
have a direct influence on the quality of the molded product. These do not include
parameters such as mold open or close speeds and so on. In most molding pro-
cesses, the compensation phase, also known as the 2nd stage, consists of only one
subphase known as the holding phase. In some cases, molders will differentiate
the compensation phase into two phases known as the pack and the hold phase. In
such cases, 2 more parameters are added to the 11 primary parameters, so the
t
otal number of parameters is 13. These 13 parameters are shown in Figure 7.3.
SHOT
SIZE
TRANSFER
POSITION
CUSHION
0 0.83 5.35MOLD
TEMP
0.13
INJECTION
PRESSURE
INJECTION
SPEED
COOLING
TIME MELT
TEMP
SCREW
ROTATION
SPEED BACK
PRESS
1
2
4
11 10 9
8
7
6
5
HOLD PRESSURE
12 PACK PRESSURE
3 HOLD TIME
13 PACK TIME
Figure 7.3 The 11 + 2 plastic injection molding parameters
Following are the 13 molding parameters that are machine inputs:
1.
Bar
rel Temperatures: The plastic needs to be in a molten state to be injected into
the mold. The heaters around the barrel heat the it, which conducts the heat to
the plastic on the inside to aid the melting. Depending on the length of the bar -
rel, there can be several heater bands, and the temperature for each of these will
have to be individually set depending on the material that needs to be processed.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 163 (page 163)

1397.2 The 11 + 2 Plastic Injection Molding Machine Parameters
The result of these settings is reflected in the melt temperature. The shear from
the screw rotation also contributes to the melt temperature. The recommenda-
tions for melt temperatures are available from the material manufacturer.
2.
Mold T
emperatures: Because molding is a heat transfer process, the molten
plastic is cooled in the mold. The temperature of the mold is set using a control-
ler that circulates is a heat transfer fluid such as water of oil. Usually water is
used for achieving mold temperatures below 100 °C, and oil is used for achiev-
ing higher temperatures. Sometimes cartridge heaters are also used. The set-
tings are on the controllers. Some machines are equipped for connecting these
mold temperature control units directly to the screens of the molding machine.
The recommendations for melt temperatures are available from the material
manufacturer.
3.
Injection Speed (V
elocity): This is the speed at which the screw moves linearly
to inject the molten plastic into the mold. The injection speeds must be set fast
enough so that the plastic is still in the molten state until the complete mold is
filled to the optimum requirement. Once the mold is filled with molten plastic,
the injection of the plastic under the injection speed is stopped, though contin-
ues at a slower pace under the compensation phase. The technique of in-mold
rheology, also known as an in-mold viscosity curve, is used to optimize the injec-
tion speed of the machine.
4.
Injection
Pressure: This is the pressure that is applied to the molding screw to
maintain the set injection speed. If the viscosity of the plastic increases, the
effor
t or the pressure required to maintain the set speed will also increase so it
is important that the speed is kept constant during injection. The machine
should always a surplus of pressure available for a robust process. A pressure
drop study is used to optimize the injection pressure.
5.
P
ack Pressure: This is the first subphase of the compensation phase. Once the
mold is completely filled in the injection phase, to compensate for the shrinkage
that will take place, additional plastic is packed in. This pressure is known as
the pack pressure. Pack pressure is one of the most important parameters that
determines the shrinkage and hence the dimensions of the part. Data from a
Design of Experiments (DOE) is used to optimize the pack pressure.
6.
P
ack Time: This is the time for which the pack pressure is applied. Data from
the gate seal study is used to optimize the pack time.
7.
Hold Pr
essure: This is the second phase of the compensation phase. This is the
pressure that is applied to plastic during the hold phase to ensure that the ex-
cess plastic does not go into the cavity nor does the molten plastic come back
out from the cavity. In theory, during this stage, there is no movement of the
plastic until the gate is frozen. Data from the gate seal study is used to optimize
the hold pressure.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 164 (page 164)

140 7  Scientific Processing, Scientific Molding, and Molding Parameters
8. Hold T ime: This is the time when the hold pressure is applied. Data from the
gate seal study is used to optimize the hold time.
9.
Scr
ew Rotation Speed: This is the speed of the screw rotation during the pick -
ing up of the plastic during the shot build up. Crystalline materials need higher
screw speeds than amorphous materials. Presently, there is no proven tech-
nique of optimizing screw rotation speeds. It is mainly based on measuring the
melt temperature and examining the melt for burning and unmelted particles.
Screw speed is explained in detail in Section 8.12 in Chapter 8.
10.
Bac
k Pressure: This is the pressure that is applied to the back of the screw
during screw recovery in order to achieve melt homogeneity and a melt free of
any volatiles. Back pressure is explained in detail in Section 8.13. Presently,
there is no proven technique of optimizing back pressure.
11.
Cooling T
ime: This is the time the mold is kept closed to cool the plastic to the
ejection temperature. Once the cooling time has elapsed, the mold opens and
the part is ejected. It is important to realize that this is the set cooling time
and not the actual cooling time. The plastic starts to cool off as soon as the
plastic touches the mold, therefore, the actual cooling time is equal to the addi-
tion of the injection time (fill time), set pack time, set hold, and set cooling
time (Figure 7.4). Cooling times are optimized via the technique of Design of
Experiments.
Inj. Time
1.0 sec
Set Cooling Time
10.0 sec
Actual Cooling Time = 1.0 + 2.0 + 3.0 + 10.0 = 16 seconds
Pack Time
2.0 sec
Hold Time
3.0 sec
Figure 7.4 Set and actual cooling time
12. Sho t Size: This is also known as the dosage. The zero position of the screw is
when the screw is all the way in the forward position. The screw moves back to
pick up the molten material. The set distance that the screw moves back to is
called the shot size. This is measured in linear distance or in terms of volume.
The shot size can be calculated based on the total shot weight and the melt
density of the plastic. However, because melt densities are temperature de-
pendent, and it is difficult to estimate the exact temperature, shot size calcula-
tions are usually estimations. A correction has to be also provided for a cush-
ion value during the pack and hold phases.
13.
T
ransfer Position: The point of transfer from the injection phase to the com
-
pensation phase is called t
he transfer point. When this point is determined by
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 165 (page 165)

1417.3 Process Outputs
position, it is called the transfer position or the switchover position. This trans-
fer can also be done via time, hydraulic pressure, or by external means. In
theory, at the transfer position the mold should be filled exactly 100 % with the
melt. In practice the mold is filled less than the 100 % before the compensation
phase takes effect. This is described in detail in Section 8.5.
There are a couple of secondary parameters that do not get adjusted as often as the
13 just mentioned. They also do not have a substantial effect on the part quality:
1.
Decom
pression or Suck Back Position: Because the shot is built up in the pres-
ence of back pressure, the plastic that is in front of the screw is compressed and
is under pressure. At this time there is an injected shot in the mold. As soon as
the mold opens and the molded sprue moves back with the mold, the melt pres-
sure is released. This can cause the plastic to flow out of the machine nozzle. For
this reason, at the end of the screw rotation, the screw is pulled back in a linear
movement and the pressure is released to decompress the melt. This distance
through which the screw is pulled back is called decompression or suck back.
These distances are usually very small (less than 1
cm) and can affect t
he cos-
metics of the part.
2.
P
ack Speed: This is the speed at which the screw moves linearly during the pack
phase. This is an option on some machines only.
If one looks at the screens of the modern day molding machines, one can get
o
verwhelmed with all different settings for the parameters and options. There are
several process monitoring screens that are available to track part quality and the
cycle efficiency. The machine manufacturers sometimes tend to provide a number
of redundant and unnecessary controls. For example, some machines will have an
option of ten second stage pressures for the pack and hold phase. In most system-
atically developed molding processes, two pressures should be more than suffi-
cient. In some cases, to compensate for an unoptimized part and/or mold design,
the processor may need to add a few more profiles.
 7.3  Process Outputs
The molding parameters discussed in the previous section are machine inputs. The
following are the outputs from the machine, which are a result of the settings of
the molding parameters as available on the molding machine screens.
1.
F
ill Time: This is also known as the injection time and is the time the screw takes
to move from the shot size to the transfer position. This is also the duration of
the fill phase.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 166 (page 166)

142 7  Scientific Processing, Scientific Molding, and Molding Parameters
2. Pr essure at Transfer: This is the actual pressure that is required to reach the
transfer point to the compensation phase.
3.
P
eak Pressure: This is the maximum actual pressure that is reached during the
injection phase. This may or may not be equal to the pressure at transfer and
depends on the mold and part design.
4.
Cushion V
alue: The position of the screw at the end of the holding phase is the
cushion value. It is the buffer that is required for the shrinkage compensation. If
the cushion value is zero, then there is no pressure being applied to the melt,
therefore, the melt is not being packed to the optimum value. In other words, the
shrinkage is not being compensated. Cushion values should never be zero.
5.
Scr
ew Rotation Time: This is the length of time the screw rotates to pick up the
required material for the next shot.
6.
Cy
cle Time: This is the time it takes for one complete molding cycle. It can also
be described as the time to mold one shot.
The optimization of each of these phases in mentioned in detail in Chapters 8
and 9.
 7.4  What Scientific Molding and Scientific
Pr
ocessing Are Not
Good molding practices start with a robust process development strategy. Molders
gather information from either a seminar, a book, and/or online resources about
the concepts of scientific molding and scientific processing. It is very important to
understand that these techniques are not about blindly following procedures.
There are exceptions to every procedure, and after understanding the science be-
hind these techniques, the molder needs to know when and how to use these tech-
niques. This is the importance of the word ‘scientific.’ For example, the in-mold
rheology study (viscosity study) is the first study that is taught in molding semi-
nars. There is a lot of science behind this, and a molder gets fascinated by generat-
ing these graphs; a Eureka moment for some! However, there are several excep-
tions to the use of this technique. The same follows for all the other techniques that
are used in process optimization. One must do what is necessary to understand the
process rather than follow procedures because they were a requirement.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 167 (page 167)

1437.5 The Injection Molding Cycle
 7.5  The Injection Molding Cycle
The basic phases of an injection molding cycle are shown in Figure 7.5. The cycle
starts with the mold closing and the buildup of clamp tonnage. Once the mold is
clamped under the tonnage necessary to keep it closed under injection pressure,
the injection of the plastic starts. This is followed by the packing phase and then
the holding phase. Once the cavity filling is complete, the part is cooled down to or
below its ejection temperature, the mold is opened, and the part is ejected out of
the mold. During the cooling phase of the cavity, the reciprocating screw rotates to
pick up new material for the next shot. This is referred to as the screw recovery
phase.
Injec/g415on
Phase
Pack
Phase CoolingM old Open Ejec/g415onM old Closed
Screw Rec
Complete Cycle
Hold
Phase
Compensa/g415on
Phase
Figure 7.5 The injection molding cycle
7.5.1Injection, Pack, and Hold
The process of filling the cavity can be divided into three phases: injection, pack,
and hold. During the injection phase, the mold cavity is completely filled with the
molten plastic. The plastic begins to cool down as soon as the plastic hits the walls
of the mold and forms an outer frozen skin. As the injection continues, the plastic
flows in between the frozen layers. The aim of the injection phase is to get the cav-
ity completely filled with molten plastic. As the plastic begins to cool, the mole-
cules start to get closer to each other, resulting in shrinkage. At this point, if the
addition of plastic were stopped, the parts would be under-packed and would ex-
hibit a defect known as sink. Sink shows up as depressions on the surface of the
part. Therefore, to avoid this and to compensate for the volumetric shrinkage, the
injection phase is followed by the packing phase, where the required amount of
plastic is packed into the mold. The required amount is equivalent to the volumet-
ric shrinkage. At the end of this phase, the amount of plastic in the cavity must
equal the theoretical weight of the part. Any less plastic in the cavity will result in
an under-packed part and any more will result in an over-packed part.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 168 (page 168)

144 7  Scientific Processing, Scientific Molding, and Molding Parameters
The molten plastic enters the cavity through the gate. If this area freezes off, fur -
ther filling of the cavity is impossible. Therefore, the gate must be large enough to
prevent plastic freeze-off during the injection and pack phases. After the packing
phase, the molten plastic is under very high plastic pressures. If the pressure on
the screw is removed at the end of packing phase, the high pressure inside the
cavity will force the melt out of the cavity. Therefore, a certain amount of pressure
must continue to be applied in order to hold the melt inside the cavity. Care must
also be taken not to apply excess pressure because that will pack in more than the
required amount of plastic in the cavity and over-pack the part. This balance of
pressure is called holding pressure, and this phase of the injection process is
called the holding phase. The holding pressure must be applied until the gate is
frozen; this time is referred to as holding time. The gate must be frozen before the
pressure behind the screw is released, otherwise the plastic inside the cavity will
be forced out of the gate by the high pressure in the cavity. Figure 7.6 shows the
injection, packing, and holding phases.
End of
Injection
-G ate
Open
Empty Mold End of
Packing –
Gate Open
End of
Cooling –
Gate
Closed
End of
Holding –
Gate
Closed
Scenario 1: Ideal case
Part
Results
in Sink
Scenario 2: Gate closed during or at the end of injection
End of,
or during
Injection
-G ate
Closed
Empty Mold
Part
Results
in Sink
Scenario 3: Gate closed during or the end of packing
End of
Injection
-G ate
Open
e t a Gd l o M y t p m E
Closed
before or
at the End
of Packing
End of
Injection
-G ate
Open
Empty Mold End of
Packing –
Gate Open
Part Results
in Sink
Insufficient
Hold Time
Scenario 4: Gate closed after packing is complete but
holding time is not sufficient
Figure 7.6 Representation of the injection, pack and hold, and the cooling phases
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 169 (page 169)

1457.5 The Injection Molding Cycle
The pack and hold phases are used for compensating the shrinkage during the
filling process and are collectively called as the compensation phase. It is difficult
to determine the switchover point between pack and hold without employing some
advanced methods, such as using cavity pressure measurement equipment. For
the most part, pack and hold are taken as one phase and are usually called the
holding phase. In many cases, the processes are set with profiles on the holding
pressure to yield acceptable parts via trial and error. In doing so, the processor has
actually set up a process that has a pack and a hold phase but is not aware of it or
has not been able to distinguish the two phases from each other. Under-packing
results in defects such as sinks and internal voids in the parts. Such parts usually
exhibit some amount of post-molding shrinkage as well. Over-packed parts can
have molded-in stresses that usually get relieved after the parts are ejected, result-
ing in defects such as warpage or premature failure.
A systematic procedure to develop a process with a clear differentiation between
pack and hold has been described in the next chapter.

7.5.2Speed and Pressure
To illustrate the phenomenon at hand, consider a gaylord filled with a packing ma-
terial such as styrofoam that needs to be pushed across the hall at 1000
mm per
minut
e. The task requires one person, so the force required to move the gaylord is
one person, and the speed is 1000
mm per minut
e. Now, if the gaylord is filled with
metal, and the speed still needs to be 1000
mm per minut
e, the force required to
perform this action may now require four people, see Figure 7.7. The force has
changed, but the speed has remained the same. In other words, as the resistance to
movement changes, the required force changes. Viscosity is the resistance to flow.
Therefore in molding, the weight of the gaylord is synonymous to the viscosity of
the plastic. The speed of the gaylord is synonymous to the injection speed. The
force is synonymous to the required injection force needed to move the screw at
the set speed. The force is represented in terms of the applied pressure to the
screw. Pressure is the force divided by the cross sectional area of the screw; this is
further explained in Section 6.7 under the topic of intensification ratio.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 170 (page 170)

146 7  Scientific Processing, Scientific Molding, and Molding Parameters
Figure 7.7 Explanation of speed and pressure
7.5.3Pressure Limited Process
In the same example just discussed, if there were only three people instead of four
to move the gaylord of metal at 1000
mm per minut
e, the required speed cannot be
reached. In injection molding this means that if the screw needs 2500
psi
of injec-
tion pressure to move at 5 in/s, but the machine is only capable of producing
2200
psi of t
he 2500 required, then the screw will never reach the required speed.
The limited supply of pressure will limit the injection speed to the speed attainable
at 2200

psi. When this situation exists, the process is said to be pressure limited.
7.5.4Decoupled MoldingSM
The term Decoupled MoldingSM was coined by Rod Groleau of RJG Inc. (see Figure
7.8). During the injection phase, the cavity is filled with molten plastic. The vol-
ume of melt injected during the injection phase must be equal to the collective
volume of the cavities and the runners. (Note that melt density is lower compared
to solid densities.) Once this volume of plastic is present in the mold, the injection
phase is followed by the packing phase which is then followed by the holding
phase. Before such an understanding was developed by the molding industry,
molders would either overpack or underpack the mold with molten plastic and
would apply the pack and hold phase based on some previous experience. To stress
the importance of the separation of the phases and educate the molders, the term
Decoupled Molding
SM was introduced. Since each phase has a specific reason, they
must be decoupled from each other and controlled separately.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 171 (page 171)

1477.5 The Injection Molding Cycle
Figure 7.8 The concept of Decoupled MoldingSM (Decoupled Molding is a service mark of
RJG Inc.)
Decoupled molding provides the best control over the molding process and offers
the most consistency. It is common practice to fill the cavity to 95–98 % capacity
during injection before entering the pack and hold phases because, in decoupled
molding, the goal is to make sure the mold is not filled more than 100 % during the
injection phase. Targeting 95–98 % provides a small margin of safety to make sure
that the part is not excessively filled. The second reason is to compensate for the
momentum of the screw during injection, which allows the melt to slow down be-
fore the start of the next phase. The melt is also compressible and therefore the
cavity can get overpacked to more than a 100 % fill. The packing phase is a less
dynamic phase because we are only packing at the rate of shrinkage that is taking
place in the cavity. A slowdown is therefore essential to insure the mold is not over-
packed and or blown open and flashed.
7.5.5Intensification Ratio (IR)
The concept of IR has been explained in detail in Chapter 6, see also Figure 7.9. For
hydraulic machines, the IR is the ratio of the cross sectional area of the hydraulic
ram where the injection pressure is applied to the cross sectional area of the screw.
The hydraulic pressure multiplied by the IR is equal to the plastic pressure present
at the tip of the screw. For example, an IR of 10 : 1 means that a hydraulic pressure
of 800
psi will pr
ovide a plastic pressure of 8000
psi at t
he tip of the nozzle. In
other words, it is an amplification factor.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 172 (page 172)

148 7  Scientific Processing, Scientific Molding, and Molding Parameters
Figure 7.9 Intensification ratio = Ar/As
7.5.6Screw Speed
The setting of the screw speed is another critical parameter, especially when it
comes to crystalline materials. The shear from the rotating screw contributes a
significant amount of energy to help melt the plastic. During the machine cycle,
when the material is being processed through the barrel, the heat from the heater
bands alone is not sufficient to melt the crystallites. The additional heat required is
supplied by the shear energy created by the rotation of the screw. High screw
speeds generate high shear and help in melting the crystallites.
Screw speeds must be set such that the screw recovery time is always less than the
cooling times. The mold does not open until the screw recovery is completed and
the cooling times are reached. If screw recovery takes longer than cooling time, the
effective cooling time increases because the mold is still closed. In this case, the
screw recovery time becomes the controlling parameter. The rule of thumb is to
have the screw recovery completed approximately two seconds before the cooling
time is reached. This is acceptable in some cases; however, it is not always practi-
cal. While molding crystalline resins, high screw speeds are required and, depend-
ing on the part, a longer cooling time may also be required. For example, the screw
recovery may be completed in 4 seconds, but the required cooling time may be
10 seconds. In such cases, there is a significant delta between the two time inter -
vals. Slowing down the screw speed will result in loss of the required shear and
deteriorate the melt homogeneity. In such cases, the rule of thumb will not be ap-
plicable. In other cases, regardless of the morphology of the resin, where the cool-
ing times are long, a very slow screw speed will also induce inconsistencies in the
melt homogeneity or in the amount of the melt that is metered in by the screw for
the next shot. Some amount of shear energy is always required to melt the plastic
and improve the melt homogeneity. Looking at a cross section of the molding
mac
hine barrel with the plastic and the screw inside, the heater bands are on the
outside, followed by the barrel, the plastic, and the screw. The plastic is a bad
conduct
or of heat and therefore the inner layers of the plastic, closer to the screw,
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 173 (page 173)

1497.5 The Injection Molding Cycle
do not receive sufficient heat from the heater bands. The plastic is molten but the
melt is not homogeneous. The shear from the rotating screw is what provides the
required energy to melt these inner layers and contributes to melt homogeneity.
Recommended screw speeds are provided by the material suppliers. However, the
values are typically given in revolutions per minute (rpm). This is very misleading
because, depending on the diameter of the screw, a given value of rpm will result
in high shear for large diameter screws while the same value will result in low
shear for a smaller diameter screw. The screw speeds should therefore be specified
in distance per time units, such as inches per second or meters per second. An
e
xample is given in Figure 7.10.
Screw Diameter
10 mm
20 mm
30
30
942
1884
Rev per min mm/minute
Lower shear
Higher shear
Figure 7.10 Relationship between screw diameter, revolutions per minute, and surface
linear speed
Highly filled plastics or plastics filled with long glass fibers typically require slower
screw speeds to avoid a breakdown of the fibers. In these cases the screw design
plays an important role in processing. Screw design also plays an important role in
determining the melt homogeneity for different types of materials, depending on
their shear sensitivity. In some cases, the cycle times can get longer because the
available screw on the molding machine cannot generate enough shear heat to
melt the plastic fast enough. Again specialty screws can make a difference here.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 174 (page 174)

150 7  Scientific Processing, Scientific Molding, and Molding Parameters
7.5.7Back Pressure
The example of going down a ramp with a loaded cart illustrates the natural ten-
dency to apply some force or resistance in the direction opposite to travel (see
Figure 7.11). This is done to better control the load and to gain consistency over the
travel to avoid an accident. Similarly, as the screw moves back because of the
buildup of plastic in front of the screw, an absence of pressure on the screw can
cause the screw to move erratically. This loss of control can lead to the screw reach-
ing the shot size position inconsistently and prematurely, which in turn will result
in process variations from shot to shot. In addition, the melt needs to be compacted
in order to eliminate all gases and air that has built up during the screw recovery
phase. Again, if the air and gasses are not eliminated, not only will the shot size be
inconsistent, but the air and gasses will show up in the parts as voids, splay, or
other surface or internal defects. Back pressure is also required to help in the mix-
ing action of additives such as colorants. It is also essential in achieving good
homog
eneous melt and helps in the melting action of the pellets.
FORCE APPLIED
TO CONTROL
DOWN SPEED
TRAVEL
DIRECTION
FORCE APPLIED
TO CONTROL
RECOVERY
TRAVEL
DIRECTION
DURING RECOVERY
Figure 7.11 Explanation of back pressure for control and consistency
The back pressure values provided by the material suppliers should be used as
guidelines only. The applied back pressure actually used should be as low as possi-
ble to achieve the required result. The consistency in screw recovery time is a good
indication that the back pressure being applied is sufficient. The variation in screw
recovery time must not exceed +/– 0.2 to 0.5 seconds on small to mid-size ma-
chines and approx. 1 second on larger machines. Too much back pressure can
cause excessive shear in the material which can degrade the material. Some fillers,
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 175 (page 175)

1517.5 The Injection Molding Cycle
such as glass fibers, can break down with excessive back pressure resulting in a
loss of properties in the final product. In nonshear-sensitive materials (but also in
some shear sensitive materials) degradation of certain low molecular weight addi-
tives can result in the formation of gasses. This will increase the number of defects
in the final parts and over time cause the vents in the mold to build up with resi-
due and become clogged. Vents on the parting lines are easy to clean; however, the
internal vent components, such as vent pins, are difficult to clean without pulling
the mold from the machine and dismantling it. Excessive back pressure can also
result in increased wear of barrel and screw components.
7.5.8Cycle Time
The cycle time is the time it takes to mold one shot. Production efficiencies are
linked to cycle times. As is shown in Figure 7.12, a one second reduction in a thirty
second cycle can save a company up to 145 times the cost of the hourly rate even
with 70 % machine up time. For example, if the cost of running a particular ma-
chine is $10 per hour, then the total savings would be $1456. This multiplied by
the number of machines can be a substantial savings for a molder. If there are 25
machines in a molding shop, the molder can save about $36,000 per year at a
mac
hine rate of $10 per hour or close to a $100,000 for a machine rate of $25
per hour.
Ti me s av ed p er d ay 48 mi nu tes
Ti me s av ed p er 5 da ys 4h ou rs
Ti me s av ed p er yea r2 08 hour s
Ma ch ine u/g415 liza /g415o n7 0% %
Machine rate per hour
(units of currency)
25
50
100
Savings per machine
per year
(units of currency)
3640
7280
1456 0
Figure 7.12 Cost savings by reducing 1 second in a 30 second cycle
There are other factors that will need to be taken in to this formula, such as the
lower the cycle time, the more cycles per hour, which require more energy to run
the machine and the auxiliaries. A detailed analysis must be done.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 176 (page 176)

152 7  Scientific Processing, Scientific Molding, and Molding Parameters
 7.6  References
[1] K ulkarni, S. M. and Hart, David, SPE ANTEC Tech Papers (2003) p. 736
[2]
Mer
tes, S., Carlson, C., Bozzelli, J., and Groleau, M., SPE ANTEC Tech Papers (1997)
Suggested Reading
Osswald, T. A., Turng, L., and Gramann, P. J., Injection Molding Handbook (2007) Hanser, Munich
Beaumont, J. P., Runner and Gating Design Handbook (2007) Hanser, Munich
Beaumont, J. P., Nagel, R., and Sherman, R., Successful Injection Molding (2002) Hanser, Munich
Rosato, D. V. and Rosato, D. V., Injection Molding Handbook (2000) CBS, New Delhi, India
Kulkarni, S. M., SPE ANTEC Tech Papers (2003) p. 736
Cogswell, F., Polymer Melt Rheology (1981) John Wiley, USA
Dealy, J. and Wissbun, K., Melt Rheology and its Role in Plastic Processing Theory and Applications (1990)
Van Nostrand Reinhold
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 177 (page 177)

Process Development
Part 1: the 6-Step
Study – Exploring the
Cosmetic Process
 8.1  Introduction
Developing a robust molding process is often not done by following a systematic
procedure. While decreasing ‘art to part’ times with decreasing resources, it is
often
difficult to follow the procedures. However, these shortcuts decrease the part
quality, increase scrap rates, increase workloads of personnel, and reduce the
overall efficiencies of the molding process. A process that needs to be adjusted
once a day is not a robust, repeatable, and reproducible process. The next two chap-
ters will provide an insight to the development of the most efficient process for a
given mold and will also provide techniques to improve the process even further
with recommendations for mold design, part design, and material selection.
 8.2  Introduction to Process Development
Consider that one needs to make a road trip from Denver, Colorado to Las Vegas,
Nevada. An online program estimates this to be a distance of about 1200
km
(750
miles). The ne
xt step is to check that the car making the trip is capable of
covering a distance of 1200
km.
The engine, the tires, the windshield wipers, and
other items would need to be checked and verified by a mechanic that they would
perform during a 1200
km r
oad trip. Once it is determined that the car is capable,
the driver can punch in the address in a GPS system and drive in the required di-
rection. There were two parts to this activity: First, the equipment (the car) needed
to be verified for its capability, and second, was to steer the equipment in the re-
quired direction (a south west direction) toward Las Vegas. Refer to Figure 8.1.
8
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 178 (page 178)

154 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
Denver,
CO
Las Vegas, NV
Dallas, TX
Minneapolis, MN
Boise, ID
Figure 8.1 Cities equidistant from Denver, Colorado
Once the car is ready, if for whatever reason the driver decided not to drive to Las
Vegas, he can confidently make a journey in a direction of his choice up to a dis-
tance of 1200
km.
Looking at the map, this means he could either drive southeast
to Dallas, Texas or northeast to Minneapolis, Minnesota or northwest to Boise,
Idaho. All these cities are approximately 1200

km from Denver.
The injection molding process should also be developed in a similar two-part activ-
ity. First, the mold should be capable of consistently molding cosmetically accept-
able parts with a wide cosmetic process window. Once the preferred cosmetic pro-
cess is determined, the dimensions should be measured. If the dimensions are not
acceptable, then changes to the process within the cosmetic process window
should be examined. A process setting on the edge of a cosmetic window should
never be selected. In such cases, and in cases where the dimensions do not fall
within the cosmetic window, the most robust cosmetic process must be selected
and mold cavity dimensional changes and/or part specifications and tolerances
must be made. Going back to the driving example above it would be best to drive
long distance with a cruise control setting. But this is only possible when the lane
widths are wide enough to compensate for any varying road and driving condi-
tions. It is impossible to drive on the edge of a cliff under cruise control. Figure 8.2
shows the recommended flow chart for a two stage process for developing a robust
molding process.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 179 (page 179)

1558.2 Introduction to Process Development
STAGE 1: MOLD FUNCTION QUALIFICATION & PART
COSMETICS QUALIFICATION
6 STEP STUDY
1 -V ISCOSITY STUDY
6 -C OOLING STUDY
START
CAVITY
BALANCE
OK
OK
OK
PART OR MOLD ISSUES
5 -G ATE SEAL STUDY
PRESSURE
DROP
YES
FIX MOLD
OR
PART DESIGN
NOT OK 2 -
3 -
4 -
NO
STAGE 2: PART DIMENSIONS & QUALITY
QUALIFICATION SELECT DOE PARAMETERS
PERFORM DOE
SELECT PROCESS
RUN PROCESS
NOT OK
ADJUST
MOLD STEEL
RUN SHORT PRODUCTION
RUN TO EVALUATE THE
MOLDING PROCESS
AND
MOLDING PROCESS
CAPABILITY
DETERMINE DPW
PROCESS
WINDOW
MOLD OR PART
ISSUES
NOT OK
NOT OK
PLEASE NOTE:T HIS FLOW CHART HAS BEEN DEVELOPED
BY FIMMTECH AND IS A RECOMMENDEDP ROCEDURE.
THE USERS SHOULD USE THEIR OWN DISCRETION AND
JUDGMENT IN FOLLOWING THE PROCEDURE ESPECIALLY
KEEPING SAFETY IN MIND. THE USER IS SOLELY
RESPONSIBLE FOR ALL CONSEQUENCES.
-SUHAS KULKARNI, WWW.FIMMTECH.COM
RECOMMENDED MOLD
QUALIFICATION PROCEDURE
Figure 8.2 Mold qualification and DOE flowchart
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 180 (page 180)

156 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
In Stage 1, the process parameters are explored, and the most robust area of the
process are selected as the preferred process setting. Dimensions are not necessar-
ily examined, although by doing so, a good idea of how close the dimensions are to
the specifications can be obtained. In Stage 2, the technique of Design of Experi-
ments (DOE) is used to determine the dimensions at the preferred process and to
determine the relationship between the process parameters and the dimensions.
A simulation tool can be used to study the effect of the process changes on the
dimensions.
This c
hapter will discuss stage 1 is detail. First, the premolding setup will be dis-
cussed, followed by the procedures for optimization of each molding parameter.
 8.3  Premolding Setup
The resin that has to be molded needs to be of consistent quality and therefore has
to be controlled until it is brought to the feed throat of the hopper. This means
every step from when it enters the molding facility and exits that it needs to be
controlled. The molding machine should be selected based on the criteria men-
tioned in Chapter 6.
 8.4  Storage and Drying of Resin
Resin is supplied to the molder in a variety of ways. Most commodity resins, such
as polyethylene, polypropylene, or ABS are typically used in very large volumes.
The same material may be used in various products. Such resins are usually
shipped to the molder in gaylords. For higher volumes, large silos are filled with
resin, which is brought in by trucks or even by rail cars. When the volume of mate-
rial is not very large, such as for most engineering materials, the supplier usually
provides resin in prepackaged bags of 25
k
g each. In some materials, a loss of
properties can occur if the resin is not stored correctly. Some polyurethanes are
examples of resins with shelf life limitations. Therefore, it is important to use this
resin within the prescribed time specified by the manufacturer. In resins with
shelf life limitations it is typically not the polymer that degrades, but rather the
additives that can be time sensitive.
Other resins, such as acrylic, must not be stored such that they are exposed to sun-
light because this may result in a loss of color or transparency. The resin must also
be stored in a dry area to avoid unnecessary absorption of moisture. Some resin
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 181 (page 181)

1578.4 Storage and Drying of Resin
manufacturers prepackage hygroscopic resins in their dry/processing state and
ship them to the customer in sealed bags. Such resins do not need drying and can
be used directly at the molding press. However, unused resin that was stored back
on the shelf must be redried before being used again. Clear identification of the
resin and keeping a log of all the materials in use are considered good manufactur-
ing practices. Many times, a sample resin is brought in, and some of it is used and
the rest stored for later reuse. A date, project ID, and material ID must be recorded
on the sample bag to ensure the history of this material can be clearly identified.
8.4.1Plastic Drying
The topic of plastic drying has been discussed in detail in Chapter 4. Hygroscopic
resins must be dried in order to avoid loss of properties, surface blemishes, and/or
internal defects. The loss of properties in some resins is a result of the hydrolytic
degradation of the resin. In other resins, the presence of the moisture in the resin
results in surface defects, such as splay or internal defects like voids. Processing
difficulties, such as gassing and foaming of the melt, as in the case of nylons, may
be encountered. For these reasons, resins must be dried before processing. The
specific amount of drying time and the correct drying temperature is dependent on
the base polymer resin. The times and temperatures for each resin is dependent on
the strength of the chemical bond that the water forms with the polymer. For
e
xample, PBT needs to dry at 80 °C (180 °F) for 4 hours, whereas polycarbonates
need to dry at 121 °C (250 °F) for about 3 hours.
Additives are often added to plastic to enhance their properties for specific applica-
tions and/or to reduce their cost. Fillers such as glass and minerals are the most
widely used additives by volume. Other additives include plasticizers, lubricants,
flame retardants, heat stabilizers, colorants, blowing agents, and biocides are
added to polymers in small percentages. These are usually low molecular weight
compounds and/or oligomers. If the drying time is extended beyond the manu
-
f
acturers recommended limits, it is possible to degrade these additives and/or to
cause them to leave the resin. For example, with PBTs and nylons it was found that
if the suggested drying times were exceeded, there was a danger of producing
def
ective or out of specification parts. Drying PBT resin for more than 8 to 10 hours
produced brittle parts and loss in surface appearance. Parts that normally ap-
peared black with high gloss now appeared dull grey. Figure 8.3 shows that PBT
exhibited a drastic drop in the impact strength after it was dried for more than
12

hours [1].
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 182 (page 182)

158 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
0.75
0.80
0.85
0.90
0.95
1.00
1.05
1.10
PBT
Drying Time (Hours)
Mean Failure Energy (Joules)
Figure 8.3 Effect of drying time on the impact strength of PBT [1]
Drying nylons for more than about 12 hours steadily increased the viscosity of the
plastic, causing constant adjustments to the molding process. The viscosity graph
for nylon at different drying temperatures is shown in Figure 8.4 [1]. In this graph,
nylon-4 represents nylon that has been dried for 4 hours and nylon-48 nylon that
has been dried for 48 hours. Figure 8.5 shows the parts molded in the ‘injection
only’ phase at various drying times. Parts molded within the ‘injection only’ phase
are those that are molded with both pack and hold time and pack and hold pres-
sure set to a zero value. Therefore, the pack and hold phase are absent. With the
same set process at the molding machine, as the drying time increases, the amount
of part filling is less. This is a result of the increase in viscosity, which reduces the
flow of plastic. Overexposure or ‘overdrying’ must be prevented.
10
100
1000
100 1000 1000 0
Apparent Shear Rate (1/s )
App. Shear Viscosity (Pa-s)
NYLON-4
NYLON-48
Figure 8.4 Viscosity of nylon dried for 4 and 48 h [1]
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 183 (page 183)

1598.5 Machine Selection
Figure 8.5 Parts molded using the ‘injection phase only’ with nylon dried for 4 hours and
48 hours
The most efficient ways to prevent over drying are:
 If t
he molding operation is not ready to be started after the material is dry, turn
down the dryer temperature to about 80 °F, but keep the dryer running. Supply-
ing the hopper with room temperature dry air will keep the moisture out and will
not have detrimental effects on the resin.
 Size t
he hopper dryer such that the residence time of the plastic does not exceed
the manufacturers’ minimum/maximum recommended drying times for the
plastic. When the available hopper sizes are larger than required, it is recom-
mended to retrofit the dryers with an adjustable level sensor and adjust the sen-
sor to load only the required amount of material.
 If t
he machine is going to be down for a long time (several shifts or days) after
the drying has taken place, shut the hopper dryer off as soon as possible.
Precautions: Drying may have a cumulative effect in some resins, such as PBT.
With PBT, the drying process permanently removes the low molecular weight addi-
tives, which are not recovered when the drying is stopped, and the resin is re-
turned to the shelf for the next run. With nylons, moisture can be reabsorbed back
into the resin. The effects of over drying for PBT and nylon that are mentioned here
must not be considered typical results for other materials. The effects of the over
drying of other resins have yet to be studied because each resin and its additives
are unique. Customized experimentation and testing will best suggest the type of
drying control that is required. However, there is no real need to conduct this type
of expensive and time consuming experimentation as long as the material is not
exposed to excessive drying times.
 8.5  Machine Selection
Machine selection was discussed in detail in Chapter 6. Following are the main
requirements for the given mold:
 The
mold must physically fit in the machine with the molding area always within
the machine platens.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 184 (page 184)

160 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
 The r equired mold tonnage should be less than the machine tonnage.
 The per
centage of the shot size should preferentially be between 20 and 80 %.
 The r
esidence time of the plastic in the machine should be less than the maxi-
mum allowable residence time of the plastic.
 8.6  Importance of Adding Charge Delay Time
The three phases of mold fill are injection, pack, and hold. The pack and hold
phases are pressure and time controlled. As soon as these timers time out, the
screw begins to rotate under back pressure to pick up the next shot. At the end of
the injection phase, the gate is not frozen and the mold is about 95–98 % full, or in
other words, it is 2–5 % unfilled. If the timers for the pack and hold phases are set
to zero, then as soon as the injection phase is done the screw begins to rotate. The
applied back pressure now applies pressure on the melt, and since the cavity is
still not full and the gate not frozen, the part begins to fill to 100 %. The screw re-
covers to the shot size only after the cavity is full. If one is trying to find the decou-
pled point of the 95–98 % fill, then it becomes an impossible task to set the transfer
position. However, if one adds a screw rotate timer, more commonly known as a
charge delay or screw recovery timer, then the screw will wait for the specified
time and then begin to rotate. The idle time will give a chance for the gate to freeze
off. Once frozen, the plastic cannot enter the cavity, therefore, one can truly deter-
mine the percentage fill in the injection phase. Refer to Figure 8.6.
Back
Pressure
Screw rotation
during recovery
Mold is partially
filled at the end
of injection –
Gate still open
Gate is frozen,
mold is filled
partially
Gate is not frozen,
mold is filled by
back pressure
Add charge delay
time followed by
screw recovery
No charge delay time,
injection followed by
screw recovery
Figure 8.6 Importance of charge delay time to determine percentage fill during the
injection phase
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 185 (page 185)

1618.7 Filling in Injection: Weight or Volume?
To understand this further a quick experiment can be performed at the molding
machine. Choose a simple mold one or two cavity mold that has a history for run-
ning consistently with no issues. Care must be taken during this experiment not to
over pack the mold and any changes made must be in small steps. When running a
low viscosity material, such as a nylon or a LDPE, set the pack and hold times to
zero, and set the back pressure to very low values of around 3 to 4 plastic MPa, or
about 300 to 400 plastic psi. Please note these are plastic pressures and not hy -
draulic pressures. Increase the cooling time by an amount equal to the addition of
the initial pack and hold times. Set the charge delay time to about 5 to 7 seconds.
Mold a part and examine to see if the part is not filled to a 100 %. If the mold is
filled, adjust the transfer position to mold a short part that is filled to about 95 %.
Next, remove the charge delay time and increase the back pressure to about 14
plastic MPa, or about 2000 plastic psi, and mold a part. Weigh the parts that were
molded with and without the charge delay time. The parts without the charge de-
lay time would be heavier because the back pressure fills the parts via the un
-
fr
ozen gate. This experiment must be conducted with those who have substantial
molding shop floor experience. Parts could get over packed and get stuck in the
mold if care is not taken.
 8.7  Filling in Injection: Weight or Volume?
Filling the part up to 95 to 98 % in the injection phase is a technique that was de-
scribed in the previous sections. There is always a confusion between processors
whether the mold should be filled to that limit by volume or by weight.
The formula for calculating weight from volume is
Weight = Volume × Density.
Because the melt density is going to be constant, it does not matter if one decides
to use weight or volume, so 95 % by weight = 95 % by volume. The key is to always
use the same factor and finally weigh the part using this weight as the ‘Injection
Only Part Weight’ value. This weight must be recorded on all process sheets. Every
time a mold is started up, the injection only part weight must be matched. This
greatly enhances the consistency of the molding process especially in case of a lot
to lot variations.
On thick parts the plastic fills the walls first to form a skin and then the inside will
get packed out. There are no visual signs of the part being filled to a certain num-
ber and could get confusing to a processor.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 186 (page 186)

162 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
Comments on the % number: The 95 to 98 % number is only a recommendation.
There is no number or a range that must be followed. Here are some general guide-
lines:
 The t
hinner the part, the closer one will need to get to the 100 %. Because there
is not much shrinkage and/or because the end of fills are thin sections, the mold
will need to get filled completely in the injection phase with little amount of pack
and hold pressure and some hold time to seal off the gate.
 The t
hicker the part, then most of the work is done in the pack and hold phase
and therefore the mold may need to fill about 90 % in the injection phase and the
rest in the pack and hold phase.
 F
or better consistency, it helps to slow down before hitting the transfer position.
As an example, on one particular part, the part was filled to 85 % and was then
transferred to the pack and hold phases.
 F
or crystalline materials that freeze off fast, the number should be closer to a
100 %. Amorphous materials are more forgiving.
 8.8  Setting of the Melt Temperatures
Melt temperature selection should be the next step in the process development
procedure once a material is ready to be processed or as the material is being
dried. The material manufacturers provide processing data sheets that supply melt
temperature information. In the case of amorphous materials, the range of recom-
mended melt temperatures is wide, while for crystalline materials, the range is
rather narrow, as was explained in Chapter 2. As a starting point, the mean of
these recommended temperatures must be chosen as the target melt temperature.
Note that the target melt temperature must be the actual melt temperature of the
plastic and not the setting on the molding machine’s barrel temperature controller.
During the course of developing a molding process, the melt temperature will be
varied and the final process may have a different melt temperature as a result of
the process optimization study.
Procedure to check melt temperature: There are three common tools that are used
for measuring the melt temperature. The melt immersion probe works the best and
is the mold reliable. The IT gun method or the IR camera method are both not very
reliable because they work more on measuring the surface of the melt. The surface
tends to cool down as soon as it is exposed to the outside air.
The following is a recommended procedure to measure melt temperature.
 Ge
t an initial estimate first by purging some material and immersing the melt
probe into the melt
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 187 (page 187)

1638.8 Setting of the Melt Temperatures
 S tart the machine and let it run twice the number shots that is equal to the num-
ber of shots in the barrel.
 Pr
eheat the melt probe to close to the expected temperature. Be careful not to
damage the probe. An easy way to preheat the probe is to perform the initial
purging on large sheet of paper and then leave the probe underneath this sheet
for preheating. The paper will prevent the melt from sticking to the probe.
 Place t
he machine in semi-auto mode, pull the barrel back, purge the melt
 Immediat
ely, look for the ‘thickest’ area of the melt and place the probe in there
and move it around in the melt and record the maximum temperature as the
melt temperature.
Melt temperature is the most difficult measurement in injection molding. The main
reason for this is the temperature distribution in the melt and the rapid and un
-
e
ven cooling down of melt during the measurement process. Even when the melt is
inside the barrel as a built up shot, there will be temperature gradients and distri-
butions because of the influence of the proximity of the barrel heaters, the shear
heat being applied mainly to the melt that is closer to the screw and in case of
larger shots the efficiency and settings of the heater bands. The measurement
t
echnique is also operator dependent even if they follow the same procedure. The
key is to be repeatable in the procedure followed.
The melt temperature must fall within the range of the recommended melt temper-
atures. In the case of crystalline materials, the melt temperature window is nar -
row, but in the case of amorphous materials, the melt temperature window is wide.
It is very important for the processor to refer to the processing data sheet before
the start of molding. Two materials from the same chemical family can have com-
pletely different processing temperatures. For example, the OQ family of polycar -
bonate supplied by Sabic Innovative Plastics has a recommended melt temperature
range of 305 to 332 °C (580 to 630 °F), whereas for the SP family of polycarbonate
from the same company, the recommended temperature ranges from 248 to 271 °C
(480 to 520 °F). Setting the temperature too high for the low melt temperature
resin will degrade the resin and produce unacceptable parts. Setting the melt tem-
peratures too low for the higher melt temperature resin may result in equipment
damage, such as a broken screw or screw tip. Unfortunately, such failures are not
uncommon on the production floor.
The settings for the machine barrel temperatures in order to achieve the right melt
temperatures is different for amorphous and crystalline plastics. The barrel on a
molding machine is divided into at least three heating zones and each of these
zones can be set to a specific temperature. This results in a certain profile of barrel
temperatures. As described in Chapter 6, the screw inside the barrel of the mold-
ing machine typically has three sections. Each section performs a particular func-
tion. The base of the screw is where the plastic pellets first come in contact with
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 188 (page 188)

164 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
the screw. This part of the barrel is called the feed throat, it is designed to convey
and then soften the pellets. The plastic must not melt here because if it did, it
would stick to the barrel and/or the screw, preventing any additional material from
conveying further. Therefore, the barrel temperatures closer to the feed throat
must be set to the lower end of the recommended temperatures. The next section of
the barrel is set at a higher temperature to start the melting process. The increase
in the temperature of this zone depends on the morphology of the plastic material.
With crystalline polymers, the crystallites need considerable energy to soften and
melt and therefore the increase in temperature is typically higher than for amor-
phous plastics. But since crystalline plastics can also be heat sensitive or cannot
stand high temperatures for long periods of time, the temperature of the subse-
quent heating zones is reduced. This results in a heating profile that has a hump in
the middle (also called a hump profile). In case of amorphous plastics, such a pro-
file is not necessary because they need less energy to soften and can stand longer
times in a heated barrel. The temperatures of the subsequent zones are higher and
such a profile is called a conventional profile or regular profile. The different pro-
files are shown in Figure 8.7.
Nozzle
Amorphous
Crystalline
(Reverse profile)
Feed throatZone 1 Zone 2
Figure 8.7 Barrel heat profiles for amorphous and crystalline plastics
A hump profile can also be used for materials that are more difficult to melt or
when the material viscosity is high. Understanding the different sections of the
screw and their functions as described in Chapter 6 will further help in establish-
ing a setting for the melt temperatures. Typically, the nozzle temperatures are set
within approx. 5 °C (or about 10 °F) of the desired melt temperature.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 189 (page 189)

1658.10 Process Optimization – the 6-Step Study
 8.9  Setting Mold Temperatures
The processing data sheet provides the recommended mold temperature ranges
that should be used. It is important to make sure that the actual mold temperatures
are within this temperature range. The setting on a mold temperature unit (in case
of water and oil units) is typically a few degrees higher because there is always a
loss of heat that takes place during the transportation of the fluid. The actual mold
temperature must therefore be measured. As discussed in the thermal transitions
section of Chapter 2, the mold temperature is critical because it provides the en-
ergy for the molecules in the molten state to reach their final equilibrium resting
states without creating molded-in stresses.
The mold temperature is also critical for crystalline materials to provide the en-
ergy for crystallization because crystallization needs time and a certain tempera-
ture level. A mold that is set at a considerably lower temperature than the crystal-
lization temperature of the plastic will yield parts that have inferior properties
and/or will exhibit excessive post-mold shrinkage and warpage caused by the
lower degree of crystallization in these parts. Amorphous materials are more for -
giving. Because the molecules are randomly distributed, there is no ‘preferred’
equilibrium place for the molecules. Therefore, some deviation from the published
values is accepted. It is not uncommon to mold thick-walled ABS parts at mold
temperatures of 15 °C (60 °F) although the minimum recommended values are
above 38 °C (100 °F). Naturally, this does not imply that mold temperature devia-
tion is acceptable for all thick-walled parts molded from an amorphous resin. Each
case should be assessed individually.
 8.10  Pr ocess Optimization –
the 6-Step Study
8.10.1Step 1: Optimization of the Injection Phase–Rheology Study
All plastic melts are non-Newtonian. This means that their viscosity does not re-
main constant over a given range of shear rates. In the strict sense, the rheological
behavior of a plastic is a combination of non-Newtonian and Newtonian behavior.
At extremely low shear rates, which are rarely encountered in injection molding,
the plastic is Newtonian; but as the shear rate increases, the plastic tends to ex-
hibit non-Newtonian behavior. Interestingly, as the shear rates increase further,
the plastic tends to act more and more Newtonian after an initial steep drop in
viscosity. In Figure 8.8, the plastic viscosity is plotted on a log-log scale, and in
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 190 (page 190)

166 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
Figure 8.9, the plastic viscosity is plotted on the linear scale. Both graphs are for
PBT and are plotted from identical data, the only difference being in the scale type.
10
100
1000
1001 0001 0000
PBT-4
Apparent Shear Rate (1/s)
App. Shear Viscosity (Pa-s)
Figure 8.8 Viscosity of PBT represented on the logarithmic scale
0
200
400
600
800
02 000 4000 6000 8000
PBT– 4
Apparent Shear Rate (1/s )
App. Shear Viscosity (Pa-s)
Figure 8.9 Viscosity of PBT represented on the linear scale
On the linear scale graph, it can be seen that the change or drop in viscosity is
much greater at lower shear rates as compared to higher shear rates. This happens
because with increasing shear rate, the polymer molecules start to untangle from
each other and start to align themselves in the direction of flow. This reduces the
resistance to flow (the viscosity). The plastic tends to get more Newtonian at higher
shear rates. Although there is still a continuing drop in the viscosity, the change is
not as significant as at the lower shear rates. Figure 8.10 illustrates this phenome-
non. For the sake of discussion, we shall refer to these regions as non-Newtonian
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 191 (page 191)

1678.10 Process Optimization – the 6-Step Study
and Newtonian regions. These are no truly Newtonian regions and the slope of the
line depends on the nature and properties of the plastic. Typically, crystalline ma-
terials tend to have a flatter region compared to amorphous materials because the
viscosities for crystalline materials are lower, facilitating the ease of orientation.
No orientation
Some orientation
Maximum orientation
Injection Speed
Viscosity
Direction of flow
25000
20000
10000
5000
0
0
10 20 30 40 50 60 70 80 90 100
15000
Figure 8.10 Orientation of the molecules in the direction of flow at different injection speeds
(shear rates)
During injection molding, the material is subjected to high shear forces during the
injection phase. The shear rate is proportional to the injection speed. If the shear
rates are low and are set in the initial non-Newtonian region of the curve, then
small variations in the shear rate will cause a large shift in the viscosity. Because
there is always some natural variation, the mold filling will be inconsistent and
will therefore result in shot-to-shot inconsistencies. However, if the injection
speeds are set to higher values, the viscosity tends to be consistent. At high injec-
tion speeds, the shear rates are high and the effect of shear rate on the viscosity is
not as significant as it was at low injection speeds. Small changes in injection
speed result in small or almost no change in the viscosity of the melt. Figure 8.11
illustrates this concept using data that was generated on a molding machine. Any
natural variation in the speeds will not have a significant effect on the cavity fill in
the Newtonian region of the curve and it is therefore important to find this region
of the curve and set the injection speed, and with that the shear rate, here.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 192 (page 192)

168 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
10% Change in viscosity
= 6996 psi-s change in viscosity
50% change in viscosity
= 118 psi-s change in viscosity
Injection Speed
Viscosity
25000
20000
10000
5000
0
0
10 20 30 40 50 60 70 80 90 100
15000
Injection Speed
Viscosity
25000
20000
10000
5000
0
0
10 20 30 40 50 60 70 80 90 100
15000
Figure 8.11 Effect of change in injection speed on the viscosity of the plastic in the non-
N
ewtonian and Newtonian region
The viscosity curve can be generated at the molding machine for a given mold.
This is known as ‘in-mold rheology study’ or simply ‘developing the viscosity
curve.’ A study by Mertes et al. [2] demonstrated that at high speeds the variations
in the end of fill pressure were smaller compared to the variations at low speeds.
Perturbations were introduced on purpose and two polypropylenes with high and
low viscosities were used in the study. The results are shown in Figure 8.12.
0
50
100
150
200
250
02 04 06 08 0
Low Viscosity High Viscosity
Fast
Medium
Slow
Shot Number
EOF Cycle Integral (MPas)
Figure 8.12 End of fill cycle integral data at various injection speeds for two polypropylenes
of different viscosities [2]
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 193 (page 193)

1698.10 Process Optimization – the 6-Step Study
The other advantage of using high injection speeds is the reduction of the effects of
lot-to-lot variations. Figure 8.13 is a compilation of viscosity tests performed on
various lots of a certain grade of polycarbonate supplied to a molder on a specific
project. Different lots of the same material can have different viscosities at the
same injection speed. However, the difference is greater at the lower injection
speeds.
The procedure to determine the viscosity curve was first developed by John
Bozzelli. The basic pr
inciple is based on the melt rheometer that is used to study
the viscosity of plastics (see Chapter 3). The injection molding machine can also
be treated as a rheometer, where the nozzle orifice is the die of the rheometer and
the screw is the piston. The hydraulic pressure is applied to the molten plastic with
the help of the screw. The pressure required to move the screw at a set speed is
recorded.
Figure 8.13 Viscosity of polycarbonate of the same grade but from different lots
8.10.2 Pr ocedure to Determine the Viscosity Curve at the
Molding Mac
hine
Safety should always be given first priority when conducting any experiments:
 Se
t the melt temperature to the one recommended by the manufacturer. If there
is a range, set the temperature to the center of the range. However, as previous
discussed, because we are looking for the profile of the curve and not the actual
values, the selection of the temperature does not matter. See Section 8.10.7 for
an explanation.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 194 (page 194)

170 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
 Se t all the holding phase parameters to zero. This means that there will not be
any holding phase but rather only the injection phase.
 Pr
ovide a screw recovery delay time equal to the approximate time that would
allow the gate to freeze off. Refer to Section 8.6 for more information about this
step. The value of the charge delay time would be based on past experience. For
example, if for a similar part and material the gate freeze-off time was 5 seconds,
set the screw delay time to about 8 seconds.
 Se
t the injection pressure to the maximum available value. There is an assump-
tion here that the mold and the machine are compatible in terms of shot size and
plastic pressure usage. If the shot used is small or if the required pressure is
considerably less than the maximum available, then set the pressure to lower
values to avoid any mold damage or over packing of the cavity.
 Se
t the cooling time to a safe value such that the part will be cool and has reached
the ejection temperature before mold opening.
 The mac
hine must be set to transfer on screw position. Set the injection speed to
‘slow’ and make a part. The part should be short. If not, adjust the transfer posi-
tion to make the part such that it is filled only to about 50 %.
 Incr
ementally increase the speed as close to the maximum as possible in small
steps and make sure that the parts are still short. If the part is full, adjust the
transfer position, such that the part is about 95–98 % full by volume. This means
that at close to the maximum possible injection speed, the parts are 95–98 % full
with no holding time or pressure. If this is a multicavity mold, the part that fills
the most must be the one that is 95–98 % full. If at higher speeds, cosmetic issues
or burning issues are seen, do not increase the speeds any further.
 Mak
e another shot and record the fill time and the peak hydraulic pressure
at transfer. For example, the machine is set to 2200
psi
but may require only
1850
psi t
o move the screw at the maximum speed of 5
in/s. If t
he hydraulic
pressure was set to a value other than the maximum available, and during the
experiment the peak pressure matched the maximum value, the set pressure
must be increased. The process must not be pressure limited.
 N
ext, lower the speed by a small amount, for example from 5 in/s to 4.5 in/s or
from 90 % to 80 %. Note the fill time and the peak injection pressure.
 R
epeat the above steps until you achieve the lowest injection speed possible. Di-
vide the range of available injection speed into about 10– 12 speeds so that you
get the most data points possible.
 Obt
ain the intensification ratio of the screw from the machine manufacturer. If
this number is not available, use a value of 10. It is important to understand that
the intensification ratio is necessary to calculate the plastic pressure. However,
this should not be a show stopper for the experiment or the optimization process.
Since this is a constant used in the equation, the graph will shift up or down
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 195 (page 195)

1718.10 Process Optimization – the 6-Step Study
respectively, but the profile of the graph will remain the same, which is of pri-
mary interest to us.
 T
o get the viscosity, use the following formula:
Viscosity = Peak Injection Pressure × Fill Time × Screw Intensification Ratio
Plot the graph of viscosity versus injection speed. Figure 8.11 shows a typical vis-
cosity curve generated at the molding machine. Table 8.1 shows a sample work -
sheet that can be used for the study.
Table 8.1 Viscosity Curve Worksheet (Screw Intensification Ratio = 10.5)
No. Inj. speed
(in/s)
Fill time
(s)
Peak hyd. press
(psi)
Viscosity
(psi-s)
1 0.20 5.75  735 42263
2 0.50 2.37  805 19079
3 1.00 1.28  963 12326
4 1.50 0.87 1112  9674
5 2.00 0.68 1240  8432
6 2.50 0.57 1339  7632
7 3.00 0.50 1427  7135
8 3.50 0.44 1504  6618
9 4.00 0.41 1588  6511
10 4.50 0.38 1663  6319
11 5.00 0.36 1669  6008
8.10.3How to Use this Information
Looking at the created curve, it is noticeable that the viscosity stays fairly constant
after about 50 % of the injection speed. Therefore, setting the injection speed to
60 % would ensure that the filling stage of the process will stay consistent. Any
small natural variations will not cause large changes in viscosities that result in
shot-to-shot variations as it would at lower injection speeds. The injection speed
must be selected closer to the “knee” part of the curve. This is where a shift in the
viscosity and greater consistency can be observed. It is not advisable to inject the
plastic as fast as possible for a couple of reasons: First, plastic materials can be
shear sensitive and will degrade at higher shear rates or injection speeds. Second,
it is always difficult to get the best venting possible in a mold because of the very
valid concern of flashing plastic into the mold vents. For this reason, mold makers
are very conservative with vent depths and reliefs. A mold maker will typically
machine in the smallest vent clearances possible, as vents are not a steel safe con-
dition. Venting is also sometimes difficult in areas such as deep pockets or corners
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 196 (page 196)

172 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
that are not on the parting line of the mold. A slower injection speed helps in such
cases. Optimizing the injection speed through in-mold rheology is the first step to
achieving a robust process.
One can also plot a graph of viscosity versus shear rate. Because shear rate is pro-
portional to injection speed, the curve profile stays the same. It is easier to read an
injection speed graph so that one can directly select the injection speed from the
graph rather than having to cross reference in a table of shear rates.
When observing the short shots from a viscosity study, it is evident that the parts
get shorter and shorter as the injection speed is lowered. The question that usually
comes to mind here is why are the parts getting smaller if the shot size and trans-
fer position is not changed?
There are two phenomena explaining this condition. First, the viscosity of the plas-
tic is being reduced with the increased injection speed. One must remember that
when the viscosity of the melt is lowered, its flow rate also becomes lower. Second,
the momentum of the screw and the melt also reduces with decreasing injection
speed. When the hydraulic pressure is abruptly cut off at the end of the injection
phase, the screw and/or the melt can still travel further and fill the cavity due to
the inertia of the screw. At higher injection speeds the momentum is higher and
the viscosity is lower.
The position of the screw can also be tracked by recording the furthest forward
position it reaches during the injection phase. The cushion value displayed on the
machine can be misleading because this number represents the position of the
screw at the end of the holding phase and may not necessarily represent the fur -
thest position of screw travel. In some cases, a screw bounce-back can cause the
cushion value to be higher. In cases of electric machines, there is no hydraulic
pressure but instead a servo motor that controls the position of the screw. The
servo system will stop the screw instantly with almost no momentum, but the melt
will still have some momentum. Pictures of a fill progression during a viscosity
study series are shown in Figure 8.14.
Slow Speed Fast Speed
Figure 8.14 Progression of fill during an in-mold rheology study from a slow to fast injection
speed
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 197 (page 197)

1738.10 Process Optimization – the 6-Step Study
8.10.4Cautions and Exceptions
Generating the viscosity curve is a great tool to find out the effect of injection
speed on the viscosity of the plastic. However, it must not be used in all cases,
there are exceptions:
 Inser
t molded components typically have inserts that need to be partially or
wholly encapsulated with the plastic, and in most cases, these parts are held
inside t
he cavity. Injection of plastic at high speeds can easily dislocate and/or
deform the insert, thus molding an unacceptable part.
 High speeds also t
end to shear the material and in some cases cause gate blush
or splay. Optical components can sometimes exhibit this problem, which necessi-
tates that lower speeds be used. PVC is a prime example where faster speeds will
cause burning.
 A
t higher injection speeds, gas must be vented from the mold very efficiently.
Venting some sections of the mold can become tricky and difficult. In such cases,
only the fastest possible speed without burning should be used. In these molds,
the vents must be cleaned very frequently because any build up will result in
burning of the plastic.
 If t
he required pressure to fill the mold equals the maximum available pressure,
then the process is said to be pressure limited. In such cases, the injection screw
will never reach the set injection speed for lack of pressure. Therefore, the values
of the fill time will not be accurate and the obtained viscosity graph will be of no
value. Viscosity studies must not be done for pressure limited processes.
 T
o get accurate fill time and peak pressure readings, the machine must have
enough time to respond. Using lower that 20 % of the barrel does not allow for the
screw to have enough time to consistently build the plastic pressure and/or out-
put the fill time accurately or consistently. The plastic melt is compressible, and
this also adds on to an inconsistency of pressure readings.
 When t
he parts are small (less than about 5 to 8
mm) a viscosity cur
ve may not
be accurate. This follows the same reason of the previous bullet point.
In all such cases, the rule should be “Inject as fast as required and not as fast as
possible or what the viscosity curve provides.”
8.10.5Profiling of Injection Speeds
Refer to Figure 8.14. When the screw of the molding machine moves at predefined
injection speeds in predefined segments, the injection speed is said to be profiled.
Profiling of injection speeds is common in injection molding. For example, if the
plastic is injected at fast speeds at the gate, a cosmetic defect such as gate blush
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 198 (page 198)

174 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
could develop. For this reason, processors will slow down the injection speed in the
corresponding segment and then speed it back up. Because plastic flow is laminar,
as soon as the skin around the gate area is formed, changing the injection speed
will not change the cosmetics in the gate area.
Shot SizeTransfer
Posi/g415on
0.00 20 1501307030
V-1V-2V-3SLOW
V4
(All distances in mm)
Figure 8.15 Injection speed profiling
In the last section of the injection phase, the screw must always be slowed down.
See velocity V4 in Figure 8.15. To achieve part consistency, the point where the
process transfers from the injection phase to the pack and hold phase must also be
consistent. For example, in Figure 8.15, if the transfer position is 20
mm, t
hen the
screw must start to slow down at around 30
mm in or
der to consistently hit the
20
mm mar
k. Overshooting or undershooting will inject more or less material into
the cavity causing a variation in part quality. This slowdown is analogous to com-
ing to a red traffic light where the driver starts to slow down a few meters before
the signal line in order to avoid over passing the signal line.
Profiling must be done within reason. One must think of the distance traveled and
the number of profiles added. The melt is a viscous mass that will keep moving if it
has the momentum, even if the screw has stopped moving. The valves and hydrau-
lics also will need to react to the changes. If the total movement of the screw from
the shot size to the transfer position is, for example, 25
mm, adding 5 v
elocity
profiles with a segment length of 5
mm eac
h will not be effective. The ineffective-
ness is worse with fast injection speeds. One must keep in mind the melt momen-
tum and response times of the valves and hydraulics when setting the profiles and
the velocities.
8.10.6When a Short Shot Sticks
In some molds it is not possible to continually make short shots because the parts
can stay in the fixed side of the mold. In this case, an attempt must be made to find
the 95–98 % full cut-off position at close to the maximum injection speed. There are
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 199 (page 199)

1758.10 Process Optimization – the 6-Step Study
a couple of ways this can be done. First, would be the method described earlier and
would involve removing the part every time the short shot occurs. This will dictate
that the machine be run in a semiautomatic mode. If this is quick, without the use
of excessive times of more than about 10 seconds, it is acceptable. If it takes time
to get the parts out, then the procedure below should be used:
 S
tart molding with the least amount of pack and hold pressures and times such
that the part moves with the moveable side of the mold.
 Chang
e the transfer position such that the part looks underpacked and/or
slightly short.
 Incr
ease the injection speeds to the maximum possible with care as to not over -
pack or burn the plastic. At each speed, adjust the transfer position such that the
part looks underpacked and/or slightly short.
 S
tart the viscosity study and collect the fill times and peak pressures.
The reason this technique will work is the following: In this procedure, it is accept-
able to add any holding pressure to fill the part so that it pulls away from the fixed
side of the mold and stays on the ejection side during mold opening. The two val-
ues that are required in the calculation of the viscosity are the peak injection pres-
sure and the fill time. Therefore, what happens in the holding phase, which follows
the injection phase, does not affect these values. Whether or not the parts get filled
and packed out is not of concern. Not having any holding pressure or time and
producing a short shot has its value; however, in cases where this is not possible, it
is acceptable to fill the parts.
As the injection speed increases, the fill time will decrease and the shear rate will
increase. However, the pressure required to maintain the injection speed is an
agg
regate of the individual pressures of the various phenomena taking place as
the plastic melt travels to the end of fill. Therefore, with increasing injection
speeds, the required pressure can either increase or decrease, depending on the
dominant phenomenon. These phenomena and the resulting required pressures
are described in the following:
 As
the melt hits the mold, it starts to cool, resulting in an increase in the visco
-
sity of t
he plastic. This will result in an increase in the required pressure.
 The flo
w channels in the mold typically call for progressively smaller cross sec-
tional areas towards the end of the flow. Smaller cross sections result in higher
required pressures. However, if the cross sections are generous, the resulting
pressure may not change.
 When t
he plastic first enters the mold, the layer of plastic next to the wall forms
a frozen layer and the hot melt that is entering the mold now flows in between
these frozen layers. This is also called fountain flow. This frozen layer gets thicker
and thicker during the filling phase, again increasing the required pressure to
move the screw at the set injection speed. With thick parts or generous flow
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 200 (page 200)

176 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
channels, this effect is not significant because the filling may be completed be-
fore the frozen layer is sufficiently built up.
 Because
plastics exhibit non-Newtonian behavior, with increasing injection speeds,
the viscosity drops and the pressure required to move the screw will reduce.
8.10.7Selecting Melt Temperature for Viscosity Graphs
Referring to Figure 3.9, the lines of the viscosity graphs at various temperatures
as a function of shear rate are all parallel to each other. A reason to perform the
viscosity study on a molding machine is to find the injection speeds at where the
viscosity remains fairly consistent. The actual viscosity number is not of any value
at this point. If the temperature increases, the viscosity drops, and if the tempera-
ture decreases, the viscosity increases, but the profile of the viscosity curve stays
the same. Refer to Figure 8.16, which shows the viscosity study done on a HDPE
material at 175 °C and 220 °C. It is clear that the two profiles of the curves are
identical, the only difference is that the viscosity is higher at 175 °C and is lower
at 220 °C, therefore, the curves run parallel to each other.
Because the reason for developing the viscosity curve is to find the region of the
curve that is most consistent, the profile of the curve is all that matters. Because the
profiles are identical, the selection of the temperature for the study is not critical.
2500
5000
7500
10000
12500
15000
17500
20000
22500
25000
0.20 .5 1.01 .5 2.02 .5 3.03 .5 4.
04 .5
Relative Viscosity (psi-sec)
Injection Speed
Rel Viscosity 175 °C
Rel Viscosity 220 °C
Viscosity Curve for Polyethylene at 175 °C and 220 °C
Figure 8.16 Injection Speed
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 201 (page 201)

1778.10 Process Optimization – the 6-Step Study
8.10.8Step 2: Determining the Cavity Balance – Cavity Balance Study
A specific volume versus temperature graph was discussed in Section 2.8. The
graph is shown in Figure 8.17 with the areas that correspond to the different
phases of the injection molding cycle. The injection phase corresponds to the plas-
tic being in the melt phase and as the melt starts to cool, the pack and hold phase
come into effect. When the pack and hold is done, the plastic is cooled down below
the ejection temperature where it can be safely ejected out of the mold.
Shrinkage is directly related to specific volume. As the pressure increases, the
specific volume decreases. The packing pressure therefore affects the shrinkage of
the part. The higher the packing pressure, the higher is the pressure of the plastic
inside the cavity and the lower is the shrinkage. Therefore, to control the dimen-
sions of a part, the packing pressure or cavity pressure must be controlled. Inci-
dentally, this is the principle behind the use of cavity pressure sensing technolo-
gies that will be described in Chapter 12.
Figure 8.18 shows the effect of cavity pressure on the length of a tensile bar. The
tolerances are also shown on the graph. As the cavity pressure increases, the
length of the tensile bar increases.
Crystalline
Amorphous
Semicrystalline
Shrinkage
Cool Hold Pack Injection
- Semicrystalline Polymers- Semicrystalline Polymers
Specific
Volume
T T
Figure 8.17 Effect of temperature on specific volume and the application to injection molding
Now let us consider a two-cavity tensile bar mold. To mold tensile bars of equal
length, the plastic pressure in each of these cavities must be identical. When the
cavity fill is identical, the pack and the hold phases that follow will have the same
effect and produce identical cavity pressures. If one cavity happens to fill less than
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 202 (page 202)

178 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
the other, then at process switch-over from pack to hold, the cavity that fills first
will get pressurized more, leading to higher cavity pressure and therefore a larger
dimension. This will result in cavity-to-cavity dimensional variation. One cavity
may replicate the first tensile bar dimension in the figure and the other may repli-
cate the last one. When one is within specifications, the other may be out of speci-
fications. In addition, when the process windows are small, the cavity that fills first
may end up with flash, even when the other cavity is still unfilled (short).
Figure 8.18 Effect of cavity pressure on the length of a tensile bar
Procedure to Determine the Cavity Balance
In order to achieve cavity balance, it is important to determine the reason(s) for
any existing imbalance. First, the actual steel temperature in each cavity must be
checked via a reliable method. Contact type probes work best. A thermal imaging
system can also be very useful because it provides a quick picture even while the
mold is running. Any difference in the cavity temperatures should be close (within
a temperature difference of less than 2 °C or 5 °F).
Next, the incoming inspection of the mold should include a record of the runner
and gate sizes which must be identical. If no such record exists, the runner and
gates sizes must be inspected and recorded. Runners, and especially gates, wear
over time. Tracking these data over time is very valuable. These two factors will
determine if cooling and flow channel variations could pose a problem. The proce-
dure outlined in the following will determine if any flow imbalance exists because
of rheological or venting factors.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 203 (page 203)

1798.10 Process Optimization – the 6-Step Study
 Se t the holding pressure to zero.
 Se
t the holding time to zero.
 Se
t the screw recovery delay time to a value close to an estimated holding time,
similar to the step in generating the viscosity curve in the previous section.
 Se
t the cooling time to a value that will ensure that the part will be cool enough
to eject.
 Se
t the injection speed to the value obtained from the viscosity curve study.
 W
ith the rest of the settings identical to the viscosity study, start molding. Be-
cause this test is done immediately after the viscosity study, the settings must
yield a short part. If there is a visible cavity imbalance, the cavity that fills the
most of all cavities must still be unfilled. For example, in a four-cavity mold, if
cavity number 4 fills first, then in this study start molding parts so that cavity 4
is about 98 % filled. At this setting, the other cavities will now have filled less
than the 98 %. All cavities will now be underfilled. Save the short shot and record
the weights of each cavity. Take an average of at least two shots.
 N
ext, generate a short shot series and record the cavity weights for each shot as
in the step above. Depending on the size of the part, at least 3 to 4 progressing
shots must be recorded, starting with the smallest short shot parts that are pos-
sible to make. Next, the data must be plotted on a chart similar to the one shown
in Figure 8.19.
Table 8.2 shows an example of the worksheet that can be used to document the
cavity balance study.
Table 8.2 Cavity Balance Worksheet
Cavity ID Part weight (g)
10 % Part 25 % Part 50 % Part 75 % Part End of fill
1 1.94 3.15 6.12 8.34 12.94
2 1.92 3.14 6.20 8.21 12.85
3 1.95 3.25 6.92 8.86 12.12
4 1.95 3.36 6.55 8.52 12.82
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 204 (page 204)

180 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
Figure 8.19 shows that at lower percentage fills with all the cavities filled evenly.
8.0
6.0
4.0
2.0
0.0
Cavity number
Part weight (grams)
10.0
1 23 45 67 8
Figure 8.19 Cavity balance graph
 8.11  Reasons for Cavity Imbalance
Refer to Figure 8.20(a)–(e) that show a two cavity mold that has an imbalance in
the fill, where Cavity 1 fills less than Cavity 2. The possible reasons for the imbal-
ance between the two cavities are as follows:
1.
N
onuniform flow channel dimensions: The runners and the gates are the flow
channels that feed the cavity. If they are not of identical dimensions, then the
melt flow rate into the cavities will not be identical resulting in the imbalance.
In Figure 8.20(a), either the runner or the gate of Cavity 2 could be larger than
that of Cavity 1.
2.
N
onuniform Venting: The air has to escape out of the mold in order for the plas-
tic to get in. There can never be too much venting and the more vents, the better.
In Figure 8.20(b), if Cavity 1 has less vents than Cavity 2, then the air does not
escape as easily as in Cavity 2, and therefore the plastic flow rate into Cavity 1
is less than that of Cavity 2.
3.
N
onuniform cavity wall dimensions: Refer to Figure 8.20(c). This issue can show
up mainly in thin wall parts and is not an issue with thicker wall parts. If the
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 205 (page 205)

1818.11 Reasons for Cavity Imbalance
wall thickness decreases, a couple of phenomena can happen. First, a decrease
in wall thickness will reduce the cross section and will cause that cavity to fill
less than the other cavity. However, it could also happen that the drop in the
wall thickness can also increase the shear in the plastic, which will in turn re-
duce the plastic viscosity filling that cavity more than the other. Assuming there
is a wall thickness issue, if the thinner part fills more than the other, it is a rhe-
ology difference, where if the thinner wall fills less than the other, it is an issue
of flow rates.
4.
N
onuniform cooling: Refer to Figure 8.20(d). If the water flowing in Cavity 2 is
warmer than the water in Cavity 1, the plastic is going to flow easier into Cavity
2 and cause the imbalance. In a production environment, it is common that a
line can get plugged up or the water line was not opened during startup because
of an error. Cavity imbalances due to cooling usually do not show up until a few
shots have been molded, and the cavity has got warmer. Water flow also takes
the path of least resistance. If the pressure drop is higher in one cavity than the
other, there can also be an imbalance, especially when the flow is closed to be-
ing a laminar flow. Flow types should therefore be checked using the Reynold’s
number formula.
5.
Rheological imbalances: R
efer to Figure 8.20(f) and Figure 8.20(e). As discussed
in Chapter 3 on Polymer Rheology, there can be a rheological imbalance in the
mold filling process. The imbalance in a two-cavity mold will be different than
what you see in an eight cavity mold. In a two cavity mold, there will not be part
weight difference in the fill. A short shot in a two cavity mold will have parts
that will represent mirror images of each other. Rheological imbalances can be
fixed by altering the melt flow based on the principles and procedures devel-
oped by Beaumont Inc. Before the introduction of this technology, it was com-
mon to open the flow channels or the gates in order to balance out the flow.
When cavity balance is discussed, it is not just the fill pattern that we are inter-
ested in. Ultimately, the quality of the melt that is delivered to the different
cavities must be identical. The quality is defined not only by the flow rate, but
also by the pressure and temperature history of the melt. Although modifying
the runners and gates will balance out the flow rate, it will not balance out the
pressures or the temperatures.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 206 (page 206)

182 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
a)
Cavity 2 has a larger runner or gate size
Cav 1 Cav 2
b)
Cavity 1 has less ven/g415ng
Cav 1 Cav 2
c)
Wall thickness for
Cavity 2 is greater
than Cavity 1
Cavity wall thickness is not uniform
Cav 1 Cav 2
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 207 (page 207)

1838.11 Reasons for Cavity Imbalance
d)
Cooling in Cavity 2 is not as
eﬃcient as in Cavity 1
OR
Water temperature in Cavity 2
is greater than in Cavity 1
Cav 1 Cav 2
e)
Cav 1 Cav 2
f)
Cav 1 Cav 2
Figure 8.20(a)–(f) Reasons for cavity imbalances
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 208 (page 208)

184 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
Short
Flash
Figure 8.21 Two-cavity mold with one cavity short and the second with flash molded
in the same shot
8.11.1Determining the Cause of Cavity Imbalances
If a mold has an imbalance, the reason could be any one of the ones described in
the previous section. To determine the reason, a short shot series fill study is per -
formed and the cavities are filled progressively and collected. A short fill of about
10 % of the part, a medium fill of about 50 % of the part, and an almost full part of
about 95 % filled shots are collected. If the 10 % fill shows an imbalance, it is most
likely a flow channel variation. Venting imbalances, wall thickness imbalances,
and rheological imbalances usually do not show until more of the cavities are filled.
Filling the cavities further to 50 % and then to the end of the fill will provide the
rest of the possible reasons. If the initial 10 % is balanced, but the 50 % and 95 % are
not, then it could be a venting issue. If it is a thin walled part, the part thicknesses
must be checked. If it is a two-cavity mold and the parts are filling as mirror
imag
es,
it is a rheological imbalance. After running the mold for a few shots, if one cavity
starts to fill more than the other, the cooling must be checked. Performing a short
shot series will provide the answers to the source of the imbalance.
8.11.2Calculating Cavity Imbalance
The common formula for calculating cavity imbalance is
((Max Cavity Weight – Min Cavity Weight) / Min Cavity Weight) × 100.
However, this is incorrect.
One must realize that in the mold filling process, the plastic is preferentially enter-
ing one cavity than the other when it should have entered both cavities at the same
rate. If one cavity was partially filled and weighed 12 grams and the other was also
partially filled and weighed 8 grams, in an ideal situation they both should have
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 209 (page 209)

1858.11 Reasons for Cavity Imbalance
filled 10 g rams each. The total fill was 20 g rams and the average is 10 g rams. One
cavity filled 2
g
rams more whereas the other filled 2
g
rams less. Or in other words,
the variation from the average was + 2
g
rams and – 2
g
rams, respectively. If a
change was made to a gate size, the 20
g
rams will now get distributed again be-
tween the two cavities and the average will still be 10
g
rams. For example, if the
gate size for the 8
g
ram cavity was opened up, then it could now be 9
g
rams, but
then the other cavity would weigh 11
g
rams. The part weight in the 12
g
ram cavity
changed without any change in its gate size. Variation from the average should
alw
ays be calculated.
Following are the steps to the calculations:
 R
ecord the weights of each short filled cavity
 A
dd the weights as the total fill.
 Calculat
e the average fill by dividing the total part weights by the number of
cavities.
 Calculat
e the variation from the average using the formula:
% Variation from Average = ((Average – Cavity Weight)/Average Weight)) × 100
See the example of a cavity balance study in Table 8.3.
Table 8.3 Example of a Cavity Balance Study
Cavity No. 95 % Fill Parts % Variation from Average
1 5.154  5.00
2 5.634 –3.84
3 5.468 –0.78
4 5.446 –0.38
Total weight (g) 21.702
Average part weight (g)  5.426
Cavity imbalance numbers in small parts can get very misleading because a small
change in the weight can lead to large changes in the percentage numbers. One
must be careful in such cases and sometimes a coefficient of variation should be
considered.
8.11.3Acceptable Level of Cavity Imbalance
It is impossible to get a near perfect balance in fill. The question then comes to
mind as to what is the acceptable level of cavity imbalance. Most companies have a
fixed number and most training courses teach that there should be a fixed number.
The answer is there cannot be such an acceptable number. For example, consider a
molder who is molding forks and spoons, and the percentage imbalance between
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 210 (page 210)

186 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
the least filled and the most filled is 15 %. However, when the molder applies the
pack and hold pressures and packs the parts out, not only does he get acceptable
looking parts, but there is also an acceptable process window. Dimension on forks
and spoons do not matter, so in this case, a 15 % or, for that matter, any cavity
imbalance w
ould not matter as long as the parts are cosmetically acceptable and
the process window is acceptable. In some multicavity molds, if one cavity is not
acceptable, it is a common practice to block off that cavity and then mold the parts.
If the parts pass the quality inspection with one blocked cavity, that equals 100 %
imbalance (1 cavity is 0 % whereas the other is 100 % full). This means that there
was enough cosmetic and dimensional tolerance available to the molder to block of
a cavity and mold parts.
Keeping in mind the PVT diagram for a plastic one can easily conclude that the
higher the pressure on the plastic, the less shrinkage will take place; or in other
words, the parts will get larger with increasing pressures. Refer to Figure 8.18,
which represents this concept.
An acceptable number for cavity balance depends on the dimensional and cos-
metic tolerances for the given part, so the number should be decided on in a case-
to-case basis and never as a generic rule. Refer to Figure 8.22 and consider the two
scenarios shown. The imbalance between the two cavities is 10 %. In scenario 1,
the dimensional tolerances are +/– 0.010" on both sides of the nominal and the two
cavities are within tolerance. However, in scenario 2, the tolerances are dropped
down to +/– 0.005" and now 10 % becomes unacceptable.
2.125″ NOM
2.135″ (USL)
2.115″ (LSL)
DIMENSION
Cav 1 Cav 2
0.010″
0.010″
FILL IMBALANCE
= 10%
ACCEPTABLE
Cav 1 Cav 2
2.130″ (USL)
2.120″ (LSL)
0.005″
0.005″
2.125″ (NOM)
FILL IMBALANCE
= 10%
UNACCEPTABLE
SCENARIO 1 SCENARIO 2
Figure 8.22 Acceptable % imbalances and tolerances
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 211 (page 211)

1878.11 Reasons for Cavity Imbalance
In some molded products, such as the wall clips shown in Figure 8.23, there are
very large percentages of imbalances that do not matter. Most common users do
not realize that these are actually sold with the runner system that acts as a car -
rier or a holder. The clip is broken off and used and the runner is discarded. The
same is true with several toy kits where children assemble a figure or a vehicle,
breaking parts off an array of a grid, most of which is the runner system.
SPRUE
FILL
PROGRESSION
Figure 8.23 Fill progression in a wall clip mold
The polymer morphology also plays a role in cavity balance. Amorphous materials
can tolerate more imbalance than crystalline materials. Amorphous materials do
not shrink as much as crystalline materials, and therefore cavity-to-cavity dimen-
sional variations are smaller. At the same time, because crystalline plastics flow
easier, they tend to flash easily, reducing the process window. Balancing out the
flows between cavities helps improve the process window regardless of the mor -
phology of the material and whether the tolerances are wide or not.
Family Molds
Family molds are molds that do not mold identical parts in all cavities. It is com-
mon to build family molds for small production runs of assemblies. The balance of
fill is important in family molds, too. Again, the concept here is the same as before,
where the cavity pressure is the deciding factor for the dimensions. Typically, in
these cases, the gate and runner sizes are adjusted to balance out the fill. Depend-
ing on the configuration, the number of cavities and the cavity layout, a decision
must be made on the type of cavity fill balance technique.
8.11.4Step 3: Determining the Pressure Drop – Pressure Drop Studies
Consider a driver driving a car on a flat road at a desired speed of 70 km/h. T o
achieve this speed, the gasoline pedal is depressed 50 % of the maximum possible.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 212 (page 212)

188 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
As the driver approaches a hill, to maintain the desired speed of 70 km/h the
driver will now need to depress the pedal further to provide for more gasoline
needed to overcome the excess work to drive uphill. To maintain the desired speed,
the position of the pedal is adjusted. If the position of the pedal was not adjusted,
and was kept at the 50 %, then as the car starts to climb, the hill the speed would
drop from 70
km/h t
o a lower value. In molding, enough pressure must be avail
-
able t
o compensate for all the pressure losses and material viscosity variations
while keeping the injection speed constant. Refer to Figure 8.24.
Speed = 70 km/h
Gas pedal is depressed
half way
Speed = 70 km/h
Gas pedal is depressed more than
half way to maintain the speed of
70 km/h
Speed = 70 km/h
Gas pedal is depressed
half way
Speed = 50 km/h
Gas pedal is depressed half way
Scenario 1
Scenario 2
Figure 8.24 Maintaining the speed of car
As plastic flows through the different sections of the nozzle and the mold, the flow
front of the plastic experiences a loss of applied pressure because of drag and
fr
ictional effects. Additionally, as the plastic hits the walls of the mold, it begins to
cool, increasing the viscosity of the plastic, which in turn requires additional pres-
sure to push the plastic. Due to the fountain flow effect, the outer frozen layer also
gets thicker and thicker, thereby reducing the available cross sectional area for the
flow, therefore, increasing the required force to push the plastic through the flow
channel. Depending on the pump capacity of the molding machine, there is a lim-
ited maximum amount of pressure available to push the screw at the set injection
speed. The required pressure to push the screw at the set injection speed should
never be more than the maximum available pressure. If the pressure required is
higher, the screw will never be able to maintain the set injection speed throughout
the injection phase and the process is considered pressure limited. Initially the set
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 213 (page 213)

1898.11 Reasons for Cavity Imbalance
speed may be reached, but as soon as the process becomes pressure limited, the
screw slows down as shown in Figure 8.25.
2000
1500
1000
500
0
Flow area
Nozzle Sprue Primary Secondary Gate Mid Part EOF
Pressure (psi)
Max available pressure
2500
350
458
734
1004
1235
1420
2000
Figure 8.25 Graph to determine the pressure drop through the mold
The term ‘pressure drop study’ can be confusing. The machine pressure required
to push the plastic at a constant speed increases as the flow progresses, but the
actual pressure of the melt front drops as the flow progresses. It can easily be un-
derstood by looking at a short shot where the pressure at the end of the flow is
zero. The words pressure and drop are related to the plastic.
During process development, knowing the pressure loss in every section of the
flow path helps to determine the overall pressure loss and the sections where the
pressure drops are high. The mold must be modified to reduce this pressure drop,
if the process is pressure limited. The runner system of the mold can then be mod-
ified to reduce this pressure drop and achieve a better consistent flow. Sudden
changes in pressure drop from one channel into another are not desirable. The
sections where there are sudden changes in the pressure must be modified to
achieve a better consistent flow.
Procedure to Determine Pressure Drop
The pressure drop study is done as the third step and therefore by now, the injec-
tion speed must be fixed based on the viscosity study; the shot size and transfer
positions must be fixed based on the 95 to 98 % fill. It could be possible that a
viscosity s
tudy was not done because the process was pressure limited. In such a
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 214 (page 214)

190 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
situation it becomes even more imperative to conduct a pressure drop study and
determine the restrictive sections of the flow. The procedure is as follows:
Consider the plastic flows through the following sections: the nozzle of the ma-
chine, the sprue, the primary runner, the secondary runner, the gate, and the end
of fill.
Set the melt temperature, shot size, transfer position and the injection speed as
follows:
For a nonpressure limited process, set these based on the viscosity study and the
95 to 98 % rule as described in the previous sections.
For a pressure limited process, set the injection speeds to center of the range on
the machine and find the values of the shot size and transfer where the parts are
about 95 to 98 % full.
The injection pressure setting should be set to about 20 % higher than the maxi-
mum recorded value during the viscosity study.
Start molding and let the process stabilize. The parts should be short and almost
filled. Record the displayed peak injection pressure on the screen of the machine.
This value would represent the amount of pressure required to fill the mold almost
up to the end of fill.
Next adjust the transfer position to fill about 50 % of the part and record the peak
pressure value again.
Continue the procedure to mold 5 to 10 % of the part, the secondary runner, the
primary runner, and then just the sprue.
After this data is collected, stop molding and pull the barrel back and away from
the mold. Build a shot and inject the plastic as one would purge the barrel. This is
called an air shot. Record the max pressure during this injection. This would be the
pressure required to inject the plastic through the machine nozzle.
Plot a graph of the required pressure versus the flow section starting from the
mac
hine nozzle. The graph is called the pressure drop study and will show the re-
quired pressure progressively increasing as the plastic fills the mold and up to the
end of fill. Figure 8.26 shows such a graph.
Note: Data should be collected on stabilized cycles. Therefore, if at any time a sec-
tion of the part or runner starts to stick on the mold and it takes more than 20 to
30 seconds to remove the stuck part, the study should be stopped because the data
will not be reliable. This is very common as one comes to molding just the runner
or the sprue. It is not required to collect the data. If the last data point collected
was a number that was high, such as about 50 % of the maximum available ma-
chine pressure, the runner sizes must be investigated. This is a common problem
with some hot runner molds where one can notice that most of the available pres-
sure is taken up to get the plastic to exit the hot runner and into the mold. In case
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 215 (page 215)

1918.11 Reasons for Cavity Imbalance
of hot runners, the same steps above can be performed and the pressure drop
through the manifold can be determined.
2000
1500
1000
500
0
Flow area
Nozzle Sprue Primary SecondaryG ate Mid Part EOF
Pressure (psi)
Inj speed
2500
350
458
734
1004
1235
Pressure drop
Inj speed
Max pressure
Figure 8.26 Effect of a pressure limited process on injection speed
In all instances, the pressure drop through the nozzle should always be measured
and recorded. The pressure drop through the nozzle is inversely related to the size
of the orifice. As the orifice size decreases, the pressure drop increases. During
mold startup, the actual pressure drop through the nozzle must be compared to the
recorded pressure drop. This will give an indication of whether the right size and
type of nozzle is installed on the machine. For example, the nylon type nozzle will
have a slightly higher pressure drop as compared to a conventional nozzle for the
same diameter orifice.
If any problems arise with the part filling during production, one of the first
actions
mus
t be to pull the barrel back and check the pressure drop through the nozzle.
Any debris, such as metal shavings stuck in the nozzle, can cause an increase in
pressure drop. This loss of the pressure drop at the nozzle gets added to the sprue,
the runner, the gate, and the part. If the process is close to being pressure limited,
this can easily lead to short shots and defective parts. Moreover, the loss in pres-
sure in the runner system leads to a loss in cavity pressure and therefore a change
in dimensions, shown in Figure 8.27. The type and orifice size of the nozzle are
therefore very important and must be recorded as part of the setup sheet.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 216 (page 216)

192 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
2000
1500
1000
500
0
350
458
734
1004
1235
1420
Flow area
Nozzle Sprue Primary SecondaryG ate Mid Part EOF
Pressure (psi)
Possible shorts & underfill
Max pressure
2500
2000
Larger nozzle ortifice
Smaller nozzle ortifice
Figure 8.27 Effect of nozzle type and size on near pressure limited processes
In hot runner molds the procedure should start with the nozzle and then continue
with the section where the melt is first injected into the mold. The hot runner sec-
tion of the mold must be considered as one flow section, and then each subsequent
flow section must be analyzed. If it is possible to manually inject the plastic at the
set speed. An injection of the plastic into an open mold should be performed, and
the pressure drop should be recorded. For safety reasons some machines do not
allow the processor to inject plastic at the full set injection pressure. In such cases,
the data should still be recorded, and the machine should be clearly identified on
the setup sheet. Safety should be of primary concern, and no safety features of the
machine should be compromised. In the case of a hot runner mold, injecting
through the manifold with the mold open can provide insight into the pressure
drop through the hot runner system. Preferably, a piece of thick cardboard should
cover the moveable side of the mold to prevent any splatter of plastic onto these
surfaces. A cardboard shield should also be placed underneath the bottom of the
mold for the purge, and another over the top of the mold, to prevent any un
e
xpected
burst of high pressure plastic from splattering above the mold and falling onto
personnel near the machine.
The pressure drop through the different sections of the part must also be evaluated
especially in thin walled parts. Thin sections in a mold require more pressure to
fill and can make a process pressure limited. Although the runners and the gates are
generously designed, the part can have restrictions that may cause a pressure drop.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 217 (page 217)

1938.11 Reasons for Cavity Imbalance
Table 8.4 is an example of a worksheet that can be used to document a pressure
drop study.
Table 8.4 Pressure Drop Study Worksheet
Section Peak pressure (psi)
Nozzle  236
Sprue  454
Primary runner  734
Secondary runner 1004
Tertiary runner 1248
10 % part 1630
50 % part 1837
End of fill 2030
How to Use the Information from the Study
The maximum pressure used in the process should never reach the maximum
available pressure on the particular machine. For example, if the maximum avail
-
able h
ydraulic pressure is 2200
psi, t
he end of fill pressure should not reach
2200
psi. T
ypically, only up to 90 % of the maximum available pressure should be
used. In the generated graph, if the process is pressure limited or reaches more
than 90 % of the maximum, steep increases in the required pressure between two
sections must be identified. For example, if the required pressure to fill through
the nozzle, sprue, primary, and secondary runner is 900
psi, and if t
hrough the
tertiary runner, the pressure increases to 1600
psi, t
his increase is significant as
compared to the increases in the previous sections. Modifications to the tertiary
runner must be made. Increasing the diameter of the runner will help in reducing
the pressure.
Another reason for a pressure drop study is to prevent the mold from being over -
packed. Refer to Figures 8.28(a) and (b). Consider that the shot size and the trans-
fer positions were set in accordance to the basis of the 95 % fill and that the mold is
not pressure limited. The screw will start from the shot size position and will use
the pressure to start filling the mold with constant set injection speed. If for some
reason during production one of the gates gets plugged, then the other cavity will
get filled to 100 % first. Because the screw has not reached the transfer position, it
will now use all the available machine pressure to try and reach the transfer posi-
tion and will end up over packing the cavity with the open gate. The cavity can
flash, and the mold components can get damaged. To avoid this problem, the injec-
tion pressure must be set to about 10 to 15 % of the peak required pressure. The
other safety should be a maximum limit on the injection time.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 218 (page 218)

194 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
TIME (SECONDS) 0
PRESSURE
0.0
Shot Size = 6.50 inTransfer Position = 1.00
Max Machine Pressure
Pressure required
to ﬁll the mold 95%
TIME (SECONDS) 0 PRESSURE
0.0
Shot Size = 6.50 inTransfer Position = 1.00"
Max Machine Pressure
Max available
pressure is
reached
Posi/g415on of the
screw (stalled)
Blocked
gate
Overpacked, ﬂashed,
damaged cavity
Figure 8.28 Pressure used to fill two cavities; (a) to 95 % fill, and (b) when one cavity gets
blocked
 8.12  Effect of Pr essure Drop on the
Pack and Hold Phase
The pack and hold phase are collectively the compensation phase. Pressure must
be available so that the plastic in the cavities can be pressurized and the shrinkage
can be compensated for. If the process is pressure limited, it is very common to
produce parts with sink and/or with dimensional issues (typically undersized) and
with large variations. If process capability is measured, then the values are typically
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 219 (page 219)

1958.12 Effect of Pressure Drop on the Pack and Hold Phase
low. This is because of the unavailability of the plastic pressure to pack the parts to
the optimum levels. Refer to Figure 8.29.
Pressure available
for pack and hold
= lower varia/g415on
No pressure
available for pack
and hold
= high varia/g415on
Figure 8.29 Effect of a pressure limited process on quality variation
8.12.1 S tep 4: Determining the Cosmetic Process Window –
Pr
ocess Window Study
Of all the six steps used for the first stage of process development, this is the most
important step. The aim of a molder is to set the molding process, start the molding
run, and walk away from it, and not have to come back to constantly to adjust the
process in order to make acceptable parts. It is similar to wanting to drive a car in
cruise control. But one can only drive a car in cruise control when the road is wide
enough to allow the minor variations by the driver during a long drive. It will be
impossible to apply cruise control if one is driving on a cliff of a mountain! The
wider the road the better the chances of a smooth drive. Similarly, wider the pro-
cess window, the better the chances are for a robust process.
As described earlier, the injection of plastic into the cavity can be divided into two
main phases. The first phase is the injection phase where the mold cavity is com-
pletely filled with the molten plastic. The volume of the melt is equal to the volume
of the cavity. The second phase is the compensation phase, which consists of the
pack and hold phase. The pack pressure must pack additional plastic material,
equivalent to the volumetric shrinkage caused by cooling as the plastic makes con-
tact with the cold mold walls and the hold pressure must hold the plastic inside the
cavity till the gate freezes off. The various parameters that need to be controlled
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 220 (page 220)

196 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
during this phase are packing pressure, holding pressure, packing time, and hold-
ing time. In most production processes, packing and holding are not differentiated
and are collectively called the holding phase. For this reason, for the discussion of
this section, we shall call the pack and hold phase as just the hold phase. Section
8.15 discusses optimizing the gate freeze times. The topic of differentiating be-
tween pack and hold will be discussed then.
The packing phase consists of packing the cavity with plastic equal to the theoret-
ical weight of the part. Any less plastic will result in an under-packed part while
any more will result in a part that is over packed. Under-packed parts show defects
such as sinks and internal voids. Such parts usually exhibit considerable post
molding shrinkage. Over-packed parts can have built-in stresses that usually get
relieved after molding resulting in defects such as warpage or premature mechan-
ical failure. The ideal pack and hold pressures are determined by evaluating the
process window of the mold followed by the gate seal study. Two process variables
are varied to establish the process window. For amorphous materials, the holding
pressure and the melt temperatures are the common variables that are used. The
mold temperatures are set either in the center of the recommended values or at a
desired value within the recommended range. This could be based on experience
on a similar part or for other reasons such as for better cosmetics.
For crystalline materials, the two variables that are selected are holding pressure
and mold temperature. In case of crystalline materials, the mold temperatures are
much more critical for the formation of the crystallites that finally dictate the prop-
erties of the part. The melt temperature range for crystallites is also narrow and
therefore varying the temperature is not going to give any more information than
that is obtained at the center of the temperatures. Holding pressure usually has
the most impact on the quality of the part because it directly influences the spe-
cific volume and therefore part dimensions. Therefore, the significance of holding
pressure applies to both types of materials. For amorphous materials, melt temper-
ature usually has the higher impact compared to mold temperature, and in case of
crystalline materials, mold temperatures have a higher impact compared to melt
temperatures.
The process window is also called the molding area diagram. This is the area in
which cosmetically acceptable parts are molded. Dimensions are not considered.
The bigger the window, the more robust is your process. It must be noted that the
process window provides only the range of processing parameters within which
cosmetically acceptable parts are produced, also called the cosmetic process win-
dow (CPW). Chapter 9 is dedicated to the different types of process windows.
Dimensional data must be taken and the mold steel must be adjusted to move the
dimensions to the center of the window in order for the process to be robust. Fig-
ures 8.30 and 8.31 show the process windows for amorphous and crystalline mate-
rials, respectively.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 221 (page 221)

1978.12 Effect of Pressure Drop on the Pack and Hold Phase
Melt temp
HLD press
410 420 430 440 450 460 470 480 490 500 510
350
375
400
425
450
475
500
525
550
575
600
625
650
675
700
725
750
775
800
825
Flash Process window
Low
melt
temp High
melt
temp
Short
Center of window = 460,575
Figure 8.30 Process window study for amorphous materials – hold pressure vs. melt
t
emperature
Mold temp
HLD press
100 110 120 130 140 150 160 170 180 190 200
350
375
400
425
450
475
500
525
550
575
600
625
650
675
700
725
750
775
800
825
Flash
Process window
Low
mold
temp
High
mold
temp
Short
Center of window = 165, 580
Figure 8.31 Process window study for crystalline materials – hold pressure vs. mold
t
emperature
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 222 (page 222)

198 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
Outside the illustrated process windows, parts produced will not be acceptable be-
cause of defects such as sink, flash, or built-in stresses. Below the melt tempera-
ture limits, unmelted plastic may cause problems such as short fill or lack of re-
quired properties because of lack of melt homogenity while above the temperature
limit, degraded plastic may render the parts that are unacceptable because of prop-
erties such as mechanical properties. With low mold temperatures the plastic may
not have enough energy for crystallite formation. On the other hand, with mold
temperatures higher than necessary for crystallization, cycle time may increase.
The process is set to the center of this window so that any variations within the
window would still yield cosmetically acceptable parts. The larger the window, the
more robust is the process.
Chapter 8 will define and further discuss the concepts of dimensional process win-
dow (DPW) and control process windows (CoPW).
Procedure for Determining the Process Window for Amorphous Materials
The following details the procedure for developing a process window for
amor
phous
materials using holding pressure and melt temperature as the two variables:
 Se
t the mold temperatures to a medium value or at a desired temperature within
the range of recommended mold temperatures.
 Se
t the barrel temperatures to attain the lower value of the recommended melt
temperatures.
 Se
t the injection speed to the value obtained from the viscosity curve experi-
ment.
 Se
t all holding times and pressures to zero.
 Se
t the screw delay time to a value approximately equal to the estimated holding
time for the part. Refer to Section 8.6 for explanations.
 Se
t the cooling time to a value higher than what would be typically necessary
(e. g., if the estimated cooling time is 10 seconds, set the cooling time to 20 sec-
onds).
 S
tart molding and adjust the transfer position to make a part that is 95–98 % full.
Record the part weight as the ‘injection only part weight value.’
 Le
t the process and the melt stabilize by molding approximately 10 shots of
parts.
 Se
t the hold time to a value that makes sure the gate is frozen. (The next section
deals with optimization of this time.) The determination of hold time is typically
based on previous experience. For example, for a 30 % glass filled PBT or nylon
with a gate size of 0.070", the hold time typically ranges between 6 and 10 sec-
onds. For this part of the experiment, we would set the hold time between 10 to
12 seconds.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 223 (page 223)

1998.12 Effect of Pressure Drop on the Pack and Hold Phase
 Incr ease the holding pressure in small increments and record the pressure at
which the first cosmetically acceptable part is made. There should be no defects
such as shorts, sinks, or voids.
 R
ecord this pressure as the ‘low temperature – low pressure’ corner.
 Incr
ease the pressure further in similar increments and record the pressure at
which there is evidence of an unacceptable result, such as part sticking in the
mold, flash on the part, or warpage. Record this pressure as the ‘low tempera-
ture – high pressure’ corner.
 Incr
ease the melt temperature to the higher end of the recommended melt tem-
peratures. Drop the hold pressure and hold time to zero and add the charge delay
time. Readjust the transfer position to obtain the ‘injection only part weight.’
 Incr
ease the holding pressure in small increments, and record the pressure at
which the first cosmetically acceptable part is made. There should be no defects
such as shorts, sinks, or voids.
 R
ecord this pressure as the ‘high temperature – low pressure’ corner.
 Incr
ease the pressure further in similar increments and record the pressure at
which there is evidence of an unacceptable result, such as part sticking in the
mold, flash on the part, or warpage. Record this pressure as the ‘high tempera-
ture – high pressure’ corner.
 Joining t
hese four corners will generate the process window or the molding area
diagram.
 Se
t the process to the center of this window.
Procedure for Determining the Process Window for Crystalline Materials
The following is the procedure for developing a process window for crystalline
mat
erials using holding pressure and mold temperature as the two variables. The
procedure is the same as than for amorphous materials except melt temperature is
replaced by mold temperature in this study:
 Se
t the melt temperature to a center value or a desired value within the range of
recommended melt temperatures.
 Se
t the mold temperatures to attain the lower value of the recommended mold
temperature range.
 Se
t the injection speed to the value obtained from the viscosity curve experi-
ment.
 Se
t all holding times and pressures to zero.
 Se
t the screw delay time to a value approximately equal to the estimated holding
time for the part.
 Se
t the cooling time to a value higher than what would be typically necessary (e. g.,
if the estimated cooling time is 10 seconds, set the cooling time to 20 seconds).
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 224 (page 224)

200 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
 S tart molding and adjust the transfer position to make a that is part 95–98 % full.
 Le
t the process and the melt stabilize by molding the approximately 10 shots of
parts. Record this as the injection only part weight value.’
 N
ow set the hold time to a value that makes sure the gate is frozen based on pre-
vious experience.
 Incr
ease the holding pressure in small increments, and record the pressure at
which the first cosmetically acceptable part is made. There should be no shorts,
sinks, or voids.
 R
ecord this pressure as the ‘low temperature –low pressure’ corner.
 Incr
ease the pressure further in similar increments and record the pressure at
which there is evidence of an unacceptable result, such as the part sticking in
the mold, flash on the part, or warpage. Record this pressure as the ‘low temper-
ature – high pressure’ corner.
 R
epeat the last two steps, but use the high end of the recommended mold tem-
perature. This time the two extreme parameter combinations would be the ‘high
temperature – low pressure’ and ‘high temperature – high pressure’ corners.
 Joining t
hese four corners will now generate the process window or the molding
area diagram.
 Se
t the process to the center of this window.
Table 8.5 is an example of a worksheet that can be used to document the process
window study.
Table 8.5 Process Window Worksheet
Melt temperature
(°F)
Low hold pressure
(psi)
High hold pressure
(psi)
430 550 1050
510 600 1100
How to Use this Information
The size of the process window is an indicator of how much variation the process
will tolerate while still producing cosmetically acceptable parts. The aim is to have
a wide process window. If the process window is very narrow, there is always a
danger of molding parts with defects. For example, the graphs generated via the
process window studies show that with a very small process window even natural
process variations could cause occasional short shots or flash. A robust process is
one that has a large process window and accommodates the natural variation in-
herent in the system.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 225 (page 225)

2018.12 Effect of Pressure Drop on the Pack and Hold Phase
A mold that produces short parts and parts with flash at the same time does not
have any process window. The mold must be fixed because it will be impossible to
make acceptable parts. Molds with extremely small process windows usually have
dimensional issues. The process at which the parts are cosmetically acceptable
produces parts that are out of specifications. When a certain specification is
achieved, the parts are usually not cosmetically acceptable. Achieving consistent
production from such molds is a difficult task and the processor often has to con-
tinually adjust the process. A few molds with small process windows on the produc-
tion floor can easily consume available resources and make a plant run inefficiently.
Determination of the process window is the most important process engineering
study of all and if nothing else, this is the one study that must be done.
The concept of the dimensional process window (DPW) is presented in Chapter 9.
The DPW is a subset of the CPW. The bigger the cosmetic window, the higher the
chances that the dimensions will be met. The DPW is a subset of the CPW. Every
effort must be made to have a large CPW.
Cautions and Exceptions
The process window described in this chapter is the cosmetic process window.
Within this processing window, parts can be molded that are cosmetically accept-
able. The procedure calls out for increasing a certain process parameter, such as
the holding pressure, to a limit where the parts would have a cosmetic defect such
as flash or the parts stick in the mold due to over packing. However, consider a
case where the parts do not flash even at high holding pressures or do not show
any signs of over packing. In these cases, although there is no evidence of failure,
the parts could very well be over packed. In such cases, the higher pressure at
which cosmetically acceptable parts can be molded must not be taken as the upper
limits of the process. An evaluation of the parts and the high pressure limits is re-
quired and the process must then be set accordingly. In such cases, cosmetic pro-
cess windows can be misleading because part failures may not be seen until they
are used in an assembly. Parts with large gates, hot runner mold, and valve gated
molds fall into this category. The concept of pack and hold that will be described in
Section 8.15 should be used in such cases.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 226 (page 226)

202 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
 8.13  R elationship between Cavity Balance
and Process Windows
Refer to Figure 8.32, which is a cavity balance study graph for a four cavity mold.
Cavity 2 is the last to fill and cavity 4 is the first to fill. This indicates that Cavity 2
will get packed out last and therefore will determine the low pressure value of the
process window. Because Cavity 4 gets packed out first, it will be the first one to
show the defects, therefore, it will determine the high value of the process window.
The higher the imbalance between cavities, the smaller is the process window. The
ideal situation would be that all the cavities fill at the same rate and therefore will
pack the same rate. This will lead to a wider process window and better the chances
of a robust process. Cavity balance plays an important role not just in cosmetics
but also in process robustness and process capability.
Fir st to pack,
ther ef or e ﬁr st to
ﬂash /s how de fe cts.
De termines the high
end of packing
pressures.
La st to pack, ther ef or e
la st to get rid of shorts/
de fe cts. De termines the
low end of packing
pressures.
The be/g425er the ca vity balance,
the wider is the cosme/g415c
pr ocess windo w.
FLASH
SHORT / SINK
Figure 8.32 Effect of cavity balance on the cosmetic process windows
 8.14  The P ack and Hold Pressure Rule
Not to Be Used
There are some molders who suggest that the pack and hold pressures should be
set to 50 % of the injection pressure. In reviewing the previous sections, it can be
identified that such a rule is impossible to follow for not just for cosmetic reasons
but as will be discussed further for dimensional reasons also. Further, consider the
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 227 (page 227)

2038.14 The Pack and Hold Pressure Rule Not to Be Used
molding process of a thin part such as a laptop cover and a thick part such as a lens
for a large optical equipment. In case of the laptop cover, the required injection
pressures will be very high to get the plastic flowing through the thin walls, but
the required pack and hold pressures will be very low because the shrinkage will
be minimal. In case of the lens, the injection pressures will be very low because
the flow into the mold cavity will be very easy due to the thick sections. However
high pressures will be required to pack and hold the plastic in there because the of
the large amount of shrinkage taking place in the thick section. The 50 % rule
should never be followed.
8.14.1Step 5: Determining the Gate Seal Time – Gate Seal Study
The molten plastic enters the cavity through the gate. The mold filling phase is
dynamic, during which melt temperature, pressure, and flow velocity are all chang-
ing with time. For the mold fill phase, time begins with injection, which is the start
of the forward movement of the screw. As the cavity begins to fill and is nearly full,
the pack and hold phases start. The melt flow velocity is reduced and the melt
t
emperature simultaneously drops. This causes an increase in viscosity of the
melt. The gate area has the smallest cross sectional area is the mold. When the
viscosity of the plastic in this area drops to a value at which the plastic cannot flow
anymore, the gate is considered frozen. The plastic molecules in the gate area are
now immobile and cannot flow into the cavity anymore. The time it takes to reach
this stage is called the gate freeze time.
For an injection molding process, pressure must be applied to the melt until such
time that the gate is frozen. If pressure is not applied for a sufficiently long time,
either the part will be under-packed resulting in internal voids or sinks; or plastic
pressure inside the cavity is high enough to flow back out of the cavity, which will
also result in under-packing. The second phenomenon usually takes place when
the holding time is just a little shorter than the gate freeze time, while the cavity is
full of pressurized plastic. Gate freeze time is a function of the type of plastic, gate
size, gate design, and the processing parameters of the machine. A gate freeze
study must be completed for every mold. A gate freeze study is a graph of part
weight versus holding time. Once the gate is frozen, the part weight stays constant
because plastic can no longer get into or out of the cavity. A constant part weight is
an indication of gate freeze. Figure 8.33 shows a typical gate seal graph.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 228 (page 228)

204 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
24.4
24.4
24.3
24.2
24.1
Hold time (s)
Part weight (grams)
24.5
0 21 34 56 78
24.6
24.7
24.8
Gate seal
Possible
overpacking
24.8
24.9
Figure 8.33 Gate seal graph
Procedure to Determine Hold Time
 Se
t the injection speed to the value obtained from the viscosity curve experi-
ment.
 Se
t the process at the center of the process window or towards the upper corner
of the right hand side upper quadrant of the process window generated in the
previous section. Holding pressure, melt temperature, and mold temperature val-
ues may influence the gate seal time. The higher the pressures and tempera-
tures, the easier is the movement of the plastic in and out of the cavity. Higher
temperatures will also increase the time it will take to freeze the gate. The aim
should be to make sure that anywhere in this process window, the gate must al-
ways be sealed and, therefore, conditions towards the higher extremes of the
pressures and temperatures must be considered.
 Se
t the cooling time to a value to ensure that the part is cooled before ejection.
 Dr
op the holding time to zero and again set the screw delay time as described in
Section 8.6.
 S
tart molding and mold approximately ten shots.
 Collect one sho
t.
 Incr
ease the holding time to 1 sec, decrease the cooling time by 1 sec, and collect
a shot. Decreasing the cooling time by 1 sec will ensure that the cycle time will
remain unchanged.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 229 (page 229)

2058.14 The Pack and Hold Pressure Rule Not to Be Used
 Incr ease the holding time in increments of 1 sec and collect the shots of up to a
holding time value at which the gate should be frozen. As the holding time is in-
creased by 1 sec, drop the cooling time by 1 sec.
 W
eigh the individual cavities and plot a graph of part weight versus time.
 De
termine the gate seal time. The gate seal time is the time after which the part
weight stays constant.
Table 8.6 is an example of a worksheet that can be used to document a gate seal
study.
Table 8.6 Gate Seal Study Worksheet
Hold time
(s)
Part weight
(g)
1 12.98
2 13.26
3 13.84
4 14.06
5 14.12
6 14.23
7 14.23
8 14.23
How to Use This Information
If the cavity balance is such that all the parts fill at the same rate, then the graphs
for gate seal should be similar. In such cases, weighing the parts from one cavity
and plotting the graph is acceptable. The hold time must be set to approximately
1 second longer than the gate seal time. This will ensure that the gate will always
be sealed before the end of the holding phase. The set cooling time starts at the end
of the holding time. The plastic begins to cool as soon as it hits the walls of the
mold. Therefore, actual cooling time is the sum of the injection fill time, pack and
hold time, and the cooling time. This total cooling time is one of the factors that
define the quality of the part. If the holding time is reduced by 0.5 seconds, this
time must be added to the cooling time and vice versa. It is therefore best to add
1 or 1.5 seconds to the hold time to ensure gate freeze and then reduce the cooling
time by the same amount, keeping the total cooling time the same. In an attempt to
reduce cycle time, some processors add only about 0.5 seconds to the gate seal
time. This may not be the most optimum setting.
Cautions and Exceptions
With a gate seal study, the time at which the gate seals off or is frozen is deter -
mined. However, if the part needs a large gate, the seal-off time can be very long. In
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 230 (page 230)

206 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
such cases, if the pressure is applied for longer than the required time, there is the
risk of over packing the part. Sprue-gated components are good examples of this
problem.
If the part weight stays constant during an initial section of the holding time and if
with a further increase in holding time there is a sudden increase in the part
weight, this can be evidence that the part is being over packed, especially in the
gate area. Because the plastic behind the gate and in front of the gate is probably
still soft, the extra time causes the frozen gate section to dislocate, forcing more
plastic into the cavity. Because the rest of the plastic in the cavity is cooling down
and viscosity is very high, the excess pressure from the fresh plastic does not get
distributed or compensated for and builds up stress in the gate area. This weight
increase is shown with the dotted line in Figure 8.3.
 8.15  Differ entiating between the Pack
and the Hold Phase
In most cases, molders do not differentiate between the pack phase and the hold
phase and will typically have only one pressure setting and one time setting for
both phases. They call this collective phase as the hold phase. The optimization of
this phase is done by the gate seal study described in the previous section. How -
ever, in some cases, a part weight versus time study will never show a flat region
such as the one shown in Figure 8.34. In such cases it is easy to over pack the parts
causing failures and, therefore, in these parts, there must be a differentiation be-
tween the pack and the hold phases.
Time Weight 1
Weight
Increase
[gms]
% Weight
Increase
09 .88- -
1 10.45 0.57 5.769
2 10.77 0.32 3.062
3 10.94 0.17 1.578
4 11.07 0.13 1.188
5 11.10 0.03 0.271
6 11.12 0.02 0.18
7 11.14 0.02 0.18
8 11.16 0.02 0.18
9 11.17 0.01 0.09
10 11.18 0.01 0.09
Part Weight vs Time
9.80
10.00
10.20
10.40
10.60
10.80
11.00
11.20
11.40
0.01 .0 2.03 .0 4.05 .0 6.07 .0 8.09 .0 10.0 11.0
Part Weight vs Time
Figure 8.34 Gate seal graph for a part molded with low density polyethylene
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 231 (page 231)

2078.15 Differentiating between the Pack and the Hold Phase
Here are some typical scenarios where pack and hold will need to be differentiated:
 In softer mat
erials such as polyolefins, TPEs and TPUs, the part weight continu-
ously increases and does not stabilize in the gate seal test
 In spr
ue gated parts the gate size is big and waiting for this to freeze off could be
impractical. Part weight will also increase with increasing time and will lead to
stress build up in the gate area.
 In some par
ts there is stress failure at the gate, such as in trash cans where the
part is center gated, and the most likely failure is a crack or break through the
gate.
 In ho
t runner molds, because the gate is always molten, the gate will never seal
as long as there is movement of plastic.
 In
valve gated molds there would be only pack and no hold because the gate is
mechanically closed.
 Some
times cosmetic defects such as a gate vestige can be solved by adding
2 stages. (Gate vestige is a mold issue and must be fixed in the long run.)
In the above cases, the phases of pack and hold must be differentiated from each
other. In the pack phase the required amount of plastic must be injected and in the
hold phase this plastic must be held in there until the gate freezes off. If the hold
phase is terminated before the gate is frozen, then the pressurized plastic the
ca
vity will flow back out of the cavity, often causing sink and/or dimensional vari-
ations and issues. This is the reason why a molder will notice sink on parts with
high pack and hold pressures. When the molder lowers the pressure, the sink dis-
appears, often baffling the molder because it is opposite of what he expects.
The technique described next can be used to differentiate between the pack and
the hold phases. It is best to illustrate this with an example. Consider the graph
shown in Figure 8.35. It can be observed that the part weight increase after 5 sec-
onds is about 0.03 grams and tapers down even more as the time increases. The
0.03 grams is about 0.25 % of the final part weight (11.23
g) and 0.02
g
rams is
about 0.17 % of the final part weight. We therefore can consider that the part has
reached very close to the required part weight, or in other words, the pack phase
has been completed at 5 seconds. It is similar to visualizing when someone is pack-
ing a travel bag. Initially clothes can be placed inside until the bag seems physi-
cally full, but the remaining clothes can only be put inside after compressing the
clothes that were first put inside. As the bag is filled more and more, lesser and
lesser amounts of clothes can be packed in there. So after the initial quick fill fur -
ther additions slow down. The pressure used during this initial phase is the pack
pressure, and the time that this pressure is applied is the pack time. The pack
pressure is 8000 psi plastic pressure, and the pack time is 5 seconds.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 232 (page 232)

208 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
9.80
10.00
10.20
10.40
10.60
10.80
11.00
11.20
11.40
0.01 .0 2.03 .0 4.05 .0 6.07 .0 8.09 .0 10.0 11.0
Part Weight vs Time
Time Weight 1 Weight
Increase [g]
% Weight
Increase
09 .88- -
1 10.45 0.57 5.769
2 10.77 0.32 3.062
3 10.94 0.17 1.578
4 11.07 0.13 1.188
5 11.10 0.03 0.271
6 11.10 00
7 11.10 00
8 11.10 00
9 11.10 00
10 11.10 00
Gate Seal
Study was
done at 8000
psi
Pack Press = 8000 psi
Pack Time = 5.0 sec
The increase in
the part weight
was minimal
after 5 seconds
Part weight with
5250 psi of hold
pressure stayed
constant after 3
seconds of hold time
Hold Press = 5250 psi
Hold Time = 3.0 sec1
Part Weight vs Time
2 3
4
5
Final Se/g427ngs: Pack Pressure = 8000 psi, Pack Time = 5 seconds, Hold Pressure = 5250 psi, Hold Time = 3 seconds
Figure 8.35 Final settings for the pack and hold phases
Going back to the travel bag example, once we have packed the required amount of
clothes, we must now zip the bag up in order to hold the clothes in there. If not, the
bag top or cover will not be able to keep the clothes inside. Similarly, once the re-
quired amount of plastic is now present inside the cavity, it must be held in there.
This is done by applying another pressure setting that will be lower in value than
the pack pressure for a time until the part weight stabilizes, or in other words, till
the gate freezes off. The target part weight here will be the same part weight that
was obtained at the end of the pack time. In the experiment above, this hold
pr
essure was 5250 plastic psi and the hold time was determined to be 3 seconds.
The total of pack and hold time was 5
+
3
=
8
seconds. The final part weight was
11.10 grams.
The procedure is described in the following steps:
 Se
t only one pressure collectively for the pack pressure and hold pressure and
call this the compensation pressure. Therefore,
Compensation Pressure = Pack Pressure + Hold Pressure. Consider this pressure
to be 8000 psi plastic pressure.
 Se
t only one time collectively for the pack time and hold time and call this the
compensation time. Therefore,
 Com
pensation Time = Pack Time + Hold Time. Consider this time to be 15 sec.
 S
tart with the compensation time of 0 sec, generate a graph of ‘Part Weight ver-
sus Compensation Time’ of up to 15 sec.
 Obser
ve the graph and the part weight table to estimate where the change in the
part weight begins to slow down. A change in the slope of the graph can be seen.
In Figure 8.34, this time can be considered as 5 sec. Based on this, Pack Pressure
= 8000 psi and Pack Time = 5 sec.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 233 (page 233)

2098.15 Differentiating between the Pack and the Hold Phase
 R ecord the part weight and this will be the Pack Only Part Weight = 11.10 g.
 Initiall
y there was only one value for pressure and time called compensation
pressure and time. Split the compensation pressure and time into two phases
and identify them as pack pressure, pack time, hold pressure, and hold time. On
the molding machine add another pressure and time profile. The first profile will
be for the pack phase and the second will be the hold phase. Set the first pres-
sure to 8000 psi and the first time to 5 sec.
 The second se
t of pressures are the hold pressures and hold time. Because the
compensation time was set to 15 sec and the pack time was set to 5 sec, set the
hold time to 10 sec (15

–

5

=

10).
 Se
t the hold pressures equal to the value of pack pressures = 8000 psi, and then
mold parts.
 R
ecord the part weight. This should be the same as the 15 sec value above and
should therefore be equal to 11.23
g. It will be higher t
han the pack only part
weight of 11.10

g.
 Dr
op the hold pressures in steps of about 250 plastic psi and keep checking the
part weight at every reduction. The pressure at which the part weight equals
the pack only part weight of 11.10 grams will be the holding pressure. In this
example, the value was 5250 psi. This indicates that at 5250 psi, the plastic is
not entering the cavity nor is it existing the cavity. Or in other words, the plastic
is held in place.
 N
ext reduce the hold times in steps of 1 sec at a time, and note the time where
the part weight drops below 11.10 grams. In this example, this time setting was
2
sec, because at 2
sec of hold time, t
he part weight was 11.08 grams. This in
-
dicat
es that at 2
sec, t
he plastic is coming back out from the cavity. Add 1 sec to
2
sec making t
his time 3
sec, whic
h will bring the part weight back up to 11.10
grams. This time will be the set holding time.
The results are summarized in Figure 8.35. The final settings can therefore be
summarized as follows.
 P
ack Pressure = 8000 psi
 P
ack Time = 5 sec
 Hold Pr
essure = 5250 psi
 Hold T
ime = 3 sec
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 234 (page 234)

210 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
 8.16  Hot Runner and Valve Gated Molds
In case of hot runner molds, the weight increase with the time increment is usu-
ally steeper compared to a cold runner mold and therefore some past molding
e
xperience is helpful when determining the change in the slope in the graph. The
same technique can be successfully used.
In case of valve gated parts, since the valve is mechanically closing the gate, once
the pack time is determined with the above procedure the valve must be shut. In
case of valve gated molds, the holding phase does not exist.
The technique above is only still used within the cosmetic windows. Dimensions
are still not considered. Optimization of the pack and hold phases for dimensions is
described in Chapter 9, The Concept of Design of Experiments, is used.
Gate seal times depend on
 The melt t
emperature; the higher the melt temperature, the higher is the gate
seal time.
 The mold t
emperature; the higher the mold temperature, the higher is the gate
seal time.
 The pac
k pressures; the higher the pack pressures, the higher is the gate seal
time.
8.16.1Step 6: Determining the Cooling Time – Cooling Time Study
The plastic starts to cool down as soon as it hits the walls of the mold. Once the
pack and hold times have elapsed, the set cooling time counter starts. The mold
remains closed until the end of the cooling time. The mold then opens and the part
is ejected. Before the mold opens, the part must reach the ejection temperature of
the plastic. If the part is ejected before it reaches ejection temperature, the part is
too soft and will get deformed during ejection. Warpage can also be an issue. Exces-
sive cooling time is a waste of machine time and therefore profits. Cooling time
should also be set so that the part dimensions remain consistent and the process
is capable of molding acceptable parts over time. As discussed in Chapter 7, the
actual cooling time is the addition of the injection time, the pack time, the hold
time and the set cooling time.
The procedure to determine the optimum cooling time is relatively simple and in-
volves molding parts at various cooling times and inspecting them for any cosmetic
defects. Although stage 1 of the process development process is strictly for explor-
ing the robust areas of the molding process and not for measuring any dimensions.
It is acceptable to inspect the dimensions only to get an idea of their values and
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 235 (page 235)

2118.16 Hot Runner and Valve Gated Molds
ranges. Design of Experiments must be carried out for dimensional process optimi-
zations and to find a robust process. The procedure is outlined in the following:
Procedure to Determine Cooling Time
1.
Se
t the process with the process conditions determined by the viscosity study,
the process window study, and the gate seal study.
2.
S
tart molding, and once the process has stabilized, collect three shots.
3.
Dr
op the cooling time by one or two sec, let the process stabilize and collect an-
other three shots.
4.
Continue t
o drop the cooling time by one or two sec and collect the shots.
Continue to the lowest cooling time possible while running the machine in a semi-
automatic mode for mold safety reasons. As the cooling time is reduced, parts
could stay on the A-side of the mold, and the mold may close up on them. Run the
mold in a semiautomatic mode to avoid this. Look for cosmetic defects such as pin
push and warpage. The lowest cooling time would be defined as the lowest time at
which the parts are cosmetically acceptable. With the parts collected above, there
are two different routes that one could take based on whether a Design of Experi-
ments (DOE) would be carried out or not.
If a DOE is going to be carried out, then cooling time should be considered as one
of the factors, and the least cooling time value will be used as the low value setting
of the cooling time. DOEs in injection molding are very simple and must be carried
out. Chapter 9 discusses this technique in detail.
If a DOE is not going to be carried out, then the dimensions can be measured, and
a process can be selected. The procedure is given below:
1.
Measur
e the critical dimensions on the shots collected. If there are a number of
cooling time numbers, it is acceptable to take the low, center, and high value of
the cooling, and measure the dimensions at these three settings.
2.
Plo
t a graph of dimension versus the cooling time. Analyze the data to see how
the critical dimensions are changing with the cooling time.
3.
Decide on a cooling time t
hat best fits the data.
4.
R
un 30 shots at this cooling time, and perform a statistical analysis to determine
the process capability.
Determination of the right cooling time can become complicated. For parts with
thick sections it is difficult to measure the internal temperature in the center of the
thickest section. In some parts of the mold, it is difficult to get enough cooling and,
therefore, cooling times have to be increased to allow time for additional heat
transfer. In some cases, with large molds or thick parts, the mold temperature
could take a couple of hours to stabilize.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 236 (page 236)

212 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
Figure 8.36 shows that some dimensions may be more sensitive than others. Di-
mension B is not influenced by the changes in cooling time. However, Dimension A
changes with the cooling time. The target value for dimension A is 2.8656". There-
fore, the cooling time can either be set to 16.5 seconds, or steel changes have to be
made to run the mold faster and achieve the same dimensions. Identifying the
lower and upper limits in Figure 8.36 will also present a graphical representation
of where the cooling time can be set.
2.8651 0.060
2.8652
Dimension A (in)
Dimension B (in)
Cooling Time (sec)
0.072
0.084
0.096
0.108
0.120
0.132
0.144
0.156
0.168
0.180
8 11 14 17 20
2.8653
2.8654
2.8654
2.8655
2.8656
2.8656
2.8657
2.8658
2.8659
Figure 8.36 Cooling time study graph
Cycle time is the most important factor because it directly impacts the bottom line
profit of a molding operation. In most cases, if the process is capable at shorter
cooling times, changes in the mold steel may achieve the same dimensions at
shorter cycle times. The cooling time is usually the major part of the molding cycle.
Therefore, optimization of cooling time is critical for profitability. Figure 8.37
shows the typical cycle time break-down for all phases of the molding process. Part
design and mold design can have a significant impact on the actual cycle time re-
quired for each phase shown in the pie chart of Figure 8.37. A long thin part may
only need a short cooling time; however, the mold may need to stay closed much
longer to complete the screw recovery phase. Ideally, the recovery time would not
exceed the time required to cool the part for ejection from the mold. However, part
design, mold design, and machine selection can all have significant influence on
the actual cycle times required for each phase of the injection process.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 237 (page 237)

2138.16 Hot Runner and Valve Gated Molds
Open
Mold closeEject
Inject
Pack & hold
Cooling
Figure 8.37 Typical cycle time break-down
Table 8.7 is an example of a worksheet that can be used to document a cooling time
study.
Table 8.7 Cooling Study Worksheet
Cooling time
(s)
Dimension 1
(in)
Dimension 2
(in)
8 1.552 0.253
10 1.553 0.253
12 1.554 0.254
14 1.554 0.254
16 1.555 0.254
8.16.2Optimization of Screw Rotation Speed
At the time of writing this book, there are no reliable and simple, at-the-machine
experiments that can be performed to optimize screw rotation speed. If screw rota-
tion speeds are excessively high, the plastic and its additives can burn and degrade.
If the screw rotation speeds are too low, then the plastic melt may not be homoge-
neous even if it is up to the processing temperature. The melt that is purged should
not look burnt or degraded, in which case, the screw rotation speeds should be re-
duced. The actual melt temperature should also be close to the settings of the barrel
temperatures. For example, if the barrel temperatures are set in the range of 250 °C
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 238 (page 238)

214 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
and if the actual melt temperature is 290 °C, then the source of the additional heat
is from the shear of the rotating screw. The screw rotation speed should be reduced
to bring the temperature down. On the other side, if the melt temperature is 220 °C,
then not enough shear is provided by the rotating screw and the screw rotation
speed must be increased. For crystalline plastics, higher screw rotation speeds are
recommended because the melting of the crystallites requires high energy that can
be supplied by the shear of the rotating screw. The heat from the heater bands may
not always be sufficient to produce a homogeneous and uniform melt.
Highly fiber filled plastics or those filled with long fibers typically require slower
screw rotation speeds to avoid fiber breakage. Some shear sensitive materials, such
as PVC, also require low screw rotation speeds.
As mentioned in Section 7.5.6, screw rotation speeds should never be recorded in
revolutions per minute (rpm) because 30
r
pm on a small diameter screw would
have a different shear effect as compared to a larger diameter screw. Surface speeds
must be considered.
8.16.3Why to Not Use the Rule of Thumb
The rule of thumb that states that the screw rotation speed should be set so the
screw is turning for 2–3 seconds before the cooling time is done is commonly used
while setting the screw rotation speeds. However, it is not accurate and should
never be used. Screw rotation speed is material specific and has nothing to do with
the part design. Refer to Figure 8.38. Assume some fictitious numbers for the sake
of understanding the topic. There are two parts with identical weights equal to
10
g
rams. The wall thickness for one is 1
mm and o
ther is 5
mm. Consider bo
th
parts being molded from the same grade of a nylon. The 1 mm part will need lower
a cooling time of 10 seconds and the 5
mm par
t will require a higher cooling times
of 30 seconds. Going by the rule of thumb, the screw should rotate for 8 seconds
for the 1
mm par
t and for 28 seconds for the 5
mm par
t. This will lead to different
shear heats in each of the shot built up. The shot built up for the 1 mm part will
have a lot more shear heat as compared to the 5

mm part.
Part
Part Weight : 10 grams 10 grams
m m 6m m 1 : s s e n k c i h T l l a W
Cooling /g415me : 10 seconds 30 seconds
Figure 8.38 Screw rotation speed, part thickness and cooling time – Why not to use the rule
of thumb?
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 239 (page 239)

2158.17 Optimization of Back Pressures
Screw rotation speeds should be set such that the material gets the right amount of
shear and such that the material melt temperature is close to what is desired. Melt
homogeneity must be examined. In case of the 5
mm par
t, if the screw rotation
speeds are very slow, there may not be enough shear heat, and the part could
suffer in its final pr
operties and may not perform as intended. Setting of screw
r
otation speeds must be done independent of cooling times. However, the screw
rotation times should be less than the set cooling time for the mold. If it is more
than the set cooling time, then the mold close time is now dictated by the screw
rotation times and the actual cooling time will be higher than the set value.
 8.17  Optimization of Back Pressures
The back pressure should be kept to a minimum. The optimum back pressure is
the lowest pressure possible to keep the screw recovery time consistent and to
avoid any surface and/or internal defects visible on the part.
Start molding with a back pressure value of about 600 to 750 plastic psi. Consider-
ing the screw diameter is less than 50 to 60
mm,
and if the screw recovery times
from shot to shot are consistent within 1 second, this is an indication that the back
pressure is sufficient. If there is a variation in the screw rotation times, then in-
crease the back pressure by about 100 plastic psi and check the shot to shot varia-
tion in the screw rotation times. Increase the back pressure till the screw rotation
times are consistent.
Excessive back pressures can also increase shear and break down additives such
as glass fibers. This will result in a change in shrinkage and ultimately affect
dimensions. Ex
cessive back pressures must be avoided.
Surface defects would include splay, and internal defects would include bubbles
and voids. At lower back pressures, the air and the volatiles do not get squeezed
back out from the rotating screw and therefore end up in the melt. This produces
the defects. Increase the back pressures to a value where these disappear. Of
course, back pressure is not the only reason for these defects and therefore all the
other factors must also be evaluated.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 240 (page 240)

216 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
 8.18  The Cosmetic Scientific Process
With the techniques just described, the process that was developed is called as the
Cosmetic Scientific Process. Dimensions can be taken but the preferred route to
optimize dimensions should be the use of the technique of Design of Experiments.
The table below summarizes the optimization technique of the 11
+
2 molding
par
ameters.
Table 8.8 Summarization of 11 + 2 Molding Parameters
No. Factor Method of Optimization
1 Injection Speed Viscosity Curve
2 Injection Pressure Pressure Drop Study
3 Pack Pressure Cosmetic Process Window Study
4 Hold Pressure Cosmetic Process Window Study
5 Pack Time Gate Seal Study
6 Hold Time Gate Seal Study
7 Cooling Time Cooling Time Study
8 Melt Temperature Cosmetic Process Window
9 Mold Temperature Cosmetic Process Window
10 Screw Rotation Speed Minimum required – melt homogeneity
11 Back Pressure Minimum required – cosmetics
12 Shot Size Part fill of 95–98 %
13 Transfer Part fill of 95–98 %
8.18.1Post Mold Shrinkage Studies
When the parts are ejected from the mold, they are below the ejection temperature
but are still warm. If the temperature of the part is above the glass transition tem-
perature, the molecules have enough energy to move and settle down into their
equilibrium positions. This movement results in additional shrinkage and therefore
a dimensional change of the part. If the glass transition temperature (T
g) of the
plastic is below room temperature, the phenomenon continues until equilibrium
between ambient and T
g-temperature is reached, causing even more excessive
shrinkage. Because this shrinkage takes place outside the mold and after molding,
it is called post-mold shrinkage. Thermoplastic elastomers are common materials
with low glass transition temperatures exhibiting high post-mold shrinkage. The
rate of shrinkage is directly proportional to the temperature of the plastic and fol-
lows an exponential decline with time after ejection. The highest shrinkage is there-
fore seen as soon as the part is ejected from the mold, because at this point the
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 241 (page 241)

2178.18 The Cosmetic Scientific Process
temperature is the highest. As the part starts to cool down, the rate of shrinkage
also decreases. In some cases, part dimensions can take up to a few days to stabilize.
Because almost all molded parts are used in assemblies after ejection, the fit be-
tween the parts is very important. Therefore, part dimensions must have stabilized
before assembly. If they continue to shrink after assembly, stresses can easily be in
-
duced int
o the assembly and cause premature failure. Figure 8.39 shows a part that
continued to shrink after assembly and therefore induced stress in the assembly.
There are a number of factors that may affect post-mold shrinkage:
Glass Transition Temperature: The lower the T
g, the higher is the post-mold shrink-
age. In plastics with their T g above room temperature, post-mold shrinkage is low
because there is not sufficient energy for molecular movement. High glass transi-
tion temperature plastics, such as PEEK, show almost no post-mold shrinkage.
Fillers and Additives: In the case of filled plastics, the presence of fillers prevents
the shrinkage. Therefore, resins with a higher filler content exhibit lower post-
mold shrinkage.
Part out of
the match
Bonded via sonic
welding
Part molded
a week ago
Stress
build up
Figure 8.39 Post-mold shrinkage after assembly
Part Thickness: Part design also plays an important role with respect to the amount
of post-mold shrinkage. Thicker part sections retain more heat and therefore can
cause additional post-mold shrinkage. This can also lead to warpage, which is the
result of uneven cooling in the part. If one area of the part has cooled down, while
a thicker section of the same part is still cooling and undergoing some shrinkage,
the thicker section will influence the thinner section and pull the part in the direc-
tion of the shrinkage, thus deforming the part.
Mold Temperature: The temperature of the mold provides the energy required to
help bring the molecules to their equilibrium state. In case of crystalline materials,
the mold temperature has to be maintained high enough to crystallize the plastic.
If the mold temperature is not maintained at a sufficiently high level, the mole-
cules freeze in place without reaching their equilibrium position. When these
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 242 (page 242)

218 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
parts are ejected and are then subjected to higher temperatures during their ser -
vice life, the molecules acquire the required energy and begin to find their equilib-
rium positions, thus causing shrinkage. This phenomenon can also occur when
molded parts are stored prior to use. If mold temperatures were set lower than
room temperature, for example 5 °C when the parts were produced and then stored
at ambient warehouse temperatures of 30 to 40 °C, post-molding shrinkage can
occur. When these parts are eventually removed from storage, they could exhibit
some amount of warpage that did not exist at the time they were packaged.
Processing Conditions: Nonoptimized process conditions can also induce stress in
the part and cause post-mold shrinkage and warp. Under-packed parts commonly
exhibit post-mold shrinkage while over-packed parts exhibit built-in stresses.
These stresses are released after the part is ejected.
Annealing: Parts that have not reached their final state of equilibrium exhibit
built-in stresses. The process of annealing can be considered as a forced post-mold
shrinkage operation. In annealing, the parts are intentionally taken to higher
t
emperatures to force the movement of the molecules out of their non-equilibrium
positions and into their final equilibrium positions. In doing so all stresses are
r
elieved. Annealing will result in some amount of shrinkage, depending on the
factors described earlier.
A typical post mold shrinkage graph is shown in Figure 8.40. The shrinkage exhib-
its an exponential drop: it is higher when the part is first ejected from the mold but
then stabilizes over time.
Time (HRS)
Dimension
01 02 03 0 40 50 60 70 80
1.2475
1.2480
1.2486
1.2491
1.2496
1.2501
1.2507
1.2512
1.2517
1.2522
1.2528
1.2533
1.2538
1.2543
1.2549
1.2554
1.2559
1.2564
1.2570
1.2575
1.2580
Dimensional stabilization
Figure 8.40 Post-mold shrinkage graph
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 243 (page 243)

2198.18 The Cosmetic Scientific Process
8.18.2Procedure to Measure Shrinkage
 S tart molding with the established process parameters and let the process stabi-
lize. The stabilization of the actual mold temperatures is an indication that the
process has stabilized.
 Collect at leas
t three shots as they are ejected from the mold and record the time
each was ejected from the mold.
 After 15 minut
es measure the parts from each shot and record the dimensions.
 R
epeat after 30 minutes, 45 minutes, 1 hour, 2 hours, 4 hours, 8 hours, 24 hours,
and so on until a stable reading is achieved. The time interval between measure-
ments can increase as time after molding is getting longer. The goal is to collect
the most measurements while the part is experiencing the highest rate of shrink-
age, which is the time frame shortly after molding. As the part ages, the rate
of shrinkage decreases and the time interval between measurements can be in-
creased.
 Gener
ate a graph of dimension versus time.
If there are multiple cavities, it may be difficult to measure all parts in a short time
during the initial part of the experiment. In this case, measure any one cavity. If
the cavity fill is balanced and the mold cooling for each cavity is the same, one can
assume that the parts will behave in a similar fashion. The parts from the other
cavities must still be collected with measurements being made at longer time in-
tervals. Dimensional stability after longer relaxation times, e. g., at 2 hours or
longer, is sufficient to measure the part dimensions.
How to Use This Information
Once the graph is generated, the time interval required for the part to become di-
mensionally stable will be obvious. Any secondary operations or direct part use
must be done after the stabilization period. The stabilization time in Figure 8.40 is
approximately 36 hours.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 244 (page 244)

220 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
 8.19  Recommended Mold Function
Qualification
Procedure
The previous sections describe the science and the procedures to establish all pro-
cess parameters. During each of the steps, the most robust areas of each process
parameter must be recorded. These parameter settings will contribute to the
make-up of the final process. Once the process has been established, parts must be
molded using these process settings. The machine must be set to the established
process and a sufficient amount of parts must be run to check the process robust-
ness and the part quality. There will always be some natural variation in the qual-
ity of the parts and therefore a statistically acceptable number of parts (usually 30)
must be measured. Knowledge of this variation is essential to establish a capable
process and consistent production.
Each procedure taken along the way may reveal an issue with the mold. For exam-
ple, having a defect such as a short shot and flash at the same time is a clear indi-
cation of a mold problem. In this case, there is no process window and therefore it
will be impossible to make an acceptable part. The mold must therefore be pulled
out of the machine and fixed. This becomes a required mold trial iteration neces-
sary for successful molding and production.
Likewise, other steps may reveal other issues, such as inadequate venting or im-
properly sized gates among others. An effort must be made to try and identify all
issues with the fewest number of trials possible.
The procedure described is used to optimize the process and to make sure that the
mold function is acceptable. It is therefore also called “mold function qualification
procedure.” Part dimensions were not the focus of this qualification, which does
not mean that the dimensions should not be measured along the way. The dimen-
sions must be measured and compared to the part drawing. If all the dimensions
are acceptable and well within the quality requirements, the molding process can
be recorded as final. This is the best case scenario. However, if any of the dimen-
sions are not acceptable or the process is not deemed stable because of a large
variation, the mold steel must be altered to center the dimension. Changing the
process in turn could cause a process parameter to be in a nonrobust area, causing
inconsistencies. If the process window is wide enough, it is acceptable to move the
process within the window. The flow chart in Figure 8.41 shows the recommended
mold function qualification procedure.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 245 (page 245)

2218.20 Recommended Adjustments to Maint ain Process Consistency and Robustness
Step 1: Mold function qualification
Scientific molding section
6 Step study
Start
1 – Viscosity study
2 – Cavity
balance
3 – Pressure
drop
4 – Process
window
5 – Gate seal study
6 – Cooling study
Mold or part
issues
Not OK
Fix mold
or
part
design
Not OK
Not OK
No
Step 2: Mold-part quality qualification
Design of experiments
Figure 8.41 Recommended mold function qualification procedure
 8.20  R ecommended Adjustments to
Maint
ain Process Consistency and
Robustness
Once the process has been established, it is time to consider the dimensions of the
parts. Collection of the quality data at the established process is crucial; therefore,
a good, statistically valid sample of parts must be measured. The minimum num-
ber of acceptable parts considered to provide reliable statistical data is 30. The data
must be analyzed and a decision must then be made on how best to achieve the
required quality standards. Table 8.9 describes the various scenarios and the rec-
ommended actions. In some cases, the natural variation can be larger than the
difference between the lower and upper specification limits. For example, consider
a part with the required nominal dimension to be 2.50
mm, t
he upper tolerance of
0.05
mm,
and the lower tolerance of 0.05
mm.
The total available tolerance is
therefore 0.10
mm. If 30 par
ts were measured, and if the range (difference be-
tween the maximum and the minimum) was 0.12
mm, it will be im
possible to mold
all the parts within the required specifications, even if the average tolerance of the
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 246 (page 246)

222 8  Process Development Part 1: the 6-Step Study – Exploring the Cosmetic Process
30 parts was 2.50 mm. Ther e will always be parts molded outside of specifications.
In this case, opening up of the tolerances must be considered. Making any sort of
steel adjustments will not help. If the range is less than the difference between the
limits and the parts are out of specifications, then adjusting the mold steel will
help to center the process and mold all parts within specifications. If the parts are
functionally acceptable, the other option is to move the nominal dimension on the
part print, and leave the mold steel alone. This is a good option when the mold is
not steel safe and the decision should be made by the part designer.
Table 8.9 Recommendations for Centering Part Dimensions and Variations
Location of average –
acceptance of variation
Adjust
steel
and/or Move
nominal
and/or Open
tolerance
At nominal – acceptable NA NA NA
At nominal – not acceptable No No Yes
Closer to the spec limits –
acceptable
Will help and/or Will help No
Closer to the spec limits –
not acceptable
Will help and/or Will help and Yes
Out of spec limits – acceptable Yes and/or Yes No
Out of spec limits –
not acceptable
Yes and Yes and Yes
 8.21  Process Documentation
Injection molding is primarily a heat transfer process, involving variables related
to speed, pressure, time, and temperature. It is important to record each of these
process parameters in order to duplicate the process during the subsequent trials
and final production. The mold qualification worksheets, machine setup sheet,
w
ater line diagrams, mold temperature maps, setup instructions, and operator
ins
tructions must all be documented and/or updated during each trial. Several
sections in Chap
ter 10 describes this documentation.
Of particular relevance here is the mold qualification checklist. A master checklist
must be developed for mold trials, depending on the requirements of every mold-
ing operation. During every mold trial, the checklist must be used to evaluate
the mold and the process. This assures that every part of the mold or process is
evaluated and all the problems and/or suggested improvements are documented.
This documentation can then be passed on to the mold maker or those involved
with project improvements. A sample mold qualification checklist is provided in
Appendix F.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 247 (page 247)

2238.22 References
 8.22  References
[1] K ulkarni, S. M. and Hart, David, SPE ANTEC Tech Papers (2003) p. 736
[2]
Mer
tes, S., Carlson, C., Bozzelli, J., and Groleau, M., SPE ANTEC Tech Papers (1997)
Suggested Reading
Osswald, T. A., Turng, L., and Gramann, P. J., Injection Molding Handbook (2007) Hanser, Munich
Beaumont, J. P., Runner and Gating Design Handbook (2007) Hanser, Munich
Beaumont, J. P., Nagel, R., and Sherman, R., Successful Injection Molding (2002) Hanser, Munich
Rosato, D. V. and Rosato, D. V., Injection Molding Handbook (2000) CBS, New Delhi, India
Kulkarni, S. M., SPE ANTEC Tech Papers (2003) p. 736
Cogswell, F., Polymer Melt Rheology (1981) John Wiley, NY
Dealy, J. and Wissbun, K., Melt Rheology and its Role in Plastic Processing Theory and Applications (1990)
Van Nostrand Reinhold
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 248 (page 248)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 249 (page 249)

Process Development
Part 2: Exploring the
Dimensional Process
via the DOE
Chapter 8 introduced the first stage of the process development process where the
boundaries of the process were explored based on the cosmetics of the part. No
dimensions were considered. The bigger the cosmetic process window, the higher
the chances of a final robust process with dimensional consideration. The first
stage is the basis for the second stage of process development, because if the parts
are not cosmetically acceptable, the dimensions would not matter. In any molding
shop, the cosmetic visual check is carried out first. Once the parts are cosmetically
acceptable, the parts are then checked for the dimensions. This chapter will intro-
duce the second stage.
Planned experiments have been around for centuries. In the 17
th century a doctor
planned some experiments to find a cure for an ailment of that day. He engaged
various patients and various combinations of medicines to find the right cure.
Planned experiments were used in agriculture to find the right combination of
factors, such as soil type and fertilizer, to produce the highest yield of crops. Since
the time involved in waiting for the results of these agricultural experiments was
one complete season, which in some cases was one complete year, the technique of
a planned experiment was very helpful. As planned experiments became popular
as time saving and efficient techniques, people with a background in mathematics
and statistics became involved and developed them further. These planned and
systematic experiments involving changes to the inputs and measuring the effect
on the outputs became known as Design of Experiments or DOE. Each statistician
came up with techniques that helped in analyzing different types of data in differ -
ent scenarios. The people who have been most associated with the development of
these techniques are G. Taguchi and Ronald Fischer. The field of designed experi-
mentation is vast and considered a specialty of its own. Within the context of this
book we will focus on “Factorial Experiments.” Factorial experiments work very
well for injection molding. The use of any procedure (not just a DOE procedure)
must be backed by a complete understanding of the underlying principles, which
helps not only in the understanding of the analysis but also more importantly in
the interpretation of the analysis. Factorial experiments, their analysis, and their
interpretation are easy to comprehend and do not require a very strong mathe
-
matical bac
kground.
9
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 250 (page 250)

226 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
 9.1  Parameters in Injection Molding
Applying and using DOE in injection molding is relatively simple compared to its
use in other manufacturing or production processes, because responses to process
changes are fairly linear. There is some curvature that will needed to be modeled
into the equations and algorithms for analysis. The injection speed and related
process parameters are an exception. If large temperature differences between the
high and low are considred then again there is a non liniarity. As a simple example
the relationship between part dimension and holding pressure. If the dimensions
of a sample part molded at two holding pressures are known, it is safe to predict
that the part dimension produced when molded at the average of these two pres-
sures will lie at the vicinity of the average of the two dimensions, as shown in Fig-
ure 9.1. Confirmations must be run.
Data point 2
Data point 1
Predicted dimension at
1000 PSI
Length
Length
Holding Pressure
Figure 9.1 Relationship between holding pressure and part dimension
In injection molding, all plastic material variables are related to speed, pressure,
time, and temperature. The responses can be explained with the help of specific
volume versus temperature graph discussed earlier. In Figure 9.2 it is shown with
the molding area corresponding to the injection, pack, and hold phase of the mold-
ing cycle. In this area the curves are fairly linear regardless whether the material
is amorphous or crystalline.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 251 (page 251)

2279.1 Parameters in Injection Molding
Molding area
Injection – pack – hold
Crystalline
Amorphous
Semicrystalline
Cooling
Shrinkage
T T
Figure 9.2 Specific volume versus temperature graph showing the area corresponding to the
injection, pack, and hold phase
A similar graph for a PBT-PC blend generated at different pressures is shown in
Figure 9.3. Such a graph is also called a PVT graph.
Figure 9.3 PVT relationship for PBT-PC blend (Courtesy: Sabic Innovative Plastics)
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 252 (page 252)

228 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
Shrinkage is the change in volume as the plastic is being cooled. Based on the
r
elationship between the volume and the temperature it is safe to assume that the
part dimensions also respond similarly to process parameters such as tempera-
tures and pressures. Faster mold fill rates will result in lower heat loss in the melt
before it reaches the end of fill. Therefore, the plastic characteristics are in the top
right hand side quadrant of the PVT graph, but are still in the fairly linear area.
Increasing or decreasing the fill speeds will result in a proportional change in
dimension. Dur
ing the cooling time, the melt is now out of the shaded molding
area seen in Figure 9.2. The melt begins to solidify and the volume begins to de-
crease following the plot shown in Figure 9.2. The plot is linear until the plastic
reaches its glass transition temperature (T
g) where the curve exhibits an inflection
point. If the part is ejected above its T g, the relationship between the specific vol-
ume and the temperature is linear. If it is ejected below the T g, there will be some
non-linearity. For efficient injection molding, parts must always be ejected at a
material-specific ejection temperature that is always above the T
g. If the parts are
being ejected below the Tg, the molding is not efficient and additional time is added
to the cycle unnecessarily. The parts must always be ejected above or close to the
T
g, keeping the cooling curve in the linear region of the PVT graph. The plastic will
continue to shrink and therefore a post-mold shrinkage study must be done on the
parts. If the molding process was robust and consistent, the post-mold shrinkage
will also be consistent, producing consistent parts.
A note on the proportional changes mentioned above is required here. These rela-
tionships can be directly or inversely proportional to each other. For example,
packing pressure can increase the length of a part, but in some cases, such as an
internal diameter of a part, there can be a decrease in the diameter of the part with
increase in the packing pressure. Prediction is not easy and experimentation is
required.
9.1.1Design of Experiments: Definition
The simplest description of Design of Experiment (DOE) is a planned study. For
example, studying the effect of holding pressure on the length of the part is a de-
signed experiment. The length of the part at a low holding pressure and a high
holding pressure is measured and is then plotted as a function of the holding pres-
sure, see Figure 9.4. This is the most basic DOE that can be performed.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 253 (page 253)

2299.1 Parameters in Injection Molding
15.040
15.045
15.050
15.055
15.060
15.065
15.070
600 800 1000 1200 1400
Length
Holding Pressure
Length
400 psi
0.020 "
Figure 9.4 Study of effect of holding pressure on part length
When considering two parameters, holding pressure and melt temperature, and
their influence on the length, we need to perform four experiments and determine
the length at the following holding pressure/melt temperature combinations:
low – low, low – high, high – low, and high – high, see Figure 9.5.
Figure 9.5 Effect of holding pressure and melt temperature on part length
If we add one more parameter to this, for example mold temperature, we end up
with eight necessary experiments. We are repeating the above four experiments at
a low and high value of the mold temperature, resulting in eight experiments, as
shown in Figure 9.6. As the number of parameters to be studied increases, the
number of experiments increases.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 254 (page 254)

230 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
Melt
temp Mold
temp
Holding press
Figure 9.6 Effect of holding pressure, melt temperature, and mold temperature on part length
 9.2  Terminology
9.2.1Factor
Any input to the process is a factor. Therefore, all processing parameters that are
input to the molding machines are factors. Example: Holding pressure and melt
temperature. Factors can be set to a desired value on the machine controller or can
be selected from available options, such as a particular lot of material. Factors are
classified as follows:
Control Factors: Can be controlled and changed when required, e. g., mold tempera-
ture
Noise Factors: Cannot be controlled, e. g., lot-to-lot variation
Constant Factors: Are not changed during the study, e. g., back pressure
Quantitative Factor: Can be continuously changed in increments, e. g., holding pres-
sure
Qualitative Factor: Can be changed in discrete levels, e. g., material lots
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 255 (page 255)

2319.2 Terminology
9.2.2Response
Any output from a process is a response. A response is the result obtained at the
various level settings to which the factors are set to during an experiment. The
value or attribute of a response depends on the setting of a factor. The response
cannot be controlled directly. To get a required value of a response, the value of the
factor must be changed. Part dimensions, fill times, cavity pressure, or the amount
of splay are all examples of responses. Responses are classified as follows:
Quantitative Response: Are represented by numbers, e. g., length, weight
Qualitative Response: These are also called attributes; they are not represented by
numbers and describe the condition of the response, e. g., splay, color
9.2.3Level
A level is the number of points selected for the factor studied. For example, if we
choose a low and a high value of holding pressure, there are two levels. If we choose
a low, center, and a high value, there are three levels. The number of levels is
c
hosen based on the type of response to the factor. In injection molding, most
r
esponses to the factors are fairly linear. This means that when conducting a study
at a high level and a low level, the response at a medium value of these two factors
can be predicted to be the average of the responses. If the part length at 500
psi of
holding pr
essure is 1.10
inc
hes and at 1500
psi it is 1.20
inc
hes, we can conclude
that the length at 1000
psi will be close t
o 1.15
inc
hes. There are some exceptions,
such as cooling time, where a particular dimension may plateau off. In some cases,
the holding pressure may also plateau off at very high values. Data with injection
speeds are not linear. This is where a good amount of practical experience and
engineer
ing knowledge can help. In most cases, a two-level experiment followed by
a confirmation study suffices most needs but in case of some factors such as injec-
tion speeds, a multilevel experiment may be required. Figure 9.7 shows some of
the factors, levels, and responses in injection molding.
9.2.4Designed Experiment
A designed experiment is a study in which purposeful changes are made to the
factors and the corresponding effects on the responses are recorded. The responses
are analyzed and the results are used to optimize the process to make it robust.
The experiments mentioned earlier are all examples of designed experiments.
T
able 9.1 shows a matrix for a three-factor, two-level, and two-response designed
experiment.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 256 (page 256)

232 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
20 °C – 40 °C
210 °C – 230 °C
10 s – 20 s
Figure 9.7 Factors, levels, and responses
Table 9.1 Matrix for a 3-Factor, 2-Level, and 2-Response Experiment
Run Experimental run settings Responses
Mold temp
(°C)
Cooling time
(s)
Holding
press (bar)
Length
(mm)
Diameter
(mm)
1 40 30 30 144.73 6.35
2 40 30 55 144.40 6.15
3 40 20 30 144.60 6.32
4 40 20 55 144.30 6.15
5 20 30 30 144.83 6.37
6 20 30 55 144.50 6.16
7 20 20 30 144.65 6.32
8 20 20 55 144.34 6.16
 9.3  R elationships between the Number of
Factors, Levels, and Experiments
The main goal of performing various experiments is to understand the effect of the
factors on the final quality of the part. Therefore, when the number of factors in-
creases, the number of experiments also increase, see Table 9.2.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 257 (page 257)

2339.3 Relationships between the Number of Factors, Levels, and Experiments
Table 9.2 Number of Experiments Based on the Number of Levels and Factors
Levels Factors
1 2 3 4 5 6 7 8 9 10 11
2 2 4  8 16  32  64  128  256   512  1024   2048
3 3 9 27 81 243 729 2187 6561 19683 59049 177147
With two factors at two levels, the number of required experiments is four. The
relationship between the number of experiments, factors and levels is given by the
following equation:
n = l
f (9.1)
where,
n = Number of experiments
l = Number of levels
f = Number of factors
For example, for 3 levels and 4 factors, we have 3
×
3
×
3
×
3
=
81 e
xperiments.
Running a large number of experiments can get expensive and be very time con-
suming. As discussed in Chapter 7, there are 11 primary factors that affect the
part quality. If one was to perform a 2 level full factorial experiment, the number of
experiments would be 2048; at 3 levels it would be 177,147 experiments! Both of
these scenarios would be impractical to perform in any production environment.
Even after the completion of the experiments, the data still needs to be collected.
Inspection of all parts and collecting the data for the number of dimensions under
consideration would be even more time consuming. In injection molding, it is
common t
o work with multiple cavities and collect statistical data for several part
dimensions. If this information needs to be collected, the required time and the
effort involved can increase significantly. Through the use of statistical techniques,
there are multiple designs of experiments available where the number of experi-
ments can be reduced, yet reliable data can be obtained from them. These experi-
ments are subsets of the maximum number of required experiments and this is
where the advanced analysis techniques of designed experiments become a power-
ful tool.
Over the years, a number of researchers presented various ways to design fewer
experiments, analyze the data, and provide reliable results. Each have their own
advantages and disadvantages and are suitable to particular types of experiments.
Some of the popular designs in injection molding are screening experiments, Tagu-
chi designs, Plackett-Burman designs, and Box-Behnken designs. Although screen-
ing experiments are usually followed by full factorial experiments, in injection
molding that is usually not necessary because there are only a handful of factors
that truly make a difference in the quality of the part. Factorial experiments and
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 258 (page 258)

234 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
the Taguchi methods are most commonly used. Analysis of the results does not
require a lot of mathematical and/or technical background, which makes the Tagu-
chi screening methodology very user-friendly. Once understood, common spread-
sheets programs, such as MS Excel, can be used to analyze the data. However, be-
cause of the time involved in creating such a worksheet, it may be best to use
software specially created for such purposes. Some common software programs for
DOEs are mentioned in the bibliography.
To understand DOEs further, we will introduce a number of concepts in the following.
 9.4  Balanced Arrays
Table 9.3 represents a 2-factor experiment with 2 levels for each factor. Therefore,
an experiment resulting in 4 test runs is required.
An array is said to be orthogonal if it meets the following two conditions:
a)
F
or each factor, an equal number of highs and lows are tested.
In this case, there are two factors, holding pressure and melt temperature.
Hold pressure – 2 highs and 2 lows are tested
Melt temperature – 2 highs and 2 lows are tested
b)
F
or each level within a factor, equal number of highs and lows for every other factor
are tested.
In this case:
For low hold pressure – 1 low of melt temperature and 1 high of melt temperature
For high hold pressure – 1 low of melt temperature and 1 high of melt temperature
For low melt temperature – 1 low of hold pressure and 1 high of hold pressure
For high melt temperature – 1 low of hold pressure and 1 high of hold pressure
Table 9.3 Two-Factor, Two-Level Experiment
Experiment No. Hold pressure Melt temperature
1 Low Low
2 High Low
3 Low High
4 High High
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 259 (page 259)

2359.5 Interactions
The matrix shown in Table 9.3 is an orthogonal array because it meets both condi-
tions. There is a balance between the number of highs and lows of each factor of
the experiment. If we consider the same concept of orthogonal arrays from a math-
ematical aspect, replacing the highs and lows with numerical values, low would be
replaced with – 1 and high would be replaced with + 1. replacing the names of the
factors and calling them A and B will result in Table 9.4.
Now, we will perform the following operations on the entries in this table:
Table 9.4 Two-Factor, Two-Level Experiment
Experiment No. A B
1 −1 −1
2 +1 −1
3 −1 +1
4 +1 +1
Table 9.5 Orthogonal Arrays
Experiment No. A B A × B
1 −1 −1 +1
2 +1 −1 −1
3 −1 +1 −1
4 +1 +1 +1
Sum 0 0 0
1. Cr eate a new column called AB whose cells are the result of the product of the
cells of A and B.
2.
A
dd the cells in each of the columns in a new row.
 9.5  Interactions
We will use the following example to explain what interactions within the concept of
Design of Experiments represent: as the humidity and temperature increase, human
comfort level decreases. For this experiment, the comfort level is graded on a scale
from 0 to 10, where 10 is the most comfortable. When the humidity is low, a change
in the temperature from 20 °C to 28 °C changes the comfort level from 9 to 8.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 260 (page 260)

236 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
In fact, most people do not even notice the change. However, when the humidity is
high, the comfort level even at 20 °C is relatively low and with the same change in
the temperature to 28 °C the comfort level falls to 2. People in coastal towns often
face such discomfort, because of the high humidity even at low temperatures. If we
plot these results, as shown in Figure 9.8, it is clear that the change in comfort
between two temperatures at low humidity is different from the change in comfort
at high humidity. There is a drop of 1 point at low humidity and a drop of 4 points
at high humidity. Therefore, the amount of change in comfort due to temperature is
dependent on another factor, the humidity. In technical terms this means that
there is an interaction between temperature and humidity when it comes to human
comfort levels.
20 °C
(~70 °F)
20 °C
(~70 °F)
28 °C
(~80 °F)
28 °C
(~80 °F)
Figure 9.8 Interaction between humidity and ambient temperature regarding human comfort
level
An example for no interaction between temperature and humidity is the pressure
inside a container or an automotive tire. The change in tire pressure with an in-
crease in temperature from 20 °C to 28 °C will be the same regardless whether the
humidity is 20% or 80%. Interactions can be non-existent, mild, or strong as shown
in Figure 9.9.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 261 (page 261)

2379.5 Interactions
Length
Strong
Strong
Mild
None
Mild
Low hold
Low melt
High hold Low hold
High melt
High hold
∆Low
∆High
Figure 9.9 Types of interactions
Here, two factors are involved, therefore we refer to two-factor interactions.
Three-factor interactions have not been encountered in manufacturing processes,
let alone injection molding. In injection molding one will always notice mild
two-factor interactions. However, the effects are usually overpowered by the main
factors. If strong interactions are seen, even between two factors, the measurement
method must be questioned. The other possibility is that external effects may have
caused interactions after the molding has taken place. For example, dimensions of
the top of a deep draw box can be influenced during post-mold cooling because
they may be largely unsupported. Mechanical stresses caused during the cooling
of the part may be interpreted as interactions.
In the molding process, some mild interactions are usually observed between melt
temperature, mold temperature, and any of the filling phases.. Although the melt
temperature is considered constant, the melt is cooling down as it fills the mold
because filling is a non-isothermal process. Consider pressure and melt tempera-
ture as factors and the length of the part to be the response. If we measure the
length of the part for the four experiments, we observe that the change in length
between the low holding pressure and high holding pressure at the low melt tem-
perature is slightly different from the change in length between the low holding
pressure and high holding pressure at the high melt temperature. This means that
the setting of the melt temperature has an effect on how the holding pressure influ-
ences the length of the part. At low temperatures, there is a greater influence and
at higher temperature the influence is negligible. Therefore, we consider the inter-
action between the melt temperature and holding pressure to be present. If the
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 262 (page 262)

238 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
changes in length at the low and high temperatures were similar, interactions
would be considered absent. Interactions may be evident in cases where the levels
of the factors are at extremes. Such an example is extremely low injection speeds,
where the injection screw is barely moving at the low level while at the high level,
the screw is moving fast. At low fill speeds, the melt can cool down considerably
before it reaches the end of fill, whereas in the case of fast injection speeds, the
melt temperature can stay high through the filling stage. This would make a differ-
ence in the packing phase of the cycle and produce different results. Because the
amount of heat that needs to be removed from the mold will also change, this can
have a considerable effect on cooling. Mathematically, interactions are represented
as the multiplication columns shown in the tables. Column AB is considered an
interaction column between factor A and factor B.
 9.6  Confounding or Aliasing
Consider the orthogonal array in Table 9.6, which shows a 3-factor experiment
with two levels for each factor and all the interactions.
Table 9.6 Three-Factor, Two-Level Orthogonal Array with Interaction Columns
Experiment
No.
A B C A × B × C A × B A × C B × C
1 −1 −1 −1 −1 +1 +1 +1
2 +1 −1 −1 +1 −1 −1 +1
3 −1 +1 −1 +1 −1 +1 −1
4 +1 +1 −1 −1 +1 −1 −1
5 −1 −1 +1 +1 +1 −1 −1
6 +1 −1 +1 −1 −1 +1 −1
7 −1 +1 +1 −1 −1 −1 +1
8 +1 +1 +1 +1 +1 +1 +1
Sum 0 0 0 0 0 0 0
The sum of each of the cells for each of the interaction columns is equal to zero.
Therefore, this is an orthogonal array. In an orthogonal array, every column pro-
vides us with a unique set of information. Therefore, every row can be a unique
experiment. Since we know that interactions in injection molding are either very
mild or non-existent, we can take advantage of this fact. We can replace the names
of each of the interactions columns by the names of any factors we would like to
study. Therefore, in the above array, we can replace the four interaction columns
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 263 (page 263)

2399.6 Confounding or Aliasing
by any other four factors we would like to study. Let us say that the original three
factors were holding pressure, melt temperature, and mold temperature. Now we
would like to study four more factors. Based on our engineering knowledge, we
must first prioritize these four additional factors according to what we believe will
provide the most experimental impact or information when studying these four
factors. Let us say that after the first three main factors, the order of priority is
cooling time, injection speed, holding time, and screw speed. We now rename
columns 4 t
hrough 7 with these newly selected factors. This process of renaming
an interaction parameter column with another factor is called confounding or alias-
ing; it is executed for our example in Table 9.7. Because the fourth column is a
three-factor interaction and we know that three-factor interactions are almost
non-existent, we can be almost certain that the interaction can be confounded or
renamed as another factor. If the analysis shows that a confounded interaction has
a more significant effect on the quality of the part than a non-confounded factor,
the data must be checked and in some cases the experiments must be rerun. It is
also possible that the non-confounded factors may have been wrongly selected.
This is the reason why a molding background is required before performing DOEs.
For example, holding pressure is a very significant factor and must always be a
non-confounded factor. Consider a case where the non-confounded factors were
back pressure, screw speed, melt temperature and one of the confounded factors
was holding pressure. The holding pressure was confounded with the interaction
between screw speed and melt temperature. If the experiment was run, the analy-
sis would show that the holding pressure would be significant. But because it was
confounded, it will show that the interaction between the screw speed and melt
temperature would be significant, providing a false analysis. Column 7 “Prioritiza-
tion” is therefore important.
Table 9.7 Introducing Confounded Factors in the Interaction Columns
Non-confounded factors Confounded factors
Experi-
ment No.
Holding
pressure
Melt
temperature
Mold
temperature
Cooling
time
Injection
speed
Holding
time
Screw
speed
1 −1 −1 −1 −1 +1 +1 +1
2 +1 −1 −1 +1 −1 −1 +1
3 −1 +1 −1 +1 −1 +1 −1
4 +1 +1 −1 −1 +1 −1 −1
5 −1 −1 +1 +1 +1 −1 −1
6 +1 −1 +1 −1 −1 +1 −1
7 −1 +1 +1 −1 −1 −1 +1
8 +1 +1 +1 +1 +1 +1 +1
Sum 0 0 0 0 0 0 0
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 264 (page 264)

240 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
This shows that the biggest advantage of confounding is in the reduction in the
number of experiments required to study the process. Based on Equation 9.1,
n = l f
a 7-f
actor, 2-level study would need 128 unique experiments, but with the process
of confounding, these can be reduced to a mere 8 experiments. The general as-
sumption when using confounding is that the interactions are minimum or non-

e
xistent.
 9.7  Randomization
The experiments in the set above are all arranged in a particular order. For exam-
ple in Table 9.7, there are eight experiments, of which the first four are done with
a low mold temperature and the next four are done with the high mold tempera-
ture. The rest of the factors also have a certain regular order. Randomization is not
following any such order and completely selecting the experimental order at ran-
dom. Each row is an experiment and randomization means running the experi-
ments in a random order. Some experts advocate randomization in order to exclude
any external effects that cannot be controlled. For example, if the first four of the
above experiments are done in the morning, when the ambient temperature is low,
and the remaining eight are done in the afternoon, when it is hotter, the ambient
temperature can have an effect on the response. The results will be compounded
by the effect of the temperatures in the morning and the afternoon. This will make
it difficult to separate the effect from morning and afternoon temperature change
from the effect of the mold temperatures that were also different in the morning
and the evening. There could be other factors related to ambient temperature that
one may not be aware of. Tower water temperature, operator skills (not necessarily
time efficiency), and material lot variation are examples of these factors. Therefore,
mixing up or ‘randomizing’ the experiments will help to even out some of these
effects, although not systematically. Randomization also helps to evaluate the
r
obustness of a setting. For example, consider a knob with graduations being used
to set the holding pressure and a setting of 6 on the knob yielded a certain value of
holding pressure. Setting it once in the beginning of the experiment and leaving it
for a set of experiments will deliver the same consistent pressure. However, chang-
ing it to another value and then going back to 6 may yield another value of hold
pressure. This demonstrates the robustness of the setting and going back and forth
with the settings helps the evaluation of the repeatability of the equipment settings.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 265 (page 265)

2419.9 Data Analysis
With a large number of experiments in injection molding, it will be a good idea to
randomize at least part of the experiments. For short runs, randomization is not
required. Further in this text factor selection for DOEs is considered. In most cases
the number of runs are short and can be usually completed with couple hours.
Most machines have digital settings and settings are repeatable. If one changes the
value of the settings and goes back to the same value, the output is repeated. For
these reasons, randomization is not required. It is always good to make a note of
the other factors that are constant. Noting the operator’s name, material lot num-
ber, etc., are part of good documentation procedures.
 9.8  Factorial Experiments
The experiments and tables used in the earlier discussion are all factorial experi-
ments. The design with the maximum number of possible experiments without
confounding is called a full factorial experiment. For example, a 2-level, 4-factor
design would require 16 experiments in a full factorial design. Partial factorial
e
xperiments are designs that have fewer experiments using the technique of con-
founding. A half factorial experiment would mean half the number of runs of a full
factorial experiment or 8 runs out of the 16 full factorial runs. Reliable data can be
obtained from partial factorial experiments to analyze the effect of the factors.
 9.9  Data Analysis
Today, most analysis of DOE data is performed by computer programs that gener -
ate all the information and graphs in a matter of seconds. A typical analysis pro-
vides the following information:
 F
actors that most influence the quality of the part
 The r
obustness of the quality of the part
 Pr
ediction of the most optimized process
 Pr
ediction of the capability of the process within the range of the parameters
studied
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 266 (page 266)

242 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
Table 9.8 Experimental Settings and Response Data for a 3-Factor, Full Factorial Experiment
Runs Experimental run settings Responses
Mold temp (°C) Cooling time (s) Holding press (bar) Length (mm) Diameter (mm)
1 40 30 30 144.73 6.35
2 40 30 55 144.40 6.15
3 40 20 30 144.60 6.32
4 40 20 55 144.30 6.15
5 20 30 30 144.83 6.37
6 20 30 55 144.50 6.16
7 20 20 30 144.65 6.32
8 20 20 55 144.34 6.16
To explain the results and the analysis it is best to consider an experiment. Con-
sider the DOE results shown for the experiment in Table 9.8.
The three selected factors were mold temperature, cooling time, and holding pres-
sure. There were two levels for each factor. The response was the length of the part
and an internal diameter. Based on engineering knowledge and past experience,
the order of importance for the factors was holding pressure—cooling time—mold
temperature. However, if these three factors are arranged in the order of ‘difficulty
of change,’ then they are rearranged in the order mold temperature—cooling time—
holding pressure. ‘Difficulty of change’ simply means how soon the change is seen
in the process. For example, once the mold temperature is changed, depending on
the size of the mold, it may take anywhere from 15 minutes to an hour to see a
change in the actual mold temperature. So this is a ‘difficult’ change. On the other
hand, holding pressure is an easy change, because once the setting is changed, the
change will be reflected in the next cycle. If the experiments are not going to be
randomized, it is a good idea to have the order of the factors in the order of diffi-
culty. This is an efficient way of getting all the experiments done by making the
least amount of difficult changes during the experiments. So, in the above array,
we will have to change the mold temperature (difficult change) only once compared
to the holding pressure (easy change), which will have to be changed seven times
after the first experiment.
With the help of this matrix, the experiments are performed. It is best to collect as
many data as possible for accurate analysis. Typically, if statistical analysis is to be
done, at least 30 parts from each cavity must be checked and the data recorded.
However, as the number of cavities and recorded dimensions for a part increase,
the amount of work to collect the data increases and this can sometimes become
prohibitive. Performing full factorial experiments with a larger number of factors
will again increase the number of experiments and therefore the number of meas-
urements. In the experiment under consideration, we are going to measure the
length of the part. We will take an average of 5 samples for each experiment.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 267 (page 267)

2439.9 Data Analysis
The results are typically displayed in one of the following forms:
9.9.1Tornado Charts
Tornado charts are similar to the commonly used Pareto charts. In DOE, a tornado
chart is a bar chart in which the effect of each factor is plotted in descending order
of magnitude. A factor that has a direct effect is displayed on the positive side of
the y-axis, while a factor that has an inverse effect on the response is plotted on the
negative side of the y-axis. A tornado chart is one of the most important and in-
formative charts in DOE. It will display the factors that have the most effect on the
quality of the part in descending order of importance. For the experiment under
consideration, the tornado chart is shown in Figure 9.10.
Figure 9.10 shows that the factor with the most impact on the length of the part
is the holding pressure. For the levels of the holding pressures tested (between
30 and 55 bar), the average change in length was 0.3175 mm, compared to the
0.1425
mm c
hange observed between the cooling time levels of 20 and 30 seconds.
Change in mold temperature had the least effect on the length of the part. The
a
verage change in length between 20 °C and 40 °C was only 0.0725
mm. N
otice
that the mold temperature bar is on the negative side of the axis. This means that
when the mold temperature increases, the part length decreases. Positive values,
as seen for holding pressure and cooling time, indicate that as these factors are
increased, the length of the part also increases. The interactions are also plotted
and are very insignificant. In Figure 9.10, holding pressure and cooling time have
a significant effect and we can consider that the effect of the other factors is insig-
nificant. The tornado chart for the diameter is shown in Figure 9.11.
-0.0870
0.000
0.1002
0.1938
0.2874
0.3810
0.3175
0.1425
- 0.0725
- 0.0275
0.0125
- 0.0025
Tornado chart
Mold temperature
Cooling time
Holding pressure
Mold temperature*cooling timeCooling time*holding pressure
Mold
temperature*holding pressure
Figure 9.10 Tornado chart showing direct and inverse relations between factors and length
response
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 268 (page 268)

244 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
-0.0120
0.0348
0.0816
0.1284
0.1752
0.2220
0.185
0.02
0.02
-0.01 -0.005 00.0000
Tornado chart
Cooling time
Cooling time*holding pressure
Holding pressure Mold temperature
Mold temperature*cooling time
Mold temperature*holding pressure
Figure 9.11 Tornado chart for diameter of the part
9.9.2Contour Plots
Contour plots display contours that represent a constant value of a given response
on a graph of two of the selected factors on the x and y axis. On any given point on
a given contour, the value of the response will be constant, regardless of the values
on the axes. Figure 9.12 shows a contour plot based on holding pressure and cool-
ing as the factors.
Consider the highlighted contour that has a value of 144.65, which is also the nom-
inal value. Anywhere on this contour, the value will always be 144.65. A combina-
tion of 29 s of cooling time and 42.5 bar of holding pressure (Point A) will produce
a part with the same dimension as the combination 22 s and 52 bar (Point B).
When the nominal value and the specifications are plotted on the contour plot, the
process window inside of which dimensionally acceptable parts can be molded is
visible. In Figure 9.12, the orange contours represent the upper and lower specifi-
cations. Contour plots help to determine the extent of dimensional process win-
dows. The different types of process windows are explained in Chapter 9.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 269 (page 269)

2459.9 Data Analysis
32.5
Cooling time
Holding pressure
21 22 23 24 25 26 27 28 29 30
35.0
37.5
40.0
42.5
45.0
47.5
50.0
52.5
55.0
Dynamic process window
144.3902
144.4393
144.4883
144.5200
144.5863
144.6353
144.6500
Point A
Point B
144.7800
Figure 9.12 Contour plot for length of the part
9.9.3Prediction Equation
A relation between the response and the factors can be established by mathemati-
cal means. Figure 9.1 showed the increase in the length of a part that resulted due
to an increase in the holding pressure. If we assume the relationship to be linear,
we can generate an equation in the form y = mx + c, where y is the length and x is
the holding pressure. The value of m and c can be determined with the help of the
two points. Finding the coefficients and constants of this equation, the dimension
at any value of holding pressure or the holding pressure required for a desired di-
mension can be predicted, see Figure 9.13. This is the basis of prediction equations
that involve all factors and their interactions. Prediction equations are beneficial in
selecting process parameters for robust processes and for hitting target dimen-
sions. It is not always possible to hit target dimensions on all the responses. While
one dimension is in tolerance, another may be out of tolerance. Overlaying contour
plots or looking at composite and desirability functions is a good way to estimate
the robustness and the process capabilities.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 270 (page 270)

246 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
Mold Temperature
Response
Name + TOL NO M- TOLP redicted Value
Cooling Time Holding Pressure
30 25 42.5
Mold Temperature Cooling Time Holding Pressure
30 25 30
Length
Diamete r
0.13 0.13
0. 2
144.6 5
0. 2
144.544
6.25
Response
Name + TOL NO M- TOLP redicted Value
Length
Diamete r
0.13 0.13
0. 2
144.6 5
6.25
6.25 0. 2
144.385
6.16
Figure 9.13 Prediction equation for length and diameter
9.9.4Process Sensitivity Charts
Process sensitivity charts are line graphs that provide a quick glance of the posi-
tion of the response for each experiment. Such a chart can be considered as a
visual of the sensitivity of the response to a change in factors for each experiment.
The upper specification limit (USL) and the lower dimensional specification limit
(LSL) as well as the nominal are shown on the graph. If for all experiments the
r
esponse is within the specification limits, the response is considered stable and
not affected by the process. Such a dimension is shown in Figure 9.14. If this was
considered a critical dimension to be checked regularly during production, a case
can be made to eliminate this dimension for in-process inspection and it could
ins
tead be checked at startup only. Figure 9.15 shows a dimension that is easily
affected by process changes. Composite process sensitivity charts display all
r
esponses on one screen to give a snap shot of all dimensions at one time.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 271 (page 271)

2479.10 Using the Results from DOE
6.010
6.106
6.202
6.298
6.394
6.490
Process sensitivity graph for response diameter
1 2345678
Figure 9.14 Process sensitivity chart for the diameter
144.2500
144.3766
144.5032
144.6298
144.7564
144.8830
Process sensitivity graph for response: Length
1 2345678
Figure 9.15 Process sensitivity chart or the length
 9.10  Using the Results from DOE
The graphs and results from the above charts and equations can be used in a num-
ber of ways.
9.10.1Process Selection
The contour plots will display the constant response curves together with the spec-
ification limits. The goal should be to achieve the nominal value of the response
and be in a robust processing area, see Figure 9.12, where the LSL, USL, and the
nominal are shown. To achieve the nominal, various combinations of the holding
pressure and cooling time exist; for example, at 29 seconds and 42.5 bar or at
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 272 (page 272)

248 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
22 seconds and 52 bar. Any one of these combinations can be selected as process
parameters because both are in a robust molding area. In injection molding, lower
cycle times increase production efficiency. Therefore the lower cooling time must
be preferred and selected.
9.10.2Cavity Steel Adjustment
If the nominal values and the specifications are located towards the corners or
boundaries of a contour plot, it may be difficult to sustain production because the
process may not be robust enough to mold the parts within specifications. For the
part shown in Figure 9.16, the processing window between a short shot and
out-of-specification is only about 50
psi (3.44
bar). The process must be kept within
this 50
psi windo
w to avoid shorts and parts out of specification. The process win-
dow is small and therefore not robust.
If the process variation is large, it is easy to produce parts that are either short or
out of speci
fications. In suc
h cases, without taking the dimensions into considera-
tion, a process with a sufficient process window must be selected. Once it is deter-
mined that the process can produce parts with the required dimensional consist-
ency (not the actual dimension), the steel must be adjusted to bring the parts
within the required dimensions. For example, for the part in Figure 9.16, there is a
danger of short shots because the holding pressure must be kept low to achieve the
required dimension. If the pressure is increased, the parts will be out of specifica-
tions but the chances of short shots will be greatly reduced. Running at the center
of the process window will produce parts that have the least or zero possibility of
short shots. Parts must be molded at the center of the window and the dimensions
measured. Depending on the dimensions, the mold steel must now be changed to
bring the molded parts within the required tolerance. This will result in a robust
process that will produce parts within the desired speci
fi
cations.
0840
13 14 15 16 17 18 19 20 21 22
0880
0920
0960
1000
1040
1080
1120
1160
1200
Dynamic process window
Cooling time
Holding pressure
15.0549
15.0555
15.0576
15.0603
15.0630
15.0657
15.0684
15.0711
0840
13 14 15 16 17 18 19 20 21 22
0880
0920
0960
1000
1040
1080
1120
1160
1200
Dynamic process window
Cooling time
Holding pressure
15.0394
15.0416
15.0437
15.0450
15.0480
15.0510
15.0502
15.0545
15.0550
Figure 9.16 Using the DOE results to make steel changes and increase the processing window
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 273 (page 273)

2499.10 Using the Results from DOE
9.10.3Process Adjustment Tool
The factors used in the DOE were selected based on the assumption that they were
the most influential to the part quality. The analysis results provided the quantita-
tive effect of each of these factors. During a production run, if the part quality
drifts, the analysis results can help in adjusting the process to get the part quality
back to where it should be. For example, if the tornado diagram shows that the
holding pressure and cooling time have the most significant effect on the length of
the part, then a contour plot with holding pressure and cooling time as variables
may help the processor adjust either one or both variables and continue making
acceptable products. The guesswork regarding what parameter should be changed
is eliminated. This will also keep the process sheet clean of changes to several
par
ameters and limit the changes to the holding pressure and cooling time. Edu-
cating the workforce and providing access to this data at the molding machine is
essential.
9.10.4Setting Process Change Tolerances
The tornado charts and the contour plots provide information on the most signifi-
cant process parameters and the extent to which they affect the part quality. Based
on this data, the process change allowances and limits can be set. In the contour
plot, a box, must be set and the corresponding limits must be used as tolerance
limits for allowable changes during production.Only these factors must be changed
in case there is a quality problem.
9.10.5Reducing Inspection
The results from a DOE can be very useful in reducing and even eliminating inspec-
tion. If the process sensitivity charts indicate that a dimension does not seem to be
affected by the various process changes and provided that this dimension is within
specifications, it can be checked at mold startup and then be assumed as within
specification during the in-process inspection. The same holds true for other
dimensions t
hat are well within the process windows of the established
pr
ocess.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 274 (page 274)

250 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
 9.11  The Dimensional Pr ocess Window
(DPW)
The concept of the cosmetic process window was introduced in the previous chap-
ter. The is the window or the boundaries of the process parameters within which
the molded parts are cosmetically acceptable. Dimensions are not considered. Now
that the topic of DOE was introduced we can consider the dimensional process
window or the DPW within which the molded parts would be within spec. Refer to
Figure 9.17, which shows the DPW for one dimension for Cavity 1 of a 2-cavity
mold. A large DPW is a sign of a robust molding process. The process must be set
in the center of the window.
Dimensional Process Window:
Holding Pressure: 825 to 1100 psi
Melt Temp: 500 to 545 °F
X
Center of the Process:
Melt Temp: 525 °F,
Hold Pressure: 960 psi
DPW for Cavity 1
Figure 9.17 The dimensional process window for Cavity 1
As the number of cavities and the dimensions increase, the window can quickly
get smaller and smaller. Cavity balance plays a very important role in the size of
the DPW. If all the cavities fill and pack at the same rate, the process windows for
each cavity will overlap. If they do not fill and pack at the same rate, then each
cavity will have its own DPW, but the overlap could be a small area that will reduce
the overall process robustness and repeatability. Refer to Figure 9.18, which shows
the DPW for Cavity 2. If any of the dimensions are cornered inside the CPW, then
this is also a clear sign that the process is not going to be robust. The DPW for
Ca
vity 2 is very small and is not acceptable. The window gets even smaller when
the contours for both cavities overlap. Refer to Figure 9.19.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 275 (page 275)

2519.11 The Dimensional Process Window (DPW)
Dimensional Process Window:
Holding Pressure: 820 to 860 psi
Melt Temp: 540 to 547 °F
Center of the Process:
Melt Temp: 543 °F,
Hold Pressure: 835 psi
DPW for Cavity 2
X
Figure 9.18 The dimensional process window for Cavity 2
Dimensional Process Window:
Holding Pressure: 830 to 860 psi
Melt Temp: 543 to 545
°F
Center of the Process:
Melt Temp: 543 °F,
Hold Pressure: 835 psi
Combined DPW for Cavity 1 and Cavity 2
X
Figure 9.19 The dimensional process window for Cavity 1 and Cavity 2
A similar argument and explanation can be made considering dimensions. Refer to
Figure 9.20 where two dimensions for Cavity 1 overlap, resulting in the reduction
of the DPW. Each dimension should be considered individually first and the effort
must be made to increase the DPW.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 276 (page 276)

252 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
Dimensional Process Window:
Holding Pressure: 860 to 1150 psi
Melt Temp: 540 to 548 °F
Center of the Process:
Melt Temp: 544 °F,
Hold Pressure: 1000 psi
Combined DPW for two dimensions for Cavity 1
X
Figure 9.20 The dimensional process window for two dimensions for Cavity 1
The DPW is a subset of the CPW. Naturally, a wide CPW favors the possibility of a
wide DPW, provided the nominal of the dimension is centered in the windows. If
this is not the case, the data can be reviewed with the tooling engineer to support
justifying a mold steel adjustment to center the part dimension within the specifi-
cation limits.
 9.12  Selections of Factors for DOEs
The final shrinkage of the plastic is easily influenced by a number of molding pa-
rameters. Molding process validations therefore call for a number of procedures to
be followed to first, find the most robust areas of each processing parameter, and
then, to find the effect of each of these on part quality (DOE). The various process-
ing parameters that are typically adjusted (inputs) are given below. These are the
factors that directly influence the plastic and will therefore make a difference in
the part quality. Factors such as mold open speed or ejection speed do not contrib-
ute directly to the plastic process and are therefore left out of the list.
1.
Injection speed
2.
Injection pr
essure
3.
P
acking and hold pressures
4.
P
acking and hold times
5.
Melt t
emperatures
6.
Mold t
emperatures
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 277 (page 277)

2539.12 Selections of Factors for DOEs
7. Sho t size and Transfer (switch over) position
8.
Bac
k pressure
9.
Scr
ew rotation (recovery) speed
10.
Cooling time
Le
t us revisit the parameters above and discuss their optimization.
1.
Injection Speed
– Injection speeds are optimized using the data from the first
step of the 6-Step Study. The flat region (Newtonian region) of the curve is where
the injection speeds are set. Because the viscosity in the Newtonian region does
not change, it does not make a difference if the speed is set at a high or a low
value within the Newtonian region. Therefore, injection speed is not a factor
that should be typically included as a factor for DOE. Injection speeds typically
affect the cosmetics of the part. If the difference between the speeds is large,
then dimensions could be affected. Typically, injection speed should be set to ‘as
fast as you need’ and not ‘as fast as possible.’ In most cases injection speed is not
used as a factor for DOEs.
2.
Injection Pr
essure – To achieve a set injection speed, a finite amount of pres-
sure is required. The molding machine is set to a value that is higher than this
number so that the required pressure is always made available as and when re-
quired. If the setting is done below the required pressure, the process becomes
pressure limited. Setting the pressure to 20 % more than what is required, or to
50 % more than what is required, will not make an effect on the injection speed
because the machine will still use what it needs regardless of what is made
available to it. Varying the pressure from a high to low value is not going to have
any effect of the part quality. Therefore, the injection pressure is not used as a
factor for DOEs.
3.
P
ack and Hold Pressures – As seen from the Specific Volume versus Tempera-
ture graph (Figure 9.2), the specific volume is dependent on the pressure that is
applied to the melt. The pack and hold pressures are one of the most important
factors and must always be considered as a factor for the DOE.
4.
P
ack and Hold Times – In cold runner molds, this is optimized using the gate
seal study. This is Step 5 in the 6-Step Study. Using more time than required
does not increase the amount of plastic inside the cavity and therefore does not
affect the dimensions. Using less time than what is required to seal the gate will
cause part weight variations, resulting in part dimensional variations and is
therefore not recommended. This parameter should therefore not be used as a
factor for performing a DOE for cold runner molds. In case of hot runner molds,
there is a land that needs to freeze off to stop the flow of the plastic into the cav-
ity. However, the land area is small and the flow can easily be influenced by the
hold time. The holding time should therefore be used as a factor for hot runner
molds. The optimization technique is mentioned in Section 9.16.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 278 (page 278)

254 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
5. Melt T emperatures – The melt temperature setting is responsible for achieving
the required melt viscosity to fill the mold. In case of amorphous materials the
recommended melt temperature range is wide and the so the melt temperature
can affect the shrinkage. Therefore melt temperature should always be a factor.
In the case of crystalline materials, the melt temperature range is typically very
narrow and does not significantly influence the shrinkage. Melt temperatures
for crystalline materials should not be typically used as a factor for DOEs.
6.
Mold T
emperatures – Mold temperatures are responsible to maintain the flow
of the plastic to the end of the fill of the part. The temperature of the plastic at
the end of fill should be within the recommended range of the melt temperature.
This is true for amorphous and crystalline materials. In the case of crystalline
materials, the mold temperature has an additional function. Because the forma-
tion of the crystallites needs a certain amount of energy, this energy is supplied
by the mold temperature. The optimum crystallite formation depends on the
mold temperatures. The mold should therefore be maintained in the recom-
mended temperatures and the mold temperature should be used as a factor for
the DOEs. In case of amorphous materials, there is no requirement of crystallite
formation and so mold temperatures are only critical for the flow and cosmetics.
The lower end of the mold temperatures should be therefore used as long as the
flow and cosmetics are achieved. The mold temperature is therefore not used as
a factor for DOE for amorphous materials.
7.
Sho
t Size and Transfer (Switch Over) Position – The volume between the shot
size and the transfer position should be equal to the volume of the plastic in-
jected in the injection phase. In practical molding, the mold is filled about 95–
98 %. Because this volume is fixed, both these process parameters should not be
used as factors for DOE. When performing the experiments, the value of the
transfer position should be changed to achieve the same 95–99 % fill as and
when required. For example, if the part is 98 % full at low melt temperatures the
part will more than likely be full at the high melt temperature. For the high tem-
perature set of experiments, the transfer position (or the shot size) must be re-
adjusted to achieve the original 98 % fill before collecting the parts for the exper-
iment. The weight of the part in the injection phase should always be matched.
8.
Bac
k Pressure – Back pressure is used to help and achieve consistency in the
amount of the plastic that is metered for the next cycle. It also helps in com-
pressing the melt and squeezing off all the volatiles out of the melt. The back
pressure is optimized by monitoring the screw charge time and by observing
the cosmetics of the part. Excessive back pressure causes an increase in the
shear heat and sometimes an undesirable increase in the screw charge times. A
minimum optimal amount of back pressure should therefore be used. Because
the back pressure should be maintained at the lowest optimum value, it should
not be used as a factor for DOE. As a side note, in some cases there can be an
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 279 (page 279)

2559.12 Selections of Factors for DOEs
effect of bac k pressure on dimensions. In most cases this can happen when the
pack and hold phase is not optimized. Excessive back pressures can also in-
crease shear and break down additives such as glass fibers. This will result in
a change in shrinkage and ultimately affect dimensions. Excessive back pres-
sures must be avoided.
9.
Scr
ew Rotation (Recovery) Speed – The screw acts as an auger to move the
plastic from the feed throat to the front of the barrel. At the same time it is also
helping to melt the plastic and to form a homogeneous melt. In addition to the
heating of the plastic with the help of the heater bands, the rotating action of
the screw also provides the shear energy for the melting. This is especially
critical for crystalline materials where the crystallites rely more on the shear -
ing action to melt rather than the heat from the heater bands. The faster the
screw rotates more is the shear energy and this results in the increase in the
temperature of the melt. A high screw speed can cause the plastic material to
burn and degrade. This is especially true in case of shear sensitive materials
such as PVC and acetals. Very low screw speeds will not cause the plastic to
melt properly and form a homogeneous melt. Similar to the back pressure the
screw speed must be set to the lowest optimum screw speeds and therefore
this process parameter is not required to be studied as a DOE factor. Screw
speeds are to be set such that the screw recovery time is always less than the
set cooling time.
10.
Cooling T
ime – Cooling time is an important process parameter that must be
used for the DOE for two reasons. First the as the amount of time the plastic
remains in the mold changes, the heat transfer changes and therefore the ejec-
tion of the part on the Specific Volume versus Temperature graph changes. The
result is the change in the shrinkage value. Second, since injection molding is
a business the processes must be as efficient as possible. Cooling time should
be used as one of the factors for the DOE to find the optimum setting.
The factors mentioned above are the ones that are usually adjusted on the molding
machine to mold parts to the required specifications. Refer to Table 9.9 for the
summary of the factors to be used in the DOE. There are a maximum of five plastic
factors that will truly make a significance difference in the part. All the factors are
important, but to varying degrees. To make the DOE practical and efficient one
must select the top hitters that will provide the ‘low hanging fruit’ and help to
achieve the most optimum process. Understanding the molding parameters and
the science behind their function is necessary. The same factor can have a different
effect on the various dimensions of the part. For example, increasing cooling time
can increase the length of a part but may have no effect on the diameter of the part.
Each dimension must be dealt with case to case basis. The above discussion is a
good guide that has been successfully used for several years by the author.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 280 (page 280)

256 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
Table 9.9 Process Parameter Optimization Method and Selection for DOEs
No. Factor Method of Optimization To be used in DOE? Y/N
1 Injection speed Viscosity curve No (exceptions exist)
2 Injection pressure Pressure drop study No
3 Pack pressure Cosmetic process window study Yes
4 Hold pressure Cosmetic process window study Yes
5 Pack time Gate seal study No for cold runner
Yes for hot tip, valve gate
6 Hold time Gate seal study No for cold runner
Yes for hot tip
7 Cooling time Cooling time study Yes
8 Melt temperature Cosmetic process window Yes for amorphous materials
No for crystalline materials
9 Mold temperature Cosmetic process window No for amorphous materials
Yes for crystalline materials
10 Screw rotation speed Minimum required –
melt homogeneity
No
11 Back pressure Minimum required – cosmetics No
12 Shot size Part fill of 95–98 % No
13 Transfer Part fill of 95–98 % No
In most cases, with a cold runner mold a three factor, two level DOE is more than
sufficient. These are the pack pressure, the cooling time, and the melt or mold
temperature based on the morphology of the material. If the plastics material is an
olefin, you may require a fourth factor, which would be the mold or melt tempera-
ture, which was not considered in the first three factors. In case of hot runner
molds, the pack time must be used. Refer to Figure 9.21.
1. Hold Pressure .......YES
2. Cooling Time ........YES
3. Melt Temperature
4. Mold Temperature
5. Pack Time ...........YES FOR HOT TIPS AND VALVE GATES
MAX NUMBER OF FACTORS TO BE USED = 5, BUT IN MOST CASES = 3
OR ....... FOR POLYOLEFINS BOTH
Figure 9.21 Most commonly used factors for DOE
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 281 (page 281)

2579.13 Analysis of Variance (ANOVA)
 9.13  Analysis of Variance (ANOVA)
The topic of variation was discussed in Chapter 1. There is an inherent natural
variation in every molding process. This is the reason process capability is calcu-
lated on some of the critical dimensions. Refer to Figure 9.22, which shows the
variation and the spread of the dimensions for parts molded from two processes.
The parts with Process 1 (P1) are molded with a pack pressure of 55
bar
, and
the parts with Process 2 (P2) are molded with the pack pressure of 60
bar
. P1
pr
oduces parts with an average of 15.25
mm and P2 wit
h an average of 15.32
mm.
The v
ariation in both process is 0.10
mm. Ther
e is therefore a region where the
spread of both processes overlap. Parts with a dimension between 15.27
mm and
15.30
mm can be molded fr
om P1 and P2. ANOVA is the activity of comparing the
the inherent variation within a process to the difference in the averages of two
processes. In the example, the inherent variation is 0.10
mm and t
he difference in
the averages was 0.07
mm. Ther
e was a purposeful change of 5
bar in t
he packing
pressure between P1 and P2. Detailed discussions are beyond the scope of this
book. Most software programs will output this information.
15.25 15.3015.20
Process 1
Pack Pressure
= 55 bar
15.32 15.3715.27
Process 2
Pack Pressure
= 60 bar
Overlap Parts
Figure 9.22 Parts in the overlap region that can be molded from 2 processes
While performing injection molding DOEs there should be a sufficient change in
the molding process so as to make a difference in the quality of the parts (Figure
9.23). For example, an acceptable number for pack pressures should be about 275
to 350
bar plas
tic pressure (about 4000 to 5000
psi), f
or cooling times it should be
about 8 to 10 seconds for a 2.5
mm t
hick part. Melt and mold temperatures should
be taken from the data sheets.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 282 (page 282)

258 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
15.2515.20
Pack Pressure
= 55 bar
15.30
15.50 15.5515.45
Pack Pressure
= 85 bar
Figure 9.23 High and lows for DOE should be spread apart such that there are no overlapping
parts
 9.14  Collecting Shots for a Quality Check
A shot is defined as parts from one molding cycle. For a given experimental set-
ting, at least 5 shots must be collected. Of these shots at least 3 shots should be
measured. The reason for collecting 5 and measuring 3 is to eliminate any outliers
if any in the 3 measured shots. All shots must be collected when the process is
stable. Process changes fall under the categories of time, temperature, speed, pres-
sure, and distance.
The following are the general guidelines about the number of shots between collec-
tions:
 T
ime: An example of time related settings are hold time, pack time, and cooling
time. The number of shots in the barrel must be calculated. Once the times are
changed, mold the number of shots equal to the number of shots in the barrel
and discard them. Start collecting shots for measurement after the next shot. By
doing this, the residence time in the barrel for all the shots is identical and what
it would be if that setting was selected in production. Change in residence time
will change resin properties. The mold temperature should also be checked for
stability.
 T
emperature: Examples of temperature related changes are melt and mold tem-
peratures. In both these cases, it is advisable to stop the machine, make the
change, and wait for the temperatures to reach the desired settings. Once the
desired temperatures have been achieved, start molding, run the number of
shots equal to the number of shots in the barrel, check the actual mold tempera-
tures for stability, and collect parts. As a side note, start the DOE with the ma-
chine set at the lower value because it is easier to reach the increased settings
than trying to drop temperatures down. Dropping the temperatures and reaching
the set points is usually more time consuming.
 Speed: An e
xample of speed related change is the injection speed. A change in the
injection speed will change the fill time and therefore the rules of time mentioned
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 283 (page 283)

2599.15 Choosing the Highs and Lows for DOEs from the Process Window
above will apply. Screw rotation speeds are not a desired factor for DOEs. How -
ever, if these are changed, stability of melt temperature must be checked and
then rules of temperature must be applied.
 Pr
essures: Examples of pressures are pack pressure and hold pressure. Ma-
chines will react to this change during the next molding cycle and in some cases
instantaneously. For all practical reasons, these changes do not affect residence
times or temperatures. Shots can be collected within two shots of making the
change.
 Dis
tances: Examples of distances are the shot size and the transfer position.
These should not be used for a DOE, but if they are used, then the fill times will
change. Therefor the rules that apply when times are changed will also apply
when distances are changed.
 9.15  Choosing t he Highs and Lows for DOEs
from the Process Window
The cosmetic process window can be a parallelogram as shown in Figure 9.24. In a
DOE, the values for the high and low pressures at the low melt or mold tempera-
ture should be identical to that at the high melt or mold temperature. To determine
these values, one must therefore inscribe a rectangle within the parallelogram and
use the high and low values of this rectangle. This is shown in Figure 9.24.
FLASH
SHORT / SINK
HIGH
MELT
TEMP
LOW
MELT
TEMP
x
x
High
se/g427ng
Low
se/g427ng
Figure 9.24 Selecting the high and low when the process window is a parallelogram
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 284 (page 284)

260 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
 9.16  DOE Application t o Optimize Pack
and Hold Times
For cold runner molds, hold times are optimized by conducting a gate freeze study
where the part weight is recorded as a function of the hold times. When the gate
freezes, the part weight remains constant with increasing times. A second or so is
added to the lowest value of time where the part weight stays constant, and this
number is taken as the total time for the setting of the hold times. However, in hot
runner systems or in valve gated systems, the gate area always has molten plastic
and therefore the part weight curve never flattens out. Therefore, the above method
does not produce acceptable results.
Excessive hold time and hold pressure can cause defects such as flash, stress in
the part, part staying on the wrong side of the mold whereas not enough pressure
can cause shorts, sink and dimensional issues. A combination of hold times and
pressures must be found and then a DOE must be done to optimize the parameters
with the available limits.
Following is the procedure to optimize the hold times for hot runner and valve
gated molds. The procedure has been explained with the help of an example for a
2-cavity screen mold that is used in the irrigation industry.
A template to generate a cosmetic process window was prepared, see Figure 9.25.
The x-axis corresponds to the holding time and the y-axis corresponds to the hold-
ing pressure. Such a template is called a visual inspection template (VIT). A filled
out and completed VIT is shown in Figure 9.25. The red square markers represents
a part with a defect at lower pressures and times (sink, short, etc.), a red triangular
marker represents a part with a defect on the higher end of the pressures and
times (flash, overpacked parts, etc.), and a green circular marker represents a part
that is cosmetically acceptable.
Starting with a hold pressure value of 27.6
bar (400
psi), par
ts were molded from
27.6
bar t
o 96.6
bar (1400
psi) in s
teps of 13.8
bar (200
psi), wit
h holding times
from 4 seconds to 10 seconds in steps of 1 second. The data was collected and
r
ecorded in the VIT. The defect on the lower pressures and times was sink and on
the higher side was flash in the screen area. One can now draw several cosmetic
process windows (CPW) in the VIT.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 285 (page 285)

2619.16 DOE Application to Optimize Pack and Hold Times
20.7
27.6
34.5
41.4
48.3
55.2
62.1
69.0
75.9
82.8
89.7
96.6
103.5
345678 91 01 1
WINDOW 1 WINDOW 2 WINDOW 3
Holding Time (sec)
Holding Pressure (bar)
Figure 9.25 Visual inspection template with possible cosmetic process windows
The next step, once these windows are determined, is to look for dimensions. The
technique of DOE is used for this. The process is varied between the limits of the
windows and the dimensions are evaluated. After considering the three CPWs and
other production requirements, it was decided to pick Window 3 for determining
the limits of the DOE. The DOE matrix is shown in Table 9.10.
Table 9.10 DOE Matrix based on the Cosmetic Process Window
Exp. No. Hold Time (sec) Hold Pressure (bar)
1 10 69.0
2 10 41.4
3  6 69.0
4  6 41.4
Parts were molded at the 4 settings in Table 9.10, and then the parts were meas-
ured for dimensions. The dimensional requirement on this part was on the length
of the part and was specified at 126.80 +/–0.07
mm. The anal
ysis was carried out
with the DOE module of the Nautilus Software. The results are shown in Figures
9.26(a) through 9.26(d).
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 286 (page 286)

262 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
a)
b)
c)
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 287 (page 287)

2639.16 DOE Application to Optimize Pack and Hold Times
d)
Dimensional Process Window:
Holding Time 6.2 to 7.5 sec
Holding Pressure 43.5 to 63.5 bar
Selected Process Se/g427ngs:
Holding Time 7.0 sec
Holding Pressure5 5.0 bar
Figure 9.26 Dimension Process Window via DOE for Hot Runner Molds; (a) dimensional
pr
ocess windows for Cavity 1, (b) Cavity 2, (c) both Cavities 1 and 2, and (d) a composite
dimensional pr
ocess window for both Cavities 1 and 2
Figure 9.26(a) and (b) show dimensional process windows for Cavity 1 and 2, re-
spectively. The solid green contour lines represent Cavity 1, and the dotted contour
lines represent Cavity 2. The green lines represent the settings where the parts are
dimensionally acceptable, and the red lines represent the settings where the parts
are dimensionally not acceptable.
Because there are two cavities here, we must then overlay the two contour plots
on top of each other to determine a combined contour graph as shown in Figure
9.26(c). The area where the green contours for each cavity intersect represents the
settings where both the cavities can be molded with acceptable dimensions.
One can now draw a composite dimensional process window inside which the
parts will be dimensionally acceptable. Such a window is shown in Figure 9.26(d)
for the above experimental data. Observing the window, one can notice that vary -
ing the holding time from 6.2 to 7.5 seconds and between 43.5 to 63.5
bar of hold
-
ing pressure will produce dimensionally acceptable parts. Naturally, the bigger
this window, the more robust the process is going to be.
Process robustness is the goal of every molder and therefore it is best that the center
of the DPW in Fig 9.26(d) is taken at the process settings. A holding pressure of
55
bar and a holding time of 7.0 seconds w
ere chosen as the process settings. Vary-
ing t
he holding time from 6.2 to 7.5 seconds and between 43.5 to 63.5
bar will s
till
produce dimensionally acceptable parts. This is an indication of a robust process
and will therefore produce parts not only to specifications but also with improved
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 288 (page 288)

264 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
statistical process capability. Again, several dimensional windows are possible here.
On molding machines, the extent of pressure variation is higher than time variation
and therefore maximizing the pressure window is always preferred.
The above mold had gone through an iteration for steel adjustment resulting in an
acceptable process window. During the first iteration, the mold was incapable to
mold parts consistently to dimensional specification. The cosmetic process window
was large but the dimensional process window was extremely small. Considering
both cavities the molding process was not robust making it statistically not capable
either. Remember that molding parts to spec does not mean that all the parts will
be within spec. One must understand and measure the combined variation in the
machine, material, process, and so on.
The above procedure was described for hot runner molds but can easily be ex-
tended to molds with valve gated systems. The procedure remains the same and is
in fact slightly simpler since the valve pin shuts off the gate eliminating the true
hold phase from the original discussion of the pack and hold phase.
Optimization of holding pressure times for hot runner molds has always been an
area of trial and error. The procedure described above is a scientific way of deter -
mining the holding pressure and time in case of hot runners and valve gated sys-
tems. The procedure also evaluates and demonstrates the robustness of the pro-
cess and the ability to mold parts consistently.
An interesting study was done using polarized light on an optical cover. See Figure
9.27. In this case, the sink in the gate area was visible under polarized light. A VIT
was generated using these pictures followed by a DOE as described above.
0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0
TIME (SEC)
17000
16000
15000
14000
13000
PRESS
(PSI)
PARTS
HAVE SINK
ACCEPTABLE PARTS HAVE FLASH OR
STAYING ON THE WRONG
SIDE OF MOLD
Figure 9.27 Visual inspection template and dimensional process window for an optical cover
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 289 (page 289)

2659.17 Setting Acceptable Machine Tolerances and Alarms during Production
 9.17  Se tting Acceptable Machine Tolerances
and Alarms during Production
Tolerances are applied to the values of the inputs on the molding machine while
alarms are applied on the outputs from the molding machines. For example:
Tolerance: Consider the tolerance on pack pressure is +/–3.5
bar (50
psi). This
means t
hat if the set value is 70
bar
, the processor can change the value anywhere
from 66.5

bar to 73.5

bar.
Alarm: The limits on cushion is set to +/–1.0
mm (0.04
in). This means t
hat if the
cushion value is 8 mm with an established process that is in production and if the
cushion falls below 7 mm or goes above 9 mm, the machine will alarm.
Most companies have generic tolerance and alarms limit numbers for each of their
processes. For example, melt temperature: +/–10 % or cushion value: +/–2
mm.
The pr
oblem in using a generic method to set the tolerances is twofold.
 Using a % is misleading. If t
he melt temperature is 200 °C, then a +/–10 % is
+/–20 °C or a range of 40 °C. If the melt temp is 370 °C, as is in case of a PEI,
then a +/–10 % is +/–37 °C or a range of 74 °C. So the higher the value, the wider
is the tolerance range which does not make any scientific sense.
 Pr
ocess tolerances are applied to keep the product within the product quality
requirements or within the LSL and the USL. If one puts a generic tolerance of
+/–10 %, then one is assuming that if the parts are molded at the lower end
(–10 %), and the parts are molded at the high end (+10 %), then both these sets of
parts are acceptable. This may or may not be the case.
Machine tolerances and alarm limits must be set based on scientific reasons and
should be determined from the experiments conducted during process develop-
ment. The tolerances should be based on the results of the DOE. Output values
during the DOE should be recorded and based on the final settings so that the
alarm limits can be finalized. A contour plot and an example for setting alarm lim-
its is shown in Figure 9.28.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 290 (page 290)

266 9  Process Development Part 2: Exploring the Dimensional Process via the DOE
Dimensional Process Window:
Holding Pressure: 825 to 1100 psi
Melt Temp: 500 to 545 °F
X
Process Tolerance:
Melt Temp: +/– 20 °F
Holding Pressure: +/– 135 psi
Resultant cushion: 0.015″ to 0.009″
Alarm Limits:
Cushion: +/– 0.03″
Center of the Process:
Melt Temp: 525 °F, Hold Pressure: 960 psi
Figure 9.28 Setting alarm limits
The above procedure is for one dimension and one cavity. One must consider all
the cavities and all the dimensions. This can be a challenging task especially if the
mold cavities are not balanced and/or the cosmetic process window is narrow.
Most DOE programs will predict an optimal process. One can simulate the process
using the software, and then set the tolerances. In case of tight tolerance parts,
these process tolerances will be much narrower as compared to commodity molded
products such as buckets, pails, forks, and spoons (where dimensions require-
ments are almost nonexistent).
 9.18  Summary
Some would argue that the DPW and CPW get smaller and smaller as the number
of dimensions and cavities increase. Unfortunately that is the reality, and in fact,
typically it is not acknowledged because of the effort involved in making the pro-
cess windows larger. A small process window leads to a process with almost no
room for any adjustment, resulting in a process sheet with very small limits for
process changes. Tolerances on process parameters are usually established based
on past molding experience. However, to be successful, process tolerances must be
set based on the type of analysis described in this chapter. This further pleads the
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 291 (page 291)

2679.18 Summary
case for well built injection molds and parts dimensioned with reasonably defined
tolerances. This is where concurrent engineering principles and practices become
important. A robust process requires less human intervention, which allows the
potential for reducing the frequency of in-process inspection. A well planned injec-
tion mold and part design, along with a disciplined process development approach,
are critical to having an efficiently running production process and a profitable
manufacturing operation. Without the above, much time, money, and resources
will be wasted in trying to efficiently produce parts from an inherently inefficient
system.
Suggested Reading
Lahey, J. P. and Launsby, R. G., Experimental Design for Injection Molding (1998), Launsby, Colorado
Springs, CO
Del Vecchio, Understanding Design of Experiments (1997), Hanser Publishers, Munich
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 292 (page 292)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 293 (page 293)

Mold Qualification
Flowchart, Production
Release, and
Troubleshooting
This chapter will discuss a flowchart that includes all necessary measurements
and the documentation that must be carried out for successful release of a molding
process into production. The tools required for mold qualifications and trouble-
shooting are also mentioned. Development of troubleshooting guides is a continu-
ous process, and they need to be revised and updated during production runs.
 10.1  Mold Qualification Flowchart
Process developmental procedures described in the previous chapters are key to
releasing the mold to production. A robust process needs little or no supervision
during the production run. The required supervision usually involves for the pro-
cessor to perform a visual check on the product, verify the process, answer any
alarms, or perform scheduled or preventive maintenance such as cleaning the
mold faces. If processes are not robust, a technician needs to constantly attend the
machine to adjust the process parameters in order to yield acceptable parts. Robust
processes yield consistent parts, shot to shot, cavity to cavity, and run to run.
The mold qualification procedure can be split into two parts, the mold-function
qualification and the mold-part qualification. The flowchart is shown in Figure 10.1.
10
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 294 (page 294)

270 10  Mold Qualification Flowchart, Production Release, and Troubleshooting
Step 1: Mold function qualification
(Scientific processing
section)
6 Step study
Start
1 – Viscosity study
2 – Cavity
balance
3 – Pressure
drop
4 – Process
window
5 – Gate seal study
6 – Cooling study
Mold or part
issues
Fix mold
or
part
design
Not OK
Not OK
Not OK
Not OK
No
Recommended mold qualification procedure
Select DOE
Parameters
Perform DOE
Select process
Run process
Determine
DPW
Adjust
mold steel and/or
move nominal
and/or
open tolerances
Run short production run to
evaluate the molding process
and
molding process capability
Please note: This flow charts has been developed
by fimmtech and is a recommended procedure.
The users should use their own discretion and
judgment in following the procedure especially
keeping safety in mind. The user is solely
responsible for all consequences,
-suhas kulkarni, www.fimmtech.com
Yes
Step 2: Mold-part quality qualification
(Design of experiments
section)
Figure 10.1 Recommended mold qualification procedure
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 295 (page 295)

27110.2 Mold Qualification Checklist
10.1.1Mold Function Qualification Procedure
Mold function qualification requires a 6-step qualification study described in
Chapter 7. During this study, the function of the mold and its components, the
de
termination of some of the process parameters, and the size of the process win-
dows are evaluated. During this study, dimensional analysis to measure process
capability are typically performed. The actual dimensions are not of major impor -
tance because the next step is to adjust the mold steel dimensions to mold the
parts within the required specifications. The mold function qualification step is to
determine the aesthetic process window (APW). Naturally, a wide window is desir-
able. Once the mold function and process windows are acceptable, the next step
will evaluate the part quality.
10.1.2Mold and Part Quality Qualification Procedure
This step involves performing the DOE, selecting the process, and determining the
size of the dimensional process window (DPW) and the control process window
(CPW). At this point, based on the knowledge from initial statistical dimensional
analysis, there must be enough confidence that the process is stable and that the
mold steel can be and must be adjusted to center the process in the DPW and thus
in the CPW. At this point, if the dimensional variation for a particular dimension is
greater than the difference between the Upper specification limit (USL) and the
lower specification limit (LSL), it becomes clear that it is impossible to consistently
mold all the parts within specifications because some parts will always be out of
specifications. The product designer must revisit the product specifications and the
material selection for the parts. It is acceptable to stop the mold qualification pro-
cess at the end of step 1 (the mold function qualification), if the dimensions are
acceptable. However, the only way to know whether the process has been optimized
is to perform a DOE. The benefit of performing a DOE outweighs the time and effort
required to perform it. Process tolerances, alarm limits, and process robustness are
some of the critical pieces of information available only through a DOE.
 10.2  Mold Qualification Checklist
Having a mold qualification checklist makes sure that all features of the mold and
the process have been assessed. A sample checklist is included in Appendix F. The
checklist should be used during the mold trial and should be completely filled out
with comments by the end of the trial. Any suggestions must be passed on to the
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 296 (page 296)

272 10  Mold Qualification Flowchart, Production Release, and Troubleshooting
mold maker or the concerned department, including reasons for any recommended
or required changes. For example, if the mold is flashing, a sample part with flash
must be given to the mold maker. An example of a completed mold qualification
checklist is shown in Table 10.1.
Table 10.1 Mold Qualification Checklist
No. Question Comment
1 Are gate sizes acceptable? Open gate size to 0.060″
2 Are runner sizes acceptable? Yes
3 Is venting acceptable? Vents on runners required
4 Is part fill acceptable? Yes
5 Is the ejection acceptable? Parts do not fall off the ejector pins
6 Has the rheology study been done? Yes
7 Is the cavity balance acceptable? No, Cavity 2 is shorter than the others
8 Is the process window acceptable Process window is small. Part flashes soon after fill
9 Has the gate seal study been done? Yes. Will be repeated after gate size change
10 Has the cooling study been done? No
 10.3  Process Documentation
Because there are a number of factors that affect the process, a detailed record
must be kept of each of these factors. The factors include machine settings, actual
process outputs, material drying parameters, machine setup instructions, mold
setup details, operator work instructions, secondary processes, and any other fac-
tors involved in the journey of the plastic pellet until it is shipped out of the facility
as a finished product.
10.3.1Process Sheet
The process sheet is usually the first piece of documentation that is generated dur-
ing the initial sampling of the mold. It primarily contains the machine settings for
the process. It should also include other factor-setting information. A typical list of
factors is included in the sheet shown in Table 10.2.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 297 (page 297)

27310.3 Process Documentation
Table 10.2 Process Variables and Outputs to Be Recorded on a Process Sheet
Temperatures Speeds Pressure Times Other Outputs
Drying Injection Injection Drying Shot Size Part weight
Barrel Mold open Packing Packing Transfer position Runner weight
Hot runner Mold close Holding Holding Material info Injection time
Mold Ejection Back Cooling Nozzle length Cushion
Fixtures Screw Tonnage Nozzle orifice Cycle time
Annealing Coolant flow rate Melt temperature
Core sequences Screw recovery time
A process sheet must be generated and updated at the end of every mold trial
it
eration. Any new process changes that are made must be recorded over the old
parameters, but a log of all the process changes with the corresponding dates must
be maintained. This essential history is useful in debugging future issues. The
history also provides information on the evolution of the process to the current
state from “what it used to be.” For example, over a few runs cycle times seem to
drift away from the standard and the question always asked is “What changed?”
A process change log is very useful in such cases and the changes over time can be
evaluated. A process change log must also be maintained during production runs
and should be a part of the process documentation.
10.3.2Waterline Diagrams
Injection molding is a heat transfer process and the mold is the primary heat
e
xchanger. The mold temperature plays a very important role in the part quality
because it affects the rate of heat transfer. Mold temperatures must not only be
kept constant during a run, but also must be maintained at the same values from
run to run. This will help to achieve the run-to-run consistency goal. This leads to
the necessity of hooking up cooling waterlines in the same manner for every run.
The Ins, Outs, and the loops must be placed in the same place during every run to
ensure the same heat transfer from the mold. A water line diagram must be main-
tained in the records, showing the hookup for every waterline. An example of a
water line diagram is shown in Figure 10.2.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 298 (page 298)

274 10  Mold Qualification Flowchart, Production Release, and Troubleshooting
Figure 10.2 Waterline diagram
Because the heat transfer also depends on the coolant temperature and flow rate,
these values must also be recorded. The differential pressure or the pressure drop
is useful in evaluating whether there is any scaling or other obstruction in the wa-
ter lines. This information should typically be recorded by the tooling department.
10.3.3Mold Temperature Maps
Even when the water lines are hooked up properly as documented in water line
diagram, the actual mold temperatures are also important. For example, if the set-
ting on the mold temperature control unit is 60 °C, but the water line is obstructed,
the mold will not reach the required temperature. There is also a loss of heat be-
tween the temperature control unit and the mold. Water leaving the temperature
control unit at 60 °C may cool down to a temperature of 50 °C by the time it reaches
the mold. Therefore, the actual mold temperatures of the mold cavities must be
recorded before startup. The temperature at each of the water fittings must also be
recorded. Any plugged line will cause a different OUT line temperature than the
rest of the lines. When the mold temperature is set close to ambient room temper -
ature, a plugged line will not negatively affect the temperature distribution in the
mold cavity, because the mold temperature will always find equilibrium in the
cavity steel. It is therefore important to record and check the mold temperature
when the mold has been running for some time. This time must be specified and
recorded. Examples of mold temperature maps are shown in Figure 10.3.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 299 (page 299)

27510.3 Process Documentation
Figure 10.3 Mold temperature maps, before and during molding
10.3.4Setup Instructions
The procedure and the tools required to set up the mold must be recorded to facili-
tate a quick and hassle-free set up. This is particularly important for molds that
need special instructions, such as mold open and close sequences for a mold with
cores. Molds can easily get damaged if the sequences are not correct, costing the
company sometimes thousands of dollars for the components to be replaced, the
manpower, machine time, loss of production, and so on. Mold start-up instructions
must also be included. A mold must be started up by lowering both pressure and
speeds. Mold shut-down procedures and material purging instructions must also
be provided. Times for heat soaking of hot runner manifolds must also be provided
for molds that utilize a hot runner system.
10.3.5Operator Instructions
Packaging and any secondary operations performed by an operator must be clearly
defined. The operator is usually the last person to handle a part before it goes into
the box, making him/her the integral part of all quality control efforts. Operators
should be given clear instructions regarding handling the product and performing
any secondary operations, such as deflashing the product. Packaging is another
important step, because parts not packaged correctly could become damaged dur -
ing transportation and in some cases this could result in a change in quality, such
as warpage.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 300 (page 300)

276 10  Mold Qualification Flowchart, Production Release, and Troubleshooting
 10.4  Documentation Books
It is best to have two types of documentation records, the mold qualification book
and the production book. The mold qualification book should record all details of
the qualification process, and the production book must include all information
required for production, including some of the qualification results to help the
technician debug and fix any problems during production. Table 10.3 provides a
list of documents that should be included in these books.
Table 10.3 Documents to Be Included in Qualification and Production Books
Document Qualification book Production book
Part drawing Y Y
Properties data sheet Y N
Processing data sheet Y Y
Mold setup instructions Y Y
Viscosity curve Y Y
Cavity balance Y Y
Pressure drop Y Y
Aesthetic process window Y N
Gate seal study Y Y
Cooling study Y N
DOE matrix Y N
DOE results – Pareto charts Y Y
DOE results – contour plots Y Y
DOE results – other Y N
Process sheet Y Y
Dimensional process window Y Y
Control process window Y Y
Process change log (during development) Y N
Process change log (during production) N Y
Operator instructions * Y Y
Daily mold maintenance (during production)* Y Y
Start-up and shut-down instructions* Y Y
*  These ar e living documents that should be started during mold development and must be constantly updated
during production
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 301 (page 301)

27710.6 Mold Specific Troubleshooting Guide
 10.5  Qualification Production Runs
Once part quality, process windows, and process capability are acceptable, a short
qualification run must be performed. The length of this run should be determined
based mainly on the production volumes and the criticality of part quality. For
molds that would typically run for most of the year, a robust process and mold
design will r
elieve production personnel of constant production management and
will allow running a lean manufacturing operation. For such molds a qualification
run of 24 hours should be considered. For critical parts, such as parts that require
zero defect quality, the same procedure must be followed. It is extremely important
that the process is closely monitored during this production run and process
changes must be avoided. If process changes are required to maintain the quality,
the whole process must be reevaluated, because this is an indication of a non-ro-
bust process. The parts molded from these runs must be initially quarantined and
released to the customer once all the information and quality has been verified.
Longer runs will provide a better understanding of the dimensional variations.
 10.6  Mold Specific Troubleshooting Guide
Even for a commonly known defect, the solution to fix the problem may be differ -
ent for each mold. For example, splay on one part could be a result of excessive in-
jection speed, while for another mold running the same material, the splay could
be the result of low mold temperature. Every mold has its own characteristics and
therefore, although a general troubleshooting guideline is a good starting refer -
ence point, every production book must contain a living document that contains
the record of the typical problems and the respective solutions. This record should
be updated every time a new defect is seen and a solution for the defect has been
found, saving effort the next time the defect is seen. The factors that must not be
changed must also be mentioned. For example, if mold temperatures are important
for a particular dimension, or if it was found not to be a significant contributor to
the solution of the problem, then this must also be mentioned. Often, there is more
than one solution to fix a defect and therefore the solutions must be prioritized.
The results from the DOE must also be included here. They will give an indication
of the most important factors that have an effect on the parts. An example of a trou-
ble shooting guide is shown in Table 10.4.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 302 (page 302)

278 10  Mold Qualification Flowchart, Production Release, and Troubleshooting
Table 10.4 Mold Specific Troubleshooting Guide
No. Defect Recommendation DO NOT CHANGE
Clean vents Injection speeds
1 Splay Check material moisture
Reduce melt temperatures
(not below 210 °C)
2 Shorts on the sleeve Clean vent pin Holding pressure
3 15.055 dimension is undersized Check water flow through the cores Holding pressure
 10.7  Molding Startup and Shutdown
10.7.1Purging
The barrel must be purged off all the material present in it to eliminate any purg-
ing compound that was used and/or eliminate any degraded material present in
the barrel. Injecting degraded materials in the mold can cause two potential prob-
lems. First, the degradation could have been so significant that all mechanical
properties of the plastic have been lost and injecting this material in the mold can
produce a brittle part, posing ejection problems. Parts getting stuck in the mold,
parts breaking off during ejection, ejector pins piercing through the parts, break -
ing of ejection components due to stuck parts are all problems caused by degraded
materials. The second problem that may arise is the excessive gassing that takes
place due to the material degradation. The gasses build up in the barrel and if not
purged, they get injected into the mold and again end up clogging the vents that
are the last points to fill. The products of degradation are easy to transport through
the mold and clog the vents. If the vents get clogged during the first shot and this
problem is not noticed and fixed, the molded parts may develop cosmetic and di-
mensional problems immediately. This forces a process change further effecting
parts and finally leading to a chain of process changes.
Hot runner systems must also be purged of possible degraded materials using
fresh material. A large piece of cardboard must be placed on the moving side of the
mold to avoid any degraded material from being sprayed on the mold, because if
this happens, the mold often needs to be pulled out for cleaning, especially if there
are complicated slide or lifter mechanisms. Care must also be taken to inject at
lower speeds and pressures, because some hot runner manifold components rely
on the clamping pressures to keep them from leaking under injection pressure.
A good starting method is to use the screw speed and a high back pressure to ex-
trude the melt out of the hot manifold. All molds are different and can pose unique
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 303 (page 303)

27910.7 Molding Startup and Shutdown
problems with regard to purging. Each purging procedure must be evaluated for
the particular mold before being carried out.
10.7.2Startup of a Molding Machine
All molding operations involve high pressures, temperatures, and speeds. These
can be extremely dangerous and accidents, from burns to fatalities, have been re-
corded. Safety should always be a priority and starting up the molding machine
must be done following a careful and systematic procedure. From the process
standpoint, it is preferable start up the molding process using a conservative ap-
proach, detailed in the following, before full pressures and speeds are set on the
molding machine. This will prevent any accidental damage and over-packing of the
parts in the mold. Over-packing of the parts causes flash and in some molds the
flash can fill up internal vents. Stationary vent pins are examples of such internal
vents. In addition, when the parts get over-packed, mold opening pressures in-
crease and it becomes difficult to open the mold.
To better illustrate the startup procedure, here is an example with the following
conditions: Holding pressure = 1000
psi, holding time = 8
seconds, and cooling
time = 20 seconds.
Based on these conditions, a recommended startup procedure would be:
1.
V
erify the process with the documentation that was recorded during the qual-
ification run
2.
Chec
k melt temperature
3.
Chec
k mold temperature and make sure water is flowing
4.
Incr
ease cooling time by an amount equal to the pack and hold time
(cooling time = 28 s)
5.
Se
t pack and hold, pressure, and time to zero (HP = 0, HT = 0)
6.
Se
t the screw delay time equal to the set HT: Screw delay = 8 s
7.
Purg
e the machine and take the first shot in a semi-automatic mode
8.
Matc
h the ‘Injection Only’ part with the recorded documentation or sample
part
9.
T
ake a couple more shots
10.
A
dd half the hold and pack time and pressure and reduce the cooling time by
half the set HT (HP = 500 psi, HT = 4 s, cooling time = 24 s)
11.
T
ake about 5 shots
12.
Se
t screw delay time equal to zero or the value in the recorded documentation
13.
Se
t the process to match the recorded documentation
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 304 (page 304)

280 10  Mold Qualification Flowchart, Production Release, and Troubleshooting
Note: Some parts cannot be molded short. In such molds, leave the holding time to
the set value and gradually increase the holding pressure.
10.7.3Shutdown of a Molding Machine
The shutdown procedure is equally important. If a heat sensitive material or an
easily degradable material is molded, it must purged from the barrel before shut-
ting the machine down. Molding must be stopped and an appropriate purging
com
pound must be used to purge the barrel. If the mold has a hot runner system,
follow the recommendations of the hot runner supplier to purge the hot runner
system before shut-down. All material in the barrel must be emptied out and the
screw must be left in the front position. If the material is not emptied out and the
screw is not left in the forward position before being shut down, a solid cylinder of
plastic will be formed once the machine has cooled, which will pose a problem
during start-up.
Because plastic is a bad heat conductor, the center of the cylinder takes a long time
to melt; therefore, the solid cylinder prevents any purging or injection from taking
place. When chilled water is run through the molds, the water is shut off and a few
shots are run to prevent water condensation in the cavities.
The last shots with the runners must always be saved with the mold. No secondary
operations such as degating or deflashing should be done on these shots because
they are evidence of the condition of the mold and process before shut down.
 10.8  Troubleshooting
Troubleshooting is probably the most important job function in any production
environment. As equipment and processes have become more and more complex,
the need for highly knowledgeable workers with good troubleshooting skills has
become increasingly important. The molding process is complex in terms of plastic
flow characteristics and the speeds, pressures, times, and temperatures involved
with the process. Each of these factors can affect the quality of the part. For exam-
ple, increasing melt temperature can increase flow rate, or increasing injection
speed can also increase flow rate. Increasing cooling time can increase the dimen-
sion of the part, while decreasing the mold temperature can also increase the di-
mension of the part. Because multiple actions can have similar effects on part
quality, different people have their own preferred method of solving a problem.
The downside of this fact is that the process sheet is often updated with the latest
changes and after a few months of running the mold, the set process ends up being
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 305 (page 305)

28110.8 Troubleshooting
completely different from when it was first created. This illuminates two problems:
first, the process was not established scientifically and second, the personnel were
not trained to troubleshoot the process in a systematic manner with the right tools.
But even with a robust process, often production problems may still occur. When a
robust process is established, documenting the complete process with all inputs
and outputs must be done; however, it is sometimes impossible to capture the
s
tatus of each related process or equipment. For example, recording the response
time of a hydraulic valve controlling the injection or a pneumatic air valve con-
trolling the gate is difficult and probably never done, although this may have an
impact on the part quality. If the conditions of these components change, so will
the molded part quality requiring troubleshooting skills.
There are no hard and fast rules for troubleshooting an injection molding process.
First, the problem with the parts must be understood and then the possible rea-
sons for the issue must be considered. No process parameter must be changed un-
til the complete set of process parameters is compared with the original recorded
process parameters and the outputs are scrutinized. Every other factor that is not
recorded on the process sheet must also be looked into.
The following are some guidelines that can be followed for general troubleshooting.
1.
Com
pare the set process to the original documented process. If there are any
changes, do not change the process back to the original (because they may have
been made for a reason).
2.
Obser
ve the whole process for ten shots and record all the outputs for these ten
shots. These include: injection fill time, cushion, screw recovery time, and cycle
time. Compare the above actual outputs to the documented ones.
3.
S
top the machine and compare the actual mold temperatures to those that were
documented in the book.
4.
R
ecord the melt temperature and compare with the documented measurements.
5.
Chec
k the temperature of the hoses to check for water flow as described earlier.
Remove any obstructions in the lines and let the water circulate for some time to
allow the mold temperature to stabilize.
6.
If t
here have been any changes compared to the original process sheet, refer to
the results from the DOE and see if those changed parameters would have any
effect on the quality of the part. If not, set the process back to the original. If the
changes are influential to part quality, check if the out-of-specification part was
a result of this change made. If so, change the process parameter back to the
original. If not, make the appropriate change and bring the parts back into spec-
ifications. Any process changes must be recorded.
Once the parts are running meeting quality requirements, the process and quality
must be constantly monitored for about a shift’s worth of production. Any unusual
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 306 (page 306)

282 10  Mold Qualification Flowchart, Production Release, and Troubleshooting
trends, such as increasing injection pressures, decreasing fill times, or any other
variations must be noted. This change may sooner or later cause the parts to go out
of specifications and one must be proactive to find the root cause of the trend or
variation. A good example is inadequate cooling of the mold because of lack of
cooling lines. In its role as a heat exchanger the mold must remove all heat that is
put into it to maintain steady state. If the heat is not removed, the mold tempera-
ture will rise and affect the quality of the part. This change will be gradual and will
be manifested in a certain trend in the dimensions of the part.
A process change log sheet must be maintained with the production book. The
original process must always be present in the book, together with the updated
process sheet. Every time a change is required, the old and new process para
-
me
ters must be recorded on the process change log sheet. This disciplined record
keeping will ensure that a history of all changes made to the process sheet is main-
tained for review.
Checking water flow through the mold is not a very easy task. When the mold tem-
perature control water unit is turned on, it is assumed that the water is flowing
through each line in the mold. One of the most common reasons for dimensional
issues in production is that a water line (or oil line) becomes obstructed. These is-
sues can be detected only by physically checking the temperature of the hose with
a pyrometer, if the water temperature is high. For temperatures between approxi-
mately 30 to 45 °C (85 to 115 °F), the most efficient way is to hold a hose by hand
and feel the heat of the water flowing through the lines. For water temperatures
below 30 °C, this technique can be confusing because the temperature is not very
different from room temperature and holding the hose by hand and trying to feel
for a warm hose may not indicate water flow. Machine vibration can easily be con-
fused for water flow and therefore trying to ‘feel’ the water flowing through the
mold must be avoided. It is good practice to raise the temperature to approximately
35 °C and check for the water flow. Safety must be practiced. The practice of check-
ing for water flow must also be followed at the start of every job. The water must be
set to approximately 35 °C, the water flow must be checked, and then set to the
required process temperature. Certainly for molds that use oil as a coolant a pyro
-
me
ter must be used because the mold temperatures can be very high depending on
the material. For example, PEEK is processed at mold temperatures between 175 °C
and 205 °C (350 °F to 400 °F). The importance of safety cannot be stressed enough
here because of the high temperatures of the coolant oil that is used in processing
such materials.
Below are some of the common problems encountered on the production floor:
1.
Pinc
hed or kinked waterlines
2.
W
ater line control valve not turned on
3.
IN and OUT r
eversed
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 307 (page 307)

28310.9 Important Equipment and Tools for Qualifications and Troubleshooting
4. Inle t volume of water to the manifold is less than the required output to the ma-
chine
5.
When using a T
-junction for water lines, the IN must be such that it is the verti-
cal line of the letter and the OUTs are the horizontal lines. If the water IN is one
of the horizontal lines, the OUT on the vertical line can get starved of water. A
venturimeter works on the principle that vacuum is generated in a vertical line
of a T-junction if the internal geometries and sizes of the T-junction and the fluid
velocities satisfy Bernoulli’s equation. Although the generation of vacuum is
unlikely, the effect of reduction of water flow is highly possible.
6.
W
ater lines from the controller to the mold are too long, causing loss in temper-
ature and increasing pressure drop
7.
F
eed throat temperature is not regulated
 10.9  Im portant Equipment and Tools for
Qualifications and Troubleshooting
Although this seems like a topic that does not need discussion, it is included here
more as a checklist and to emphasize the importance of this equipment.
1.
Melt p
yrometer
2.
Sur
face pyrometer
3.
W
eigh scale with the following accuracy (preferred)
 1 g f
or parts weighing over 250–300 g
 0.1 g f
or parts weighing between 50–250 g
 0.01 g f
or parts weighing less than 50 g
 0.001 g f
or micro-molded parts
4.
Flo
w meter
5.
Magnifying g
lass
6.
Flash light and mir
ror
7.
Br
ass tools – rods of various sizes (diameter and length), pliers.
8.
Flame t
orch
9.
Heat g
loves – thin and thick
10.
Pr
ocessing data sheets
11.
Camer
a – still and video
12.

Calculator
13.
N
otepad, forms (with copies) and procedures of mold qualification
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 308 (page 308)

284 10  Mold Qualification Flowchart, Production Release, and Troubleshooting
The use and benefits of most of the equipment is self-explanatory. The actual melt
and mold temperatures must be measured with the pyrometers, rather than re-
cording the settings. Accurate weigh scales are required to perform gate seal tests
or to perform statistical analysis on part weights. Part weight is a valuable output
that directly correlates to the quality of the part. If no variation is seen in the part
weights, the weigh scale resolution is not small enough. An accurate scale with
sufficient resolution to detect small changes in part weight is a necessity. A flow
meter need not be installed on every single water line, but it should be used to
check the water flow during the preventive maintenance schedules. Those num-
bers should be used to compare the flow rates during production, if there is a prob-
lem with part quality. When dealing with plastic or parts stuck in the mold, brass
tools or those made of soft materials must be used to prevent damage to the mold.
For highly polished surfaces, it is best that only experienced technicians handle
any stuck plastic or any issues with the mold. The polished surfaces can easily get
damaged and repairs are not only expensive but also time consuming. Video cam-
eras can help with infrequent problem occurrence. In such cases, setting up and
then reviewing the recording is an easy solution. The recording can be paused or
played back in slow motion to pinpoint the issue. Because documentation is a large
part of the whole qualification process, documents, such as data sheets and forms,
should be readily accessible to make the process efficient. Laptops and work
-
s
tations are becoming commonplace on the production floor and the need for paper
documents is slowly decreasing.
 10.10  Common Def ects, Their Causes,
and Prevention
Defects in injection molded parts could result from any one of the five factors that
contribute to part quality. These are part design, material selected, the mold de-
sign and the build, the choice of the molding machine, and the molding process.
The quickest and easiest change that can be done is always in the molding process
and, therefore, it seems like processing could take care of all defects. In most cases,
it is quite the opposite. See Figure 10.4, which is a representation of the part that
had the gate in the wrong location. In the process of packing out the thick section
at the end of the fill, the rib area near the gate would get overpacked and stick in
the mold. The thick section at the end of fill had sink. The problem was clearly with
the mold design. The actual part is not shown for anonymity of the customer.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 309 (page 309)

28510.10 Common Defects, Their Causes, and Prevention
Gate
Thick Section
(needs to be
packed)
Thin Section
(does not need
to be packed)
Underpacked Section
Overpacked Section
(section sticking in the
mold during ejection)
Figure 10.4 Mold design related issue
10.10.1Splay: What is it? How to get rid of it?
In injection polded parts, the most common cosmetic defect is splay. Almost every
molding operation rejects parts for this reason.
Injection molding is the process of injecting molten plastic into a mold. The cavity
steel has a desired texture that gets picked up by the molten plastic and is repli-
cated on the part. Depending on the base polymer being molded, the plastic melt
temperature is anywhere between 175 °C to up to even 400 °C, as is in case of
some PEI resins. At these temperatures, water turns to steam, and some of the low
molecular additives can burn to produce volatiles. The speed of injection of the
plastic into the mold generates shear. Excessive shear can degrade the molecules.
Steam and volatiles (collectively grouped as volatiles) from degradation flow with
the plastic into the mold. Because of the fountain flow of the plastic into the mold
cavities, the volatiles get to the surface and prevent the molten plastic from coming
in contact with the mold steel, at the same time, smearing the volatile on the inter-
face of the melt and the mold steel. This shows up as streaks and is called splay.
Splay is also called silver streaks. See Figure 10.5.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 310 (page 310)

286 10  Mold Qualification Flowchart, Production Release, and Troubleshooting
Volatile Mold steel
Splay
Plastic melt under
fountain flow
Figure 10.5 Formulation of splay
Sources of splay:
 Mois
ture in the material.
 Gat
e sizes are smaller than required. If the gates are too small or have sharp
edges, the plastic can get excessively sheared and produce volatiles. In that case,
mold design is the culprit.
 Some
times a worn out screw and/or barrel can also cause excessive shear result-
ing in splay.
 R
egrind is another source of splay especially if the regrind has excessive fines.
During the regrind process some of the plastic gets ground up into very fine and
almost powder like material called as fines. The fines don’t convey well because
they can get stuck to the screw and finally degrade causing volatiles.
 The v
ents in the mold provide an outlet for the volatiles. If the vents are plugged
up and/or are not deep enough and/or are not sufficient in number, then the
volatiles have nowhere to go resulting in splay.
There will always be some volatiles and definitely air that gets trapped in the melt
stream. This air is the air that is present between the pellets as the pellets go from
the feed section to the compression section of the screw. Back pressure applied
during the screw recovery process helps get rid of this air and volatiles. Back pres-
sure should always be kept to a minimum because excessive back pressure can
also increase shear and result in splay.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 311 (page 311)

28710.10 Common Defects, Their Causes, and Prevention
10.10.2Defects in Molding
All troubleshooting must be done during the mold qualification stage. As dis-
cussed, it is important that a mold have a large cosmetic window, which will then
increase the chances of a robust molding process. Following are some of the de-
fects in molded parts. The solutions listed are a living, dynamic list and are only
possible solutions. A solution to a problem in one part may not be the solution to
the identical problem in another part. So judgement must be used.
1.

Short Shot
Possible Reason:
 Molt
en plastic is not reaching the mold
cavity section.
Possible Solutions:
 Incr
ease melt temperature
 Incr
ease mold temperature
 Incr
ease injection speed
 Incr
ease injection pressure if process
is pressure limited
 Chec
k if the mold is vented in the area of short shots
 Incr
ease gate and runner sizes
2.Flash
P
ossible Reason:
 Molt
en plastic flowing into unwanted
sections of the mold cavity.
Possible Solutions:
 Chec
k for mold shut-off and mold dam-
age
 Decr
ease melt temperature
 Decr
ease mold temperature
 Decr
ease injection speed
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 312 (page 312)

288 10  Mold Qualification Flowchart, Production Release, and Troubleshooting
3.Sink
P
ossible Reason:
 Plas
tic is shrinking as it cools but addi-
tional plastic cannot be further com-
pensated for the shrinkage.
Possible Solutions:
 Incr
ease pack and hold pressures
 Incr
ease pack and hold times
 Decr
ease mold temperature
 Decr
ease melt temperature
4.

Splay
Possible Reason:
Refer to Section 10.10.1 for a detailed
e
xplanation.
 A
layer/streak of a unwanted gaseous
byproduct from the melt or moisture in
the material, which comes in between
the melt flow and the cavity walls, pre-
venting the texture from being picked
up and, in addition, eventually leaving
a residue.
Possible Solutions:
 Dr
y plastic to suggested moisture levels
 Decr
ease injection speeds
 Decr
ease melt temperature
 Decr
ease screw rotation speeds
 Decr
ease back pressure
 Incr
ease mold temperature
 Incr
ease venting
 Incr
ease gate sizes
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 313 (page 313)

28910.10 Common Defects, Their Causes, and Prevention
5.Warpage
P
ossible Reason:
 A differ
ential cooling rate of the melt
in two sections of the molded product.
Possible Solutions:
 Decr
ease melt temperature
 Exper
iment with differential mold temperatures on the fixed and movable sides
 Incr
ease pack and hold pressures
 Incr
ease pack and hold times
 Incr
ease cooling time
6.

Burn Marks
Possible Reason:
 When air and g
asses get trapped in-
side the mold cavity during plastic
injection, t
he high pressure results in
the dieseling of the of the plastic re-
sulting in the burning of the plastic.
Possible Solutions:
 Incr
ease venting in the mold
 Decr
ease injection speed
 Decr
ease melt temperature
 Decr
ease screw rotation speeds
7.

Contamination or Black Specks and Streaks
Possible Reason:
 This can be caused b
y degraded plastic
and/or foreign material that can get
mixed with the plastic to be molded.
Possible Solutions:
 R
educe melt temps
 R
educe injection speeds
 R
educe screw speeds
 F
ind source of foreign material
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 314 (page 314)

290 10  Mold Qualification Flowchart, Production Release, and Troubleshooting
8.Voids
P
ossible Reason:
 Usuall
y occur when the parts are
thick; the walls solidify and the plastic
melt shrinks towards the wall and
moving away from the center. This cre-
ates a vacuum void inside the part.
 P
ossible Solutions:
 R
educe melt temperature
 R
educe mold temperature
 R
educe injection speed
 Incr
ease pack and hold pressures
 Incr
ease pack and hold times
9.

Bubbles
Possible Reason:
 When mois
ture and/or a gaseous by -
product gets mixed with the melt and
injected into the mold cavity, this mois-
ture or gas, if embedded inside the
melt, can show up as bubbles.
Possible Solutions:
 Dr
y material to suggested moisture levels
 Incr
ease back pressure
 R
educe melt temperature
10.

Gate Blush
Possible Reason:
 Sho
ws up at the gate when the mate-
rial is sheared differently as compared
to the rest of the part.
Possible Solutions:
 Slo
w down the injection speeds in the
gate area
 Pr
ofile the injection speeds if necessary
 Exper
iment with increasing and decreasing melt temperatures or hot tip temper-
atures, in case of hot runner molds
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 315 (page 315)

29110.10 Common Defects, Their Causes, and Prevention
11.Jetting
P
ossible Reason:
 Seen when t
he part is thick, and caus-
ing the injected plastic ‘snake fall’ on
to the cold mold surface. The incoming
plastic does not blend with the first
material, causing the jetting marks.
Possible Solutions:
 R
educe injection speed
 Incr
ease melt temperature
 Chang
e gate location
12.

Weld Lines
Possible Reason:
 The melt flo
w front is usually cold due
to exposure to the cold cavity. When
two flow fronts meet, as in a flow
around a mold pin, they do not fuse
uniformly causing a weld line. Some-
times air can also get trapped inside to
form the defect.
Possible Solutions:
 Incr
ease melt temperature
 Incr
ease mold temperature
 Incr
ease injection speeds
 Incr
ease venting
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 316 (page 316)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 317 (page 317)

Role of Mold Cooling,
Venting, and Regrind
in Process Development
 11.1  Mold Cooling
The mold is basically a heat transfer unit. The hot plastic melt is injected into the
cold mold cavity where it is cooled down until it is ejected out of the mold. The
mold is kept at a lower temperature compared to the melt, which is sufficient to
bring the melt down to the ejection temperature of the plastic. The temperature of
the mold is very important because it controls the rate of heat transfer. The aim of
scientific processing is to achieve three different consistencies: shot-to-shot con-
sistency, run-to-run consistency, and cavity-to cavity consistency. Consistent heat
transfer is important to achieve this goal. The rate of heat transfer between the
melt and the mold is directly proportional to the difference in the temperature be-
tween the two. If melt and mold temperatures are held constant throughout the
molding run, it is safe to assume that the rate of heat transfer was consistent dur -
ing every shot. Melt temperatures are achieved by setting the barrel temperatures
on the molding machine and typically they are not a major source of variation. It is
always good practice to set alarms on the actual barrel temperatures to detect any
changes and out-of-limit conditions. Although it is not common practice to have a
melt temperature sensor inside a mold, this is an excellent way to measure the
consistency of the melt temperature.
Maintaining a constant mold temperature is much more challenging compared to
maintaining constant melt temperatures. This is where the mold design is critical.
Cooling circuits must be designed for efficient heat transfer. The choice of the cool-
ant must also be considered. The word cooling is used because it is necessary for
the mold to be at a lower temperature than the melt in thermoplastic injection
molding. Mold temperatures can be as high as 162 °C (325 °F) for materials such
as polyimides, with melt processing temperatures as high as 400 °C (750 °F).
Therefore, a few important considerations regarding the design of cooling chan-
nels for molds are discussed in the following.
11
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 318 (page 318)

294 11  Role of Mold Cooling, Venting, and Regrind in Process Development
11.1.1Number of Cooling Channels
Uniform heat transfer between every section of the melt and the mold steel will
reduce the melt temperature evenly throughout the part. This will lead to consist-
ent shrinkage, eliminating any warpage or built-in stresses in the molded part. The
most ideal scenario is to have a constant steel temperature at every point in the
cavity, which means that the coolant needs to envelope the cavity steel. Naturally,
this is not possible and therefore an attempt must be made to place the maximum
amount of cooling lines around the part. This is not an easy task because with an
increasing number of cooling lines there is always a risk of mold damage and
weakened mold cavity steel. The plastic is injected at very high pressures and
therefore the mold steel needs to be capable of withstanding these pressures. The
presence of ejector pins, core pins, or other mold components can also weaken the
mold plate. The need for these mold components often presents the problem of how
to fit them in without interfering with desired flow channels. On the other hand,
too few water lines will cause insufficient heat transfer, leading to hot and cold
spots that result in inconsistent cooling. Over time the overall mold temperature
can also increase, changing the heat transfer rate and therefore the part quality.
The goal is always to find a balance between mold integrity and under-cooling.
The other factor is the total length of the flow channel, including the hoses that
connect to the mold temperature unit. Long flow lengths have high pressure drops,
reducing flow rates and thereby reducing heat transfer. There are no easy formulas
to calculate or estimate the number of cooling lines required because each part is
different, with different surface areas, thickness, orientation in the mold, and so
on. Computer programs are available to predict mold and part temperatures during
molding. These should be used as guidelines when possible. A recent development
called contour cooling is gaining popularity. Here, the cavity is built in laminates
or plates in which the cooling channels are machined following the contours of the
part surface. When the mold is assembled, the cooling channels form a circuit that
resembles the part contours. This is an effective way to achieve uniform cooling,
but the price can become prohibitive.
11.1.2Reynolds Number of the Coolant Flow
The Reynolds number gives an indication whether the coolant flow is laminar,
transitional, or turbulent. For maximum heat transfer the flow must be turbulent
and never laminar. In laminar flow, the coolant flows in layers. As it passes through
the mold and begins to pick up heat from the cavity, the temperature of the coolant
layers close to the steel increases. Because the heat transfer rate is directly pro-
portional to the difference in temperatures between the steel and the coolant, an
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 319 (page 319)

29511.1 Mold Cooling
increase in temperature of the coolant layer causes a drop in heat transfer rate. A
change in heat transfer rate in turn will cause a change in part quality and affect
consistency. In turbulent flow, the coolant molecules do not move in layers but are
constantly mixed around in the flow channel, absorbing the heat from the steel and
distributing it evenly in the coolant. This helps to maintain water temperature and
therefore the heat transfer rate remains constant. Figure 11.1 shows the difference
between laminar and turbulent flow. Even with turbulent flow conditions, the wa-
ter can slowly begin to heat up, indicating that there is more heat to be transferred.
In this case, the diameter of the water lines or the number of water lines need to be
increased. If the diameter of the water line is increased, the flow rate of the water
must also be increased. A Reynolds number higher than 4000 will ensure turbu-
lent flow (some texts recommend a Reynolds Number of approximately 3500 for
turbulent flow).
Figure 11.1 Laminar and turbulent flow
The calculation for the Reynolds number Re is given in Eq. 11.1.
Re = ρ
µ
VD (11.1)
ρ
is the coolant density
V is the coolant velocity
D is the diameter of the pipe
μ is the dynamic viscosity of the coolant
Calculations of the Reynolds number for water with a viscosity table are given in
Appendix C.
11.1.3Type of Coolant
As described in Section 11.1, the word ‘coolant’ is used because it is cooling the
melt. The coolant temperature can be as high as 165 °C, where it is essentially
heating the mold but still cooling the melt and maintaining the mold at a desired
temperature. Water and oil are typically used to maintain the mold temperature.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 320 (page 320)

296 11  Role of Mold Cooling, Venting, and Regrind in Process Development
Water is inexpensive, easier to work with, can easily achieve turbulent flows, and
is therefore most widely used. If an additive, such as ethylene glycol, is added, the
properties of the additive must be considered regarding heat transfer and type of
flow calculations. The disadvantage of water is that it can only be used up to tem-
peratures of approx. 95 °C (~ 205 °F), which is close to its boiling point.
For temperatures above 95 °C oil is frequently used. Many high performance mate-
rials, such as polyimides, need mold temperatures in the range of 162 °C (325 °F).
Oil must be used in such cases. The disadvantage here is that oil flow is rarely
turbulent, making heat transfer more difficult. From a safety standpoint, oil heat-
ers are equipped with features that shut their pumps off in case of a sudden rup-
ture of an oil line. In some cases, electric heaters are also used but these are less
common. There is no mechanism to take the heat added by the plastic out of the
mold. An injection mold relies on convection and conduction to transfer the heat.
The temperature in the cavity steel area is therefore not reliable and cannot be
maintained accurately. Some mold designs do call for a hybrid system and use a
combination of electric and oil heaters. In this case the mold temperature is more
reliable.
11.1.4Series and Parallel Cooling
When the number of water lines in a mold increases, there may not be sufficient
outlets on a water manifold to hook up each individual water line separately. In this
case, some of the water circuits through the mold are looped or ganged together
and supplied by a single water line. There can be two types of such arrangements,
as shown in Figure 11.2, and each has its own advantages and disadvantages. The
important factor is to make sure there is turbulent flow in the lines.
Figure 11.2 Parallel and series configurations for coolant lines
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 321 (page 321)

29711.2 Venting
Parallel cooling lines exhibit less pressure drop allowing the coolant to flow at a
higher velocity and therefore they pose less risk for laminar flow of the coolant
through them. However, the flow through the lines may not be uniform. Because the
coolant will take the path of least resistance, it is possible that a cooling channel
with any restriction or blockage may not get sufficient coolant flow. It will be difficult
to observe this without having a flow meter on every individual line. In case of a
series arrangement, any restriction or blockage in a water line can be easily located;
here, one flow meter is sufficient. If all molded parts suddenly start having quality
problems, this could indicate a problem in a water line. Water lines hooked in series
can exhibit large pressure drops, if the overall length of the line is too long.
 11.2  Venting
The air inside the cavity needs to be evacuated to ensure plastic filling the cavity.
Therefore, vents are added to the cavity blocks in the mold. Air that is not evacu-
ated gets pressurized and super-heats, resulting in a dieseling effect on the plastic
parts. This will cause the plastic to burn and/or create an unfilled area, causing a
short shot. Over time, the mold steel can get damaged because of the excessive air
pressures in a local area at the end of fill or in corners where the air and plastic
tend to get pressurized. Figure 11.3 shows a part with burn marks before venting
and without burn marks after venting. Figure 11.4 shows a rib that was short for
lack of venting. Internal voids are another common defect that is seen with insuffi-
cient venting. Depending on the flow pattern of the plastic, the air gets trapped
inside the part, forming voids. An example of a part with internal voids is shown in
Figure 11.5. Once the vents were added to the mold, the voids disappeared. Lack of
vents can also create excessive pressures in the cavity, causing the mold to open
sufficiently enough to cause flash on the parting line. Some machines have an op-
tion for mold ‘breathing’ before the start of the holding phase. The mold is allowed
to open slightly to let the air out and then is clamped before the start of the pack
and hold phase.
Before Venting After Venting
Figure 11.3 Elimination of burn marks after the addition of vents
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 322 (page 322)

298 11  Role of Mold Cooling, Venting, and Regrind in Process Development
Figure 11.4 Rib not filled completely for lack of venting
Figure 11.5 Elimination of voids after the addition of vents
11.2.1Dimensions of the Vent
The vents connect the inside of the mold to the outside the mold. The viscosity of
the plastic must be high enough to prevent it from flowing out of the mold through
the vent. Figure 11.6 shows the cross section of the mold with the vent area. The
relieved section that is closest to the cavity steel is the primary vent. The dimen-
sions of the primary vent are the most critical. First, the vent depth should be such
that it provides evacuation of air but prevents leaking of plastic material through
the vent. Vent depths are discussed in detail in the next section. Second, the length
of the vent land should not cause a pressure drop, preventing air from being
pushed out, nor should it be so short that the plastic finds its way out to the secon
-
dar
y vent. Typical land lengths should range from 1.2 to 1.5
mm (0.060 t
o 0.080 in),
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 323 (page 323)

29911.2 Venting
assuming the vent depth is designed correctly. The vent width should be at least
between 5 and 8
mm (0.200 in t
o 0.320 in) in size. On the high end, it can be as
wide as desired and in some cases it can run around the entire perimeter of the
part (ring vents).
The secondary vents are also called vent reliefs. The dimensions of the secondary
vents are larger than the primary vent and therefore provide easy transport of
the air inside the mold out to the atmosphere. Secondary vents should be approx.
0.25
mm
(0.010
in).
In all cases, the vents must be well polished to avoid any
build-up of residue caused by the gases. The vents must also be draw polished in
the direction of air flow. If the path of the air to the atmosphere is long, another
step in the vents must be considered. The additional step could be as deep as
0.6
mm (0.025 in). These t
ertiary vents help in reducing the pressure drop and
should also be draw polished in the direction of air flow.
Figure 11.6 Details of the vent section
11.2.2Primary Vent Depths
Vent depths depend on the viscosity of the plastic at processing temperatures and
therefore differ from plastic to plastic. Typically, the material manufacturer will
provide recommendations regarding vent depths. For example, the recommended
vent size for ABS is 0.05 mm (0.002
in). Mold mak
ers typically follow these recom-
mendations when building an injection mold and tend to stay at the lower end of
the recommendation to avoid flashing of the mold. If the plastic is able to enter the
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 324 (page 324)

300 11  Role of Mold Cooling, Venting, and Regrind in Process Development
vent, this indicates that the vent is too deep and that it must be corrected. This in-
volves welding and repairing the surface. To avoid this, mold makers are conserv -
ative and leave the vent depth steel safe. It has always been thought that it is the
viscosity of the plastic that is the only factor important when determining the size
of the vent. In a recent study it was found that the size of the vent depends not only
on the viscosity of the plastic but also on the thickness of the plastic section be-
hind the vent. To conduct this study, a special mold was constructed (see Figure
11.7). The test part produced by this mold was center-gated and had 18 tabs of
varying combinations of tab thicknesses and vent sizes, shown in Figure 11.8. The
center gate delivered the melt to each of the tabs at the same time. There were
three tab thicknesses: 0.125
in (3.175
mm), 0.0625
in (1.587 mm), and 0.0312
in
(0.792
mm) and six v
ent sizes: from 0.0005
in (0.0127
mm) t
o 0.0030
in
(0.0762
mm) in s
teps of 0.0005
in (0.0127
mm). Differ
ent materials were molded
and for each tab the minimum vent size that produced flash was recorded. The test
results indicated that it was the thickness of the tab that also played an important
role in determining the vent size. The thicker tab was able to accept larger vents
without flashing. For example, with an ABS material that was tested with a 0.125
in
t
ab, the vents flashed at 0.0030
in v
ent size. On the other hand, the vents for the
0.0312

in tab, flashed at 0.0020

in vent size, see also Figure 11.9.
Figure 11.7 Vented mold for studying vent sizes
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 325 (page 325)

30111.2 Venting
Tab
Figure 11.8 Test part molded with the vent test mold
75 µ
63 µ
50 µ
Figure 11.9 Graph showing the combination of tab thickness and vent depth where flash
begins to occur for ABS (medium flow)
As the plastic is forced into thinner sections, the plastic pressure increases, thus
forcing the plastic out of the primary vent. In thicker sections, the overall plastic
pressure is lower and therefore the vent sizes can be larger. The published vent
size value for ABS is 0.002
in (0.0508
mm), but t
he test results from the vented
mold showed that a vent size of 0.003
in (0.0762
mm) is accep
table. This value was
used on several molds successfully. Figure 11.10 shows the various tab/vent size
combinations that defined the start of noticeable flash in the vent. Tests on nylons
also showed surprising results. The published vent size value for nylons is 0.0005
to 0.0007
in (0.0127 t
o 0.017
mm), but f
or thicker sections, a vent size of close to
0.0015
in (0.038
mm) could be used. In all cases it is im
portant that proper pro-
cessing techniques were followed. This again makes a case for following scientific
molding procedures to establish robust processes.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 326 (page 326)

302 11  Role of Mold Cooling, Venting, and Regrind in Process Development
Figure 11.10 Tab/vent combinations showing no flash and evidence of flash
11.2.3Location of Vents
The most efficient location of a vent is at the end of fill of the part. As the plastic
flows into the cavity, it begins to push the air out and continues to displace the air
until the cavity is full of plastic. This means that the flow rate of the air leaving the
mold is equal to the flow rate of the plastic entering the mold. If there was only one
vent at the end of fill, the size of the vent would have to be equal to the size of the
gate. But if this was the case, the plastic would easily get out of the mold through
the vent during the pack and hold phase of the molding cycle. Because the vent
depths have to be substantially smaller, the required amount of cross sectional
vent area must be distributed across the mold. The area most accessible in the flow
path of the plastic is at the parting line of the mold. Therefore, the parting line
must be vented as much as possible. Once the cavity in the area of the parting line
is filled, the plastic now pushes the air to other areas of the mold. Any ejector pins,
core pins, cavity inserts, or cavity blocks in these areas should be used to help vent
the air out of the mold. For each of these components, vents must be added based
on the recommended vent depths. Ejector pins offer the most advantage, because
they are self-cleaning. The residue from the gasses released through the ejector
pin vents will get cleaned as the ejectors cycle back and forth during every cycle.
Using ejector pins for venting does build up residue elsewhere in the ejector box
and increases the frequency of maintenance. The vents on stationary components,
such as the core pins, can get plugged easily and may need frequent cleaning.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 327 (page 327)

30311.2 Venting
Sometimes a positive air blast during the ejection can help clean the vents. In re-
cent years, porous steel has become increasingly popular. For example, in deep
draw parts, where placing an ejector pin is not possible or not acceptable, the end
of fill areas are made of porous steel inserts that allow pressurized air to escape
from the cavity. These inserts do require frequent cleaning and therefore the molds
are typically built such that these inserts can be taken out of the mold while the
mold is still in the machine. The inserts are removed, cleaned, and put back into
the mold while it is still bolted into the molding machine. Using porous steels does
not allow for mirror finishes or high polish surfaces.
One area of the mold that is often not given much consideration with respect to
venting is the runner. If the runner is not vented, the complete volume of air in the
sprue and runner enters the cavity through the gate of the part. This air burdens
the cavity vents with additional work. Runners must therefore be vented as much
as possible and even up to a depth where some flash can be seen. It does not really
matter if the runners exhibit some flash because the molded parts are of primary
interest. The sprue puller pin must also be vented. Often, at the end of the screw
recovery, the screw is sucked back without rotation to relieve any pressure on the
melt and prevent it from drooling from the nozzle tip. This causes air to be sucked
into the machine through the nozzle. Because the air is present in the heated noz-
zle with some of the plastic, there can be some build-up of gasses in the time after
screw recovery and before injection. During the start of injection, this air and gas
is injected into the mold. This is another reason that the runners must be vented.
Figure 11.11 shows a mold with possible vent locations on the parting line.
Runner
Cavity
Vents
Figure 11.11 Possible location of vents on the parting line
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 328 (page 328)

304 11  Role of Mold Cooling, Venting, and Regrind in Process Development
11.2.4Forced Venting or Vacuum Venting
In every mold there will be corners where air will get trapped. Because the volume
of the air may not be large, defects are not easily seen. Close examination will show
a rounded corner rather than a crisp corner. In other molded parts, shorts may be
easily seen with the naked eye. Placing ejector pins in these areas to provide vent-
ing may not always be possible. If the corner detail is important to the function of
the part, the only solution to eliminate the defect is to install vacuum in the mold.
The vacuum evacuates all air from the system before injection, so that all cavity
details fill with plastic, thus producing an acceptable part. Molds that need to be
fitted with vacuum have parting line vents in the cavity blocks that are relieved
into an outlet to which the vacuum line is attached. There is a seal around the cav-
ity inserts to prevent outside air from being sucked in. This seal is formed when
the mold is closed. Molds with slides and other contours are not good candidates
for adding vacuum vents, because their mold faces are not always flat. Adding the
seal may require additional real estate, increasing the size of the mold. The ejector
pins may also need seals to hold the vacuum. Cold runner molds have an open
sprue and will leak the vacuum. Although vacuum can be used successfully on
cold runner molds (by slight modification of the process), valve gate molds and hot
runner molds are better candidates for vacuum assist. In many cases, vacuum is
added after several attempts of adding conventional vents have failed to produce
acceptable parts. By then, all the ejector pins and/or core pins are vented and the
parting lines, cavity blocks, and slides have been relived to the atmosphere. Addi-
tional work may now be required to fix these so-called leaks in the molds. Venting
must therefore be considered at the mold design stage and the product designer
must clearly specify the requirements on the part print. Figure 11.12 shows a
mold configured for of vacuum venting.
Runner
Cavity
Vent
groove
Vacuum
port
Vacuum
seal
Mold
Figure 11.12 Venting using vacuum
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 329 (page 329)

30511.3 Regrind
 11.3  Regrind
In injection molding manufacturing processes, runners that fall out of the mold or
parts that are found defective can be ground up for reuse. This material is called
regrind. Regrind material is generated from plastic that comes with at least one
heat history cycle at the processing facility. Materials supplied by the resin sup-
plier are classified as virgin materials, even though they may have gone through a
melt processing process for compounding of additives such as fillers or colors.
Regrind material is traded either directly or through third parties between compa-
nies that cannot use regrind material, such as companies manufacturing medical
applications and those companies that produce certain consumer products, such
as garden equipment or trash carrying equipment, who can use some amount of
regrind and still manufacture products within their product requirements. Park
benches are an example for a product where 100 % regrind material is used.
11.3.1Effect of the Molding Process on the Part Properties
The molding process has been redefined as the collection of all the processes the
plastic is subjected to from the moment it enters the manufacturing facility as
loose pellets to the point when it leaves the facility as a finished molded product.
The process can be broken down into the drying, melting, mold filling, cooling, and
the final packaging of the part. Each phase of the process can affect the plastic, the
additives in the plastic, and the fillers. During the drying process there is no break-
down in the molecular weight of the plastic. However, as discussed in Chapter 4,
exposure of the material to excessive drying times can cause a loss or breakdown
of the additives. Drying times in some resins are cumulative. If the lost additives
happen to be those that contribute to the heat stability of the melt, then the plastic
molecules will break down during melt processing. Fillers are not affected by ex-
cessive drying times.
During the melting phase, the plastic is transformed from pellet to melt in the in-
jection barrel. The plastic is subjected to heat from the heater bands and through
shear from the rotating screw. The plastic material may contain fibrous or non-fi-
brous fillers. There are other additives, such as plasticizers, heat stabilizers, and a
variety of other materials that are compounded into the material as it moves
through the barrel. The heat from the heater bands and the shear from the rotating
screw will cause the polymer molecules to break down and it is the extent of this
breakdown that must be considered. Processing the plastic at the high end of the
recommended melt temperature can be increasingly more detrimental to the mo-
lecular weight of the plastic because the plastic is now subjected to higher temper-
atures where the allowable residence time may not be large. Having the screw
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 330 (page 330)

306 11  Role of Mold Cooling, Venting, and Regrind in Process Development
speed set at a high value can also increase the shear rate, again contributing to the
breakdown of the molecules. High screw speeds can create large mechanical forces
breaking down the fibers, while non-fibrous fillers may not be as affected.
During the mold filling phase, the material passes through the nozzle, the sprue,
the runners, the gates, and into the cavity and finally reaches the end of fill. Dur -
ing this filling phase, the material is subjected to high shear forces, causing a
breakdown in the plastic molecules. The fillers may not be impacted, unless the
gate sizes are small. Shear is higher in smaller diameter runners and therefore
smaller runners cause larger drops in molecular weight. Large tab gates offer the
least amount of molecular weight decrease through the gates. The part geometry
can also play a role in the degradation of the plastic. Thinner cross sections in-
crease the shear and therefore increase the chance of plastic degradation. Insuffi-
cient venting in the mold can cause a dieseling effect and burn the plastic which in
turn lowers the molecular weight. This may be difficult to observe on dark color
parts.
The discussion above shows that each phase of the process has an effect on the
molecular weight of the plastic and the integrity of the fillers. If any one of these
processes is not controlled properly, it is easy to degrade the plastic. In many cases,
plastic degradation or filler breakdown may not be cosmetically noticeable, making
it easy to assume that the process was acceptable.
The generation number for a quantity of regrind is defined as the number of times
the regrind has been generated from the same batch of plastic. For example, if a
runner was ground up to be used back into the process, it is considered as first
generation regrind. When the regrind is reprocessed back into the machine and
regrind is generated from the molded runner, then this regrind is called second
generation regrind. With each progressive generation, there is a deterioration of
the plastic properties.
When regrinding, the runner or the parts are reduced to a size close to the virgin
plastic pellets with the help of a granulator (grinder). Because of the random me-
chanical breakdown of the plastic, the particle size distribution ranges from fines
to coarse particles. Low rpm grinders are best suited to achieve a narrow particle
size distribution. A large amount of fines can cause two problems: First, due to a
lack of mass, the fines melt immediately and stick to the feed section of the screw,
causing inconsistent screw recovery. Second, these fines tend to degrade much
faster, causing defects in the part. Fines must therefore be removed before they
enter the feed throat. This is done with fine separators also called cyclone separa-
tors. In addition, regrind pellet size must be close to the virgin pellet size to achieve
consistent mixing and feeding of material that contains regrind.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 331 (page 331)

30711.3 Regrind
11.3.2Using Regrind
It is clear that using regrind can cause a varying degree of loss in material proper-
ties. Therefore, the amount of regrind that can be used in a product will depend on
how this loss affects the performance of the final product. It is impossible to pro-
vide general hard and fast rules or equations to calculate the acceptable amount of
regrind that can be used in a part. The only reliable method is to experiment with
varying percentages of regrind and different generations of regrind. A good
s
tarting point may be to run the product with 100 % first generation regrind and
perform functional testing on the parts. Surprisingly, on some products this may
be completely acceptable. If the initial process was carefully controlled and if the
molding process was developed using scientific molding principles with large pro-
cess windows, the material properties may stay well within the required specifica-
tions. If the 100 % product is unacceptable, various ratios of virgin to regrind must
be evaluated. When testing the product, the properties that are important to the
product must be evaluated. Testing of the product in its final assembly and service
environment is critical. Lab results from tensile or impact testing can only provide
a comparison of the property, but product testing results will provide the actual
value. The testing procedures must be standardized and should be used in regular
production. An acceptable part can also be used to create a standard which all
products can be compared to or checked against to determine their acceptability.
11.3.3Batch and Continuous Processes of Incorporating Regrind
There are two methods of incorporating regrind into the product. In the batch pro-
cess, the regrind is generated offline, away from the molding machine. A predeter-
mined amount of regrind is either blended with the virgin material and loaded into
the machine hopper, or the regrind and virgin material are blended together at the
molding machine hopper, using blending equipment. In this system, the regrind
will have to go through the drying process together with the virgin plastic. Blend-
ing equipment based on weight (gravimetric blenders) is most reliable. Some sys-
tems rely on loading time of virgin plastic and regrind to achieve the right percent-
age. For example, to achieve an 80 : 20 blend the virgin plastic is fed into the system
for 80 seconds and the regrind for 20 seconds. This system is not reliable because
time does not equate to weight considering the possible differences in the bulk
densities of the virgin plastic and regrind. If the plastic gaylord or container, which
feeds the hopper, runs out of material, it may only be loading either the virgin or
the possible worst case, only regrind. Gravimetric feeders look for a particular
amount by weight of the virgin and regrind before delivering the mixture to the
molding machine. If one of the components is not available, either the blending
equipment or the molding machine will set off an alarm for lack of material. Blend-
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 332 (page 332)

308 11  Role of Mold Cooling, Venting, and Regrind in Process Development
ing equipment is also physically mixing virgin material and regrind before deliver-
ing it into the hopper of the molding machine. Systems that rely on time may end
up having layers of virgin and regrind in the hopper because they alternately de-
liver each component for the specified length of time to the hopper of the molding
machine.
In a batch process, the chances of contamination are very high and this is probably
the main reason why regrind projects often are not successful. It is easy for two
runners of the same color but of different materials to be thrown into the same
grinder. Contamination can show up right away when the barrel is being purged
for molding. If the contaminant melts at a relatively lower temperature but is now
subjected to a higher temperature, it can easily start gassing or spurting. It may
also show up as splay or other cosmetic defects. If the contaminant is a higher
melting plastic, there is a possibility of it getting stuck in gates and hot tips or it
may show up as unmelted pellets in the part if the gate sizes are large. In both
cases, delamination, structural integrity or other issues can be the result and the
part quality will suffer.
With a continuous process of regrind incorporation, the runners are picked up
with the help of a sprue picker or robot and directly dumped into a granulator; the
grinder grinds up the runner and delivers the regrind to the hopper immediately.
The runners are not separated in a separate area to be mixed later, such as in the
batch process. The continuous process is a cleaner way of incorporating the regrind
with almost no chances of contamination. The disadvantage here is that some mol-
ecules have gone through the process multiple times because this is a continuous
process and the runner is always recycled. It is impossible to figure out the gener-
ation of the regrind, because it is all one homogeneous mixture. The smaller the
ratio of part to runner weight, the greater is the percentage of older generation
regrind present in the system. Continuous processes are suitable for parts that are
able to accept a large percentage of regrind and that have a larger ratio of part to
runner weight. The smaller the runner, the lower is the amount of regrind and
therefore the fewer are the chances of processing problems or product failure. If
the runner is directly fed back to the feed throat, in most cases drying is not re-
quired, eliminating the risk of additive loss caused by the drying process.
11.3.4Estimating the Amount of Regrind from Different Generations
Consider a part to runner weight ratio of 80 : 20. Assuming the whole runner is
incorporated back into the plastic, the percentage of each generation of regrind
present at each pass of molding is shown in Table 11.1. The concept of generation
at each pass may seem confusing. First generation regrind during pass four will be
the regrind generated from the virgin material from pass three. It will not be
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 333 (page 333)

30911.3 Regrind
regrind generated during pass one. The regrind generated during pass one be-
comes third generation regrind. Because part and runner are molded in the same
shot, the percentage of regrind will be the same in the runner and in the part.
It is a common perception that as the number of passes increases, the material
starts to deteriorate very fast. This is true in cases where the part to runner weight
ratio is high; for example the runner weight is 75
g
rams and the part weight is
25
g
rams. In the above example, where the part to runner ratio is 80 : 20, Table
11.1 shows that there is always 64
g or 80 % of virgin mat
erial in the part,
12.8
g
rams of 1st generation regrind, 2.56
g
rams of 2nd generation regrind and so
on. If a disciplined approach has been taken to dry the plastic and process the ma-
terial, the properties of the plastic may well be within the required specifications.
This will be true with filled or unfilled plastics and in most cases this should be
acceptable. If the part design was not robust, it is possible that the small decrease
in the properties would result in the failure of the part.
Table 11.1 Percentage of g Generation Regrind after p Number of Passes for a Part to Runner,
Ratio of 80 : 20
Regrind genera-
tion number (g)
Pass (p)
1 2 3 4 5
0 (Virgin) 100 80.00 80.00 80.00 80.00
1 – 20.00 16.00 16.00 16.00
2 – –  4.00  3.20  3.20
3 – – –  0.80  0.64
4 – – – –  0.16
Total 100 100 100 100 100
Table 11.2 Weight of g Generation of Regrind after p Number of Passes in an 80 g part with a
20

g runner
Regrind
g
eneration (g)
Pass (p)
1 2 3 4 5
0 (Virgin) 80 64.00 64.00 64.00 64.00
1 – 16.00 12.80 12.80 12.80
2 – –  3.20  2.56  2.56
3 – – –  0.64  0.51
4 – – – –  0.13
Total 80 80 80 80 80
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 334 (page 334)

310 11  Role of Mold Cooling, Venting, and Regrind in Process Development
Table 11.3 Weight of g Generation of Regrind after p Number of Passes in a 20 g Runner of a
80

g Part
Regrind
g
eneration (g)
Pass (p)
1 2 3 4 5
0 (Virgin) 20.00 16.00 16.00 16.00 16.00
1 –  4.00  3.20  3.20  3.20
2 – –  0.80  0.64  0.64
3 – – –  0.16  0.13
4 – – – –  0.03
Total 20 20 20 20 20
The following formula can be used to estimate the percentage of regrind from each
generation in a part:
(1) If , then
(2) If , then
()
()
pg R
pg R x
−< =
−= = 





10
1 100
 












−> = 





g
pg R x
100
1 100(3) If , then ()  
 −


















g
x1 100 100
(11.2)
wit
h
x = percentage weight of the runner
g = generation of the regrind
p = molding pass number
R = percentage of regrind
Example
Part weight = 35 g, runner weight = 7 g
therefore,
x = +







×=7
73 5 100 16 67.
.
In the 4 th pass (p = 5), the amount of 3 rd generation regrind (g = 3) can be deter -
mined with (p – g) = (5 – 3) = 2 > 1 as
R = ((16.67 / 100)3 (1 – (16.67 / 100))100 = 0.39 %
Regrind tables for various runner ratios are given in Appendix G.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 335 (page 335)

31111.3 Regrind
11.3.5Effect of Regrind on Processing
Regrind can have lower molecular weight, degraded additives and/or their byprod-
ucts, damaged or destroyed fillers, and contaminants. Depending on the extent of
these changes it may be necessary to change the process to compensate for some
of the changes in the outputs and make acceptable parts. A decrease in molecular
weight will cause a drop in viscosity of the plastic, affecting all the outputs related
to viscosity. Fill times and cushion values will be lower. If part of a processing aid
or a viscosity reducer was lost, it is possible that the fill times and cushion values
will be higher. If the filler was fibrous, the breakdown of the fiber length will cause
the plastic to flow easier, resulting in shorter fill times and lower cushion values.
Lower viscosity can also lead to an increase in plastic cavity pressure, although the
pressure behind the screw remains unchanged. Excessive amounts of decrease in
molecular weight can cause the plastic to degrade easier, causing excessive gas-
sing and plugging of the vents. Cosmetic defects such as splay can occur. These
effects can be compensated for by changing some of the process parameters. For
example, reducing melt temperature will increase the viscosity of the plastic or
reduce the gassing that occurs. In all cases, it is important that the process be
r
obust and more importantly be redeveloped based on the presence of regrind.
11.3.6Closing Remarks
Using regrind is a good and effective way to save money and at the same time pro-
tecting the environment from waste plastic being dumped into landfills. However,
many processors tend to switch back to virgin resin as soon as they detect a quality
problem. Often the quality issue is fixed and the processors are hesitant to go back
to using regrind because they identify the cause of the problem being the regrind.
Although this could be true, the reason why the regrind was causing the problem
must be investigated. Sometimes the regrind is not properly dried or there may be
too many fines from the regrind process that could have caused the problem. A
proper analysis of the amount of regrind and a procedure to incorporate it into the
molding process are two very important steps that must be followed. The imple-
mentation plan can be pursued as far back as in the part design stage. A part de-
signed to be molded from virgin plastic can be overdesigned to compensate for the
loss of properties when regrind is used. Using regrind should be part of the pro-
duction plan and as seen in the above 80 : 20 example, the part will always contain
92.8 % of virgin and first generation regrind resin and should therefore be able to
function satisfactorily. Most companies that are not successful in implementing a
regrind program fail because of lack of discipline and training of the shop floor
personnel. For example, the operators who assist in grinding the runners need to
be educated about the different types of plastics and that every clear runner in the
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 336 (page 336)

312 11  Role of Mold Cooling, Venting, and Regrind in Process Development
molding facility is not necessarily the same material. Instituting a regrind pro-
gram requires discipline and is a culture change.
Suggested Reading
Osswald, T. A., Turng, L., and Gramann, P. J., Injection Molding Handbook (2007) Hanser, Munich
Beaumont, J. P., Nagel, R., and Sherman R., Successful Injection Molding (2002) Hanser, Munich
Rosato, D. V. and Rosato D.V, Injection Molding Handbook (2000) CBS, New Delhi, India
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 337 (page 337)

Related Technologies
and Topics
This chapter will introduce a variety of technologies and techniques that can be
applied to enhance the robustness of a process and/or to speed up the complete
project from conceptualizing the part to its release as a molded product. Cavity
pressure technology, which takes process monitoring and control to a completely
new level, increasing product quality and plant efficiency many fold, will be intro-
duced. Companies can build a knowledge base of their experiences to apply to fu-
ture projects based on their past experiences. Concurrent engineering is an exten-
sion of the teamwork concept, keeping the whole team involved with the decisions
and progress of the project.
 12.1  Cavity Pressure Sensing Technology
When we discussed processing in the previous chapters, everything has all been
related to the molding machine. For example, process optimization dealt with opti-
mizing the processing parameters, such as injection speed and holding pressure.
However, the part is finally made inside the mold, and therefore knowledge of what
happens inside the mold can give the most valuable information about the quality
of the part. The molten plastic will follow the specific volume–temperature graph
(Figure 2.10) that dictates the part quality. Tracing this information for every shot
will reflect the quality of the part. Needless to say, if every shot follows the same
curve each time, all shot will be identical. Although it is not easy to output a spe-
cific volume–temperature graph for the mold, there are other indirect methods.
Placing a pressure transducer inside a mold can provide information about the
melt pressure in the mold and as the melt starts to cool, the pressure decrease can
be plotted. Temperature transducers inside the mold will provide information on
the temperature of the plastic. Although the “transducer” is technically the right
term, the term sensor is most commonly used and we shall adopt that terminology
in this text.
12
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 338 (page 338)

314 12  Related Technologies and Topics
12.1.1Sensors and Output graphs
Figure 12.1 shows the placement of a ‘Near the Gate Sensor’ and an ‘End of Fill
Sensor’ in a mold. A typical cavity pressure graph is shown in Figure 12.2. The
graph also identifies the injection, holding, and cooling phases. There are three
pressure traces in the figure that will be described in the following:
Hydraulic Pressure Curve: To measure hydraulic pressure, the sensor is placed in
the hydraulic line. Since the injection phase is a fast dynamic phase, the pressure
increases very rapidly until the start of the holding phase is reached. Once the
switch-over from injection to holding takes place, the pressure drops to the holding
pressure value and stays constant until the end of the holding time. After the hold-
ing time is complete, the hydraulic pressure drops to zero. If the screw rotation
starts immediately, the back pressure shows up right after the end of the holding
phase. If there is a delay, the trace picks back up indicating the back pressure for
the screw recovery time.
Plastic Pressure
and Temperature
in the Barrel
Ri = 10
Injection
Cylinder Pressure
Injection Speed
Control
Pump
Pressure
From
Hydraulic
Power Unit
Screw
Travel
Runner Pressure
Pressure at Gate
Near the Gate Sensor
Pressure at end of cavity
End of fill sensor
Figure 12.1 Schematic of placement of sensors inside a mold (Courtesy: RJG Inc.)
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 339 (page 339)

31512.1 Cavity Pressure Sensing Technology
Inject
Pressure (PSI)
Pack & Hold
Hydraulic pressure
Cavity pressure at gate
Cavity pressure
at end of fill
Back
pressure
Cooling
Time (seconds)
Figure 12.2 Typical representation of a cavity pressure graph
Cavity Pressure Curve Near the Gate: As the plastic begins to enter the mold and the
cavity, it is in contact with the sensor placed just behind the gate. The pressure
increases until the injection phase is complete, but does not drop down like the
hydraulic pressure, because the cavity is pressurized and the gate is frozen or
closed. The decrease in melt pressure is caused by the shrinkage taking place in-
side the mold and it causes the plastic to move away from the mold wall and the
sensor. The start of the curve has a delay which is equal to the time the plastic
takes to reach the sensor from the start of injection.
The Cavity Pressure Curve at the End of Fill: This curve looks similar to the curve
described above, the only difference being the starting point of the curve. Here, the
starting point represents the time the plastic requires to reach the end of fill. If the
process is decoupled (see Section 7.5.4), this time is almost equal to the injection
fill time.
12.1.2Types and Classification of Pressure Sensors
There are various types of sensors used in plastics processing. Their classification
is based on the type of technology used to collect information.
Strain Gage Sensors: The underlying principle of a strain gage is based on the
Wheatstone bridge that has a network of resistance elements. The electric current
flowing through this network is measured. When any external force is applied to
the strain gage, the amount of current changes. This change in the amount of the
current is proportional to the applied force and hence the amount of force can be
determined.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 340 (page 340)

316 12  Related Technologies and Topics
Quartz-Based Sensors (Piezoelectric Sensors): Some materials, such as quartz,
g
enerate an electrical potential when an external stress is applied. The electrical
potential is directly proportional to the applied force. A quartz-based sensor can
therefore measure the force applied on the face of the sensor.
Another type of sensor classification is based on the location of the sensor in the
mold.
Direct Sensor: These are also called flush mount sensors, see Figure 12.3. Here, the
sensor face forms part of the cavity wall. The sensor is fitted such that it comes in
contact with the molten plastic and measures the pressure. Such sensors are not
commonly used because it is not always possible to get the sensor inside the mold
cavity. It can also be a risky task to work inside the cavity to fit the sensor. The
cavity wall would need rework if damaged. Some molds are subject to high temper-
atures and this could also pose a problem because pressure sensors may not with-
stand high temperatures.
Figure 12.3(a) Flush mount sensor (Courtesy: RJG Inc.)
Cavity Surface
Flush Mount Sensor
Mold
Retaining Nut
Sensor Cable
Retaining Plate
Figure 12.3(b) Flush mount sensor (Courtesy: RJG Inc.)
Indirect Sensors: When a sensor is placed underneath an ejector pin or a core pin,
it is called an indirect sensor. The force is applied on the face of the pin and trans-
ferred to the base of the pin where the sensor is located, see Figure 12.4. These
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 341 (page 341)

31712.1 Cavity Pressure Sensing Technology
sensors are more common because there is room to work with inside the ejector
box where the sensor has to be fitted.
Counterbore
for Ejector Pin
Sensor
Pocket
Ejector Plate
Ejector Pin or
Dummy Pin
Ejector
Retainer
Plate
Chamfer
Cavity Surface
Ejector Pin
Button Sensor
Figure 12.4 Button sensor behind an ejector pin (Courtesy: RJG)
Yet another type of classification of the sensors is based on the function the sensor
will perform in the mold.
Control Sensors help control the process (which will be described in the following).
Monitor Sensors are used for monitoring the process. Process alarm limits can be
set based on the information acquired from this sensor.
12.1.3Use of Information from the Pressure Graphs
The information obtained from the pressure graphs is valuable in a number of ways.
 The pr
essure graphs that are traced provide information about the cavity pres-
sure and therefore the part quality based on the specific volume−temperature
relationship.
 Inconsis
tencies from shot to shot can be observed. If the pressure traces do not
repeat, the part quality is not repeated, see Figure 12.5. It can be observed that
the hydraulic curve overlays itself every shot, proving the hydraulic pressure
is consistent. However, the plastic pressure curves are not being duplicated. If
there was no cavity pressure hookup, one would automatically assume that the
process is consistent and that the part quality should also be consistent from
shot to shot. A leaking check ring can cause such a variation and can only be
noticed with a cavity pressure sensor.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 342 (page 342)

318 12  Related Technologies and Topics
Figure 12.5 Repeatable hydraulic curve with varying cavity pressure showing inconsistency
in part quality (Courtesy: RJG Inc.)
 If t here are sensors present in each cavity, the quality of each cavity can be com-
pared, see Figure 12.6. In this example, there are four cavities and the traces for
each cavity are different. Based on the specific volume–temperature curve, each
cavity will produce different parts. Although there is consistency within a cavity,
there is cavity-to-cavity inconsistency.
Figure 12.6 Cavity pressure variations between cavities showing cavity-to-cavity inconsist-
ency, note that cavity 11 has the greatest variation, ranging from well-packed to nearly short
(Courtesy: RJG Inc.)
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 343 (page 343)

31912.1 Cavity Pressure Sensing Technology
 The ca vity pressure graph can also provide gate seal information. If the gate is
not sealed, the plastic will leak out of the cavity, causing a sudden drop in cavity
pressure. The curve will therefore show a sudden change in its slope. A frozen
gate will show as a gradual drop in cavity pressure rather than a sudden change
in slope, see Figure 12.7.
 If t
he sensor is at the end of fill, a short shot will result in a ‘zero’ value for the
pressure. This can be used to detect short shots and contain the parts. Usually, a
signal is sent to a robot to reject the parts or sent to a conveyor to reverse and
reject the parts.
Figure 12.7 Cavity pressure curve showing the status of gate freeze (Courtesy: RJG Inc.)
12.1.4Controlling the Process with Cavity Pressure Sensors
A decoupled process is the most efficient and consistent method of molding. The
switch-over from the injection phase to the holding phase can be initiated by mon-
itoring one of the following parameters: hydraulic pressure, time, or screw posi-
tion. The most common and consistent method used is the screw position. When
the screw reaches a preset position, it transfers to the holding phase. The screw
position controls the percentage of the volume filled and, when using decoupled
molding (see Section 7.5.4), this percentage should be between 95 and 98 %. In re-
sponse to the injection phase there is an increase in the cavity pressure and then
a slow decrease. Figures 12.8 through 12.11 show the various cycle integrals.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 344 (page 344)

320 12  Related Technologies and Topics
Inject
Pressure (psi)
Pack & hold
Hydraulic pressure
Hydraulic ‘fill only’ integral
Time (s)0
Figure 12.8 Shaded area representing the hydraulic ‘fill only’ integral
Inject
Pressure (psi)
Pack & hold Cooling
Hydraulic pressure integral
Time (s)0
Figure 12.9 Shaded area representing the hydraulic integral
Inject
Pressure (psi)
Pack & hold Cooling
Hydraulic pressure integral
Time (s)0
Figure 12.10 Shaded area representing the post-gate cavity pressure integral
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 345 (page 345)

32112.1 Cavity Pressure Sensing Technology
Inject
Pressure (psi)
Pack & hold Cooling
Hydraulic pressure integral
Time (s)0
Figure 12.11 Shaded area representing the end-of-fill cavity pressure integral
Peak pressure, time to the peak pressure, and the area under the curve before the
peak pressure (shaded area) represent the injection phase. Therefore, if this is
duplicat
ed every shot, the fill is duplicated every shot. If the information from the
sensor can be fed back to the machine and if the switch-over is now controlled
using a v
alue on the graph (usually the peak pressure), the switch-over for every
shot will take place at the precise fill amount of the cavity, resulting in shot-to-shot
consistency. Injection will always be ended when the desired pressure is reached
in the cavity. This is called process control using cavity pressure sensors. Other
than process consistency, the other advantage lies in the fact that the process is
now machine-independent. If the same curve is repeated on another machine, the
part quality will be the same. Controlling the process using pressure sensors leads
to the most consistent process.
12.1.5Sensor Locations
Sensor locations are important because the location will dictate the amount and
quality of the information it will acquire. Preferably, sensors to control the process
must be located near the start of the fill (in the first third of the part) and the sen-
sors to monitor the process should be near the end of the fill, in the last third of the
part. For extremely small parts, a sensor can be located in the runner. The compro-
mise here is that real gate seal information is not available because it can be ob-
tained only from the pressure traces in the cavity. Table 12.1 shows the benefits of
certain types of sensors and their locations (direct or indirect).
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 346 (page 346)

322 12  Related Technologies and Topics
Table 12.1 Comparative Benefits of Types of Sensors and Technology (Courtesy: RJG Inc.)
Types of sensors and technology
Flush mount
(direct)
Under the
pin (indirect)
Piezoelectric Strain gauge
Accuracy of data Yes Yes Yes Yes
Ease of calibration/configuration Yes Yes
Location flexibility Yes
Lower installation cost Yes
Easier replacement Yes
Removable cables Yes
Limited mold space Yes Yes*
High temperature Yes
Easy troubleshooting Yes** Yes
Use with long cycles Yes
Lower costs Yes
* Smaller connector
** Easier removal
 12.2  Building a Knowledge Base
Many molding companies try to find and dominate a niche in the market. For ex-
ample, a molder may be known to be an expert in molding gears with high preci-
sion while another may be an expert in two-shot molding. Companies reach these
levels of expertise having perfected the technologies over a number of years. The
collected knowledge comes from a pool of experience, trial and errors, and applied
science. This knowledge and solutions to the problems should be recorded to make
future projects efficient during project development, the release to production pro-
cess, and finally in production. For example, consider a company that molds con-
nectors of various types, primarily from nylons and polyesters. Over the years they
may have built hundreds of tools for similar types of connectors. There may be a
commonality in the shape of the connectors, the gate locations and sizes, cooling
channel locations, wall thicknesses, and so on. If the scientific processing princi-
ples are followed, the processing parameters would also end up being very similar.
For example, the mold and melt temperatures or the plastic pressures in the cavi-
ties can be very similar for parts being molded from the same materials. Similar
processing parameters will lead to similar shrinkage values. This can be verified
by taking the steel dimension and comparing it with the part dimension. If the
cavity steel for a number of molds and their respective molded parts are measured,
a database can be built and a simple formula or a trend graph can be developed.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 347 (page 347)

32312.2 Building a Knowledge Base
When a new similar project comes in, this database can then provide a better esti-
mate of the shrink values that can be used when designing the mold. This tech-
nique can be very useful when designing components that are difficult to make
and when mold dimensions cannot be kept steel-safe. A threaded insert is a good
example of this type of component. A 16-cavity threaded core insert would be very
expensive to rework, if the final thread size on the molded part was not within
specifications and not within the required capability. Here, prior knowledge of a
similar mold would come in very useful. If the plastic flow is similar in an existing
mold compared to a new mold, the molecular orientations can be similar, leading to
similar shrinkage values. If the process using the existing mold was robust, using
similar parameters will lead to a robust process in the new mold. Again, the part
quality becomes predictable. In referring to the threaded part mentioned earlier,
determining the size of the cores can be done with a higher confidence level.
Alt
hough shrinkage can be estimated with the help of simulation programs, the
data acquired by modeling is rarely accurate, because of the basic assumptions
that go into building the software algorithms. For example, a software program will
assume perfect venting and perfect packing of the parts, although in practical
molding this is never the case. Building a knowledge database for similar products
eliminates the need for assumptions and at the same time takes into account all
common factors, making the estimation more reliable. It is important to keep the
steel safe and to start the mold dimensional modifications only after the first mold
trial where a robust process was developed.
Figure 12.12 Knowledge worksheet
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 348 (page 348)

324 12  Related Technologies and Topics
Building a knowledge base helps taking the guess work out and reducing the num-
ber of iterations to the final product release to manufacturing. This saves time and
money, making the overall process efficient. An example of a summary sheet is
shown in Figure 12.12. The data can also be used to build a second mold for an iden-
tical part, especially when in the first mold some of the required part dimensions
were unattainable, possibly because of the cost or time of modification or of making
new mold components. In such cases, the mold design can be reverse-engineered
and the parts in the new mold can be molded within the required specifications.
 12.3  Concur rent Engineering in
Injection Molding
A molding company usually receives a new project request through the sales de-
partment. The sales department then asks the engineering department about the
feasibility of the molding. Once the job is accepted, the tooling department gets
involved. They design the mold and help building the mold through the mold
maker. The mold is then mounted on the machine and the expectation is that the
process engineer can mold acceptable parts in the first attempt. Unfortunately,
molding the parts successfully in the first attempt is not common, because the
process, although having followed a logical sequence, did not involve all depart-
ments in the appropriate sequence of the decision making process, leading to cer -
tain failures. Many mistakes are often discovered during the first trial of the mold.
‘They should have done it this way’ or ‘The parts will never fall off the mold’ are
typical comments during the first trial of the mold. This could have been avoided,
if all departments were made aware of the project and its requirements before the
mold was built. ‘Over the wall engineering’ is a term used to describe the project
activity where each department is disconnected from each other. Each department
performs the activities requested by the previous one and passes the project on to
the next (Figure 12.13).
‘Concurrent Engineering’ involves representatives from every department in the
project at the earliest stage (Figure 12.14). This should be followed by subsequent
meetings, where the project details and any changes should be reviewed by the
team to evaluate the impact a change may have on their own individual depart-
ments. Therefore, when the product designer mentions that the material is, for
example, a long fiber thermoplastic (LFT), the process engineer knows, he will
need a different screw and nozzle tip, or the scheduler knows that he will need to
schedule time on the one specific machine in the shop with the required special
screw. Raising a red flag at this stage saves time and money and delivers the prod-
uct on time. Although conventional ‘Over the Wall’ approaches are commonplace
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 349 (page 349)

32512.3 Concurrent Engineering in Injection Molding
in most companies, disengaging each department is a common cause of failures,
inefficiencies, and delayed launch of the product.
Figure 12.13 Over the wall engineering – departments are disconnected from each other
The concept is further explained in the matrix in Table 12.2. The first column is a
typical list of departments involved in the design and manufacture of a product.
The first row describes the activities involved. A ‘Yes’ at the intersection of a row
and a column means that the particular activity has an impact on that department.
For example, for the process engineer, the mold design is very important, while for
the quality department, the mold design has no direct impact. Please note that this
is a universal matrix and there will be exceptions. This matrix should be used as a
guideline to set up individual company matrices.
Figure 12.14 Concurrent engineering
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 350 (page 350)

326 12  Related Technologies and Topics
Table 12.2 Suggested Personnel – Activity Chart for Implementing Concurrent Engineering
Job
function
A ctivity
Product
design
Material
selection
Mold
design
Mold
cons
truc-
tion
Machine
selection
Process
develop-
ment
Quality
require-
ments
Product
designer
Yes Yes No No No Yes Yes
Tooling
engineer
Yes No Yes Yes No Yes Yes
Mold
maker
No No Yes Yes No Yes No
Material
supplier
Yes Yes No No Yes Yes No
Process
engineer
Yes Yes Yes No Yes Yes Yes
Quality
engineer
No Yes No No No Yes Yes
Sales
team
No Yes No Yes No No Yes
12.3.1The Product Designer
Conventional Involvement: Product design is where the concept first takes shape
through a CAD model or a prototype. At this time, there is a general idea of what
the requirements for the plastic material are and therefore a selection may or may
not have taken place. The machine, the mold design, the molding process, or any of
the other factors are of no concern to the designer, who is focused on a functional
concept.
Required Involvement: A product designer should understand the manufacturing
process, especially the processing part of it. Design for manufacturability princi-
ples must be implemented. For example, the designer must be aware of the fact
that a thick section in a part must be cored out to reduce sink or sufficient draft
must be provided on the part to release the part from the mold. An explanation of
the function of the part to the molder and his team would be beneficial to the
molder. This way, the process engineer knows the particular material he needs to
process or can raise a flag when tolerances are impractical for a specific material.
12.3.2The Tooling Engineer
Once the product designer presented an acceptable design, the tooling engineer
gets involved in the design and the economics of building the mold. Of all job
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 351 (page 351)

32712.3 Concurrent Engineering in Injection Molding
functions, the tooling engineer is probably the one who is most involved in the
project because his direct involvement is required at the various stages.
Conventional Involvement: The tooling engineer is usually the liaison between the
mold maker and the molder. His job is to deliver the mold to the molder and fix any
issues the molder discovers during processing. Any design changes to the parts –
features and/or dimensions – need to be reflected in the mold and the tooling engi-
neer is responsible for these changes.
Concurrent Requirement: A tooling engineer must understand the concepts of de-
veloping a robust process. The techniques and the benefits of Scientific Processing
should be familiar to him. The tools must be qualified using these techniques and
changes to the mold must be made to support a robust process. For example, iden-
tifying a process window is extremely important. The tooling engineer must closely
work with the process engineer, the quality engineer, and the mold maker.
12.3.3The Mold Designer and Mold Maker
Most mold makers work with their own mold designers. They are given the part
model and design the mold accordingly.
Conventional Involvement: The mold designer receives the design from the part de-
signer, designs the mold for the chosen number of cavities and the mold maker
fabricates the mold. He knows the type of material that will be used for molding
the part, but sometimes the details are not made available to him.
Concurrent Involvement: The mold designer and the mold maker must get in touch
with the material supplier to get information before designing the runners, gates,
and vents. For example, it makes a big difference whether a 30 % glass filled
mat
erial or a 30 % long fiber glass filled material is used. Apart from this, the mold
design must be reviewed between the part designer, the mold designer, the mold
maker and the process engineer. When the first shots are produced the mold maker
must be present to see how the mold functions. The mold maker must also under -
stand the concepts of Scientific Processing and why a process window is important.
12.3.4The Material Supplier
In most cases, the material suppliers sell the resin but do not get involved, unless
there is a processing issue. Since they are the suppliers of the materials they have
all the information such as data sheets, processing information, mold design require-
ments, part design requirements and are therefore the best source of information.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 352 (page 352)

328 12  Related Technologies and Topics
Conventional Involvement: They provide material specs to the designer, help with
material selection, and sell the resin.
Concurrent Involvement: Material suppliers will be able to review gate types, gate
sizes, and vent sizes for any given material. For example, sub-gates are popularly
and commonly used because they automatically separate the part from the runner;
however, they should not be used for highly fiber-filled materials. In case a material
is molded for the first time in a particular facility, the molder must invite the mate-
rial supplier. The material supplier can make sure that the material is processed
properly for optimum properties and cycle time. It also helps to involve the material
supplier at the mold design stage, again in particular if this is a new material.
12.3.5The Process Engineer
Unfortunately, often the process engineer is the least involved member of the
whole team when in fact he is the most important one. The process engineer is the
person who has to deliver the final molded product. Project managers are anxious
to see the first molded part in their hand and therefore are usually waiting at the
molding machine on the day of the trial. Every other stage of the project, for exam-
ple mold build, typically has an end date, but the process engineer is under pres-
sure to deliver the parts hours after the mold has arrived into the molding facility
and minutes after the mold is mounted in the molding machine. Most likely, the
project manager has promised the customer parts by next day delivery or may
have also invited the customer to be present for the trial. This puts tremendous
pressure on the process engineer who is expected to mold acceptable parts. How -
ever, in many cases the process engineer has to take the blame for all the factors
that were not taken into consideration and all the mistakes and miscommunica-
tions during the entire project if the parts were not acceptable.
Conventional Involvement: In some organizations the process engineer sees the
mold or knows about the project on the day it is scheduled and in some cases they
are involved at the mold design stage.
Concurrent Requirement: The process engineer must be involved at every stage of
the project. Based on his molding experience, he can give a number of suggestions
to improve the moldability and the molding process of the part. Process engineers
are better judges of features such as vents, gate locations and so on. Mold design-
ers tend to place gates in locations convenient for mold making which are not al-
ways the best locations regarding processing. Even non-technical requirements,
such as the orientation of the mold, should be reviewed by the process engineer.
The choice of the machine must be left to the process engineer. Again, based on his
calculations of tonnage, % shot size used, and residence time, he can suggest the
best machine for the job at hand.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 353 (page 353)

32912.3 Concurrent Engineering in Injection Molding
12.3.6The Quality Engineer
Typically, the quality engineer is only a ‘measurement guy’ and often not involved
appropriately. The quality engineer past experience with similar parts or plastics
can prove valuable. He usually has knowledge about shrinkages and appropriate
tolerances during production.
Conventional Involvement: He is one of the invitees to the product release meetings
and is usually assigned the task to obtain drawings and work on methods for meas-
uring the final molded parts.
Concurrent Requirement: The drawings must be discussed with the product de-
signer. If an stereolithography model of the part or a prototype model is available,
it should be used to detail the inspection plan. Sometimes fixtures are required
and these can be planned in advance. Initial Gage Reproducibility & Repeatability
(Gage R & R) studies can even be performed on prototype parts. Any impractical
tolerances can be mentioned to the designer in advance.
12.3.7The Sales Team at the Molder
The sales team is usually the one that introduces the product designer to the
molder. They are looking to increase the sales of the molder and therefore try to
acquire as much business as possible. However, they must understand the techni-
cal aspects of the molding in order to get the right set of customers. They must
evaluate if an incoming project is suitable to and compatible with the capabilities
of the molding operation. If product and molder are not the right match, this could
have a negative impact not only on the program but also on the relations between
the two parties. All future work between the two parties can get jeopardized.
Conventional Involvement: The sales force brings in a job mainly based on machine
tonnage. Then there are other factors that they consider, such as any special re-
quirements. Special requirements include clean rooms, in-mold decoration, or in-
sert molding.
Concurrent involvement: The sales team must understand the capabilities of the
molder. This also includes the strength and weaknesses of each department in the
organization. If not, he is setting up the company for failure. The rules of machine
selection for a particular job must be clearly understood. Tonnage, shot sizes, per -
centage of shot size used, residence times and other parameters must be known
before accepting a job.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 354 (page 354)

330 12  Related Technologies and Topics
12.3.8Mandatory for All Departments
The final molded part is the result of the efforts of all departments involved. In
traditional ‘Over the Wall’ practices, every department performed their list of
things to do and passed the project on to the next department. However, the prac-
tice fails to address the issues the receiving departments could have as a result of
an action from a department previously involved. Understanding the needs of each
department and moreover a ‘why these needs’ makes the jobs easier, efficient, and
ensures on-time delivery of a part that meets the specifications. Every department
must understand cross-functional duties and have a basic understanding of each
other’s job function.
For example, everyone must be trained scientific processing methods and under -
stand why it is important to have a good process window. If the process engineer
sends a mold back to the mold maker or the tooling engineer because he does not
have a sufficient process window, he has a very valid reason. He can probably mold
ten good parts, but that does not mean that he can make half a million good parts,
because the process will not be capable. Knowledge of process capability must be
commonplace in every department of the molding facility.
12.3.9Implementing Concurrent Engineering
Concurrent engineering is probably the easiest concept to implement, because all
it takes is to get all the involved departments in one room or on a conference call to
discuss the project. Table 12.2 provided a simple matrix of typical job functions
and activities involved. Set up a meeting between the representatives of each de-
partment for the various phases of the project. The following must be taken into
account when following the table.
1.
The or
der of certain decisions does not necessarily reflect the order in which
certain activities are performed. For example, a machine must be selected at the
quoting stage to make sure the molder has the machine for the particular job
and not when the job has been accepted and a machine must be selected from
the ones that the molder has.
2.
The lis
t of activities and job functions is a general list and every company has its
own organizational structure. Therefore, every company must generate a cus-
tomized matrix. A meeting or updates at the end of every stage should be man-
datory. Although all job functions may not have a direct role in every stage, their
decisions will be based on the information provided to them from the previous
stages. Therefore, the status and decisions made regarding the project must be
communicated to the whole group.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 355 (page 355)

33112.3 Concurrent Engineering in Injection Molding
The molding business is getting extremely competitive in terms of cost and lead
times. The time lines from conceptualizing the project to having an actual molded
part are shrinking and it is expected that acceptable parts are produced on the first
molding attempt. Only companies that can achieve this are likely to survive in the
more and more competitive market. Concurrent engineering should be practiced
because it provides the extra set of eyes to ‘Look out of the Box’ and raise potential
concerns. These are meetings and times well spent. Regular reviews must be done,
especially if there is a change in design, material, time line, etc., and must be com-
municated to everyone. The final product, good or bad, is a result of the involve-
ment of the whole team.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 356 (page 356)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 357 (page 357)

Quality Concepts
This chapter is included to give the reader some basic knowledge and understand-
ing of some of the terminology used in injection molding. At the end of the chapter,
a list of some suggested texts is mentioned for readers who would like to further
their knowledge.
 13.1  Basic Concepts
Population: The population is the complete collection of elements to be studied. All
the 10,000 parts molded in a production run is a population.
Sample: A subcollection of elements drawn from a population is a sample: 100
parts drawn from the above 10,000 parts will be a sample.
Statistics: The method of analyzing data form a sample and drawing conclusions
about the population based on the data is called statistics. Of the 100 parts molded
above, if 10 parts had flash, then the observed defects in the sample will help in
estimating the defects in the population.
Variation: Variation is present in all processes. If any process or its output does not
show variation, then the measuring method is not sensitive enough to measure the
variation. If the weight of each of the 100 parts is 4.15
g
rams, then a scale with a
least count of 0.001
g
ram must be considered to measure the variation. A stable
system only shows effects of natural cause variation. There are no sudden or
pur
poseful changes to the inputs of the process that get reflected in the responses.
In special cause variation, there is a sudden or purposeful change in the inputs
that is reflected in the responses. For example, power usage during the night be-
fore
office hour
s is constant until office personnel begin to arrive. Then there is a
sudden increase of power requirement when everyone in the office begins to turn on
their computers at 8:00
AM.
Figure 13.1 shows natural and special cause variations.
13
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 358 (page 358)

334 13  Quality Concepts
PROCESS WITH NATURAL VARIATION
PROCESS WITH SPECIAL CAUSE VARIATION
Figure 13.1 Natural and special cause variation
 13.2  Histogram
A histogram is a graphical representation of the frequency of each data set. For
example, if the weights of 40 parts were recorded and the frequency of each weight
was represented graphically, it would be a histogram as shown in Figure 13.2.
It shows that there was 1 part that weighed 4.10
g
rams, 3 parts that weighed
4.11

grams, 2 parts that weighed 4.12

grams, and so on.
Figure 13.2 Histogram of part weights
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 359 (page 359)

33513.3 Normal Distribution
 13.3  Normal Distribution
In a given population of data, if the data is equally distributed around its mean, the
data is said to be normally distributed. If the data for 40 parts were represented by
the histogram shown in Figure 13.3, it can be observed that the data are equally
distributed on each side of the mean value of 4.15 grams. This is called a normal
distribution. The data cluster around the mean value. The curve joining the values
is called a bell curve. Figure 13.4 shows examples of normal distributions. The
data can also be such that the mean can be skewed to one side as shown in Figure
13.5. Such skewed data is said to have non-normal distribution.
Figure 13.3 Normal distribution
Figure 13.4 Examples of normal distributions
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 360 (page 360)

336 13  Quality Concepts
Figure 13.5 Representation of data that is not normally distributed
Significance of normal distribution: Processes that are stable, with only natural
cause variations, output data that is normally distributed. The variation is predict-
able and therefore the output can be predicted. In injection molding, having a
s
table process with predictable variation translates to quality assurance and the
reduction of inspection. Once the production run is completed, the molded parts
can be confidently shipped to the customer without any rework or worrying about
having returns for rework or scrap. In the presence of any special cause variations,
the data can show two distinct sets of data for the same population, each having its
own mean and distribution. Such distributions are called bimodal distributions.
Clearly, these must be avoided and the source of variation must be investigated.
 13.4  Standard Deviation
Refer to Figure 13.6, which shows a normal distribution. Consider the mean to be
at a value of 4.15 grams. Because this is a normal distribution, the data are distrib-
uted evenly on both sides of the mean. If the area under the curve is divided as
shown into 34 %, 13.5 %, and 2.35 % on each side of the mean, it is found that the
points intersecting the x-axis are all at equal intervals. Each interval is called one
standard deviation or one sigma (1
σ). T
o help understand this concept further,
consider that one standard deviation is equal to 0.02 grams (σ = 0.02 grams). The
standard deviations on the right side of the mean are positive sigma (+1
σ, +2
σ,
+3
σ, and so on) and t
he standard deviations on the left side of the mean are nega-
tive sigma (–1
σ, –2
σ, –3
σ, and so on). Ther
efore, the area between –1
σ and +1
σ
is 68 %, t
he area between –2
σ and +2
σ is 95 %, and t
he area between –3
σ and +3
σ
is 99.7 %. Ther
efore, if the data is normally distributed, 99.7 % of the data will fall
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 361 (page 361)

33713.5 Specification Limits and S tandard De viation
between –3 σ and +3 σ. S tandard deviation represents the extent of the variation
from the mean. The higher the standard deviation, the higher is the variation.
In the example, because 1σ = 0.02 grams, and the average is 4.15 grams, +1 σ =
4.17, +2 σ = 4.19, +3 σ = 4.21, –1 σ = 4.13, –2 σ = 4.11, and –3 σ = 4.09 grams.
Figure 13.6 Standard deviation and area under the curve
 13.5  Specification Limits and
S
tandard Deviation
The average part weight in the previous example is 4.15 grams. Assume the nomi-
nal value on the part drawing is also 4.15 grams. Refer to Figure 13.7. If the toler -
ances on the part weight are +/–0.06 grams, the lower specification limit (LSL) is
equal to 4.09 grams and the upper specification limit (USL) is equal to 4.21 grams.
These tolerances also coincide with –3
σ and +3
σ. Because t
he data is normally
distributed, 99.7 % of the parts will be within specifications, and 0.3 % of the parts
will be out of specifications; 0.15 % will be below the LSL, and 0.15 % will be above
the USL. If the production run was for a 1,000,000 parts, then statistically speak -
ing, 3000 parts will be out of specifications, 1500 parts will be below the LSL, and
1500 parts will be above the USL.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 362 (page 362)

338 13  Quality Concepts
Figure 13.7 Specification limits at –3 σ and + 3 σ
To assure that all the molded parts are within the required tolerances, the specifi-
cation limits must be well outside –3
σ and +3
σ assuming t
hat the average value of
the parts is always at the nominal value on the part print. In day to day production
it is rare that the average will always stay at the nominal value because of natural
variation. Refer to Figure 13.8. If the specification limits are placed at –6 σ and
+6
σ t
hen it is certain that all the parts will fall well within the required specifica-
tions. Such a tolerance will easily be able to cushion any natural variations in the
process. In recent years this is the reason for the push for the six sigma tech-
niques. It is important that the process is stable and all the variation is natural
cause variation. The extent of the variation is debatable. Sometimes, although the
data is normally distributed, there can be special cause variation present. For ex-
ample, ambient temperature during the day and the night may make a significant
shift in the distribution. Efforts must be made to minimize this variation by trying
to find the source of the variation. It is impossible to eliminate variation.
Figure 13.8 Specification limits at –6 σ and +6 σ
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 363 (page 363)

33913.6 Capability Index
 13.6  Capability Index
Figure 13.9 shows three processes. All the three have identical distribution and
therefore identical standard deviations. Process 2 is the same data that we have
been looking at in the earlier sections. The LSL and USL have been placed at –6
σ
and +6
σ, wit
h 4.15 grams being the nominal weight. With these limits, all the parts
molded with Process 2 will be acceptable. Now consider Process 1. Process 1 has
the same distribution and standard deviation as Process 2. However, the average is
now shifted to the left to 3.91 grams. All the parts molded with Process 1 will be
out of specifications. Process 3 also has the same distribution and standard devia-
tion as Process 2, but the average part weight is 4.29
g
rams. Some of the parts
molded with this process will be acceptable. These are shown as the green shaded
area under the curve. All three processes have identical variation of data except
their averages are different. But Process 2 is much more capable of producing parts
within the required specifications. To make Process 1 and 3 capable, the only change
that needs to be made is shifting of their averages towards the nominal.
Because 99.7 % of the data falls between –3 σ and +3
σ, t
hese measures are consid-
ered to be the practical limits for the spread of the data. Therefore, the data is spread
over 6
σ (3
σ bef
ore the nominal and 3
σ after t
he nominal). If all the parts must be
acceptable, then 6
σ
must be less than the distance between the LSL and USL, or in
other words, the ratio of the difference between the USL and the LSL to 6
σ should
be g
reater than 1. This ratio is called capability index and is denoted as Cp.
Capability Index EngineeringR equirements
StatisticalR equirem= eents

Cp USL −LSL= 6σ
(13.1)
The capability inde
x is not related to the average or nominal value. Having a large
Cp value equates to having a low standard deviation or a wide tolerance or both.
In Figure 13.9, Cp1 = Cp2 = Cp3, they all have identical capability indices.
Figure 13.9 Three processes with identical distributions but different averages
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 364 (page 364)

340 13  Quality Concepts
Case 1: Cp < 1. If Cp < 1, then (USL – LSL) is less than 6 σ. The variation is too large
or the specifications limits are too tight. Even if the process is centered, a large
number of parts will still be out of specification.
Case 2: Cp = 1. If the Cp = 1 then (USL – LSL) = 6 σ. If centered, the process is
capable, but is s
till molding 0.3 % bad parts.
Case 3: Cp > 1. If Cp > 1, then (USL – LSL) is greater than 6 σ. The probability of
molding good parts is certainly over 99.7 %, depending on the actual value of the
Cp. If the Cp value if 1.33, then the probability of molding 100 % good parts is very
high if the process is centered. If Cp = 2, then the ratio of the (USL – LSL) to the
standard deviation is high enough to ensure acceptable parts if the process is
cent
ered. The higher the Cp value, the better the chances of molding acceptable
parts. Such processes can easily withstand variations and some movements in
their averages.
 13.7  Process Capability
Process capability is the estimate of how capable the process is in relation to the
nearest specification limit. Unlike the capability index, process capability takes
into account the average value of the data. Process capability is denoted as Cp
k.
Cpk is calculated using Eq. 13.2. The smaller of the two values is used.
Cp
USLX
k =
−()
3σ
or Cp
XL SL
k =
−()
3σ
(whichever is smaller) (13.2)
R
efer to Figure 13.10.
Figure 13.10 Process capability for two processes with identical distributions
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 365 (page 365)

34113.7 Process Capability
The ideal process is shown by the dotted lines. The standard deviation from the
previous discussion is 0.02 grams. Consider Process 2. The average of the part
weights is 4.27 grams but because of the distribution some of the parts will be out
of specifications shown by the red shaded area. If we move the average closer to
the nominal, then the chances of molding all the parts acceptably will increase.
Cp
k measures how far away the average is from the nominal or in other words, how
close is it to one of the specification limits. Applying the formula, we can calculate
the Cp
k of Process 2
Cpk2
42 74 24
3 × 0.02 05= −() =.. .

(13.3)
The number
s for Cpk follow similar rules as for Cp. A Cp k value less of than 1.33
suggests that the process is capable of making unacceptable parts at the current
location of its average. The confidence of molding acceptable parts increases as the
Cp
k increases. A very high Cp k value suggest that the possibility of molding bad
parts is very small.
Consider Process 1. Applying the formula, we can calculate the Cpk of Process 1.
Cpk1
39 14 03
3 × 0.02 2= −() = −..

(13.4)
N
otice that in this case, there is a negative sign associated with the value of the
Cpk. This is in indication that the average is outside the specification limits and,
therefore, depending on the distance from the LSL or USL, at least 50 % of the parts
will be unacceptable.
If the Cp value is high and the Cp k value is low, this suggests that the process if
centered can make acceptable parts. In molding, this is often a steel dimension
change in the cavity. If a robust process has been established, the process must not
be changed, but the steel must be altered. It is also clear from the previous discus-
sion that if one part is within specifications, then this does not mean that all the
parts will be within specifications. There is always a natural variation and there-
fore a distribution of data. A statistically acceptable sample size of parts must be
measured. A minimum acceptable sample size for any statistical sampling is 30.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 366 (page 366)

342 13  Quality Concepts
 13.8  S tatistical Quality Control (SQC) and
Statistical Process Control (SPC)
Application of the above concepts to part quality is SQC. Quality inspectors track
the quality of the part to make sure that not only are the parts within specifica-
tions, but that the distribution over time is acceptable. The Cp
k values are kept in
check for critical dimensions. Control limits are tolerances that are calculated
based on the spread of the data. For example, if the USL = 20, LSL= 10, Avg = 15,
and the data is spread out over 4 units (2 on each side of 15), then a lower control
limit (LCL) of 13 (15
–
2) and an upper contr
ol limit (UCL) of 17 (15
+
2) can be
applied. If t
he data starts to drift out of these limits, it can give an early indication
of a process shift or an imminent problem. The parts will still be acceptable and a
proactive step can be taken to investigate the cause and rectify it. This will ensure
continued acceptable production with no stoppage or scrap. In SPC, machine
outputs suc
h as cushion values, fill times, and cycle times are tracked following
the same methodology. Figure 13.11 displays a run chart showing the different
specification limits. The LSL and the USL are usually not shown on control charts,
but are included here to help understand the concept.
Figure 13.11 Run chart showing the different specification limits
 13.9  References
[1] Wheeler , Donald J., Understanding Statistical Process Control (2010), SPC Press, Knoxville, TN
[2]
T
riola, Mario F., Elementary Statistics (2015), Pearson Publishing, NY
[3]
Montgomer
y, Douglas C., Introduction to Statistical Quality Control (2009), John Wiley & Sons Inc.,
NJ
[4]
Jur
an, Joseph M., Juran’s Quality Handbook (2010), McGraw-Hill, NY
[5]
Car
ender, Jay W., Managing Variation for Injection Molding (2003), Advanced Process Engineering
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 367 (page 367)

Appendix A
Materials Data Sheet
List of processing related data for commonly injection molded materials – SI system.
(Courtesy www.ides.com)
Note: These are guidelines only – Individual datasheets must be obtained from the
material suppliers or from www.ides.com
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 368 (page 368)

344   Appendix A Materials Data Sheet
Long name Short name Specific
gravity
Mold
shr
inkage,
flow %
Drying temperature
(°C)
Drying
time (h)
Suggested
max
moisture (%)
Processing (melt)
temp (°C)
Mold temperature
(°C)
min max min max min max
Acetal (POM) cCopolymer Acetal (POM) copolymer 1.37–1.43 1.6–2.6  79 121 1.5–5.0 0.15–0.20 189 211  49  96
Acetal (POM) homopolymer Acetal (POM) homopolymer 1.42 1.9–2.0  79  86 2.0–3.5 0.2 199 216  47  91
Acrylic, polymethyl methacrylate Acrylic (PMMA) 1.14–1.20 0.4–0.6  65  86 3.5–5.0 0.097–0.10 225 271  54  76
Acrylic, styrene methyl
me
thacrylate copolymer
Acrylic (SMMA) 1.05–1.09 0.4  65  82 2 – 215 227  40  60
Acrylonitrile butadiene styrene ABS 1.04–1.11 0.05–1.4  80  91 2.0–3.5 0.010–0.15 223 246  49  76
Acrylonitrile butadiene styrene +
PC
ABS+PC 1.10–1.22 1.6  78 111 3.0–4.0 0.020–0.043 248 288  59  88
Acrylonitrile styrene acrylate ASA 1.04–1.12 0.50–0.6  80 100 3.0–4.0 0.038–0.10 239 262  55  73
Acrylonitrile styrene scrylate + PC ASA+PC 1.11–1.24 0.5–0.6  79 110 3.0–4.0 0.020–0.052 250 280  60  80
Cellulose acetate CA 1.23–1.32 0.5  60  71 2.0–3.0 0.2 220 230  48  60
Ethylene tetrafluoroethylene
copolymer
ETFE 1.70–1.74 1.8
NA NA NA NA 323 331 135 –
Perfluoroethylene propylene
copolymer
FEP 2.14–2.16 0.7
121 3 NA 364  93 –
Perfluoroalkoxy PFA 2.14–2.15 – NA NA NA NA 330 371 180 204
Polyvinylidene fluoride PVDF 1.75–1.79 2.2–2.5 121 150 1.0–2.0 NA 215 249  71  72
Methyl methacrylate/ABS MABS 1.08–1.10 5.5  70  80 3 NA 220 246  55  65
Polyamide 11 Nylon 11 1.03–1.05 1.2–1.5  79  80 4.0–12 0.1 256  52 –
Polyamide 12 Nylon 12 0.980–1.23 0.4–1.9  79 100 3.0–10 0.020–0.50 233 275  38  87
Polyamide 46 Nylon 46 1.17–1.20 0.3–8.3  89 104 4.0–12 0.050–0.053 310 313 100 114
Polyamide 6 Nylon 6 0.922–1.18 0.01–4.4  78  82 2.0–5.5 0.095–0.20 182 314  59  81
Polyamide 610 Nylon 610 1.07–1.17 0.3–2.0  79  82 2.0–4.0 0.020–0.20 249 288  52  88
Polyamide 612 Nylon 612 1.06–1.35 0.10–6.0  77  82 3.0–4.0 0.020–0.25 243 267  69  80
Polyamide 66 Nylon 66 0.994–1.23 0.02–7.5  79  83 3.0–5.5 0.15–0.20 268 296  65  88
Polyamide 66/6 copolymer Nylon 66/6 1.09–1.15 1.1–1.6  80  81 2.5–3.0 0.099–0.20 245 281  67  82
Polyphthalamide PPA 1.10–1.16 1.1–2.0  79 135 4.0–7.1 0.045–0.15 311 333  78 151
Polyarylate Polyarylate 1.20–1.37 0.81 130 7 NA NA NA 100 135
Polycarbonate PC 1.17–1.22 0.1–0.16 102 128 3.0–4.5 0.019–0.020 282 308  79 102
Polycarbonate + acrylic (PMMA) PC+Acrylic 1.15–1.29 0.6–0.7  82  83 4.5 NA 227 253  49  52
Polycarbonate + PBT PC+PBT 1.10–32.1 0.5–1.0  94 121 2.0–5.0 0.020–0.022 257 272  62 105
Polycarbonate + PET PC+PET 1.20–1.22 0.5–0.9  97 118 2.0–8.0 0.019–0.020 267 271  79  81
Polybutylene terephthalate PBT 1.00–33.6 0.1–0.5 113 132 3.0–6.0 0.020–0.043 234 265  58  92
Polyethylene terephthalate PET 1.32–1.41 0.3–1.8 120 180 4.0–5.5 0.0030–0.20 256 285  15 130
Polyethylene terephthalate glycol
comonomer
PETG 1.25–1.28 0.3–0.5
65  75 3.0–9.0 0.05 218 260  27  40
Polyether imide PEI 1.26–1.36 0.1–0.2 134 151 5.0–5.5 0.020–0.021 373 374 148 151
Polyetheretherke-ne PEEK 1.25–1.40 0.1–1.7 135 150 3.0–4.0 0.1 374 384 149 192
Ethylene vinyl acetate copolymer EVA 0.929–0.962 1.2–1.5  60  61 7.0–8.0 NA  98 230  20 180
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 369 (page 369)

345   Appendix A Materials Data Sheet
Long name Short name Specific
gravity
Mold
shrinkage,
flow %
Drying temperature
(°C)
Drying
time (h)
Suggested
max
mois
ture (%)
Processing (melt)
temp (°C)
Mold temperature
(°C)
min max min max min max
Acetal (POM) cCopolymer Acetal (POM) copolymer 1.37–1.43 1.6–2.6  79 121 1.5–5.0 0.15–0.20 189 211  49  96
Acetal (POM) homopolymer Acetal (POM) homopolymer 1.42 1.9–2.0  79  86 2.0–3.5 0.2 199 216  47  91
Acrylic, polymethyl methacrylate Acrylic (PMMA) 1.14–1.20 0.4–0.6  65  86 3.5–5.0 0.097–0.10 225 271  54  76
Acrylic, styrene methyl
methacrylate copolymer
Acrylic (SMMA) 1.05–1.09 0.4  65  82 2 – 215 227  40  60
Acrylonitrile butadiene styrene ABS 1.04–1.11 0.05–1.4  80  91 2.0–3.5 0.010–0.15 223 246  49  76
Acrylonitrile butadiene styrene +
PC
ABS+PC 1.10–1.22 1.6  78 111 3.0–4.0 0.020–0.043 248 288  59  88
Acrylonitrile styrene acrylate ASA 1.04–1.12 0.50–0.6  80 100 3.0–4.0 0.038–0.10 239 262  55  73
Acrylonitrile styrene scrylate + PC ASA+PC 1.11–1.24 0.5–0.6  79 110 3.0–4.0 0.020–0.052 250 280  60  80
Cellulose acetate CA 1.23–1.32 0.5  60  71 2.0–3.0 0.2 220 230  48  60
Ethylene tetrafluoroethylene
copolymer
ETFE 1.70–1.74 1.8 NA NA NA NA 323 331 135 –
Perfluoroethylene propylene
copolymer
FEP 2.14–2.16 0.7 121 3 NA 364  93 –
Perfluoroalkoxy PFA 2.14–2.15 – NA NA NA NA 330 371 180 204
Polyvinylidene fluoride PVDF 1.75–1.79 2.2–2.5 121 150 1.0–2.0 NA 215 249  71  72
Methyl methacrylate/ABS MABS 1.08–1.10 5.5  70  80 3 NA 220 246  55  65
Polyamide 11 Nylon 11 1.03–1.05 1.2–1.5  79  80 4.0–12 0.1 256  52 –
Polyamide 12 Nylon 12 0.980–1.23 0.4–1.9  79 100 3.0–10 0.020–0.50 233 275  38  87
Polyamide 46 Nylon 46 1.17–1.20 0.3–8.3  89 104 4.0–12 0.050–0.053 310 313 100 114
Polyamide 6 Nylon 6 0.922–1.18 0.01–4.4  78  82 2.0–5.5 0.095–0.20 182 314  59  81
Polyamide 610 Nylon 610 1.07–1.17 0.3–2.0  79  82 2.0–4.0 0.020–0.20 249 288  52  88
Polyamide 612 Nylon 612 1.06–1.35 0.10–6.0  77  82 3.0–4.0 0.020–0.25 243 267  69  80
Polyamide 66 Nylon 66 0.994–1.23 0.02–7.5  79  83 3.0–5.5 0.15–0.20 268 296  65  88
Polyamide 66/6 copolymer Nylon 66/6 1.09–1.15 1.1–1.6  80  81 2.5–3.0 0.099–0.20 245 281  67  82
Polyphthalamide PPA 1.10–1.16 1.1–2.0  79 135 4.0–7.1 0.045–0.15 311 333  78 151
Polyarylate Polyarylate 1.20–1.37 0.81 130 7 NA NA NA 100 135
Polycarbonate PC 1.17–1.22 0.1–0.16 102 128 3.0–4.5 0.019–0.020 282 308  79 102
Polycarbonate + acrylic (PMMA) PC+Acrylic 1.15–1.29 0.6–0.7  82  83 4.5 NA 227 253  49  52
Polycarbonate + PBT PC+PBT 1.10–32.1 0.5–1.0  94 121 2.0–5.0 0.020–0.022 257 272  62 105
Polycarbonate + PET PC+PET 1.20–1.22 0.5–0.9  97 118 2.0–8.0 0.019–0.020 267 271  79  81
Polybutylene terephthalate PBT 1.00–33.6 0.1–0.5 113 132 3.0–6.0 0.020–0.043 234 265  58  92
Polyethylene terephthalate PET 1.32–1.41 0.3–1.8 120 180 4.0–5.5 0.0030–0.20 256 285  15 130
Polyethylene terephthalate glycol
comonomer
PETG 1.25–1.28 0.3–0.5  65  75 3.0–9.0 0.05 218 260  27  40
Polyether imide PEI 1.26–1.36 0.1–0.2 134 151 5.0–5.5 0.020–0.021 373 374 148 151
Polyetheretherke-ne PEEK 1.25–1.40 0.1–1.7 135 150 3.0–4.0 0.1 374 384 149 192
Ethylene vinyl acetate copolymer EVA 0.929–0.962 1.2–1.5  60  61 7.0–8.0 NA  98 230  20 180
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 370 (page 370)

346   Appendix A Materials Data Sheet
Long name Short name Specific
gravity
Mold
shr
inkage,
flow %
Drying temperature
(°C)
Drying
time (h)
Suggested
max
moisture (%)
Processing (melt)
temp (°C)
Mold temperature
(°C)
min max min max min max
Polyethylene, high density HDPE 0.932–0.988 0.7–3.0  79  80 1.0 NA 180 251  10  46
Polyethylene, low density LDPE 0.893–0.955 1.3–3.1  79  82 1.0 NA 164 222  15  43
Polyethylene, linear low density LLDPE 0.918–0.948 1.5–2.0  90 1.0 NA 180 240  18  35
Polyethylene, ultra high
molecular w
eight
UHMWPE 0.920–0.947 0.6–3.0 NA NA 1.0 NA 285  45 –
Polylactic acid PLA 1.23–1.26 0.3–1.1  49  51 3.5–4.0 0.010–0.032 199 240  20 105
Polyphenylene ether PPE 1.04–1.10 0.6  70 125 3 0.02 260 315  74  90
Polyphenylene sulfide PPS 1.26–1.75 0.1–0.3 134 150 4.0–6.0 0.015–0.20 313 323 121 156
Polypropylene homopolymer PP Homopolymer 0.901–0.950 1.2–1.8  75  85 1.0–3.0 0.050–0.20 202 249   2  50
Polystyrene, general purpose PS (GPPS) 1.03–1.06 0.4–0.6  69  82 1.5–2.0 0.02 214 248  30  60
Polystyrene, high impact PS (HIPS) 1.03–1.06 0.4–0.6  70  78 1.5–2.0 0.1 208 236  29  61
Syndiotactic polystyrene SPS 1.01–1.44 0.3–2.0  80 3.5 NA 310  70 –
Polyether sulfone PES 1.37–1.38 0.6–1.4 134 177 2.5–6.0 0.020–0.050 355 366 134 160
Polysulfone PSU 1.24–1.25 0.6–1.0 134 149 3.0–4.0 0.020–0.10 352 366 121 151
Polyvinyl chloride, chlorinated CPVC 1.47–1.52 0.6 NA NA NA NA 203 204 NA NA
Polyvinyl chloride, flexible PVC, Flexible 1.14–1.45 0.9–2.1 NA NA NA NA 165 200  24  30
Polyvinyl chloride, rigid PVC, Rigid 0.779–1.47 0.3–0.4  66 3 NA 186 206  32  32
Polyvinyl chloride, semi-rigid PVC, Semi-Rigid 1.30–1.58 1.1 NA NA NA NA 188 194 NA NA
Styrene acrylonitrile SAN 1.04–28.1 0.3–0.5  77  80 2.0–4.0 0.020–0.20 204 251  49  65
Styrene butadiene block
copolymer
SBC 0.850–1.03 0.5–2.4  52  77 0.5–3.0 NA 184 250  39  50
Styrene butadiene styrene block
copolymer
SBS 0.922–1.05 0.4–1.4  52  52 0.0–3.0 NA 155 232  23  45
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 371 (page 371)

347   Appendix A Materials Data Sheet
Long name Short name Specific
gravity
Mold
shrinkage,
flow %
Drying temperature
(°C)
Drying
time (h)
Suggested
max
mois
ture (%)
Processing (melt)
temp (°C)
Mold temperature
(°C)
min max min max min max
Polyethylene, high density HDPE 0.932–0.988 0.7–3.0  79  80 1.0 NA 180 251  10  46
Polyethylene, low density LDPE 0.893–0.955 1.3–3.1  79  82 1.0 NA 164 222  15  43
Polyethylene, linear low density LLDPE 0.918–0.948 1.5–2.0  90 1.0 NA 180 240  18  35
Polyethylene, ultra high
molecular weight
UHMWPE 0.920–0.947 0.6–3.0 NA NA 1.0 NA 285  45 –
Polylactic acid PLA 1.23–1.26 0.3–1.1  49  51 3.5–4.0 0.010–0.032 199 240  20 105
Polyphenylene ether PPE 1.04–1.10 0.6  70 125 3 0.02 260 315  74  90
Polyphenylene sulfide PPS 1.26–1.75 0.1–0.3 134 150 4.0–6.0 0.015–0.20 313 323 121 156
Polypropylene homopolymer PP Homopolymer 0.901–0.950 1.2–1.8  75  85 1.0–3.0 0.050–0.20 202 249   2  50
Polystyrene, general purpose PS (GPPS) 1.03–1.06 0.4–0.6  69  82 1.5–2.0 0.02 214 248  30  60
Polystyrene, high impact PS (HIPS) 1.03–1.06 0.4–0.6  70  78 1.5–2.0 0.1 208 236  29  61
Syndiotactic polystyrene SPS 1.01–1.44 0.3–2.0  80 3.5 NA 310  70 –
Polyether sulfone PES 1.37–1.38 0.6–1.4 134 177 2.5–6.0 0.020–0.050 355 366 134 160
Polysulfone PSU 1.24–1.25 0.6–1.0 134 149 3.0–4.0 0.020–0.10 352 366 121 151
Polyvinyl chloride, chlorinated CPVC 1.47–1.52 0.6 NA NA NA NA 203 204 NA NA
Polyvinyl chloride, flexible PVC, Flexible 1.14–1.45 0.9–2.1 NA NA NA NA 165 200  24  30
Polyvinyl chloride, rigid PVC, Rigid 0.779–1.47 0.3–0.4  66 3 NA 186 206  32  32
Polyvinyl chloride, semi-rigid PVC, Semi-Rigid 1.30–1.58 1.1 NA NA NA NA 188 194 NA NA
Styrene acrylonitrile SAN 1.04–28.1 0.3–0.5  77  80 2.0–4.0 0.020–0.20 204 251  49  65
Styrene butadiene block
copolymer
SBC 0.850–1.03 0.5–2.4  52  77 0.5–3.0 NA 184 250  39  50
Styrene butadiene styrene block
copolymer
SBS 0.922–1.05 0.4–1.4  52  52 0.0–3.0 NA 155 232  23  45
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 372 (page 372)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 373 (page 373)

Appendix B
Conversion Tables for
Commonly Used
Process Parameters
Speed 1 mm/s = 0.0394 in/s
1 in/s = 25.4 mm/s
Pressure 1 psi = 0.0069 MPa
1 psi = 0.0690 bar
1 bar = 14.50 psi
1 bar = 0.1 MPa
1 MPa = 145.04 psi
1 MPa = 10 bar
Temperature °Fahrenheit = (1.8 × °Centigrade) + 32
Example: 50 °C = (1.8 × 50) + 32 = 122 °F
°Centigrade = (°Fahrenheit – 32) / 1.8
Example: 200 °F = (200 − 32)/1.8 = 93.3 °C
Weight 1 ounce (oz) = 28.35 g
1 gram (g) = 0.035 oz
Tonnage 1 kN = 0.11 US tons
1 kN = 0.1 metric ton
1 US ton = 9.09 kN
1 US ton = 0.909 metric tons
1 metric ton = 10 kN
1 metric ton = 1.1 US tons
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 374 (page 374)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 375 (page 375)

Appendix C
Water Flow Tables
Minimum Water Flow (gal/min) Required to Achieve Turbulent Flow
Water
t
emperature
(°F)
Pipe diameter in inches
¼" 3⁄8" 1⁄5" ¾" 1"
(0.25 in) (0.375 in) (0.5 in) (0.75 in) (1 inch)
50 0.41 0.62 0.82 1.23 1.64
60 0.35 0.53 0.71 1.06 1.42
70 0.31 0.46 0.62 0.93 1.23
80 0.27 0.41 0.54 0.81 1.09
90 0.24 0.36 0.48 0.72 0.96
100 0.22 0.32 0.43 0.65 0.86
125 0.17 0.25 0.33 0.50 0.67
150 0.13 0.20 0.27 0.40 0.54
175 0.11 0.17 0.22 0.34 0.45
200 0.09 0.14 0.19 0.28 0.38
Note: This table should be used for water only. The presence of additives, such as rust preventives, will alter the
viscosity and therefore the flow rates. It is always better to use more than the recommended flow rates for this
reason.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 376 (page 376)

352   Appendix C Water Flow Tables
Minimum Water Flow (l/min) Required to Achieve Turbulent Flow
Water
t
emperature
(°C)
Pipe diameter in mm
8 10 15 20 25
10 1.96 2.45 3.68 4.90 6.13
15 1.71 2.14 3.21 4.29 5.36
20 1.51 1.89 2.83 3.78 4.72
25 1.34 1.68 2.52 3.36 4.20
30 1.20 1.50 2.26 3.01 3.76
35 1.08 1.36 2.03 2.71 3.39
40 0.98 1.23 1.84 2.46 3.07
45 0.90 1.12 1.68 2.24 2.80
55 0.76 0.94 1.42 1.89 2.36
65 0.65 0.81 1.22 1.62 2.03
80 0.53 0.66 0.99 1.32 1.66
95 0.44 0.56 0.83 1.11 1.39
Note: This table should be used for water only. The presence of additives, such as rust preventives, will alter the
viscosity and therefore the flow rates. It is always better to use more than the recommended flow rates for this
reason.
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 377 (page 377)

Appendix D
Part Design Checklist
Following are examples of some of the important questions that must be asked
during a part design review:
Part Design Checklist
 Is t
he gate location acceptable for fill?
 Is t
he number of gates sufficient for part fill?
 Is t
he gate location acceptable for cosmetics?
 Is t
he gate location acceptable for warpage?
 Can t
he thick areas be cored out?
 Is pr
ocessing information about the plastic material available?
 Is t
he shrink factor available?
 Is t
he engraving in an acceptable position?
 Is t
he texture acceptable?
 Is t
he part designed to stay on the B-side of the mold?
 Is sufficient dr
aft provided on the part for ejection?
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 378 (page 378)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 379 (page 379)

Following are examples of some of the important questions that must be asked
during a mold design review:
1.
Mold Cooling:
a)
Is t
he mold cooling acceptable?
b)
Does t
he mold require waterlines or oil lines?
c)
What is t
he size of the waterlines?
d)
Ar
e the waterlines recessed?
2.
Mold Cons
truction:
a)
Is t
he ‘TOP’ of the mold acceptable for part ejection and removal?
b)
Ar
e eyebolt holes provided on the ‘TOP’ of the mold?
c)
W
ill the mold fit between the tie bars?
d)
Ar
e the clamp slots/holes acceptable?
e)
Do t
he waterlines and tie bars interfere with each other?
f)
Ar
e parting line interlocks necessary?
g)
Ar
e pry bar slots necessary?
h)
Is t
he mold opening sequence acceptable?
i)
Ar
e insulator plates necessary?
j)
Ar
e any spares necessary?
k)
Ar
e the machine tie bars shown on the drawings?
3.
Ejection:
a)
Is t
he number of ejector pins sufficient?
b)
Ar
e the sizes of ejector pins sufficient?
c)
Does t
he ejector pattern on the mold match the ejector pattern on the
mac
hine?
d)
Is t
he ejection distance sufficient for the part to get ejected out of the mold?
Appendix E
Mold Design Checklist
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 380 (page 380)

356   Appendix E Mold Design Checklist
e) Ar e return springs necessary?
f)
Is an ear
ly ejector return system necessary?
g)
Ar
e support pillars necessary?
h)
Is guided ejection necessar
y?
i)
Does
the path of any of the ejector pins and the slides interfere with each
other?
4.
V
enting:
a)
Ar
e vents identified on the mold?
b)
Is t
he last point to fill vented?
c)
Ar
e all the corners vented?
d)
Ar
e bosses, ribs, and tabs vented?
e)
Ar
e deep pockets vented?
f)
Ar
e the runners vented?
5.
Gat
es and Runners:
a)
Is t
he gate size acceptable?
b)
W
ill the gate leave a gate vestige?
c)
Is t
he runner size acceptable?
d)
Is t
he runner balanced?
e)
W
ill the runners stay on the B-side?
f)
In case of a t
hree-plate mold will the runner drop freely?
g)
Is t
here a sprue puller?
h)
Do an
y of the sucker pins interfere with the plastic flow?
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 381 (page 381)

Appendix F
Mold Qualification
Checklist
a) Ar e the gates acceptable?
b)
Ar
e the parts dimensionally acceptable?
c)
Has t
he cooling study been done?
d)
Has t
he gate seal test been done?
e)
Has t
he viscosity test been performed?
f)
Is t
he cavity balance acceptable?
g)
Is t
he cycle time acceptable?
h)
Is t
he ejection acceptable?
i)
Is t
he part fill acceptable?
j)
Is t
he process window acceptable?
k)
Is t
he runner acceptable?
l)
Is t
he venting acceptable?
m)
Is t
he water flow through the mold acceptable?
n)
W
as the mold safe to be hung in the press?
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 382 (page 382)

© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 383 (page 383)

(The runner and part will always have the same percentage of regrind.)
Table 1 Part Weight = 95 % Runner Weight = 5 %
Regrind
Generation
(g)
Pass (p)
1 2 3 4 5
0 100 95.00 95.00 95.00 95.00
1 -  5.00  4.75  4.75  4.75
2 - -  0.25  0.24  0.24
3 - - -  0.01  0.01
4 - - - -  0.00
Table 2 Part Weight = 90 % Runner Weight = 10 %
Regrind
Generation
(g)
Pass (p)
1 2 3 4 5
0 100 90.00 90.00 90.00 90.00
1 - 10.00  9.00  9.00  9.00
2 - -  1.00  0.90  0.90
3 - - -  0.10  0.09
4 - - - -  0.01
Appendix G
Regrind Tables –
Percentage of Regrind
in Total Shot
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 384 (page 384)

360   Appendix G Regrind Tables – Percentage of Regrind in Total Shot
Table 3 Part Weight = 80 % Runner Weight = 20 %
Regrind
Generation
(g)
Pass (p)
1 2 3 4 5
0 100 80.00 80.00 80.00 80.00
1 - 20.00 16.00 16.00 16.00
2 - -  4.00  3.20  3.20
3 - - -  0.80  0.64
4 - - - -  0.16
Table 4 Part Weight = 75 % Runner Weight = 25 %
Regrind
Generation
(g)
Pass (p)
1 2 3 4 5
0 100 75.00 75.00 75.00 75.00
1 - 25.00 18.75 18.75 18.75
2 - -  6.25  4.69  4.69
3 - - -  1.56  1.17
4 - - - -  0.39
Table 5 Part Weight = 50 % Runner Weight = 50 %
Regrind
Generation
(g)
Pass (p)
1 2 3 4 5
0 100 50.00 50.00 50.00 50.00
1 - 50.00 25.00 25.00 25.00
2 - - 25.00 12.50 12.50
3 - - - 12.50 6.25
4 - - - - 6.25
Table 6 Part Weight = 25 % Runner Weight = 75 %
Regrind
Generation
(g)
Pass (p)
1 2 3 4 5
0 100 25.00 25.00 25.00 25.00
1 - 75.00 18.75 18.75 18.75
2 - - 56.25 14.06 14.06
3 - - - 42.19 10.55
4 - - - - 31.64
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 385 (page 385)

Index
A
ABS  98
acetal  102
acrylate  98
acrylics  101
acrylonitril  98
addition polymerization  14
additives  103
aesthetic process window (APW)  196,
271
aliasing  238, 239
alloys  96
amorphous  20
– plas
tics  164
– pol
ymers  17
anisotropic material  37
anti-aging additives  105
apparent shear rate  53
apparent viscosity  47
array
– or
thogonal  234
atactic  19
B
back pressure  150
balanced array  234
barrel clearance  113
barrel heat profile  24
Beaumont Technologies  60
blowing agents  106
Box-Behnken design  233
bubbles  72
built-in stress  218
burn marks  72
butadiene  98
C
capability index  339
capillary rheometer  66
cavity balance  179
– pr
ocedure  178
– s
tudy  177
cavity pressure  177
– cur
ve near the gate  315
– sensing t
echnology  313
– sensor
319
cavity pressure curve at the end of fill
315
cavity steel adjustment  248
chain scission  105
characterization of polymer viscosity  66
check ring  118
clamp force  113, 124
clamp tonnage  122, 124
classification of polymers  95
coefficient of friction  106
co-injection molding  64
colorants  106
commercial plastics  97
common defects
– cause
284
– pr
evention  284
concurrent engineering  10, 324
condensation polymerization  14
confounding  238, 239
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 386 (page 386)

362 Inde x
consistency  133
– ca
vity to cavity  3
– q
uality  2
– r
un to run  3
– sho
t to shot  2
constant factors  230
contact type probes  178
contour cooling  294
contour plot  244, 245
control factors  230
control process window (CPW)  198, 271
control sensor  317
coolant
– type of
295
cooling line  294
cooling phase  143
cooling time  26, 211, 212
– op
timization  212
– s
tudy  210
copolymers  96
critical dimension  246
critical factors of molding  7
crystalline  20
– pol
ymers  17, 164
crystallinity  21, 32
crystallite  17
crystallization  105, 165
– t
emperature  24, 31
cushion value  172
cycle time  212
– br
eak-down  213
cyclone separator  306
D
decoupled moldingSM  146, 319
degradation  71, 278
degree of crystallinity  18
desiccant dryer  81
design of experiments (DOE)  235
– definition
228
dew point  79, 84
dieseling effect  297
differential scanning calorimeter (DSC)
31
dilatant  49
dimensional process window (DPW)  198,
244, 271
dimensional variation  73
DIOP  104
direct sensor  316
dispersive mixing  116
distributive mixing  116
documentation books  276
DOE, See design of experiments
drying
– eq
uipment  80
– of plas
tics  77
– pr
ecautions  159
– t
emperature  77, 78
– time
77, 78, 158, 305
E
effect of regrind  311
elastomers  96
electronic moisture analyzer  83
end-chain degradation  71
end-of-fill cavity pressure integral  321
epoxidized soybean oil (ESO)  104
F
factor  230, 232, 245
factorial experiments  225, 241
family molds  187
feed depth  115
filler  104
– cont
ent  217
fill pattern  181
fill progression  172
fines  306
flame retardants  104, 105
flow
– fr
ont  50
– imbalance
57
– laminar
294
– pr
omoters  106
– tr
ansitional  294
– turbulent
294–296
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 387 (page 387)

363
Index
fluoropolymers  103
flush mount sensor  316
forced venting  304
fountain flow  50, 62, 175
fountain flow, effect on
– cr
ystallinity  65
– fiber or
ientation  65
– molecular or
ientation  65
free radicals  105
free state  38
frozen layer  62
full factorial experiment  241
G
gage reproducibility & repeatability  329
gassing
– e
xcessive  278
gate freeze study  203
gate seal  204
– cautions and e
xceptions  205
– pr
ocedure  203
– s
tudy  203
– time
205
general purpose polystyrene (GPPS)  113
general purpose screw  115
glass transition temperature  28
glassy state  54
H
heater bands  114
heat history  305
heat soaking  275
helix angle  117
high-shear lamina  58
histogram  334
holding phase  143, 144
holding pressure  144, 195, 196
holding time  196
homopolymers  96
horizontal clamp molding machine  111
horizontal injection machine  111
hot air dryer  81
hump profile  164
hydraulic ‘fill only’ integral  320
hydraulic pressure curve  314
hydrolytic degradation  71, 157
hydrophilic  69
hydrophobic  69
hygroscopic  69, 75
I
indirect sensor  316
injection
– molding cy
cle  143
– molding, par
ameter  226
– phase
143
– speed
145
injection force  145
in-mold rheology study  168
inorganic polymers  96
intensification ratio (IR)  119, 120, 147
– of t
he screw  114
interaction  235, 237
– column
238
– types of
237
intermolecular forces  15, 29
internal voids  145
isotropic material  37
K
Karl-Fischer titration  83
knowledge base  322
L
laminar flow  58
L/D ratio  113, 117
level  231, 232
lot-to-lot variations  169
lower specification limit (LSL)  137, 246
lower tolerance  221
low temperature – high pressure corner
199
low temperature – low pressure corner
199
lubricants  106
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 388 (page 388)

364 Inde x
M
machine selection  9, 122
machine specifications  112
material purging instructions  275
material selection  7, 8
material supplier
– concur
rent involvement  328
– con
ventional involvement  328
maximum moisture level  69
MeltFlipper®  60
melt flow index (MFI)  67
melt flow rate (MFR)  67
melt homogeneity  25, 114
melting point  30
melt processing range  22, 23
melt processing window  30
melt rheology  66
melt rotation technology  60, 62
melt temperature  23, 29, 162, 196
melt viscosity reducers  106
moisture determination  82
mold cooling  293
mold design and construction  7, 9
mold designer
– concur
rent involvement  327
– con
ventional involvement  327
molded-in stress  145
mold filling speed  23
mold function qualification  271
– pr
ocedure  220, 221
mold height  123
molding area diagram  196, 200
molding machine  7
– classification
110
molding process  7, 9
– effect on t
he part properties  305
molding shut down  280
molding startup  279
mold length  123
mold maker
– concur
rent involvement  327
– con
ventional involvement  327
mold open stroke  124
mold qualification
– book
276
– c hecklist  222, 271, 272
– flo
wchart  269
mold shut-down procedure  275
mold stack height  123
mold temperature  24, 165, 196
– map
274
mold width  123
molecular weight  15, 21, 306
– dis
tribution (MWD)  15, 16
monitor sensor  317
morphology  17
– r
ole of  22
multishot machine  112
N
natural cause variations  133
naturally balanced runner  58
Newtonian  49
noise factors  230
nominal dimension  221
non-Newtonian  49, 95
non-return valve  118
normal distribution  335
nozzle drool  74
nozzle temperature control  25
nucleating agents  105
number average molecular weight  15
number of experiments  232
nylon overdrying  89
O
operator instructions  275
optical clarity  26
organic polymers  96
orthogonal array  235
Ostwald and de Waele  51
out of specifications  137
oven dryers  80
overdrying  70, 85
– contr
oller  93
– pr
evention  92
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 389 (page 389)

365
Index
P
packing phase  143
packing pressure  177, 196
packing time  196
parallel cooling  296
Pareto chart  243
part design  7
partial factorial experiment  241
parting line shot  111
parting line vent  304
part quality qualification  271
PBT overdrying  86
percentage shot size used  127
phthalates  104
piezoelectric sensor  316
Plackett-Burman design  233
plasticating capacity  114
plastic drying  69, 157
plasticizers  104
plastic pressure  114
platen  123
– deflection
123
plugging up of the vents  73
Poisson’s effect  38
polar group  75, 77
polyamides  99
polycarbonates  101
polyesters  101
polyethylene  97
polymer  13
– blends
107
– cr
ystallinity  20
– mor
phology  187
– r
heology  47
polyolefins  97
polyoxymethylene  102
polypropylene  97
polystyrenes  100
polyvinyl chloride  101
post-gate cavity pressure integral  320
post-molding shrinkage  145, 216
prediction equation  245
pressure drop  192
– s
tudies  187
– s
tudy procedure  189
pressure graph  317
pressure limited  189, 191, 192
– pr
ocess  146
pressure sensor  315
process capability  340
process change log  273
– shee
t  282
process consistency  2, 135, 221
process documentation  222, 272
process engineer
– concur
rent requirement  328
– con
ventional involvement  328
processing aids  106
process optimization  165
process robustness  135, 221
process selection  247
process sensitivity chart  246
process sheet  272, 273
process window  196, 200, 244
– cautions and e
xceptions  201
– cr
ystalline materials  199
– s
tudy  195
– s
tudy procedure  198
product designer
– con
ventional involvement  326
– r
equired involvement  326
production book  276, 282
progression of the melt  63
purging  278
– com
pound  280
PVT graph  227, 228
Q
qualification runs  277
qualifications  283
qualitative factor  230
quantitative factor  230
quartz-based sensor  316
R
racetrack effect  59
randomization  240
reducing inspection  249
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 390 (page 390)

366 Inde x
regrind  305
– batc
h process  307
– continuous pr
ocess  307
– g
eneration estimating  308
– g
eneration number  306
– molecular w
eight  311
– par
ticle size distribution  306
– pr
ocessing  307
relative humidity  79
residence time  130
resin storage  156
response  231, 232, 245
– q
ualitative  231
– q
uantitative  231
Reynolds number (Re)  294, 295
rheological behavior  165
rheological imbalance  58, 181
rheology study  165
– cautions and e
xceptions  173
– pr
ocedure  169
robust process  133, 137, 138, 245
runner
– v
enting  303
S
scientific molding  6, 133
scientific processing  133,
153
– definition
6
screening experiment  233
screw  114
– bounce-bac
k  172
– c
hannel depth  115
– com
pression ratio  116
– com
pression zone  116
– designs
117
– diame
ter  113
– f
eed zone  115
– me
tering zone  116
– outside diame
ter  115
– r
ecovery speed  25
– r
ecovery time  148, 150
– r
oot diameter  115
– slipping
115
– speed   148
– tr
ansition zone  116
semicrystalline  18
sensor  314
– locations
321
series cooling  296
setup instructions  275
shear energy  148
shear force  48
shear friction  25
shear heat  114
shear rate  48, 49, 52, 66, 167
shear rate profile  55
shear stress  49
shear thinning  49, 95
shelf life limitations  156
short shot  178, 191, 297
shot control  74
shot size  112, 113, 116
shrinkage  22, 36, 38, 177, 216, 217
– additiv
es  217
– annealing
218
– filler
217
– glass tr
ansition temperature  217
– measur
ing procedure  219
– mold t
emperature  217
– par
t thickness  217
– pr
ocessing conditions  218
– r
ate of  216
sink  143
solution rheology  66
special cause variations  133
specifications  133
specific volume  29, 177
splay  72
standard deviation  336
startup procedure  279
statistical analysis  242
statistical data  233
statistical process control (SPC)  342
statistical quality control (SQC)  342
stereoregular  19
strain gage sensor  315
stress build-up  59
styrene  98
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 391 (page 391)

367
Index
surface defects  71
syndiotactic  19
T
Taguchi design  233
target dimension  245
Teflon  103
tensile properties  96
thermal imaging system  178
thermal region  54
thermal transition  28, 31
thermoplastics  96
thermosets  96
Thomasetti volatile indicator test  82
toggle machine  123
tolerances
– pr
ocess change  249
tonnage  113, 124
tonnage calculation  127
tooling engineer
– concur
rent requirement  326
– con
ventional involvement  326
tornado chart  243, 244
troubleshooting  280, 283
– guideline
277, 281
TVI Test  82
U
upper specification limit (USL)  137, 246
upper tolerance  221
UV stabilizers  105
V
vacuum assist  304
vacuum venting  304
valve gate mold  304
velocity  55
– pr
ofile  55
vent
– dep
th  299
– dimensions
298
– locations
302
– r
eliefs  299
– size
300
venting  297
vertical clamp molding machine  111
vertical injection  112
virgin material  305
viscosity  15, 23, 47, 52, 53, 145, 165, 167
– cur
ve  169
– cur
ve worksheet  171
– effect of t
emperature on  54
– in pol
ymer melts  50
– linear scale
166
– log
arithmic scale  166
– model
66
volumetric shrinkage  143
W
warpage  145, 218
waterline diagram  273, 274
water lines  296
weld line  74
Wheatstone bridge  315
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

### Segment 392 (page 392)

Robust Process Development
and Scientific Molding
Kulkarni
Suhas Kulkarni
Robust Process Development
and Scientific Molding
This book, Robust Process Development and Scientiﬁ c Molding, second edition, introduces the concepts of Scientiﬁ c
Molding and Scientiﬁ c Processing for Injection Molding, geared toward developing a robust, repeatable, and repro-
ducible (3Rs) molding process. It explains the underlying principles of polymer science: the properties that are important
to injection molding and their application to molding process development. The effects of polymer morphology,
thermal transitions, drying, and rheology on the injection molding process are explained in detail. The development
of a robust molding process is broken down into two sections: the Cosmetic Process and the Dimensional Process.
Scientiﬁ c molding procedures to establish a 3R process are provided.

The concept of Design of Experiments (DOEs) for and in injection molding is explained, giving insight into the cosmetic
and dimensional process windows. A plan to release qualiﬁ ed molds into production with troubleshooting tips is also
provided. Topics that impact a robust process such as the use of regrind, mold cooling, and venting are also described.

Readers will be able to utilize the knowledge gained from the book in their day-to-day operations immediately.

This second edition includes a completely new chapter on Quality Concepts, as well as much additional material
throughout, covering fountain ﬂ ow, factors affecting post mold shrinkage, and factor selections for DOEs. There are
also further explanations on several topics, such as in-mold rheology curves, cavity imbalances, intensiﬁ cation ratios,
gate seal studies, holding time optimization of hot runner molds, valve gated molds, and parts with large gates.
A troubleshooting guide for common molded defects is also provided.

Contents:
/uni25A0 Introduction to Scientiﬁ c Processing
/uni25A0 Properties of Polymers and Plastics
/uni25A0 Polymer Rheology
/uni25A0 Plastic Drying
/uni25A0 Common Plastic Materials and Additives
/uni25A0 Injection Molding and Molding Machines
/uni25A0 Scientiﬁ c Processing, Scientiﬁ c Molding,
and Molding Parameters
www.hanserpublications.com
Hanser Publications
ISBN 978-1-56990-586-9
/uni25A0 Process Development 1: Cosmetic Process
/uni25A0 Process Development 2: Dimensional Process
/uni25A0 Mold Qualiﬁ cation Flowchart, Production Release,
and Troubleshooting
/uni25A0 The Role of Mold Cooling, Venting, and Regrind
Management in Process Development
/uni25A0 Related Technologies and Topics
/uni25A0 Quality Concepts
Suhas Kulkarni
Robust Process Development
and Scientific Molding
Theory and Practice
2nd Edition
Booke Bonus
© 2017 Carl Hanser Verlag. All rights reserved.
No unauthorized disclosure or reproduction; licensed to purchaser only.

## Source: EMS-GRIVORY Injection Molding Trouble Shooting Guide(English Version, Second Edition, 2022).pdf
- source_path: /home/gabri/udemy/llm_engineering/myRAG_knowledge/Process_Trouble-Shooting/EMS-GRIVORY Injection Molding Trouble Shooting Guide(English Version, Second Edition, 2022).pdf
- source_ext: .pdf
- parser_used: rapidocr_onnxruntime
- fallback_used: True
- parse_status: success
- extracted_chars: 107099

### Segment 1 (page 1)

INJECTIONMOLDING
Trouble Shooting
Guide
EMS
Booklet as a Quick Guide for
Processing Problem Solving
EMS-GRIVORY

### Segment 2 (page 2)

Injection Molding Trouble
Shooting Guide
Jason Jin

### Segment 3 (page 3)

This booklet was produced with the technical collaboration of
the Application Development department of EMS-CHEMIE
(Suzhou) Ltd.
The advice and information in this publication is based on our
present knowledge and experience. The given figures and
data area guidance values and do not represent binding
specifications.
No warranties of any kind, either express or implied, includ-
ing warranties of merchantability of fitness for a particular
purpose, are given regarding advices, design, data and pro-
ducts.
2nd Edition @ Feb 2022
All rights reserved with EMS-CHEMIE (Suzhou) Ltd.
llustration: Jason Jin
[ADEngineerEMS-CHEMIE(Suzhou)】
Printing and binding: Dongxin

### Segment 4 (page 4)

Preface
This is the 2nd Edition of the EMS-Grivory Injection Molding
Guide. New processing information for Grivory HT6, Grivory
G5V, Grivory G7V, Grilamid TR HT 200, Grilamid TR HT 170,
and Grilamid TR ICR 20 have been included.

### Segment 5 (page 5)

Injection Molding Trouble Shooting Guide
Contents
Injection Molding Trouble Shooting Guide
1
Sink Mark
1
2
Streaks
2.1 Burn Streaks/Burn Marks
4
2.2 Moisture Streaks
7
2.3 Color Streaks/Discoloration
9
2.4 Air Streaks/Gas Mark
13
2.5 Glass Fiber Streaks
15
3
Gloss/ Gloss Difference
18
4
Jetting
21
5
Record Groove/Flow Mark
25
6
Stress Cracking
28
7
Short Shot
35
8
Flash
39
9
Ejector Marks
42
10
Delamination\Flaking
45
11
Cold Slug
48
12
Black Spots
51
13
Gate Bloom /Matt Point
54
14 Tool Deposits
56
15 Part Sticking on Core Side
61
16 Part/Runner Sticking on Cavity Side
63
17 Nozzle Drooling
66
18 Excessive Warpage
67
19 Failure Analysis of Plastics
71

### Segment 6 (page 6)

Injection Molding Trouble Shooting Guide
Appendix
I
Purging Guide of EMS Material
78
I
Mechanical Screw & Barrel Cleaning Method
80
III
Quick Processing Guide for Grilamid TR
84
IV
Quick Processing Guide for Grivory HT
88
V
Quick Processing Guide for Grivory GV/GC/GM
91
VI
Quick Processing Guide for Grilamid L (PA12)
92
VlI Process vs. Part Quality Chart
93
VIll Trouble Shooting Guide Overview Chart
95
EMS

### Segment 7 (page 7)

Injection Molding Trouble Shooting Guide
Chapter 1 - Sink Mark
1.1 Description
Sink marks are surface depressions often identified by different
light reflections and changes in gloss. Sink marks typically oc-
cur in areas of material accumulation, wall thickness changes,
around ribs, and opposite of bosses
1.2 Root cause
Sink marks occur during the cooling process when material can-
not compensate for shrinkage in localized areas. If the stiffness
of the skin layer is too low (inadequate cooling time), the outer
layer will be drawn inward by shrinkage forces as is shown in
Figure 1.
Figure. 1: Molded part with sink marks (gating at the thin wall)
Solidified peripheral layer
Disadvantageous gate
+
There are three fundamental cases resulting in sink marks:
1). Slow melt solidification
2). Inadequate holding pressure and time
3). Low holding pressure at transfer (due to high flow resista-
nce in the tool)
For optimization holding pressure transfer, the gate should be lo-
cated onto the thickest cross section of the part, and in order to
avoid premature solidification of the gate and runner system, suf-
ficient dimension is also necessary.
As illustrated by Figures 2 and 3, if thermal contraction (shrink-
age) cannot be compensated, then the sink marks may appear
near material accumulations, ribs and bosses.
01

### Segment 8 (page 8)

Chapter 1 - Sink Mark
Fig. 2: Sink marks due to wall
Fig.3: Sink marks on the cylindri-
thicknessvariations
calcorewheretemperature
is notcontrolledcorrectly
1.3 Remedy
1.3.1 Processing:
Remedy method
Why?
1
Extend holding time
Increase material in
2
Increase holding pressure
cavity to compensate for
shrinkage
3
Reduce V/P transfer position
4
Reduce melt temperature
Faster material solidifi-
5
Reduce nozzle temperature
cation
6
Reduce tool temperature
Steel has better heat
Increase cooling time
transfer than air, hence
less time for shrinkage
1.3.2 Part and tool design:
Remedy method
Why?
Enlarge gate and runner size
Easier to inject & pack
additional material into
Increase the number of gates
cavity to compensate for
shrinkage
Proper rib to base ratio
Avoid excessive wall
Round off sharp transitions
thickness concentration
at certain area
Uniform part thickness distribution
Mask appearance of
Textured tool surface
remaining sink marks
EMS
02

### Segment 9 (page 9)

Injection Molding Trouble Shooting Guide
1.3.3 Material:
Remedy method
Why?
Use amorphous material
Use material with higher mole-
Decrease material's
cular weight, fiber and filler
shrinkage properties
content
Use lower crystallinity material
1.3.4 Injection machine & auxiliaries:
Remedy method
Why?
Use gas/water assisted injection
Uniform thickness distri-
molding technology
bution
Compensate shrinkage
Switch to electrical injection
with high injection speed
molding machine
and pressure - more
effective packing time
1.4 Checkpoints
Part design
- Thickness accumulation, uniform, sharp corners?
Tool design
- Proper runner & gate dimension, venting, number and
location of gates
Nozzle diameter
Process stability
- Cushion, metering, part weight?
Filling study
- Flow pattern, hesitation, weld line, air trap
Proper melt and tool temperature?
Gate sealing point study?
Screw wear and non-return valve acceptable?
Influence of post-operations
- Painting, heating, drilling, gluing, etc.
03

### Segment 10 (page 10)

Chapter 2 - Streaks
Chapter 2 - Streaks
2.1 Burn streaks/burn marks
2.1.1 Signs for burn streaks
d s s
molded parts. The location of the burn streaks and marks are typi-
cally behind narrow cross-sections (high shear points), sharp
corners and at the end of deep hole/ribs and flow. (Figures 4 and
Fig.4:Burnmarkinblind holearea
Fig. 5: Burn mark in filling end area
2.1.2 Root cause
s a s
caused by localized thermal degradation due to:
1. High melt temperature
2. Long barrel residence time
3. Excessive shear ofthe melt
- Fast screw speed/high back pressure, etc.
4. High shear within the cavity
- Fast injection speed/small gate, etc.
5. Inadequate venting
- Air being unable to properly evacuate cavity duringfill,
compressed material and gas that is creating localized
heating, "dieseling"
6. High regrind content
- Increased material degradation after processing
EMS
04

### Segment 11 (page 11)

Injection Molding Trouble Shooting Guide
2.1.3 Remedy
2.1.3.1 Processing:
Remedy method
Why?
Reduce melt temperature
Avoid thermal damage
2
Reduce screw speed
Avoid thermal damage caused
3
Reduce back pressure
by high shear rates
Apply or increase dosing
4
delay times
Decrease residence time in
barrel
Reduce melt cushion /
5
metering stroke
6
Reduce injection speed
Decrease shear rates
Reduce cycle time
Avoid long residence time
2.1.3.2 Part and tool design:
Remedy method
Why?
Increase vent size and
Avoid thermal damage caused
numbers
by air trap
Reduce shearing via lowering
Increase wall thickness
injection speed/pressure
Soften sharp transitions
Avoid thermal damage caused
(runner, ribs and corners
by excessive shear at sharp
etc.)
corners
Avoid thermal damage caused
Increase runner and gate
by excessive shear at the
size
runner and gate area
Avoid tool design with hot
Avoid thermal damage caused
runner (especially for
by extended residence time
Grivory HT grades)
Avoid thermal damage caused
Reduce wall thickness
by excessive shear at abrupt
variation
thickness change area
Increase cold slug catcher
Reduce amount of gas entering
and add dead end at runner
into the cavity
05

### Segment 12 (page 12)

Chapter 2 - Streaks
2.1.3.3 Material:
Remedy method
Why?
Reduce regrind content
Avoid excessive gas com-
Avoid volatile polymer
ing from material
components
Avoid high shear via lower
Increase material flow-ability
injection speed
Enhance heat stability of
Avoid thermal damage via
additives and base polymer
enhancing heat stability
2.1.3.3 Injection machine & auxiliaries:
Remedy method
Why?
Increase nozzle diameter
Avoid excess shear occurr-
Align nozzle and sprue bushing
ed at nozzle area
Reduce shear rate by reduc-
Screw treatment/ coating
ing the friction between
(PVD, Nickel-PTFE,DLC)
material and screw
Machine utilization between
Reduce material residence
50% and 80% barrel capacity
time
2.1.4 Checkpoints.
Part design
- Thickness accumulation, uniform, sharp corners?
Tool design
- Runner & gate dimension, venting, gate location and am-
ounts
Check the recipe
- Volatile components, heat stability of the additives
Processing settings
- Melt and tool temperature, back pressure,injection speed,
residual time, etc.,
Granule appearance
- Over dried (surface oxidation), black spots
Filling study
- Flow pattern, hesitation, weld line, air trap
EMS
06

### Segment 13 (page 13)

Injection Molding Trouble Shooting Guide
Appropriate moisture content?
- Drying method, sealing bag status?
Melt cake quality
- Foam, bubbles, gassing
Paper testing
- Put a paper into the sprue and location ring area, and then
forward thebarrel manuallyuntilit touches thesprue.Che-
ck if there is a hole on the paper.
Leakage of the coolant.
2.2 Moisture streaks
2.2.1 Signs for moisture streaks
Normally, moisture streaks appear as light grey or silver streaks
radiating from the gate along the flow direction (Figure 6). If
moisture is trapped within the material, bubbles may also occur
in the part.
Fig. 6: Left - Streaks due to moisture granules.
Right-Streaksduetomoistureonthemoldsurface
2.2.2 Root cause
Hygroscopic materials like PA, ABS, CA, PBT, PMMA, SAN
etc. will absorb moisture from the air. During injection, the ad-
vancing flow front forces the absorbed moisture to the surface
of the melt (Figure 7).With the pressure change, the blisters will
deform and burst resulting in a streaks, bubbles etc. on the part
surface.
07

### Segment 14 (page 14)

Chapter 2 - Streaks
Fig.7:Flowofwatervaporblistersneartheflowfront
P (atmosphere)
Solidified peripheral “skin" layer
Water vapor blisters
Flow front
2.2.3 Remedy
2.2.3.1 Processing:
Remedy method
Why?
Release water vapor via high
Increase back pressure
back pressure during dosing
stage
Avoid the risk of degradation
2
Reduce melt temperature
at higher melt temperature
level
Reduce residence time in
3
Reduce cycle time
barrel
Vaporize residence moisture
4
Increase tool temperature
on tool's surface
2.2.3.2 Tool design:
Remedy method
Why?
Increase venting size and
Release water vapor via effic-
numbers
ient venting
2.2.4 Checkpoints
Check the material handling before molding
Damaged packing? Incorrect storage environment? Closed
feeding system? Appropriate dry blend procedure?
(Adding pigment, master batch etc.) Adding regrind granules?
EMS
08

### Segment 15 (page 15)

Injection Molding Trouble Shooting Guide
√ Maintenance venting.
Re-trial material from unopened bag
Measure actual melt & tool temperature
Verify proper moisture content
Moisture on the tool surface? (Leakage of the coolant)
Melt patty quality
- Foam, bubbles, gassing, etc.
/Measure material degradation via relative viscosity
2.3 Color streaks / discoloration
2.3.1 Description
Poorly blended material can lead to occurrences of color stre-
aks partially or over the entire part. The difference in color may
appear as streaks parallel or transverse to flow.
Fig. 8: Examples of color streaks in a molded part
2.3.2 Physical cause
A homogeneous melt cannot be achieved when the base poly-
mer and additives are incompatible. Specific areas of difficulty
include manual pigment introduction, pigment accumulating in
corners and sharp transitions and pigment separation in weld
line areas.
Similar to thermoplastics, pigments and dyes are sensitive to ex-
cessive processing temperature and residence times. If thermal
damage is the reason for color streaks, such streaks should be
considered as burn streaks.
09

### Segment 16 (page 16)

Chapter 2 - Streaks
Fig. 9: Smaller color differences at abrupt thickness change area due to higher
shearing
Color pigments accumulation
Direction
of flow
2.3.3 Remedy
2.3.3.1 Processing:
> If caused by overheating
Remedy method
Why?
Reduce melt temperature
Avoid overheating material
2
Reduce screw speed
Avoid overheating caused
3
Reduce back pressure
by excessive shear
Apply dosing delay or
4
increase delay time
Avoid degradation caused
by long residence time
Reduce melt cushion/
5
metering stroke
Avoid degradation caused
6
Reduce injection speed
by excessive shear
7
Reduce cycle time
Avoid degradation caused
Machine utilization between
by long residence time
8
50% and 80% barrel capacity
If caused by poor blending (inhomogeneous)
Remedy method
Why?
Increase back pressure
Achieve better homogeniza-
2
Increase screw speed
tion via increasing shear rate
3
Increase injection speed
EMS
10

### Segment 17 (page 17)

Injection Molding Trouble Shooting Guide
2.3.3.2 Part and tool design:
Remedy method
Why?
Increase venting size and
numbers
Avoid overheating material
in certain areas due to air trap
Design a vacuum evacuation
system for the tool
Avoid overheating caused by
Soften sharp transition areas
excessive shear
Avoid overheating caused by
Reduce wall thickness
excessive shear at abrupt
variation
thickness change areas
Increase runner size
Reduce shear stress during
Increase wall thickness
injection
Avoid using hot runner (espe-
Avoid overheating caused by
cially for Grivory HT grades)
long residence time
2.3.3.3 Material:
If caused by overheating
Remedy method
Why?
Molding parts at a relatively
Use material with improved
lower melt temperature level
flow ability
- avoid overheating
Enhance heat stability of
additives and base polymer
Strengthen the heat
resistance of material
Reduce regrind material ratio
If caused by poor blending (pigment accumulating)
Remedy method
Why?
Use granular additives with
smaller or spherical shape
Improve the compatibility
with base polymer
Adding plasticizer
11

### Segment 18 (page 18)

Chapter 2 - Streaks
2.3.3.4 Injection machine & auxiliaries:
Remedymethod
Why?
Align nozzle and sprue bushing
Reduce the shear rate
Use smaller screw diameter
Reduce shear rate by reducing
Screw treatment/coating
the friction between material
(PVD, Nickel-PTFE, DLC)
and screw
Avoid overheating (degrad-
Machine utilization between
ation) via reducing residence
50% and 80% barrel capacity
time in barrel
2.3.4 Check points:
Check the process settings
- Melt temperature, injection speed, back pressure and etc
Contamination in granules and barrel/nozzle purging
Measure the real melt & tool temperature
Check the material handling before molding
- Damaged packing? Storage environment? Closed feeding
system? Appropriate dry blend procedure? (Adding pigm-
ent, master batch etc.) Adding regrind granules
Proper moisture content
Granule appearance (before-after drying)
- Surface oxidation? Black spots
Check recipe
- Homogeneous between master batch and base polymer
Verifying with natural color
Complicated design
- Appropriate wall thickness? Uniform thickness distribu-
tion? Sharp corners at certain area
Appropriate design of nozzle-runner-gate
/ Regular venting maintenance
√ RV (relative viscosity) test
EMS
12

### Segment 19 (page 19)

Injection Molding Trouble Shooting Guide
2.4 Air streaks / gas mark
2.4.1 Signs for air streaks
Air streaks can occur on the surface of a molded part when mold-
ing in an environment with high relative humidity. Additional en-
vironmental conditions and a combination of cold tool and gran-
ules increase the likelihood of air streaks. When checking the
melt patty the blisters are visible (especially for transparent ma-
terial). However, it can be improved via reducing the decom-
pression and injection speed.
The solidified flow front of a partially filled part (short shot)
will show crater-like structures.
Examples:
Fig.10:Air streak (near sprue)due to
Fig.1l: Air streak due to entrained
suckedinairduringdecompression
andstretchedair
2.4.2 Physical cause
Air streaks appear when the air
Fig.12: Air streak forms behind the
engraving
within the mold cavity cannot
escape during injection. The tr-
apped air is drawn to the sur-
face and stretched in the flow
direction. The presence of air streaks can increase near ribs and
depressions where moving material can trap air (Figure 12).
During decompression, the air will be injected into the cavity
during filling if it is pulled into the nozzle, and the injected air is
pushed towards the mold wall where it freezes. Finally, the air
streaks will appear near the gate after injection.
13

### Segment 20 (page 20)

Chapter 2 - Streaks
For fire retardant materials, the
Fig. 13: Air streaks cause by fire
retardantrelease
gas tends to release during plas-
ticization when the process set-
tings of melt temperature,
screw speed and back pressure
are inappropriate. Finally the
air str-eak appears on the part
surface as is shown by Figure
13.
2.4.3 Remedy
2.4.3.1 Processing:
Remedy method
Why?
Allows more time for gas to
1
Reduce injection speed
escape
2
Reduce decompression
Avoid drawing air into nozzle
Easier to release gas under
3
Increase back pressure
higher back pressure during
dosing stage
2.4.3.2 Part and tool design:
Remedy method
Why?
Eliminate the risk of air
Reduce surface roughness and
streak formation behind
engraving depth
engravings
Increase venting size and
Easy to release the gas
numbers
during injection
Soften transition (runner,
Eliminate the risk of air
ribs, corners)
streak formation behind
Smooth wall thickness change
sharp areas
Gate relocation or adjust gate
Keep smooth flow front
numbers
EMS
14

### Segment 21 (page 21)

Injection Molding Trouble Shooting Guide
2.4.3.3 Injection machine & auxiliaries:
Remedy method
Why?
Align the nozzle and sprue
Allows more time for gas to
bushing
escape from cavity
Avoid long residence time
Machine utilization between
which causes degradation -
50% and 80% barrel capacity
less gas release
2.4.4 Check points:
Processing stability, e.g. Cushion, metering, part weight
Check the air streak location and around structure
Paper test
- Check alignment and dead ends between machine nozzle
and sprue)
Check with microscope
-Air streak or fiber streak?
Bridging in feeding throat/agglomerations
Measure the real melt and tool temperature
2.5 Glass fiber streaks
2.5.1 Description
Glass fiber streaks may occur partially or over the entire part. It
will result in a rough part surface and individual fibers may be
visible on the surface, even at individual areas (e.g. weld lines).
They may also protrude from the surface.
Fig.14:Surfacefiber streaks
Fig.15: Fiber streaks under 50 X
optical microscope
15

### Segment 22 (page 22)

Chapter 2 - Streaks
2.5.2 Root cause
1. Premature melt solidification
glass fibers.
2. Difference in shrink
Large difference in shrinkage between glass fiber and matrix.
(Glass fiber:plastic = 1:200).
3. Restricted shrinkage
Glass fibers impede matrix shrinkage, especially in the longitu-
dinal direction of the fiber, thus producing an uneven surface
(Figure 16).
Fig. 16: Formation of a rough surface due to different shrinkages
Glass fiber
Plastic before shrinkage
Plastic after shrinkage
2.5.3 Remedy
2.5.3.1 Processing:
Remedy method
Why?
1
Increase injection speed
Avoid premature melt
2
Increase tool temperature
solidification
3
Increase melt temperature
4
Extend packing time
Compensate for melt
Increase holding pressure
shrinkage
5
EMS
16

### Segment 23 (page 23)

Injection Molding Trouble Shooting Guide
2.5.3.2 Part and tool design:
Remedy method
Why?
Enlarge round off sharp transitions
Maintain constant
Smooth wall thickness change
injection speed profile
Adding radii at gate area
Enlarge gate size
Improve packing
efficacy
Relocate gate
Increase shear rate to
Reduce wall thickness
improve fiber orientation
2.5.3.3 Material:
Remedy method
Why?
Reduce solidification speed
Avoid premature melt
Increase flow ability
solidification
reduce fiber content
Reduce the shrinkage differ-
ence between fiber and matrix
Increase fiber length
2.5.4 Checkpoints
Check the process settings
- Melt and tool temperature, injection speed, packing
pressure, times etc.
Improve part and tool design.
- Wall thickness distribution, gate size, location etc.
Processing stability
- Cushion, metering, part weight
Measure actual melt and tool temperature
Filling study
- Flow pattern, hesitation, weldline, air trap
Check the fiber location and corresponding part structures
Use microscope to check ifit is a real glass fiber streak or
other defects
17

### Segment 24 (page 24)

Chapter 3 - Gloss/Gloss Differences
Chapter 3 - Gloss/Gloss Differences
3.1 Description
The shine or luster on a smooth surface (gloss) is seen when a
part is exposed to light. One part of the light will be reflected on
the surface and another part will reflect inside the part or pene-
trate it with different intensities.
As is illustrated in Figure 17, the impression of gloss is at its op-
timum when the surface roughness is lower. To achieve this, the
steel surface should be polished as smooth as possible (a tex-
tured steel surface will work).
Right: Only slightly glossy impression due to reflection on a rough
surface and on fillermaterials
Narrow intensity distribution
Broad intensity distribution
Gloss differences are caused by behaviors of the plastic with re-
spect to the steel surface due to uneven cooling and non-uniform
shrinkage. The stretching of cooled areas (e.g. due to warpage)
can be another reason for gloss differences. Various related ex-
amples of glossy defects are shown in below Figures.
Fig. 18: Gloss difference due to wall
Fig.19: Different gloss levels
thicknessvariations
EMS
18

### Segment 25 (page 25)

Injection Molding Trouble Shooting Guide
3.2 Remedy
3.2.1 Processing:
Remedy method
Why?
Allow the melt to touch the
1
Increase injection speed
tool surface efficiently
2
Delay V/P transfer point
Increase holding pressure
Compensate for shrinkage of
3
level
the melt
4
Extend packing time
5
Adjust tool temperature
Avoid too-early melt freezing
and allow the melt to touch
6
Adjust melt temperature
the tool surface efficiently.
Keep constant flow front
Achieve uniform flow front
7
profile
temperature
Uniform the temperature of
Reduce melt cushion /
8
melt that enters into the
metering stroke
cavity
Fill the part efficiently and
g
Increase back pressure
reduce the shrinkage
3.2.2 Tool and part design:
Remedy method
Why?
Apply Beryllium-Copper
Avoid heat accumulation on
insert
tool due to uneven cooling
Uniform cooling distribution
Avoid uneven cooling
Achieve uniform flow front
Balanced fill pattern
temperature and shrinkage
Improve tool surface
Improve projection behaviors
polishing quality
ofthe plastic at steel surface
Improve tool venting
Avoid diesel effect
Avoid heat accumulation at
Round off sharp transitions
sharp transition area
19

### Segment 26 (page 26)

Chapter 3 - Gloss/Gloss Differences
Remedy method
Why?
Uniform wall thickness
Avoid heating accumulation
distribution
on tool surface due to uneven
cooling
Enlarge gate and runner size
Shorten flow length or
Improve packing and minimize
increase number of gates
shrinkage difference
3.2.3 Material:
Remedy method
Why?
Increase flow ability (adding
flow modifier additives)
Enhance impression between
Reduce reinforcement
plastic and tool surface
(glass/carbon fiber) content
Reduce filler content
Avoid the gloss difference
Sufficient drying
caused by moisture streaks
3.3 Checkpoints
Get processing protocol.
Venting channel been blocked or crushed?
Tool cleanliness and integrity
- Mold deposits, dirt
Check tool surface quality
- Corrosion and wear occurs?
Part design
- Thickness abrupt change area?
Runner and gate design
- Appropriate size? Location and numbers?
Processing stable
- Cushion, metering, part weight
Measure the real tool temperature
- Hot and cold spots on tool surface
Filling study
- Flow pattern, hesitation, weldline, air trap
Verify with natural color or different batches
EMS
20

### Segment 27 (page 27)

Injection Molding Trouble Shooting Guide
Chapter 4 - Jetting
4.1 Description
Jetting is seen as a spiral-shaped surface pattern from which
the structure of the jet is often possible to be identified, as is
shown by Figure 20.
Fig.20:-Sign of jetting
The gas will be entrapped by the folded melt strand during the de-
velopment of the spiral shape, as is shown by Figure 21. (Fig. 22
shows the fountain flow) and the fast jetting makes the gas being
unable to escape timely, thus the bubbles or burn marks occur.
For the glass fiber reinforced material, jetting not only affects
the stiffness, but also causes surface defects (bump, depression,
gloss difference and color deviation) of air trap and fiber streaks.
Fig. 21:Melt strand and air trap
Fig.22:Fountainflow
MS
Meltstrand
Air trap
4.2 Root cause
1. When the melt flow front enters the narrow gate, the injection
pressure increases abruptly, and the melt pressure increases
correspondingly. Hence, the melt volume will be highly com-
pressed. After entering into an open and larger cavity area,
the pressure releases and the volume rapidly expands due to
the reducing of flow resistance. This is why jetting occurs.
21

### Segment 28 (page 28)

Chapter 4 - Jetting
2. Extremely high injection speed also causes jetting - high
speed results in the melt flow to travel in various directions in
a turbulent flow pattern.
3. The melt strand fills the cavity in an undefined filling process
due to the adhesion loss between melts and tool surface.
4.2.2 Formation of jetting
1. Melt strand formation
2. Melt strand forces together without homogeneous bonding
3. Form a brittle and wrinkled part
Fig.23:-Shortshotofformation
40% filling
70% filling
85% filling
99% filling
4.3 Remedy
4.3.1 Processing:
Fig.24:-Hintsonstagedinjectionprofile
(1
Melt reaches the gate
(2)
Melt enters the cavity
(1)
(2)
Set ram speed
Ram (Advancing) speed
V3
WithClosed-Loopcontrol
V1
V4
Time (or Stroke %)
EMS
22

### Segment 29 (page 29)

Injection Molding Trouble Shooting Guide
Remedy method
Why?
Reduce injection speed
Avoid the formation of
Apply a staged injection
2
melt strand
profile (slow-fast-slow)
Increase part quality and
3
Increase melt temperature
toughness
Increase part quality and
4
Increase tool temperature
toughness
4.3.2 Part and tool design:
Remedy method
Why?
Ensure that the emerging melt
encounters an obstacle immedi-
ately after the gate
Move gate position to more
favorable areas
Avoid the formation of
melt strand
Enlarge the gate size and apply a
radius at transition
Change the gating type (fig.25)
Apply pre-distributor (fig.26)
4.3.3 Material:
Remedy method
Why?
Use material with higher visco-
Avoid the formation of
sity (higher molecular weight)
melt strand by reducing
melt flow ability
Increase filler content
Fig.25: Recommended gating type
Overlap gate
Tab gate
Fan gate
23

### Segment 30 (page 30)

Chapter 4 - Jetting
Fig.26: Pre-distributor
Normal runner design
Pre-distributor runner design
Fill time
Fast filling speed
Fill time
=0.2127[s]
=0.2127[s]
[s]
[s]
0.2200
0.2200
0.1650
0.1650
0.1100
0.1100
0.0550
0.0550
Slow filling speed
0.0000
0.0000
4.4 Checkpoints
Check the processing settings
- Injection speed (especially speed of passing gate), melt
temperature, tool temperature,etc.
Check the tool design
- Appropriate gate location and type
- If possible, add an obstacle feature opposite of the gate
Measure the tool and melt temperature
Is maintenance of venting OK?
Filling study
√ Is moisture content OK ("too high - too low")?
EMS
24

### Segment 31 (page 31)

Injection Molding Trouble Shooting Guide
Chapter 5 - Record Groove/Flow Mark
5.1 Description
The part exhibits fine grooves (depressions and elevation) at the
surface area. Normally, circular grooves tend to form with a pin
gate and parallel grooves with a film gate or at the end of flow,
and propagate along the flow path of the melt front. (The ap-
cord.)
Fig. 27 - Sign of groove
5.2 Root cause
Rapid melt cooling causes the flow hesitation, and finally
result in flow marks. There are 3 fundamental reasons for rapid
cooling
· Too-low injection speed
· Too-low melt temperature
· Too-low tool temperature
5.3 Formation of a record groove
Flow front melt on tool surface cools quickly and the rapidly
cooled skin hinders the direct flowing of melt to the tool surface,
which causes the hot melt be transferred to the tool wall in an ab-
normal way but stretched in the middle of the flow front.
At a certain pressure the melt is again pressed against the tool
surface. The overcooled areas, however, have no full contact
with the mold wall thus forming a wave. This condition occurs
generally as a result of rapid cooling and slow injection (i.e. dur-
ing transition from thin wall to thick wall areas).
25

### Segment 32 (page 32)

Chapter 5 - Record Groove/Flow Mark
Fig.28: Flow front
Flow front has cooled down
near the wall
Cooled down peripheral layer
hinders the flow front to the
wall directly
Flow front touches mold
wall again
Notes:Theblue area indicates solidified layer
5.4 Remedy
5.4.1 Processing:
Remedy method
Why?
Increase injection speed or
apply a staged injection
profile (slow - fast - slow)
Increase melt and tool
Avoid melt flow front
temperature
freezing too quickly
Ifit only occurs in gate area,
increase nozzle temperature
gradually (5°C each step)
Sufficient packing to allow
Increase holding pressure
4
the melt to be compressed
level
more densely
EMS
26

### Segment 33 (page 33)

Injection Molding Trouble Shooting Guide
5.4.2 Part and tool design:
Remedy method
Why?
Move gate to more favorable
areas
Adjust (increase, reduce, unif-
orm) wall thickness if possible
Obtain constant flow front
Smoothen transition areas
Avoid family tools with
different flow resistance
Increase gate size or numbers
Obtain efficient packing
5.4.3 Material:
Remedy method
Why?
Use high flow-ability and slow
solidification material
Avoid rapid solidification of
Use flow modifier (enhancer)
the melt flow front
additives
5.5 Check points:
Check the processing settings
- Injection speed
Measure the tool and melt temperature
Filling study
Complicated part design?
- Wall thickness distribution, layout of ribs
Check the nozzle area's temperature
- Avoid cold slug
27

### Segment 34 (page 34)

Chapter 6 - Stress Cracking
Chapter 6 - Stress Cracking
6.1 Description
What is internal stress? Plastic internal stress is a kind of inter-
nal stress caused by the influence of macromolecular chain ori-
entation and cooling contraction in the process of plastic melt so-
lidification.
The essence of internal stress is an unbalanced structure, which
formed during the melting process of macromolecular chains
and can't be immediately restored to equilibrium during solidi-
fying and cooling. The essence of the unbalanced conformation
is a reverse high elastic strain, which was frozen in the plastic
product (usually in the form of potential energy).
Under mechanical loading and chemical erosion (contact with
solvent, agent, etc.), the frozen unbalanced structure will be con-
verted to a free and stable structure, as a result the potential en-
ergy converts into kinetic energy and is released.
When the intermolecular force cannot afford the kinetic energy,
the internal stress balance was destroyed, thus micropores and
cracks will be produced and gradually will form stress cracking.
Almost all injection molding plastic products will have internal
stress in various degrees, especially the amorphous thermoplas-
tics, which have a high sensitivity to internal stress.
Internal stress not only makes plastic products deform and crack
during storage and usage, but also affects the mechanical prop-
erties, optical properties, electrical properties and appearance
quality.
6.2. Classification of internal stress
The stress can be divided into the following categories accord-
ing to the reasons that cause internal stress.
1. Orientation stress
During the filling and packing stage, the directional arrange-
ment of macromolecular chains along the flow direction were
EMS
28

### Segment 35 (page 35)

Injection Molding Trouble Shooting Guide
frozen, and then produce a kind of internal stress.
Normally the out-layer of the melt has the highest shear rate,
whilst the minimum is in the central layer therefore the orienta-
tion stress distribution of the plastic product tends to get smaller
from the surface layer to the central layer of the part.
II. Cooling stress
n s s s s
shrinkage of the melt during solidification. Especially for the
thicker part, the out layer cools down, solidifies and shrinks
first, whilst the inner layer of the melt may still be hot, so that
the surface layer will limit the core layer's contraction, resulting
in surface layer in the compressive stress state, and the core
layer in tensile stress state.
The cooling stress distribution of the plastic products is tending
to become larger from the surface layer to the central layer of the
part.
Besides, for metal insert over-molding, it is easy to form a
shrinkage internal stress due to the different thermal expansion
coefficient between the metal and plastic.
In addition to the above two kinds of internal stress, there are
also other kinds of internal stress (account for a small propor-
tion), e.g. crystallization internal stress (the internal stress ap-
pears due to the different crystal structure and crystallinity),
structure internal stress and demolding internal stress.
6.3 Detection method of internal stress
Usually put the parts into the solvent for 15s to 2mins, then take
out and determine whether there is a stress based on the result of
cracking. For transparency materials, the stress situation can be
checked through using a polarizing film.
Table 1: Commonly used solution for the stress detection
ABS
Kerosene, glacial acetic acid
PA
N-heptane, M-cresol
PC
Carbon tetrachloride
PSF
Carbon tetrachloride
PS
Kerosene, glacial acetic acid
PPO
Carbon tetrachloride
29

### Segment 36 (page 36)

Chapter 6 - Stress Cracking
6.4 Remedy
6.4.1 Processing:
Remedy method
Why?
Optimize switch over point
Avoid orientation stress
Use less holding pressure/
caused by over-packing
2
time (limited by sink mark
and voids)
Apply a staged injection
Avoid producing high
profile (slow - fast - slow)
orientation stress during
and graduated holding
injection and packing
pressure (high-low)
stage
Slow down the cooling
Increase melt and tool
rate and speed up stress
4
temperature
relaxation and strengthen
disorientation
Reduce orientation stress
Apply injection compression
level occurred in injection
molding
and packing stage.
Avoid high demolding
Adjust injection and packing
stress via making the tool
6
time
opening pressure close to
the atmosp-here pressure
Fig.29: Stress levelcomparison
Injection moulding
Injection compression molding
EMS
30

### Segment 37 (page 37)

Injection Molding Trouble Shooting Guide
6.4.2 Tool and part design:
General Remedy method
Why?
Avoid sharp edges, right
In order to reduce the
angles, notches and a sudden
internal stress concentration
enlargement or reduction of
factor
the cross section
Make a gradient transition at
Avoid the cooling and
the abrupt thickness change
orientation stress cause by
area.
uneven cooling
Appropriate design of the
Avoid stress concentrate at
(metal) insert-see chapter
the bonding area
19, page 72
Design a round hole rather
than square, diamond holes,
In order to reduce the int-
and the ellipse hole is the best
ernal stress concentration
(the long axis should parallel
factor
to the force direction)
Gate into thick wall area
Apply a gate diameter as big
Avoid the orientation stress
as possible (0.8x nominal wall
caused by the high injection
thickness)
speed and pressure
Aim for uniform wall thickness
Appropriate cooling layout
Avoid cooling stress
Appropriate demolding angle,
high polish of the core and
Avoid the demolding stress
large area of ejection.
Reduce the shear stress level
Apply pre-distributor
at gate area
* Gate and runner design:
Avoid steps, sharp angles and grooves at the runner which gen-
erate shear stress and frictionheat
Gate design with generous radii is highly recommended
Apply a tab gate (see page 23, Fig.25): make the high stress level
area locate in the tab gate and then trim it after demolding.
31

### Segment 38 (page 38)

Chapter 6 - Stress Cracking
Fig.30:Indication of runner design
No Steps
Adding radii
No sharp angle
No groove
* Ribs and bosses fillets:
fillet radius rules: implement large radius under the premise of
non-sink marks visible on top surface
Fig.31: Indication of radius design
Stress Concentration Factor [-]
r=Radius
3.5
s = wall thickness
r >0.4 to 0.6s
3.0-
2.5
Typical value
2.0
1.5
1.0
r/s
0.2
0.4
0.6
0.8
1.0
1.2
1.4
6.4.3 Material:
Remedy method
Why?
Less orientation stress level
Increase the flow ability
under the low injection and
packing pressure
Demolding modification
Reduce the demolding stress
Micro-crystalline modi-
Nuclear can prevent propagation
fication grade
of the crack to a certain degree
EMS
32

### Segment 39 (page 39)

Injection Molding Trouble Shooting Guide
Remedy method
Why?
Prefer materials with slower
It is beneficial to stressing
solidification speed (Grilamid
relaxation and strengthening
TR60 > Grilamid TR90)
disorientation
Use the resin with high
molecular weight and narrow
Improve stress cracking
molecular weight distribution
resistance
Fiber reinforced/high crystal-
linity material
6.4.4 Heat treatment - annealing
The annealing of plastic products is the best method to elimi-
nate the internal stress by staying at a certain temperature for
some time. It makes the polymer molecule convert to equilib-
rium. The forced frozen part (during molding) has an unstable
high elastic deformation and needs energy for relaxation,
thereby reducing or substantially eliminating the internal stress.
Normally the annealing temperature is 10 to 20°C higher than
the usage temperature or 5-10°C lower than the HDT, and the an-
nealing time is dependent on the type of plastic, wall thickness,
temperature used and the processing setting. Generally for the
a i s
increase of thickness, the annealing time should be extended as
well. Increasing annealing temperature and time have a similar
effect while the latter is much more effective.
The heating medium has a significant effect on the annealing.
The common used mediums are air, water, glycerin, mineral oil,
ethylene glycol, liquid paraffin, etc. for Nylon products. We rec-
ommend using water or potassium acetate solution (boiling
point 120°℃) which can prevent the oxidation effect (vellowing)
during annealing and speed up to achieve equilibrium of the
moisture absorption.
Carrying out annealing on the demolded parts immediately is
much more beneficial to reducing the stress level. Increasing
tool temperate and extending the cooling time and heat preser-
vation for the demolded part is also helpful to reduce the stress
level.
33

### Segment 40 (page 40)

Chapter 6 - Stress Cracking
Notes: Long annealing time for the amorphous material (like
PC) will result in below defects:
1). Molecular rearrangement, even crystallization, so as to re-
duce notch impact strength.
2). Part deformation
Therefore, the annealing should not be used as the only way to
reduce the internal stresslevel.
6.6 Check points
Get the crack sample: check break area
Residual stress checking with polarized film (suitable for
transparency part)
Check the process settings:
- Injection speed, V/P switchover point, packing time and
Measure the real melt and tool temperature
Filling study (flow pattern, hesitation, weldline, air trap...)
Filling study
- Fill pattern, hesitation, weld line and air trap
Part and tool design
- Uniform wall thickness distribution, sharp corners?
Gatelocation andsize
On-site testing
- Reasonable method, crack starts position
Post-processing/treatment (painting, heating, drilling, and
gluing etc.)
EMS
34

### Segment 41 (page 41)

Injection Molding Trouble Shooting Guide
Chapter 7 - Short Shot
7.1 Description
What's a short shot? The cavity isn't filled which causes the miss-
ing of details of the product.
Fig. 32: Sign of defects
Fig.33:Fillingproblem near thin ribs
Flow front
Poor venting
7.2 Root cause
Reasons for a short shot can be:
Too small shot volume of the injection molding machine
Premature freezing of a channel cross-section (e.g. low injec-
tion speed or wrong temperature control in the mold)
The mold venting being inadequate (= air entrapment)
Injection pressure being not sufficient due to excessive flow
length
Melt flow back to the barrel due to the defect of non-return
valve
Excessive melt leakage between the nozzle and sprue bush
35

### Segment 42 (page 42)

Chapter 7 - Short Shot
7.3 Remedy
7.3.1 Processing:
Remedy method
Why?
Make sure there is enough
Increase metering stroke
material to fill part
Increase injection speed
and pressure (valid for
Increase the amount of material
hydraulic IMM machine)
into cavity before solidification
for thin walled parts
Increase melt and tool
3
Increase material flow-ability
temperature
Reduce V/P transfer
point closer to end of fill
4
(inparticular for thin
Increase the amount of material
wall/ complex parts)
into cavity before solidification
5
Increase holding pressure
6
Increase backpressure
Control drooling
Avoid material leakage at
(process stability)
nozzle area
Avoid short shot caused by
8Balance the filling
hesitation (race-tracking effect
-see details on page 38)
7.3.2 Part and tool design:
Remedy method
Why?
Increase and make uniform
wall thickness of the comp-
Avoid race-tracking effect
onent
Increase injection speed
and pressure (valid for
Avoid premature freezing of
hydraulic IMM machine)
runner and gate
for thin walled parts
Improve venting
Reduce flow resistance
Relocate /add gates
Reduce the material flow length
EMS
36

### Segment 43 (page 43)

Injection Molding Trouble Shooting Guide
Remedy method
Why?
Avoid or balance family tools
Uniform cooling layout
Avoid short shot caused by
hesitation
Locate gate at thick area
instead of thin area
Apply vacuum evacuation to
Reduce flow resistance
eliminate air in cavities
7.3.3 Material:
Remedy method
Why?
Avoid over-dried material
Slow solidification and lower
viscosity
Improve the flow-ability
Less filler and fiber content
Flow modifier additives
(enhancer)
7.3.4 Injection machine & auxiliaries:
Remedy method
Why?
Gas assisted injection molding
Reduce the injection press-
Injection compression molding
ure via thickening the part
Switch to electrical injection
Provide efficient injection
molding machine
pressure & speed
7.4 Check points
Check machine size:
- Shot volume to < Max. 90% metering stroke
Check the process setting
- Injection speed, V/P switch over point and pressure profile
Measure the real melt and tool temperature
Check for location of defect
- Flow end? Bottom of rib? Thin area?
Check part design
- Thickness distribution, depth of rib
37

### Segment 44 (page 44)

Chapter 7 - Short Shot
Check tool design
-Gateamounts,size andlocation
Filling study or moldflow analysis
Stability of the processing
- Metering, cushion and part weight
Drooling or leakage at nozzle area
※ Explanation of the racetrack effect
Figure 34 show an example of the racetrack effect. The part con-
sists of a thin top, nominal wall on the sides, and a heavy rim. The
part is gated in the rim. Race tracking occurs because the polymer
will take the path of least resistance, therefore favoring the heavy
rim. The flow front will "race" around the heavy rim. This will of-
ten cause serious problems with filling, including air traps and
weld lines. With an understanding of the basic principles involved,
it is possible to completely control which flow path fills first.
Fig.34 fill pattern of the race track
Thin top
Gate
Nominal wall
Thick rim
EMS
38

### Segment 45 (page 45)

Injection Molding Trouble Shooting Guide
Chapter 8 - Flash
8.1 Description
Flash refers to the excess material around parting lines, ejector
pins, or openings in the part. (The visible degree of the flash of-
ten gets worse after the painting process.)
Fig. 35: Large and small area over-spraying (flash)
8.2 Root cause
Reasons for flash can be:
An oversized gap at parting lines, inserts, slides, etc., due to in-
sufficient tool accuracy
An insufficient stiffness of the tool and/or insufficient ma-
chine's clamping force which results in the parting surfaces
opening (breathing) too much so that the melt flows into the
parting surfaces and forms the flash
Rheological properties of material (a low viscosity material
will flow much easier into an available gap)
A key parameter namely obvious cavity pressure. The higher
the pressure is, the larger the flash size/risk will be.
8. 3 Remedy
8.3.1 Processing:
Remedymethod
Why?
Increase clamping force
Reduce the cavity pressure
Reduce holding pressure level
39

### Segment 46 (page 46)

Chapter 8 - Flash
Remedy method
Why?
Adjust/optimize switch over
3
point
Reduce the cavity pressure
4
Reduce the injection speed
Lower the melt temperature
5
gradually (5°C steps)
Avoid flash via reducing
Lower the mold and nozzle
flow ability
6
temperature gradually (5°C
steps, check V/P position)
8.3.2 Part and tool design:
Remedy method
Why?
Increase number support pillar
and thicker tool plate
Tool modification to ensure:
- reduction of the slide core
Eliminate the risk of flash
clearance
via improving tooling
- improved tool (matching)
stiffness and precision
accuracy
Apply appropriate venting size
Extensive use of mold interlocks
(alignment)
Reduce flow length by adding
more gates or improving balance
Avoid flash occurs caused
Shorten runner length and
by high injection pressure
increase runner size
8.3.3 Material:
Remedy method
Why?
Use higher amorphous content
material
Avoid flash via reducing
Use higher molecular weight
flow-ability and increase
polymer
viscosity
Increase fiber and filler content
EMS
40

### Segment 47 (page 47)

Injection Molding Trouble Shooting Guide
8.3.4 Check points:
Check the location of the flash occurred
- Parting line, slider, inserts, and ejectors
Check the support pillars in the tool
- Amounts, even distribution?
Check parting line mismatch with pressure sensitive paper
(rating 1400 to 7000psi or 1000 to 18000psi)
Check when flash occurs
- At filling or packing stage?
Check maintenance of venting
Measure the real melt and tool temperature
- Temperature differential in different zones
√Is moisture content OK?
41

### Segment 48 (page 48)

Chapter 9 - Ejector Marks
Chapter 9 - Ejector Marks
9.1 Description
The ejector marks refer to the contour of the ejector which is vis-
ible on the ejected part. It can be sorted into “raised" and “sun-
ken" ejector marks. Due to thickness and (cooling) shrinkage dif-
ference of the wall, gloss differences may occur.
Fig.36:Glossdifferencesnear the
Fig. 37: Shrinkage near an overheated
ejector
andpoorlyfittedejector
9.2 Root cause
Reason for the ejector mark can be sorted into:
High demolding forces due to unfavourable parameter settings
(insufficient cooling, high ejector force, over-packing, etc.)
Tooling design issue e.g.:
- wrong fitting or wrong ejector length
-toosmallejectordiameter
- ejector located at thick area
Temperature difference
- High temperature differences between ejector and mold wall
Incorrect draft design, long demolding stroke
Uneven ejector system distribution
Vacuum effect during ejection (large adhesive force)
EMS
42

### Segment 49 (page 49)

Injection Molding Trouble Shooting Guide
9.3 Remedy
9.3.1 Processing:
Remedy method
Why?
Ensure the demolding tem-
Extend cooling time
perature is lower than HDT
2
Adjust V/P transfer position
3
Reduce holding pressure level
Avoid over-packing
4
Reduce holding time
Avoid a "rise" on part
5
Reduce ejecting speed/force
surface caused by high
ejection force
Decrease tool temperature on
Eliminate the hot spot at
6
core side
ejector area
Less cooling time, speed
7
Decrease melt temperature
up solidification
9.3.2 Part and tool design:
Remedy method
Why?
Increase number of ejectors,
enlarge ejector size and balance
ejectors distribution
Reduce/Balance the
ejecting force
Correct ejector's end position
- Parallel to the parting surface
Avoid rough part surface
Improve venting
caused by burnt mark and
deposits on tool surface
Increase the stiffness of
Increase wall thickness
the nominal wall
Add air blow valve
Avoid vacuum effect
Improve polishing along the
Reduce demolding force
demolding direction
Increase draft angle
Reduce demolding force
Avoid the design of forced
Avoid sticking onto the
demolding structure
tool
43

### Segment 50 (page 50)

Chapter 9 - Ejector Marks
9.3.3 Check points:
Check the process settings
-Packing time and level
Check for ejector system and movements/position
Tool surface finish checking (polishing)
Check draft angle
Check for undercuts and stickiness
Conduct filling study
Measure the real melt & tool temperature
- Uniform temperature distribution. Check if there is cold or
hot spots on the tool
Check for venting system
EMS
44

### Segment 51 (page 51)

Injection Molding Trouble Shooting Guide
Chapter 10 - Delamination/Flaking
10.1 Description
The delamination refers to the layers of material which are not
homogeneously joined together and start flaking. Normally, it
occurs at the gate or on the molded part, and can be either large
or very small and thin depending on the intensity. Sometimes it
is not so easy to recognize such delamination when the surface
is unharmed or un-cut out however it is easy to blister when put
into the oven.
Fig.38:Signofdelamination
10.2 Root cause
The reasons to cause the delamination can be sorted of:
Delamination of surface layers is due to insufficient bonding
of adjacent surface layers.
Different layers are formed by different flow effects and cool-
ing conditions over the cross-section.
Shear stresses and inhomogeneities can reduce the bonding of
these layers to such a degree that single surface layers start flak-
ing off as is shown in figure 39.
45

### Segment 52 (page 52)

Chapter 10 - Delamination/Flaking
Fig.39:Delaminationonacross-sectionofamolded
part with different structure formation
High shear stresses and thermal damage can be caused by:
High injection speed
High melt temperature
Sharp corners and sub-gate
High moisture content in the granules
Inhomogeneities can be caused by:
Impurities or other materials among the granules
Incompatible dye or master batch
Poorly plasticization
Partially crystalline melts where layers are formed with differ-
ent crystal structures -- structure is inhomogeneous
10.3 Remedy
10.3.1 Processing:
Remedy method
Why?
Reduce injection speed through
Avoid high shear rate at
the gate
the gate
Apply staged injection profile
Avoid the injection of cold
Increase nozzle temperature
slug into the cavity
Adjust melt temperature
1. If caused by high shear stress,
then reduce melt temperature
2. If caused by inhomogeneities,
Secure sufficient
thenincreasemelttemperature
plasticization in the barrel
Increase back pressure and
reduce dosing speed
EMS
46

### Segment 53 (page 53)

Injection Molding Trouble Shooting Guide
10.3.2 Part and tool design:
Remedy method
Why?
Avoid overheated at dead
Improve venting
areas
Increase gate size
Increase wall thickness and
Reduce the shear rate thru
smoothen transitions
the gate
Add radius at the gate
Independent cooling at the
Secure sufficient cooling
gate if hot runner is used
10.3.3 Material:
Remedy method
Why?
Use lower solidification speed
material
Reduce the shear stress via
Use material with less fiber
improving the flow ability
content
Use lower viscosity material
Use compatible pigment or
Avoid incompatibility
master batch
Secure correct material
Prevent contamination
handling
10.4 Check Points:
Check the process settings
- Injection speed, dosing speed, back pressure and etc.
Measure the real melt temperature
Check for moisture content
Check for contamination
Check for melt homogeneity
Check for compatibility of pigment or masterbatch
Sufficient cooling around the gate (if hot runner is used)
Use virgin/natural color
-Ifthedelamination occurs
47

### Segment 54 (page 54)

Chapter 11 - Cold Slug
Chapter 11 - Cold Slug
11.1 Description
Cold slug refers to the mark on the molded part caused by melt
which has been cooled in the nozzle or in the sprue system and
been injected into the cavity. Normally it is often visible as a
comet tail on thin-walled or transparent parts. And an inner de-
fect may occur on thick walled parts. Besides, the cold slug may
create narrow sections in the cavity which will be encapsulated
(=weldline).
Fig. 40: Sign of cold slug
11.2 Root cause
Reasons for the cold slug can be sorted into:
The too-cold machine nozzle and the material solidified there
and injected into the cavity
Melt emerging (drooling) from the nozzle, cooling down and
been injected into the cavity
A non-aligned or fitted nozzle with the sprue bushing might cre-
ate dead ends where cold material can develop and is injected
into the cavity
E.g. when the tip of a submarine gate which uses brittle materi-
als breaks
Granules that unmelted throughly been injected into the cavity
EMS
48

### Segment 55 (page 55)

Injection Molding Trouble Shooting Guide
11.3 Remedy
11.3.1 Processing:
Remedy method
Why?
Increase nozzle temperature
-if caused by solidified material
at nozzle
Avoid the injection of
Retract plasticization unit earlier
cold material into the
Increase nozzle diameter
cavity
Avoid drooling by reducing back
pressure and increasing/
applying screw decompression
11. 3. 2 Part and tool design :
Remedy method
Why?
Add a cold slug catcher at end of
sprue runner
Avoid the injection of
Add cold well at end of runner
cold material into the
cavity
Align nozzle with sprue bushing
(Rnozzte<Rbushing)
11. 3. 3 Material:
Remedy method
Why?
Avoid cold material of
Avoid using materials with fast
the nozzle area been
solidification
injected into the cavity
Avoid the cold material
Using materials with higher
caused by drooling been
viscosity
injected into the cavity
11. 3. 4 Injection machine and auxiliaries :
Remedy method
Why?
Using a shut-off nozzle
Avoid drooling
Using a reversed tapered nozzle
49

### Segment 56 (page 56)

Chapter 11 - Cold Slug
Remedy method
Why?
Avoid cold material of the
Increase number of nozzle
nozzle area been injected
heaters or shorten nozzle length
into the cavity
Fig.41: Illustration of reversed tapered nozzle(drooling and freezing control)
Thermocouple well
0.25mm
radius
Diameter
to suit
-0.32cm
3D-
Taper to suit
10D
Dminimum=0. 32cm,Dtypical=0. 48cm~0. 64cm
11.4 Check point:
Check for optimized time control in the cycle
- Injection, packing, cooling, plasticization and retract time
Check for nozzle temperature control
Sufficient cold well for the runner system
Check moisture content
Check design of submarine gate
Perform paper test
Check the moisture content in case of the cold slug was caused
by drooling
EMS
50

### Segment 57 (page 57)

Injection Molding Trouble Shooting Guide
12.4 Check points:
√ Check for contamination (foreign material, dirt, dust) and purg-
ing procedure (see page 78)
Check processing history (material change)
Check for machine maintenance (screw pulling out)
Check cleanness of nozzle tip
Measure the real melt temperature
Check for hot runner or shut off nozzle
Check melt cake and granules
Check the plasticization unit for wear and dead spots
Check the alignment between the nozzle and sprue bush
53

### Segment 58 (page 58)

Chapter 13 - Gate Bloom (Matt Point)
Chapter 13 - Gate Bloom (Matt Point)
13.1 Description
Gate bloom refers to the matt area with concentric rings (micro
waves), which appears at around gate area. Sometimes cold mate-
rial enters the cavity also will cause the gate boom.
Fig.46:Sign ofmatt points
13.2 Root cause
Reason forthe gate bloom can be sorted into:
Matt points near the gate caused by high shear rates by too high
flow rates or too small gate sections.
RheologyRelationshipIndication:
Shear stress
Shear rate
(π)~
()
r3
r3
二
Volume flow
=
Gate radii
The high shear stresses on the mould wall resulting in the melt
losing its wall adherence
The highly sheared layer sliding off the mold wall even resul-
ting in melt fracture, and finally appearing as a matt point
Fig.47:High shearratematerial flow intocavity
Layer slides off the mould
wall even crack
EMS
54

### Segment 59 (page 59)

Injection Molding Trouble Shooting Guide
13.3 Remedy
13.3.1 Process:
Remedy method
Why?
Reduce the injection speed
Reduce the shear rate at the
through the gate
gate area
Increase melt temperature
Avoid melt front freezing too
Increase nozzle temperature
early at gate area
Increase tool temperature
13.3.2 Tool and part design:
Remedy method
Why?
Enlarge gate size
Round off the gate
Gate into thicker wall area
and avoid large re-direction
of the melt
Reduce the shear rate
Ensure smooth transitions
between cross section
Apply a pre-distributor (see
page 24)
13.3.3 Material:
Choose a high flow-ability material
Try to use low viscosity material
13.4 Check points:
/ Tool design
- Size ofthe gate and runner
- Runner balance
Process settings
- Injection speed
Filling study
- Short shot (focus on gate area)
/ Measure the real Melt-tool temperature
55

### Segment 60 (page 60)

Chapter 14 - Tool Deposits
Chapter 14 - Tool Deposits
14.1 Description
The tool deposits refer to the sediment occurring on tool and
part surface due to the precipitin (transfer) of the small molecu-
lar substances and additives during molding process. And it will
result in:
· Poor surface quality and non-reproducible surface structure.
Process and quality instabilities, e.g. blocked venting channels
can cause burn marks, bad weldline strength, unfilled parts,
higher injection pressure, flash and increased material degrada-
tion
Fig.48: Sign of tool deposits
14.2 Root cause
Reasons to cause the tool deposit can be sorted into:
Bad molecular distribution and low molecular weight polymer
prone to separate out with time
Hydrolysis caused by high moisture making the low molecular
weight polymer easy to separate out
Flame retardants reacting at high temperatures, forming decom-
positions which may produce deposits.
Impact modifiers and pigments affected by excessively high
temperatures and also by shear.
In areas of overheating (such as cores), modifiers, stabilizers
and other additives may stick to the surface and build up depos-
its.
Modifiers separate from the polymer and form deposits on the
cavity surface.
Inadequate venting leading to diesel effect
EMS
56

### Segment 61 (page 61)

Injection Molding Trouble Shooting Guide
14.3 Remedy
14.3.1 Processing:
Remedy method
Why?
1
Decrease melt temperature
Avoid overheating and re-
duce the risk of precipit-
Machine utilization between
2
50% - 80% barrel capacity
ation of micro molecules
3
Adjust V/P position
Avoid burning at end flow
Reduce injection speed and
4
apply staged injection profile
Decrease screw speed and
5
Reduce the shear rate
back pressure
Reduce tool temperature
Avoid additives sticking
6
(especially at cores)
on the core
Reduce screw decompression
Avoid material oxidation
14.3.2 Part and tool design:
Remedy method
Why?
Increase channel size of runner
/gate section
Reduce the shear rate
Reduce sharp corner and round
off transitions
Avoid additives sticking
Application of copper/beryllium
on the core via fast heat
cores
dissipation
Apply vacuum evacuation
Reduce the risk of air trap
Degassing screw
Reduce surface roughness, tex-
Avoid occurrence of de-
turing (especially at ventsarea)
posit on the rough surface
Reduce filling pressure (add or
relocate gates)
Reduce the shear rate via
lowering cavity pressure
Balancing for multi cavity tools
Reduce amounts ofweld
Reduce flow ends
lines
57

### Segment 62 (page 62)

Chapter 14 - Tool Deposits
14.3.3 Material:
·Reduce volatile polymer components
Optimize demolding agent
- Adding a Masterbatch (MB) or compound it directly; (Do not
using stearate yields higher risk of deposits for flame retardant
products -too high agent content might be counter-productive)
Decrease oligomer content
Reduce the filler content (less shear)
Use natural color instead ofblack
14.4 Check points:
Check for sources of deposits
- Recipe , part or tool design, process setting
cially atsliders and cores)
Check process setting
- Injection speed, back pressure, cushion and etc.
Check runner and gate design
-Appropriatesize and avoid sharp corners
Analyze deposits
- FTIR, TGA, chromatography...
Check tool surface roughness
/ Apply filling study
Verifying with pure materials or natural color
Venting check and maintenance
14.5 Venting:
Appropriate venting design has a significant influence on the tool
deposits, so the following notices should be taken during tooling.
In all dead ends in which air may be trapped, vents must be
placed through parting line, additional ejectors, venting blocks
(porous steel, lamellar packs), split mold insert, hole-in core
venting, etc...
Apply venting on flow ends and runner system
Polish venting areas
Increase venting depth
Lay flow end in parting line
EMS
58

### Segment 63 (page 63)

Injection Molding Trouble Shooting Guide
Venting design:
1. Runner venting
W:1.5-2mm
Venting Channel
first venting width)
H2:1mm
H1
first venting depth)
Runner
2. Parting line venting
Pitch25mm
Cavity
Part
5mm
mm
H1
W:1.5-2mm
first venting depth)
5mm
300
draft angle
2 mm
10 mm
3. Venting trough ejector pins and inserts
3D (Max.10mm)
A
1. 5mm (and)
D+0.
8
(venting depth)
SectionA-A
R2. 5x 1mm dep.
59

### Segment 64 (page 64)

Chapter 14 - Tool Deposits
Notes:
Venting channels must extend to the edge of the mold
Sufficient venting for the entire part is necessary, especially in
weldline and dead end area
H1 various from material type - for HT&GV, H1<0.02mm
EMS
60

### Segment 65 (page 65)

Injection Molding Trouble Shooting Guide
Chapter 15 - Part Sticking on Core Side
15.1 Description
The part is not pulling out of the core half (ribs/protrusions), and
in rarer circumstances cannot be ejected off of the male cores.
Extensive sticking in combination with high demolding forces
may lead to component deformation and/or damage
The demolding force can be influenced by part and tool design,
processing and plastic materials
15.2 Root cause
Reasons for sticking on core side can be sorted into:
High affinity between tool steel and plastic material (influenced
by contact temperatures).
The amount of shrinkage which is directly connected with the
needed demolding force. (Higher shrinkage increases the risk
of sticking.)
Design which often plays a major role and demolding problems
which are often related to rough surface finish, long core stroke
length and insufficient draft angles (e.g. in case of sleeve-
shaped and box-shaped parts).
15.3 Remedy
15.3.1 Processing:
1. Reduce tool temperature
2. Adjust V/P position - delay
3. Adjust holding pressure
4. Enhance knock-out action
5. Reduce melt temperature
6. Optimize cooling time
15.3.2 Part and tool design:
Improve the cooling efficiency of the core and slide
- Add channels or apply the Be/Cu inserts
Increase ejector size, number and change ejector system (air
ejection)
61

### Segment 66 (page 66)

Chapter 15 - Part Sticking on Core Side
· Polish the tool, sliders, ribs, pins along demolding direction
Reduce surface roughness
Decrease texturing
Increase draft angle
Heat removal (e.g. beryllium-copper pin/ insert)
Avoid the thickness accumulations
Enlarge gate size
Relocate gates (increasing holding pressure efficiency)
Balancing for multi cavity tools
Apply tool surface coating (e.g. Nickel/PTFE for Grilamid TR)
Tool surface coating (Diamond like Carbon and IKOS) for
Grivory HT showed improvements, and also in terms of depos-
its (but long term reliability still unclear!)
Apply core venting (vacuum)
15.3.3 Material:
Increase the filler content - Less shrinkage and more stiffer
Increase demolding agent - Adding MB or compound directly
Avoid unfilled extrusion grades
Increase amorphous content of semi-crystalline grades
Increase the stiffness of the material (higher stability)
15.4 Check points
√ Understand the tool operation and study the demoulding action
in slow motion - Smooth and synchronism
Measure melt and tool temperature with pyrometer (especially
at sliders and cores)
Check process setting
- Injection speed, packing pressure, V/P position and cooling
time
Check the 3D tool drawing
- Undercuts, depth and draft angle of ribs, ejector distribution,
etc.
Check wall thickness distribution
Check tool surface cleanness and integrity
Use demolding spray
Check gate designs - may cause sticking (banana/cashew gates
etc.)
EMS
62

### Segment 67 (page 67)

Injection Molding Trouble Shooting Guide
Chapter 16 - Part/Runner Sticking
on Cavity Side
16.1 Description
Runner/Sprue is getting not pulled out of the fixed mold half
Part is getting not pulled out of the cavity side or is deformed
during ejection.
, (
age"and also sticking which will require high demoulding
forces. This may lead to part deformation and/or damage
The demolding force can be influenced by part and tool design,
processing and plastic materials
16.2 Root cause
Reasons for sticking on cavity side can be sorted into:
High affinity between tool steel and plastic materials (influ-
enced by contact temperatures).
The amount of shrinkage which is too less and the part which
cannot disconnect from the cavity side.
Design which often plays a major role and demolding problems
which are often related to rough surface finish and insufficient
draft angles as well as tool inaccuracies (sliders and pullers)
16.3 Remedy
16.3.1 Processing:
1. Decrease holding pressure level
2. Reduce holding pressure time
3. Adjust V/P position (avoid V/P too late)
4. Apply graduated injection profile (slow-fast-slow) and gradu-
ated holding pressure (high-low)
5. Increase cooling time
6. Adjust injection speed
7. Increase melt and nozzle temperature
8. Adjust tool temperature
9. Apply plasticization unit retraction (in case of sprue sticking)
63

### Segment 68 (page 68)

Chapter 16 - Part/Runner Sticking on Cavity Side
16.3.2 Part and tool design:
Decrease texturing
Apply undercuts, puller and puller pins in order to have the
part ideal separated from the cavity side
Increase/Change ejector size/number/system
Polish the tool, sliders, ribs and pins along demolding direc-
tion
Improve surface roughness
Increase draft angle
Balancing for multi cavity tools
Appropriate rib design and distribution
Reinforce tool stiffness
Apply coating (e.g. Nickel/PTFE for Grilamid TR)
Tool surface coating (see page 62)
16.3.3 Material:
Easy flow material (less injection pressure)
Decrease the filler content (higher shrinkage)
Increase demolding agent
- Add MB or compound directly
Switch to material with higher crystallinity
Increase stiffness in case of part deformation during ejection
16.4 Check points:
√ Understand the tool operation and study the demolding action in
slow motion ( Smooth and synchronism)
√ Measure melt and tool temperature with pyrometer (especially at
sliders and cores)
√ Check process setting, e.g. injection speed, packing pressure, V/P
position and cooling time
√ Check the 3D tool drawing, e.g. undercuts, depth and draft angle
of ribs, ejector distribution and etc.
√ Check wall thickness distribution
√ Check cleanness and integrity of tool surface
√ Use demolding spray
√ Check for gate designs which may cause sticking
(banana / cashew gates etc.)
EMS
64

### Segment 69 (page 69)

Injection Molding Trouble Shooting Guide
Chapter 17 - Nozzle Drooling
17.1 Description
The drooling refers to the leakage of material out of the nozzle
during or after the metering. Drooling may lead to filling incon-
sistencies due to different shot volumes and sometimes drooling
is related to stringing of the sprue. Besides, drooling in combina-
tion with unit retraction might lead to frozen or degraded material
into the cavity (cold flow lines and burn marks).
17.2 Root cause
a). Causing by the metering melt which is transported in front of
the screw by generating a specific pressure (caused by the
back- pressure)
b). By releasing the nozzle opening during retraction of the plas-
tification unit (or ejecting the part with sprue runner), material
might be able to leave the screw chamber depending on:
1). Back pressure
2). Melt viscosity
3). Nozzle design
4). Nozzle opening time
5). Moisture content
17.3 Remedy
17.3.1 Processing:
Remedy method
Why?
一
Reduce nozzle temperature
Reduce the flow -ability of
2
Reduce barrel temperature
material
Avoid overheating caused
Machine utilization between
3
by long residence time in
50% to 80% barrel capacity
barrel
Avoid drooling caused by
4
Reduce back pressure
high barrel pressure
Delayed or avoid plastifi-
Efficient heat dissipation at
5
cation unit retraction
nozzle area
65

### Segment 70 (page 70)

Chapter 17 - Nozzle Drooling
Remedy method
Why?
6
Apply metering delay time
Avoid too-long exposure
Decrease the overall cycle
time of melt polymer in
7
time
the barrel
Decompression acts as a
8
Increase melt decompression
plug of nozzle
17.3.2 Material:
Remedy method
Why?
Material with higher viscosity
Reduce content of regrind
Reduce the melt flow
Reduce moisture content
ability
Faster solidifying material
17.3.3 Injection machine & auxiliaries:
Reduce nozzle diameter
Use reverse taper nozzle
Shut off nozzle
Longer nozzle - may causing nozzle block issue
17.4 Check points:
Measure the real melt temperature
Check the nozzle type and diameter
Check the bag sealing and moisture content
Check the melt cake
EMS
66

### Segment 71 (page 71)

Injection Molding Trouble Shooting Guide
Chapter 18 - Excessive Warpage
18.1 Description
Warpage is defined as the deviation of the shape (shrinkage is de-
fined as the deviation of the dimensions only) between the injec-
tion molded part and the specified design, coming with curva-
ture or twisting of surface or changes of angles. Shrinkage and
Warpage depends on processing conditions, gating concept, part
geometry and material properties.
Fig. 49: Sign of warpage
Bending
Twisting
18.2 Root cause
The most fundamental reason for the deformation is: during pro-
cessing, the unbalanced internal stress occurred due to uneven
shrinkage in different regions. After the part had been ejected, the
stress is prone to balance status and then the deformation comes
out immediately. Reasons for uneven shrinkage can be sorted
into:
1. Different volumetric shrinkage
2. Uneven cooling effect
3.Differential orientation
Different volumetric shrinkage
With the influence of the thickness differential, gate location
and process settings, the entire part will has uneven volumetric
shrinkage between the regions.
67

### Segment 72 (page 72)

Chapter 18 - Excessive Warpage
Fig.5o:Deformationcausedby thicknessdifferential
3mm-
2mm
1mm
Uneven cooling effect
Shrinkage variation through the thickness or regions due to dif-
ferential temperature across the mold (core vs. cavity) or un-
even temperature distribution on the tool surface (hot spots/
cold spots)
Fig.51:Deformationcausedbytemperaturedifference
Hot side
Result in warpage
Cold side
Note: The corner effect also can be sorted by uneven cooling effect.
·Orientation effects
Fiber filled thermoplastics exhibit anisotropic shrinkage based
on orientation of the fibers. Orientation in the flow direction will
reduce shrinkage values whilst increasing shrinkage on the trans-
verse direction. Such shrinkage differential causes the deforma-
tion.
18.3 Remedy
18.3.1 Processing:
Remedy method
Why?
Increase packing time or level
Reduce tool and melt
Reduce parts overall
temperature
shrinkage
3
Adjust V/P switch over point
4
Increase cooling time
The tool acts as a fixture
EMS
68

### Segment 73 (page 73)

Injection Molding Trouble Shooting Guide
Remedy method
Why?
5
Ensure high filling speed for
Reduce parts overall
thin-walled parts
shrinkage
Adjust two cavity side's tool
temperature
18.3.2 Part and tool design:
Remedy method
Why?
Aim for uniform wall thickness
Change flow pattern by adding,
Minimize the volumetric
removing or relocating gates
shrinkage differential
Optimize the rib layout (e.g. plan
for symmetrical ribbing)
Reduce corner area's wall
Minimize the corner
thickness or adding Be-Cu inserts
effect influence
Aim for uniform cooling line
Achieve uniform
layout
volumetric shrinkage
Minimize the volumetric
Increase gate diameter
shrinkage differential
Using overflows to divert flow at
Minimize the fiber
end of fill
orientation effect
Counter correction ofthe tool
after prototyping
18.3.3Material:
Remedy method
Why?
Use amorphous material
Enhance material's
Decrease fiber content (e.g. from
isotropic properties,
60%GF t0 40%GF)
hence reduce shrinkage
differential in different
Use X-modified glass fiber
direction
grades (e.g. Grivory GVX-5H)
Using lower crystallinity and
Reduce parts overall
fast solidification material
shrinkage
69

### Segment 74 (page 74)

Chapter 18 - Excessive Warpage
18.4 Check points:
Keep your options open (gate relocation and design modifica-
tions); use prototype tooling if possible
Pre-solve deformation related factors during part design stage
(assistant with CAE)
- Ribs, thickness distribution, gate location, structure and etc.
Check whether warpage is caused by demoulding
If tool temperature is higher than the Tg point for the semi-
crystal material
- Tool temperatures below Tg will result in post crystallization
(shrinkage), hence increase warpage during exposure at the
temperature higher than Tg.
Annealing in hopper dryer or oven (quick test)
※
Explanation of the corner effect
Figure 52 shows an-injection-molded part of the typical box-type
structure. In the box structure, there is an inside corner (the core)
that is normally difficult to cool and where heat tends to concen-
trate. The cavity side is easy to cool, and there is a larger volume
of mold to absorb the heat from the plastic. As a result, the inside
of the corner runs hot, allowing more time for the molecules to
cool down and shrink, therefore collapsing the corner a bit. This
will pull the sides of the box toward the core.
Fig. 52: Cooling of box structures
Heatisconcentratedin
Hot Core
thecornerofthecore
Hotinsidecornershrinksmore
Cold cavity
relativetocooleroutsideportions
of the part
EMS
70

### Segment 75 (page 75)

Injection Molding Trouble Shooting Guide
Charper 19 - Failure Analysis of Plastics
19.1 Description
The performance of plastic products will decline over time
and change with the temperature. Time and temperature are
among the most common causes of failure in plastic products,
although they have much less influence on metal parts.
Other factors can also lead to failure in plastics, e.g. long-
term (cyclic) mechanical 1oading (causing creep), hydrolysis
(chemical attack), and short-term stress peaks.
19.2 Root cause
The factors that affect the failure of products are various but
belong to one of the following five categories:
1. Material
2. Process
3. Design
4.Serviceconditions
5. Pre-& Post operations
19.2.1 Material
First of all, in the product development selecting, select an
inapp-ropriate raw material or additives without fully
considering the properties (viscoelastic, creep, fatigue, etc.)
makes the material unable to fulfill the requirements. This
will finally result in failure in the part. Of course, defects in
material will also cause failures, e.g. performance
differences along the bat-ches and high moisture content of
the granules.
Physical property changes of the recipe cause the failure as
well, e.g, in the testing phase, material produced with brand A
glass fiber, flexibilizer, master batch and etc., but when it comes
to the mass production period, it has to change the brand from A
to B due to the uncertainty.
Pollution of the material during dry blend and adding regrind
(even high ratio) both can lead to failure.
71

### Segment 76 (page 76)

Chapter 19 - Failure Analysis of Plastics
19.2.2 Process
Firstly inappropriate process settings will result in degrada-
tion of the materials, which will lead to decrease of mecha-
nical properties of the products and ultimately product fail-
ure. The following should be avoided during molding pro-
cess: high melt temperature, high shear rate (especially pas-
sing the gate), long residual time, and high moisture content.
internal stress, which leads to failure of the product. So, in the
molding process, too low melt temperature, excessive injection
speed (especially passing the gate), excessive packing level and
time, and too late V/P switch over should be avoided.
Additionally unstable molding process can lead to part failure as
well. For example, if part weight is inconsistent, the first shot
product may pass the test but the second shot may fail due to in-
sufficient packing. In the molding process, it is necessary to ob-
serve and record the stability of cushion, metering, and part
weight. If inconsistent part weight happens, please check the
non-returnvalvefirst.
Generally below points should be paid attention to during pro-
cessing: inappropriate injection speed, V/P switch over, back
pressure, dosing speed, and packing time and level. the insert
lecting insert and pre-treatment are as follows:
·Use plastic insert as much as possible
Use the metal insert that has a small difference in CTE with
the plastic part
Coat the metal insert with a layer of rubber or polyurethane
elas-tomer
·Pretreatment of degreasing on the metal insert
·Preheating on the metal insert
Sufficientthickness around themetalinsert
Design a sleek shape insert, preferably with exquisite
rolling pattern
19.2.3 Part and tool design
From the point of view of product design, the following
factors can easily cause failure of the product:
tMS
72

### Segment 77 (page 77)

Injection Molding Trouble Shooting Guide
Insufficient overall structural strength
Part design with the sharp corners and thickness abrupt
transition area - result in Notch effect
Part with thick wall or thickness accumulations regionally
-result in high shrinkage evenvoids inside
Thin wall thickness -lead to excessive internal stress
cause by high injection speed and pressure
Poor rib design and distribution
From the point of view of tool design, the following factors are
easy to cause failure of the product:
Too small size of runner and gate - easy to result in high shear
and insufficient packing
Inappropriate gate location - result in weld line locates at load-
ing area, air trap, flow hesitation around thin area and insuffi-
cient packing for the thickness area.
Poor venting design - influence on the weldline strength and
degradation regionally
Too small demolding angle - result in high demolding stress
Uneven ejector distribution
Uneven cooling channel layout - result in cooling stress
Insufficient design of the cold well at the end of runner - results
in the brittleness due to the poor bonding between the melt and
cold slug
Less amount of gates - result in long flow length and insuffi-
cient packing
19. 2. 4 Service conditions
When the product is used improperly or exceeds its design
service life, failure is easily caused.Unstable service
conditions (e.g. abrupt change of temperature and humidity)
and harsh service conditions (e.g., exceeding the reasonable
range) can also cause product failure.
With the long-term or simultaneous influence of impact, tensile,
bending, vibration, etc., it is easy for the part to get creep, defor-
mation, fatigue and buckling which ultimately leads to product
failure. In addition, long-term exposure to UV, heat exposure
and high humidity
73

### Segment 78 (page 78)

Chapter 19 - Failure Analysis of Plastics
environment can lead to product failure due to mechanical prop-
erties reduction.
Physical properties change: contact with chemicals and loss of
additives all can result in part failure.
Physical change: water uptake, thermal expansion, surface
wear,etc.
· Chemical contact: craze or crack
· Additive lost: migration and precipitation
19.2.5 Pre- & Post operations
Part failure has a close relationship with transportation, storage
condition and time.
Part easy to get squeezed, impacted and worn during transpor-
tation
Storage: mechanical property reduction due to high tempera-
tureandhumidity
The assembly type will also cause a part failure due to internal
stress, e.g., weld, gluing, snap fit, screw fastening and press. It
is recommended to condition and anneal the part before assem-
bly.
In addition treatment of sterilization, painting, coating, degre-
asing and hot stamping can also result in part failure.
19.3 Strategy for identifying failures
When failure occurs collect enough information to help identify
and judge the root causes of failure, then find solutions based on
the 5 key factors. Below are items that should be considered:
Failure part and raw material, which produced the part (same
batch)
On site checking of the testing in case of the part failure at test-
ing stage, and make a record of failure initial position, failed
loading point and finished cycles before failure.
Get the part function and requirements e.g. required burst pres-
sure level, usage temperature, long-term out door use and long-
termcontactwithwaterorchemicals.
EMS
74

### Segment 79 (page 79)

Injection Molding Trouble Shooting Guide
Check whether there is a design or requirement change. (from
initial development stagetofailed stage)
Gather basic information -- date of purchase, date of installa-
tion, date of first failure, geographic location, types of chemi-
cals used around, indoors or outdoors, number of cases re-
ported, number of cycles and consistence in failure occur-
rence/frequency...
Get the record of the machine maintenance
Does part failure always occur in the same cavity?
Get the detailed testing procedure
·Verify with the nature color material
19.4 Techniques to determine failures
Certain visual defects can be effectively identified by eyes e.g
burn marks, surface aesthetics/gloss, sink marks, contamination,
color streaks, black specs, poor weldline, and stress level (check
by polarized film).
The root cause of failure can be determined by equipments in ad-
dition to judgement by the eyes. For example, check for burn m-
arks, surface quality, location of failure (gate, wall thickness,
notch, insert, weldline) contamination, color change, black sp-
ots, weldlines, and stress level under microscope, amplifier and
polarized film.
Rheology test (RV, MFI test), CAE (structure and moldflow anal-
ysis), mechanical testing (tensile and impact test), weathering
testing and operation simulation all can help to judge the cause
of failure.
In general instruments can help to get a deeper analysis on the
failure cause. The commonly used instrument analysis method
and its basic functions are listed on table 1.
75

### Segment 80 (page 80)

Chapter 19 - Failure Analysis of Plastics
Table 2:Commoninstrument analysismethod and basic functions
Analysis method
Application and function
1. Observing the surface
structure and change can
enlarge 20X-20millionX. (In
somespecificcases,parthave
to be put into the organic
solvent before observation of
the surface change)
SEM
2. Dispersion of the filler and
(Scanning Electron Microscope)
elastomer
3. Adhesion between the polymer
and fiber
4. Combination ofSEM+EDS
and quantitative analysis of
elements on object surface
even at the microcosmic
region can be done. (Hydrogen
can't be detected)
1. To observe the crystal
TEM
appearance and structure of the
(Transmission Electron
polymer
Microscope)
2. To observe the structure of
nanometer
1. Detect the heat stability of
polymers
2. Qualitative analysis of the
material composition
TGA
3. Analysis of the curing process
(Thermal Gravity Analysis)
of the thermoset materials
4.The temperature at the fastest
speed of weight loss
5.Ash content
6. Gas release content
1. Detection of melt point (Tm)
DSC
2. Detection of glass transition point
(Differential Scanning
(T)
Calorimetry)
3. Post-crystallization
4. Compatibility of the polymers
EMS
76

### Segment 81 (page 81)

Injection Molding Trouble Shooting Guide
Analysis method
Application and function
1.Detection of glass transition
temperature - Tg point. (more
accurate than DsC)
DMA
2.Detection of melt point (Tm),
(Dynamic Thermomechanical
3.Detection ofthe Tv (temperature
Analysis)
ofviscosity flow) of amorphous
material
4.Compatibility of the polymers
and the mechanical loss ability
(damping properties)
1.To identify material through the
FTIR
detection of functional groups
(Fourier Transform Infrared
2.Identification of the elastomer
Spectroscopy)
(filter thehydrolyzed nylon
first)
XRF includes WDX/EDX: Detect
the element and content. (Detect the
elements after No.20 on the periodic
table.)
XRF
(X Ray Fluorescence)
EDX ( Energy Dispersive X-ray de-
tector)
WDX ( Wavelength Dispersive Spe-
ctrometer)
1.Detect the monomer of the
degraded polymer
GC/MS
2.Identification of organic
(Gas Chromatograph/Mass
antioxidants
Spectrometer)
3.Quantitative analysis of
residence monomer and
caprolactam
1. Identification of polymer, addi-
tives and contaminant (liquid and
NMR
solid NMR)
(Nuclear Magnetic Resonance)
2. Identification of organic phospho-
rus flame retardant (solid NMR)
REM
1. Observe the defects of crystal
(Reflection type Electron
(seldom used)
Microscope)
77

### Segment 82 (page 82)

1. Purging Guide of EMS Material
1. Purging Guide of EMS Material
For longer shutdown time, it is recommended to thoroughly
purge and clean the injection unit. The following recommenda-
tions are provided for EMS materials.
Grilamid TR: use glass-reinforced Nylon 6 or 12
Note: Purging is necessary after a production downtime of more
than15minutes.
Grilamid and Grilon/T: normal purging of barrel is sufficient
and no further cleaning of the injection unit
Grivory G: use glass-reinforced PA6 or PA66
Note: Purging is necessary after a production downtime of more
than15minutes.
Grivory HT:
actual processing temperatures. If possible, use Grivory GV-
material for initial purging and afterwards purge with a glass fi-
ber reinforced nylon 66. During purging lower the barrel tem-
peratures down to a processing temperature level of nylon 66.
Grivory HTV processing and incorrect purging:
A solidified Layer of Grivory HTV...1 will remain on the head
and contaminate the following production if the temperature is
decreased immediately to PA66GF level for purging (see dia-
gram below)
CCylinder
350
Solidified layer of
340
Grivory HT
330
330330330
320
325
325
310
300
290
280
280
270
275
270
270
265
260
Processing with
Purging at low
Grivory HT
Temperature
Wrong
EMS
78

### Segment 83 (page 83)

Appendix
Grivory HTV: processing and correct purging.
To clean the injection unit, the temperature of the nozzle and the
metering zone must be increased in short-term to a higher level
(seediagrambelow)
°C Cylinder
360360
350
340
330
330330330
320
325
325
310
300
290
280
280
270
275
270
270
265
260
Processing with
Purging at high
Decrease
Grivory HT
Temperature
withPA66GF
Right
Note: Purging is necessary after a production downtime of more than 15 min-
utes.
79

### Segment 84 (page 84)

H1. Mechanical Screw & Barrel Cleaning Method
I. Mechanical Screw & Barrel Cleaning Method
Cleaning tools
Appropriate tools for mechanical cleaning:
High-heat gloves, safety glasses, a brass putty knife, brass wire
brush, copper gauze, stearic acid flakes, an electric drill, cotton
rags, and a barrel brushes.
Heat resistance glove
Copper gauze
Stearic acid
Brass wire brush
Safety glasses
Brass putty knife
Barrel brush
Cotton rags
Electric drill
Wrong tools for mechanical cleaning:
Do not use an acetylene torch to clean the screw
Do not use a screwdriver and methane burner
Notes: Reasons why the use of acetylene torches are not recom-
mended:
1) It may destroy the metal matrix of the screw
2) It will undo the annealing of the base metal
3) It affects the screw tolerance
EMS
80

### Segment 85 (page 85)

Appendix
4) It reduces the yield strength & can lead to breakage during
screwoperation
Mechanical cleaning procedure of screw:
1. Push out the hot screw with screw extractor
2. Remove remaining materials with brass putty knife & wire
brush
3. Sprinkle stearic acid flakes onto the root of the hot screw
4. Use copper gauze to remove any remaining residue and polish
Notes: Remove the purging resin through using brass tools & a
brass wire brush but never steel since steel will damage screw
andbarrelsurfaces
Before clean
After clean
Mechanical cleaning procedure of nozzle:
Disassemble the nozzle and sprinkle stearic acid flakes onto in-
ner channel of the nozzle; use the brass wire brush to remove
any remaining residue; do final clean-up condition using a soft
cotton rag
Before cleaning
After cleaning
81

### Segment 86 (page 86)

H1. Mechanical Screw & Barrel Cleaning Method
Mechanical cleaning procedure of barrel:
Pull the screw out (keeping barrel temperatures still at 205°℃)
Assemble the brush, extension rod and electric drill
Wrap the wire brush with copper gauze and sprinkle stearic acid
flakes onto the round wire brush
Use the electric drill to rotate the brush while moving it in &
out until it moves easily
s g
purge or stearic residue
EMS
82

### Segment 87 (page 87)

Appendix
ml. Quick Processing Guide for Grilamid TR
Grilamid
Grilamid TR
OX
00
70
lamid TR55
lamid TR55
lamid TR30
lamid TR90
lamid TR90
lamid TRV)
lamid TR
20
LXS
TR
HT
HT
X
Tg[°C]
160
110
160
155
125
125
200
170
140
Flange
40
40
80
40
40
60
80
70
70
Zone 1
265
240
290
255
240
270
290
275
260
Zone 2
270
245
295
260
245
275
300
280
270
Zone 3
255
250
300
265
245
280
310
285
280
Nozzle
270
245
295
260
245
275
295
280
275
Tool Temp.
80
40
100
80
40
100
120
100
70
Melt Temp.
280
265
300
280
265
280
310
305
290
1.Processing
Injection speed
: medium-high
Hold-on pressure spec.
: 300-500 bar
Back-pressure (hydr.)
: 5-10 bar
Circumference speed
: 0.05-0.25m/s (Vlinear=II*D*N/60)
D: Screw diameter
2. Use of regrind
Grilamid TR is a thermoplastic material so that incomplete mold-
ings as well as sprues and runners can be reprocessed. The fol-
lowing points have to be observed:
No thermal degradation in last processing.
No contamination of foreign material (dust, oil, etc.)
Regrind has to be dry and free of dust
When adding regrind, special care has to be taken by the molder.
For high-quality optical and technical parts, only virgin material
should be used.
83

### Segment 88 (page 88)

IHI. Quick Processing Guide for Grilamid TR
3. Storage
Amorphous polyamides can be stored over long periods of time
without negatively influencing its mechanical properties.
However, in order to ensure optimal color and transparency,
Grilamid TR natural should not be stored for more than 6 months
and at temperatures above 25°C. The storeroom must be dry and
protect the bags from the influence of weather and damage.
4. Drying conditions
Grilamid TR90 grades are delivered dry, ready for processing. In
case the material becomes damp, dry according to the following
table:
Max.: 80°C /4-6hours
Desiccant dryer:
Dew point: -30°C ~-40°C
Vacuum oven:
Max.: 80°C /4-8 hours
Do not dry the material with hot air oven
5. Moisture content
Grilamid TR90 grades are delivered dry, ready for processing.
Excessive high moisture (>0.08%) content leads to: foaming
melt, melt drooling and silver streaks on the molded part, whilst
over-dried material (<0.025%) can reduce flowability and process
stability.
Fig.53:Moisture absorptionvs.storagetime
Moisture absorption vs. storage time
at 20°C / 50% Rel. Humidity
Moisture Content [%]
0.15
0.10
Granulate
Bulk Depth 1 cm
-Bulk Depth 3 cm
0.05
0.00
0
2
3
Time [h]
EMS
84

### Segment 89 (page 89)

Appendix
6. Machine
Screw
A conventional 3 zone screw is recommended.
Length: 18 D - 22 D
Compression ratio: 2 - 2.5
To prevent black spots from formation, a special screw coating
(PVD coating) is recommended.
Shot volume
The metering stroke (less decompression distance) must be longer
than the length of the non-return valve
Shot volume = 0.5 to 0.8x max. shot volume of the injection unit
Clamping force
7.5 kN* x projected area [cm?]
* for a cavity pressure of 750 bar
7. Mold
Runner diameter
1.4 x thickest wall section of the injection molding part (mini-
mum 4mm)
Gate diameter
0.8 x thickest wall section of the molded part
Venting
To prevent burn marks and to improve weldline strength, the fol-
lowing venting recommendations should be followed:
a. Vents much be on the parting line and exhausted to atmo
b. Venting depth: 0.02mm
c. Venting width: 2 - 5mm
8. Part and mold design
Besides the usual guidelines for thermoplastic, the following
modifications should also be considered:
85

### Segment 90 (page 90)

II. Quick Processing Guide for Grilamid TR
Avoid sharp corners and notches
Avoid abrupt and large changes in wall thickness
If possible maintain a constant wall thickness
Avoid local material accumulation
Keep the weld lines to a minimum (single gate)
Place weld lines at the least stressed areas or at the thickest wall
Provide mould vents at the end of the flow path or in the weld-
line area
Provide draft angles
Provide direct or secondary ejectors with regard to possible
ejector marks
9. Processing
Injection stresses
Injection stresses generates when the orientation of the polymer
from the injection phase and hold phase is "frozen in" during the
cooling phase.
The most important processing parameters are:
Injection speed
Switch over point (transfer position)
Holding pressure
Melt temperature
Mold temperature
Internal stresses are influenced by:
Mold temperature: frozen stress
Holding pressure: over packing the part
Switch over point (too early): melt hesitation
Mold / part design: gate dimensions and position to allow effi-
cient holding pressure to eliminate sink marks without exces-
sive pressure
EMS
86

### Segment 91 (page 91)

Appendix
Reduction of stresses
Stress level will be reduced by slightly increased storage time
(relaxationovertime)
The stress level is dependent on the part design and how the
part has been molded (influence of the hold pressure)
The speed of stress level reduction is mainly dependent on tem-
perature
Remove the gate with thermal cutting plier
Stress concentrations from notches and/or edges will not be
eliminated, but their effects will be reduced.
87

### Segment 92 (page 92)

IV. Quick Processing Guide for Grivory HT
IV. Quick Processing Guide for Grivory HT
1. Barrel, melt temperature setting
Grivory HT-Type
Nozzle
Zone 3
Zone 2
Zone 1
flange
330-
330-
330-
330-
80 -
Grivory HT1
340℃
345°℃
345℃
340℃
100℃
310-
315-
315-
315-
Grivory HT2
60 - 80°C
325°℃
335℃
340℃
330℃
310-
310-
310-
305-
Grivory HT3
60 - 80°C
325°℃
330°℃
330℃
320℃
330 -
330 -
330 -
330-
80 -
Grivory HT6
345°C
345°C
345°C
345°C
100°C
Recommended melt temperature :
Grivory HT1... Types: 330 - 345°C
Grivory HT2... Types: 315 - 330℃
Grivory HT3... Types: 300 - 330℃
Grivory HT6... Types: 330 - 350°C
Note:Toohighmelt temperatureand toolongdwell timewilldam-
age the material (thermal degradation). Shot volume must be >
50% of the cylinder volume.
2. Tool temperature
Grivory HT-
Grivory HT1
Grivory HT2
Grivory HT3
Grivory HT6
Type
Tool
140 - 160C
100-140°C
120 -160°C
160 -170°C
temperature
The Recommended Tool Temperature should be understood as
the tool surface temperature. The temperature must be con-
trolled with oil or pressurized water equipment with sufficient
output. Cooling tubes and fixed screw couplings of high temper-
ature resistant are recommended.
Why HT materials require a high tool temperature?
The low tool temperature will give insufficient crystallinity,
hence result in:
1). Reduction of stiffness
2). Reduction of resistance on burst pressure
3). High internal stress level, poor chemical resistance and poor
surface quality
EMS
88

### Segment 93 (page 93)

Appendix
Fig. 54: tool temperature vs.stiffness
GrivoryHT1V-4FWA
Testsample 60x10x1mm
10,000
180°Ctool temperature
1300Ctool temperature
a
[MPa
3'000
2'000
Modulus
1,000
500
Shear
torsion
pendulum test
100
0
50
100
150
200
250
Temperature [°C]
Fig.55:tool temperature vs.burst pressure
Test sample Tulip 2mm
130
GrivoryHT1V-4FWA
[bar.
120
Burst pressure
110
100
100
120
140
160
180
200
Tool Temperature [°C]
3. Speed
Injection speed
: Middle - high
Injection pressure
: 1000-2000bar
Packing pressure
: 500-750 bar
(cavity only)
Back pressure (Hydr.)
: 5-10 bar
Circumference
: 0.08-0.25 m/s (Vlinear=II*D*N/60)
speed
D:Screw diameter N:Rotation
speed (RPM/min)
Less decompression
: 2-3mm
Machine utilization
: 50-80%
89

### Segment 94 (page 94)

IV. Quick Processing Guide for Grivory HT
4. Pre-drying and drying conditions:
Grivory HT is delivered ready for processing as a dried granu-
lates in air-tight sealed bags. Once the material becomes damp,
the following conditions should be kept to when drying:
Max.:80°C /4-6hours
Desiccant dryer:
Dew point:-30°C ~ -40°C
Vacuum oven:
Max.:80°C /4-8 hours
Do not dry the material with hot air oven
Toohighmoisturecontentwill leadtomaterialdegradationandreductionofprop
ertieswhiledrying temperatures above therecommended limits will lead tooxida-
tion.Anindicationofoxidationistheyellowing(lightcolors)ofthematerial.
5. Screw / Mold:
Universal three-zone screw extruder with a non-return valve:
Effective screw length: 18D-22D, Compression ratio: 2-2.5
For the mold cavities, common mold with steel quality, which
has been hardened to a level of 56 HRC, is necessary. Additional
wear protection is recommended in areas of high flow rates in
the mold (e.g. pin point gates and hot runner nozzles).
6. Tool maintenance
Tool-lubricant: Z260 (HASCO) or Anti Seize (DEPAC)
Tool cleaning: Lusin Clean L 21,clean mold deposits with hot
tool
Corrosion 1). Spray the tool with Wd40.
Protection:2). Descale the cooling system after production and
blow out the water to avoid corrosion
7. Demolding / Draft angle:
Angles between 1° and 5° are adequate for venting
(VDI3400)
12
15
18
21
24
27
Depth ofroughness (om)
0.4
0.6
0.8
1.1
1.6
2.2
Demoulding angle (°)
1
1
1.1
1.2
1.3
1.5
(VDI3400)
30
33
36
39
42
45
Depth of roughness (om)
3.2
4.5
6.3
9
13
18
Demoulding angle ()
1.8
2
2.5
3
4
5
EMS
90

### Segment 95 (page 95)

V. Quick Processing Guide for Grivory GV/GC/GM
V. Quick Processing Guide for Grivory GV/GC/GM
1. Barrel, melt temperature setting
Grivory Type
Nozzle
Zone 3
Zone 2
Zone 1
flange
Grivory GV-2H
Grivory GV-4H
Grivory GV-5H
Grivory GV-6H
Grivory GVS-5H
270
275
270
260
70
Grivory GV-5HL
To
To
To
To
To
Grivory GVN-5H
280
285
280
270
80
Grivory GC-4H
Grivory GM-4H
Grivory G4V-5H
Grivory G5V-5H
Grivory G7V-5H
Recommended melt temperature for the Grivory GV, GM, GC-
grades: 270°C-300°C.Too high melt temperature and too long
dwell time will damage the material (thermal degradation)!
2. Tool temperature
Against above listed Grivory GV type materials, the recommended
tool temperature is 80-120°C, which should be deemed as the tool
surface temperature. For parts with high requirements on surface qu-
ality, hardness and strength, the tool temperature should be 120°C. (
Note: For G5V type, the tool temperature is in between 90-130°C)
3. Speed
Injection speed :For GV/GC, high speed (filling time 0.5-3s)
: For GM, low-middle speed
Injection pressure
: 500-1500bar
Packing pressure (cavity only)
: 300-800 bar
Back pressure (Hyd)
: 5-15 bar
Circumference Speed
: 0.08-0.25 m/s
Less decompression
: 2-3mm
Machine utilization
: 50-80%
Note: Refer to quick guide of HT against the material drying,
screw selection, tool draft angle and maintains.
91

### Segment 96 (page 96)

VI. Quick Process Guide for Grilamid L (PA12)
VI. Quick Process Guide for Grilamid L (PA12)
1. Barrel, melt temperature setting
Grilamid L-Type
Nozzle
Zone 3
Zone 2
Zone 1
flange
LV-2H
LV-2ANZ
LV-2H
245
250
245
240
60
LV-3H
To
To
To
To
To
LV-5H
265
270
265
260
80
LC-3HLKN-3H
LKN-5H
LVX-50H
Recommended melt temperature for Grilamid LV, LC, LKN-
grades: 240°C-290°C. Too high melt temperature and too long
dwell time will damage the material!
2. Tool temperature
Grilamid L-Type
Tool temperature [°C]
Grilamid LV-2H
80-100
Grilamid LV-3H
Grilamid LV-5H
The recommended mould temperature
GrilamidLC-3H
should be deem as the mould surface tem-
GrilamidLKN-3H
perature. For parts with high requirements
GrilamidLKN-5H
on surface quality, hardness and strength,
Grilamid LV-2A NZ
the mould temperature should be 1oo°C.
Grilamid LV-3A
GrilamidLVX-50H
3. Speed
Injection speed
: Middle - high (0.5-3s)
Injection pressure
: 500-1500bar
Packing pressure
: 300-800 bar
(cavity only)
Back pressure
: 5-15 bar
(hydr.)
Circumference
: 0.05-0.2 m/s
speed
Machine utilization : 50-80%
EMS
92

### Segment 97 (page 97)

Appendix
Properties Influenced by Process Parameters
Influence of tool temperature
Influence of
H.D.T
Flow
ChemicalResistance
Surface Quality
Surface
Toughness
Screw
Stiffness
Flow Ability
Impact Strength
Impact
Printability
Low
Tool Temp.
...High
Low
Melt
93

### Segment 98 (page 98)

VII. Process vs. Part Quality Chart
melt temperature
Influence of residual time
Ability
Quality
Surface Quality
Chemical Resistance
Wear
Toughness
Toughness
Impact Strength
Strength
Temp.... High
Short
Residual time ... Long
EMS
94

### Segment 99 (page 99)

Appendix
Remedy: Processing
nperature
setting
t temperature
ature
Itool
Screw retration
pressure
Tooltemperat
perature:
Unbalanced t
temperature
gressive
Screw speed
PL: Plasticization
tem
EJ:Ejection
Nozzle t
Meltt
Backj
0
tem
P
Defects
Temperature
PL
Glass fiber streaks
7↑
6↑
5↑
4↑
Matt points
2
↑
↑
3↑
Grooves/Flow mark
2
↑
3
↑
4↑
8X
Sink marks
4
↑
5
5
Air streaks
4↑
3↑
2
Moisture streaks
2
4↑
1↑
overheating
1
2
3
Color streaks
home./cont.
2←
1
↑
Cold slug
1←
2
5
4↑
Burn marks
1
↑
2
3
Gas marks
4
↑
7
8
Jetting
4
3
Mould deposits
1
↑
5
6
7
↑
↑8
Short shot
4
↑
5↑
8↑
Internal stress
6
7↑
Black spots
1
↑
2↑
3
Blistering/Voids
n.a
Excessive warpage
6
4
4
7X
Flash
5
↑
6
6
Part sticking on core
5
↑
1
Part sticking on cavity
9
↑
9 ↑
10
Low gloss/ gloss differences
6
10↑
5
9↑
Nozzle drools
6
1
2
3↑
Ejector marks
7
Delamination
3↑
5↑
4↑
6↑
Mark
↑= Increase
= Decrease X=Optimization
95

### Segment 100 (page 100)

VIll. Trouble Shooting Guide Overview Chart
un
constant flow
Delay time (plastic
retraction, metering)
Switch over point
(defect on flow end)
pressure
pressure
pressure
knock out action
stroke
speed
speed
Melt cushion/
profile
force
time
Cycle time
jection
Injection s
meetings
Cooling
profile
Holding
lding
lding
file
Clamp
Keep
front
level
e
Inje
0
101
orof
S
H
PL
Injection
Holding pressure
EJ
Cycle
3↑
8X
8X
1↑
2↑
1↓
2X
7↓
1↑
6
5←
6
3↑
2
1↑
7↑
1↓
3
5
6
8X
4↑
7
3↑
3
5
6
8X
4↑
7
1
2X
X9
3
5
10
2X
3
4X
2
1↑
2↑
3X
6
7
5
8X
1X
2
4
3X
4
5↑
6
n.a
8↑
5
2↑
1↑
3↑
4
3
2
1↑
7
2↑
3↑
8↑
4↑
6
7
8X
3
1
2
4X
5↑
6↑
8
1
7X
2↑
3↑
4↑
6
4↑
5
6
2X
3
4
5
1↑
1
2X
7
8↓
↑ = Increase or Decrease
Number represents priority sequence
EMS
96

### Segment 101 (page 101)

Appendix
Remedy: Design overview
Undercuts, puller (less dislo-
cation, pulling sprue/runner)
Apply obstacle/insert pin
Copper-beryllium inserts
Increase/change ejector
Centered clamp force
Eliminate undercuts
size/ number/system
of cores and sliders
I.D: Insert design
(scratches)
Defects
Tool design
Glass fiber streaks
n.a
Matt points
Grooves/Flowmark
Sink marks
X
Air streaks
Moisture streaks
overheating
Color streaks
home./cont.
n.a
Cold slug
n.a
Burn marks
Gas marks
Jetting
X
Mould deposits
X
X
Short shot
Internal stress
Black spots
n.a
Blistering/Voids
n.a
Excessive warpage
Flash
X
Part sticking on core
X
X
X
X
X
Part sticking on cavity
X
X
X
X
Low gloss/ gloss differences
X
Nozzle drools
n.a
Ejector marks
X
X
Delamination
n.a
Mark
↑= Increase
= Decrease
97

### Segment 102 (page 102)

VIll. Trouble Shooting Guide Overview Chart
Tool safe construction (cou-
I surface (rough
nter correction, oversizing)
,interlocks)
Tool accuracy (clearance,
(core shift)
corners" (allow free flow)
Tool stiffness (thickness,
ness, engraving depth)
nu)
promoter/ stopper
(fineness,
Spillovers or flow
Balanced tooling
support pillars,
cooling
Core stiffness (
Pre distributor
Structured
(Kauid
Polishing
Uniform
direction)
(st)
Tool design
1.D
n.a
X
仑
↑
n.a
n. a
仑
X
X
X
X
X
X
X
X
X
n. a
n. a
X
X
X
X
X
X
X
X
n.a
n.a
↑ = Increase or Decrease
X = Apply
EMS
98

### Segment 103 (page 103)

Appendix
Round off sharp transitions
Mass accumulations
(runner, ribs, corners)
Vacuum evacuation
/maintenance plan
Avoid hot runner
N!L)
Apply cleaning
Wall thickness
Tool coating
TiAIN, DLC)
Draft
Remedy:Design overview
Defects
Tool technology
Plastic design
Glass fiber streaks
↑
Matt points
↑
↑
Grooves/Flowmark
Sink marks
Air streaks
Moisture streaks
n.a
overheating
X
X
↑
↑
Color streaks
home./cont.
↑
Cold slug
Burn marks
X
↑
↑
Gas marks
X
X
Jetting
Mould deposits
X
X
X
X
↑
↑
Short shot
X
Internal stress
个
↑
Black spots
X
Blistering/Voids
n.a
Excessive warpage
Flash
Part sticking on core
X
↑
↑
Part sticking on cavity
↑
↑
Low gloss/ gloss differences
X
↑
Nozzle drools
n.a
Ejector marks
Delamination
↑
Mark
↑=Increase
= Decrease
99

### Segment 104 (page 104)

VIll. Trouble Shooting Guide Overview Chart
s
runner
(shorten flow
Istructure
e cold sulg
wall thickness
melt
:design)
(flow
d runner shape
tcher & dead end at
Gate into large wall
shear)
Avoid complicated
fthe
Apply/increase
Round off gates
Gate relocation
and
Corner effects
Redirection of t
wall thickness
area
Gate number
length, reduce
size
design
thickness
Gate size
Smooth
change
Runner
Round
Rib
Plastic design
Runner&Gate
X
v
X
X
X
x
X
↑
X
X
X
X
X
X
个
仑
X
X
n.a
X
X
X
X
X
X
X
仑
X
X
X
X
X
1
X
X
X
X
X
X
X
X
X
X
1
X
X
仑
X
X
n.a
X
X
X
↑
X
X
X
X
X
X
X
X
X
X
↑
X
n.a
X
↑
↑ = Increase or Decrease
X= Apply or Checkpoints
EMS
100

### Segment 105 (page 105)

Appendix
content
Volatile polymer
weigl
Solidification
Crystallinity
Amorphous
components
Flow ability
Molecular
Remedy: Material overview
Defects
Physics
Glass fiber streaks
↑
Matt points
↑
Grooves/Flowmark
↑
Sink marks
↑
↑
Air streaks
n.a
Moisture streaks
overheating
↑
↑
Color streaks
home./cont.
↑
Cold slug
↑
Burn marks
↑
Gas marks
↑
Jetting
↑
Mould deposits
Short shot
↑
Internal stress
↑
Black spots
Blistering/Voids
n.a
Excessive warpage
↑
↑
Flash
↑
↑
Part sticking on core
↑
Part sticking on cavity
↑
↑
Low gloss/ gloss differences
↑
Nozzle drools
↑
Ejector marks
n.a
Delamination
↑
Mark
↑ = Increase
= Decrease
101

### Segment 106 (page 106)

VIll. Trouble Shooting Guide Overview Chart
Iadditives
enhancer
Masterbatching (demolding,
Chromoshore or color paste
Heat stability of additives
and base polymer (MB)
Smaller/spherical :
additives
Mold release/flow
Mineral grade
Fiber content
Filler content
Fiber length
Organic:
(AN
grade
flow,
Fiber
Additives
n√
→
→
仑
n.a
X
#
仑
仑
仑
n.a
X
仑
x
仑
仑
仑
仑
仑
n.a
☆
↑ = Increase or decrease
X= Apply
EMS
102

### Segment 107 (page 107)

Appendix
Remedy: Equipment
procedure
overview
Machine encapsulation
Injection compression
Gas assisted injection
Screw wear and non-
Switch to electrical
&
return valve OK?
Degassing screw
Mixing system
TRA:Treatment
g
moulding
moulding
machine
Defects
Technology
Screw
Glass fiber streaks
Matt points
Grooves/Flowmark
X
Sink marks
X
X
X
Air streaks
Moisture streaks
overheating
X
Color streaks
home./cont.
X
X
X
Cold slug
Burn marks
X
Gas marks
X
Jetting
n.a
Mould deposits
X
Short shot
X
X
X
X
Internal stress
X
Black spots
X
X
Blistering/Voids
n.a
Excessive warpage
X
X
Flash
X
Part sticking on core
Part sticking on cavity
Low gloss/ gloss differences
Nozzle drools
Ejector marks
n.a
Delamination
Mark
↑= Increase
= Decrease
103

### Segment 108 (page 108)

VIlI. Trouble Shooting Guide Overview Chart
eand sprue
%S8-05 U
Machine utilization < 90%
1 tapered nozzle
area/
(PCD, Nickel-PTFE, DL
hopper /
Raise nozzle heater
utilization:
g in feeding
Nozzle diameter
ions
Shut off nozzle
Nozzle length
.
8
Conditioning
a
Owell time
Reversed
Machine
Bridgingi
bushing
funnel
B
a
D
Screw
Barrel
Hopper
TRA
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
n.a
X
X
X
X
X
X
X
X
X
n.a
X
X
X
X
X
X
X
X
n.a
X
X =Apply or Checkpoints
EMS
104

### Segment 109 (page 109)

EMS-Grivroy, a Business Unit of the EMS Group
China
Korea
EMS-CHIMIE (Suzhou) Ltd.
EMS-CHIMIE (Korea) Ltd.
Business Unit EMS-GRIVORY
Business Unit EMS-GRIVORY
227 Song Bei Road,
#817 Doosan Venturedigm,
Suzhou Industrial Park
Pyeongchon-dong, Heungan
Suzhou City215126
415, Heungan Daero,,Dongan-
Jiangsu Province
gu, Anyang-si,
P.R. China
Gye0nggi-do, 431-755
Phone: + 86 512 8666 8181
Republic of Korea
Fax:
+8651286668183
Phone:+ 82 31 478 3159
Fax:
+82314783157
Japan
Taiwan, R.O.C.
EMS-CHIMIE (Japan) Ltd.
EMS-CHIMIE (Taiwan) Ltd.
Business Unit EMS-GRIVORY
BusinessUnitEMS-GRIVORY
EMS Bldg.
36, Kwang Fu South Road
2-11-20 Higashi-koujiya
Hsin Chu Industrial Park
Ota-ku
Fu Kou Hsiang
Toky0 144-0033
Hsin Chu Hsien 30351
Phone:+ 813 5735 0611
Taiwan, R.O.C
Fax:
：+81357350614
Phone:+88635985355
Fax:
+88635985345
Switzerland
Italy
EMS-CHEMIEAG
EMS-CHEMIE (Italia) S.r.1.
Business Unit EMS-GRIVORY
Business Unit EMS-GRIVORY
Europe
Via Carloni 56
Via Innovativa 1
22100 Com0 (CO)
7013Domat/Ems
Italy
Switzerland
Phone: + 39 011 0604522
Phone:+41816327888
Fax:
+390110604522
Fax:+41816327401

### Segment 110 (page 110)

Germany
France
EMS-CHEMIE (Deutschland)
EMS-CHEMIE (France) S.A.
GmbH
Business Unit EMS-GRIVORY
Business Unit EMS-GRIVORY
Vélizy Espace, Immeuble Le
Warthweg 14
Blériot
D-64823 Gr0ss-Umstadt
13 avenue Morane Saulnier
Germany
78140 Vélizy-Villacoublay
Phone:+ 49 6078 78 30
France
Fax: + 496078 783416
Phone:+ 33 1 4110 0610
Fax: +33148255607
Great Britain
USA
EMS-CHEMIE (UK) Ltd.
EMS-CHEMIE (North
Business Unit EMS-GRIVORY
America) Inc.
Business Unit EMS-GRIVORY
Barn 4C
Dunston Business Village
2060 Corporate Way, P.O. Box
Dunston
1717
StaffordST189AB
Sumter, SC 29151
Great Britain
USA
Phone:+441785283739
Toky0 144-0033
Fax: +441785283722
Phone:+ 1 803 481 61 71
Fax:
+18034816121
EMS-GRIVORY worldwide: www.emsgrivory.com

### Segment 111 (page 111)

EMSproductionsites
EMS sales organisations
Distributors/Agents
EMS
EMS-GRIVORY

## Source: Verarbeitung Grivory HTV_c.pdf
- source_path: /home/gabri/udemy/llm_engineering/myRAG_knowledge/Process_Trouble-Shooting/Verarbeitung Grivory HTV_c.pdf
- source_ext: .pdf
- parser_used: PyPDFLoader
- fallback_used: False
- parse_status: success
- extracted_chars: 1801

### Segment 1 (page 1)

Grivory HT(耐高温尼龙): 注塑成型指导
Grivory HT1/HT2 系列聚酰胺为玻璃纤维、碳纤维或矿粉增强的热塑性工程塑料。所有HT系列材料可用商用型抗磨损注射机进行加工。为了体现Grivory HT 系列产品的优异
性能，在此提供以下技术要点。 本文仅为加工技术概要,详细资料可见材料物性数据手册(TDS)以及材料安全物性数据手册(MSDS)。
预干燥及干燥条件： 料桶温度和融胶温度：
Grivory HT融胶温度：
模具温度：
充填,保压和进料： 冷却时间及脱模：
壁厚 (mm)
Grivory HTV-5H1
冷却时间 tC,
(模具温度 140°C)
冷却时间 tC,
(模具温度 160°C)
1 3 4
2 7 9
3 12 18
4 22 32
6 38 58

料筒清洗及模具保养：
Grivory HT-系列 喷嘴 加热段 3 加热段 2 加热段 1 进料段
Grivory HT1… 330 -
340°C
330 -
345°C
330 -
345°C
330-
340°C
80 -
100°C
Grivory HT2… 310 -
325°C
315 -
335°C
315 -
340°C
315 -
330°C
60 -
80°C

Grivory HT-系列 模具温度[°C]
Grivory HT1… 140 - 160°C
Grivory HT2… 100 - 140°C

极佳的产品外观和高熔接痕强度可通 过高射速和足够
长的保压时间获得。在低螺杆转速和 低压下的进料时
，要设置足够的冷却时间。
具体建议：
Grivory HT 系列材料出厂前已被干燥，并保存于密封
袋中，可以直接使用。若材料受潮， 干燥中需注意以
下要点： 过高的含水量会导致材料降解和性能下降。干燥温度若高于建议温度 ,则会导致材料氧化。氧化的标志之一
是物料黄化(对于浅色材料)。
Grivory HT 产品在经过一定的冷却时间 (tC)后即可顺利脱
模。由于Grivory HT 的高刚性,应该避免脱模点不对称和
强迫脱模。过高的融胶温度和过长的滞留时间会破坏材料性能 (热
降解)。射出体积应大于料筒计量的50%
。
模温过低将会导致产品外观不良。
z Grivory HT1...-
系列: 330 - 345
°C
z Grivory HT2...-
系列: 315 - 330
°C
z射出压力在 1000~2000 bar
z短充填时间 0.5~3
秒,具体根据制成品体积决定
z保压范围在500~750 bar
z5~15 bar
的松退压力 (液压)和低螺杆转速 (5~15
米/
分钟，直线速度),设置足够的冷却时间
z低松退
“建议模具温度” 是指模具的表面温度。使用油温机或者
功率足够大的水温机来控制模具温度。连接管线需具有
高耐热性。
z
模具分模面排气道尺寸：深0.02 mm
，宽 2-5 mm
排气:
为了避免烧焦痕和提高熔接线强度 , 模腔须添加适当的
排气
z
干燥至物料含水量小于0.1%
z
干燥机露点为 -40°C
z
除湿干燥机最高干燥温度为 80°C,
真空干燥机最高
干燥温度为100°C
z
干燥时间：4~12
个小时
安全提示:
成型过程中, 要配备个人安全防护装备。尤其要注意高
温融胶和高模温。要避免材料过热分解。加工过程中产生的气体和烟应及时排出。
脱模剂： Z260 (HASCO)或 Anti Seize (DEPAC)
模具清洗：Lusin Clean L 21 (Klüber Chemie) ，清理
模具内残渣要先加热模具。
防腐蚀：模具表面使用 WD-40 (WD-40)喷雾
生产结束后，对冷却系统进行除垢并且吹干水分，防
止腐蚀生锈。
射出机清洗：升高喷嘴和第三加热段的温度到360°C。
用玻璃纤维增强的尼龙 66进行清洗。

### Segment 2 (page 2)

模具温度的影响 融胶温度的影响 料筒停留时间的影响
加工工艺对产品的影响
外
观
热
变
形
温
度
低 模具温度 ...高
硬
度
韧
性
抗
化
学
性
冲
击
强
度
可
印
刷性
流
动
性
低... 融胶温度 ...高
强
度
流
动
性
冲
击
强
度
螺
杆
磨
损
外
观
强
度
短... 停留时间 ...长
抗
化
学
性
冲
击
强
度
外
观

## Parse Failures

No failed files for this folder.
