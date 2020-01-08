#Ellyse Angus
#5/29/18
#BabyDragon.py
#Design your own dragon

#To use this program, you need to have Zelle graphics in the same folder
#as this program. I did not create Zelle graphics.

#Use the python shell to change the features of the dragon using the description
#shown on the window. First press the letter, then hit enter, and it will change
#that feature of the dragon.

from graphics import *

win = GraphWin("Baby Dragon", 400,560)
win.setBackground("LightSkyBlue1")

head = Polygon(Point(156, 88), Point(161, 87), Point(165, 86), Point(171, 85), Point(179, 85), Point(189, 86), Point(197, 88), Point(204, 91), Point(210, 97), Point(216, 104), Point(220, 112), Point(221, 121), Point(221, 131), Point(221, 139), Point(219, 148), Point(213, 158), Point(205, 166), Point(197, 171), Point(190, 174), Point(182, 175), Point(174, 176), Point(166, 176), Point(159, 175), Point(150, 171), Point(144, 165), Point(138, 154), Point(136, 144), Point(136, 129), Point(138, 116), Point(142, 105), Point(148, 97), Point(152, 90))
head.setFill("light slate blue")
head.draw(win)

mouth = Polygon(Point(153, 148), Point(157, 150), Point(161, 152), Point(167, 152), Point(172, 152), Point(180, 152), Point(185, 152), Point(184, 157), Point(182, 161), Point(177, 163), Point(170, 164), Point(163, 164), Point(157, 161), Point(154, 157), Point(152, 152))
mouth.setFill("black")
mouth.draw(win)

tongue = Polygon(Point(160, 156), Point(162, 159), Point(165, 160), Point(169, 160), Point(172, 158), Point(172, 156), Point(171, 153), Point(167, 153), Point(164, 153), Point(162, 153), Point(162, 155))
tongue.setFill("light pink")
tongue.setOutline("light pink")
tongue.draw(win)

lTooth = Polygon(Point(157, 150), Point(158, 153), Point(158, 156), Point(161, 154), Point(163, 152), Point(160, 151))
lTooth.setFill("white")
lTooth.setOutline("white")
lTooth.draw(win)

rTooth = Polygon(Point(170, 152), Point(171, 155), Point(173, 157), Point(175, 155), Point(176, 153), Point(175, 153), Point(173, 153))
rTooth.setOutline("white")
rTooth.setFill("white")
rTooth.draw(win)

nose=Polygon(Point(159, 138), Point(162, 135), Point(166, 135), Point(170, 136), Point(173, 138),Point(170, 136),Point(166, 135),Point(159, 138))
nose.draw(win)

lEye = Polygon(Point(144, 118), Point(143, 121), Point(142, 125), Point(142, 129), Point(145, 133), Point(149, 133), Point(153, 133), Point(155, 127), Point(155, 123), Point(156, 118), Point(153, 116), Point(150, 116), Point(147, 116))
lEye.setFill("white")
lEye.draw(win)

rEye = Polygon(Point(187, 118), Point(186, 122), Point(185, 127), Point(186, 133), Point(189, 135), Point(194, 137), Point(197, 137), Point(200, 135), Point(202, 131), Point(204, 126), Point(204, 120), Point(200, 117), Point(196, 115), Point(191, 115))
rEye.setFill("white")
rEye.draw(win)

lPupil = Polygon(Point(143, 123), Point(145, 125), Point(148, 126), Point(151, 126), Point(154, 126), Point(154, 123), Point(155, 118), Point(150, 116), Point(147, 116), Point(143, 118), Point(143, 122))
lPupil.setFill("black")
lPupil.draw(win)

rPupil = Polygon(Point(186, 123), Point(187, 126),  Point(190, 127), Point(192, 128), Point(195, 128), Point(198, 128), Point(202, 127), Point(204, 124), Point(203, 121), Point(202, 117), Point(198, 115), Point(192, 115), Point(189, 116), Point(187, 120), Point(186, 123))
rPupil.setFill("black")
rPupil.draw(win)

rLightEye = Circle(Point(197, 119), 2)
rLightEye.setFill("white")
rLightEye.draw(win)

lLightEye = Circle(Point(149, 119), 2)
lLightEye.setFill("white")
lLightEye.draw(win)

rHorn = Polygon(Point(198, 88), Point(199, 93), Point(201, 98), Point(203, 103), Point(207, 106), Point(211, 106), Point(214, 106), Point(217, 106), Point(224, 106), Point(229, 106), Point(231, 110), Point(234, 115), Point(234, 118), Point(232, 123), Point(229, 124), Point(235, 125), Point(239, 122), Point(242, 116), Point(242, 110), Point(241, 104), Point(237, 97), Point(231, 93), Point(223, 90), Point(213, 89), Point(205, 90))
rHorn.setFill("bisque2")
rHorn.draw(win)

lHorn = Polygon(Point(153, 90), Point(149, 87), Point(145, 87), Point(139, 89), Point(132, 92), Point(128, 96), Point(124, 102), Point(126, 107), Point(132, 111), Point(135, 111), Point(132, 106), Point(133, 102), Point(136, 101), Point(139, 100), Point(144, 102), Point(149, 100), Point(153, 97), Point(154, 94))
lHorn.setFill("bisque2")
lHorn.draw(win)

headScale1 = Polygon(Point(164, 89), Point(159, 93), Point(161, 98), Point(165, 98), Point(168, 94)) 
headScale1.setFill("slate blue")
headScale1.draw(win)

headScale2 = Polygon(Point(171, 96), Point(167, 101), Point(169, 105), Point(173, 105), Point(176, 101))
headScale2.setFill("slate blue")
headScale2.draw(win)

headScale3 = Polygon(Point(179, 89), Point(176, 92), Point(179, 97), Point(182, 97), Point(184, 93))
headScale3.setFill("slate blue")
headScale3.draw(win)

headScale4 = Polygon(Point(168, 87), Point(171, 92), Point(177, 86), Point(172, 86)) 
headScale4.setFill("slate blue")
headScale4.draw(win)

lEar = Polygon(Point(137, 117), Point(132, 119), Point(126, 122), Point(123, 125), Point(130, 126), Point(135, 127), Point(136, 122))
lEar.setFill("light slate blue")
lEar.draw(win)

rEar = Polygon(Point(219, 121), Point(224, 123), Point(229, 128), Point(233, 132), Point(227, 132), Point(222, 131), Point(216, 130), Point(214, 125), Point(216, 120))
rEar.setFill("light slate blue")
rEar.draw(win)

body = Polygon(Point(155, 174), Point(155, 179), Point(155, 185), Point(154, 190), Point(153, 194), Point(150, 199), Point(148, 204), Point(147, 209), Point(144, 216), Point(144, 223), Point(142, 232), Point(141, 241), Point(143, 255), Point(146, 265), Point(149, 273), Point(154, 280), Point(160, 286), Point(166, 292), Point(169, 297), Point(176, 299), Point(183, 300), Point(190, 299), Point(199, 298), Point(207, 292), Point(212, 282), Point(217, 271), Point(218, 262), Point(219, 252), Point(219, 243), Point(219, 234), Point(214, 225), Point(210, 217), Point(208, 212), Point(204, 206), Point(201, 202), Point(197, 195), Point(196, 186), Point(194, 177), Point(194, 173), Point(189, 174), Point(183, 175), Point(178, 176), Point(172, 177), Point(168, 177), Point(164, 176), Point(160, 175))
body.setFill("light slate blue")
body.draw(win)

belly = Polygon(Point(160, 199), Point(166, 198), Point(175, 198), Point(183, 199), Point(188, 204), Point(191, 212), Point(194, 220), Point(198, 231), Point(201, 241), Point(202, 250), Point(202, 261), Point(202, 272), Point(203, 280), Point(203, 288), Point(203, 292), Point(200, 298), Point(192, 299), Point(184, 301), Point(173, 298), Point(167, 293), Point(163, 286), Point(162, 279), Point(159, 273), Point(158, 263), Point(157, 255), Point(157, 246), Point(155, 241), Point(154, 234), Point(153, 226), Point(156, 218), Point(156, 212), Point(158, 206)) 
belly.setFill("bisque2")
belly.draw(win)

rWing = Polygon(Point(199, 198), Point(205, 192), Point(214, 186), Point(223, 180), Point(231, 172), Point(238, 165), Point(251, 164), Point(262, 169), Point(273, 177), Point(281, 184), Point(291, 194), Point(296, 204), Point(302, 219), Point(304, 233), Point(296, 233), Point(290, 228), Point(283, 224), Point(273, 221), Point(267, 223), Point(264, 228), Point(260, 227), Point(253, 223), Point(247, 221), Point(242, 220), Point(235, 219), Point(232, 224), Point(230, 222), Point(225, 217), Point(218, 216), Point(212, 215), Point(210, 215), Point(207, 210), Point(203, 206), Point(201, 202))
rWing.setFill("light slate blue")
rWing.draw(win)

lWing = Polygon(Point(149, 201), Point(144, 197), Point(136, 192), Point(129, 186), Point(125, 179), Point(116, 173), Point(108, 172), Point(97, 176), Point(89, 180), Point(81, 183), Point(75, 188), Point(65, 194), Point(58, 205), Point(51, 214), Point(48, 224), Point(45, 231), Point(55, 227), Point(61, 226), Point(71, 223), Point(77, 223), Point(84, 224), Point(89, 232), Point(90, 234), Point(94, 229), Point(100, 226), Point(104, 223), Point(111, 223), Point(114, 230), Point(119, 226), Point(124, 223), Point(130, 221), Point(136, 218), Point(140, 218), Point(143, 219), Point(145, 214), Point(147, 209), Point(149, 203))
lWing.setFill("light slate blue")
lWing.draw(win)

tail = Polygon(Point(163, 290), Point(165, 295), Point(167, 301), Point(171, 308), Point(174, 318), Point(174, 330), Point(173, 343), Point(162, 350), Point(149, 350), Point(138, 346), Point(130, 338), Point(129, 332), Point(126, 337), Point(125, 343), Point(128, 348), Point(134, 355), Point(144, 359), Point(155, 362), Point(166, 363), Point(173, 363), Point(178, 360), Point(185, 357), Point(188, 350), Point(194, 344), Point(197, 336), Point(201, 328), Point(203, 320), Point(207, 310), Point(208, 303), Point(210, 295), Point(210, 290), Point(207, 293), Point(201, 297), Point(195, 298), Point(186, 300), Point(181, 300), Point(172, 297), Point(169, 295))
tail.setFill("light slate blue")
tail.draw(win)

rRearLeg = Polygon(Point(208, 286), Point(209, 292), Point(213, 298), Point(215, 305), Point(220, 311), Point(224, 318), Point(230, 322), Point(235, 322), Point(242, 319), Point(245, 313), Point(244, 309), Point(239, 302), Point(235, 295), Point(229, 290), Point(225, 285), Point(220, 279), Point(218, 275), Point(213, 274), Point(210, 277), Point(209, 284))
rRearLeg.setFill("light slate blue")
rRearLeg.draw(win)

lRearLeg = Polygon(Point(148, 271), Point(144, 275), Point(142, 279), Point(137, 283), Point(133, 288), Point(128, 294), Point(124, 300), Point(124, 307), Point(128, 312), Point(132, 312), Point(138, 310), Point(141, 306), Point(147, 301), Point(152, 294), Point(154, 290), Point(156, 286), Point(157, 284), Point(152, 279), Point(150, 273))
lRearLeg.setFill("light slate blue")
lRearLeg.draw(win)

rFrontLeg = Polygon(Point(201, 202), Point(207, 204), Point(215, 209), Point(221, 210), Point(227, 214), Point(232, 215), Point(239, 220), Point(244, 225),Point(248, 229), Point(251, 234), Point(248, 238), Point(243, 241), Point(236, 240), Point(230, 238), Point(221, 235), Point(217, 231),Point(214, 225), Point(210, 219), Point(209, 213), Point(205, 208))
rFrontLeg.setFill("light slate blue")
rFrontLeg.draw(win)

lFrontLeg = Polygon(Point(153, 192), Point(147, 186), Point(143, 180), Point(140, 172), Point(136, 164), Point(132, 158), Point(126, 154), Point(117, 157), Point(116, 163), Point(117, 170), Point(121, 179), Point(126, 187), Point(132, 193), Point(136, 199), Point(140, 203), Point(143, 207), Point(147, 208), Point(148, 203), Point(149, 198), Point(152, 195))
lFrontLeg.setFill("light slate blue")
lFrontLeg.draw(win)

rib1 = Polygon(Point(156, 217), Point(160, 219), Point(166, 220), Point(173, 220), Point(180, 219), Point(188, 217), Point(192, 217),Point(188, 217),Point(180, 219),Point(173, 220),Point(166, 220),Point(160, 219), Point(156, 217))
rib1.draw(win)

rib2 = Polygon(Point(155, 239), Point(159, 241), Point(164, 242), Point(170, 242), Point(176, 243), Point(182, 242), Point(189, 240), Point(194, 238), Point(198, 237), Point(194, 238),Point(189, 240),Point(182, 242),Point(176, 243),Point(170, 242),Point(159, 241),Point(155, 239))
rib2.draw(win)

rib3 = Polygon(Point(157, 258), Point(161, 259), Point(167, 261), Point(173, 261), Point(180, 261), Point(187, 261), Point(193, 258), Point(199, 257), Point(201, 256),Point(199, 257),Point(193, 258),Point(187, 261), Point(180, 261), Point(173, 261), Point(167, 261),Point(161, 259),Point(157, 258))
rib3.draw(win)

rib4 = Polygon(Point(160, 277), Point(165, 279), Point(170, 280), Point(174, 280), Point(178, 280), Point(184, 280), Point(189, 279), Point(195, 278), Point(201, 275),Point(195, 278),Point(189, 279), Point(184, 280),Point(178, 280),Point(174, 280),Point(165, 279),Point(160, 277))
rib4.draw(win)

rBigEar = Polygon(Point(201, 93), Point(203, 88), Point(208, 79), Point(214, 70), Point(221, 65), Point(227, 64), Point(231, 64), Point(233, 70), Point(235, 76), Point(234, 87), Point(233, 92), Point(232, 97), Point(229, 102), Point(225, 106), Point(221, 110), Point(216, 110))
rBigEar.setFill("light slate blue")

rSmallEar = Polygon(Point(183, 88), Point(183, 82), Point(185, 76), Point(187, 72), Point(191, 74), Point(191, 78), Point(192, 83), Point(192, 87))
rSmallEar.setFill("light slate blue")

lSmallEar=Polygon(Point(160, 87), Point(163, 83), Point(162, 79), Point(160, 75), Point(157, 77), Point(155, 81), Point(155, 85), Point(155, 88))
lSmallEar.setFill("light slate blue")

lBigEar = Polygon(Point(150, 93), Point(147, 90), Point(145, 86), Point(137, 83), Point(131, 80), Point(118, 78), Point(113, 82), Point(109, 86), Point(111, 90), Point(119, 95), Point(125, 99), Point(134, 103), Point(142, 105), Point(145, 100))
lBigEar.setFill("light slate blue")

tailScale = Polygon(Point(134, 356), Point(130, 358), Point(125, 356), Point(119, 351), Point(118, 343), Point(119, 335), Point(123, 325), Point(128, 318), Point(131, 326), Point(136, 332), Point(140, 336), Point(142, 340), Point(142, 345), Point(139, 347), Point(136, 344), Point(133, 341), Point(130, 337), Point(130, 332), Point(128, 334), Point(126, 337), Point(126, 342), Point(127, 347), Point(130, 350), Point(133, 354))
tailScale.setFill("light slate blue")

rWingTail = Polygon(Point(130, 333), Point(133, 327), Point(137, 322), Point(138, 315), Point(141, 317), Point(143, 320), Point(143, 324), Point(146, 325), Point(149, 323), Point(151, 319), Point(152, 324), Point(152, 328), Point(152, 331), Point(155, 331), Point(158, 330), Point(158, 333), Point(156, 339), Point(156, 342), Point(155, 345), Point(153, 348), Point(151, 351), Point(147, 350), Point(141, 347), Point(137, 344), Point(134, 342), Point(131, 340), Point(130, 337))
rWingTail.setFill("light slate blue")

lWingTail = Polygon(Point(128, 333), Point(125, 331), Point(123, 328), Point(119, 324), Point(118, 320), Point(117, 316), Point(116, 320), Point(116, 326), Point(116, 330), Point(116, 335), Point(114, 340), Point(112, 340), Point(116, 343), Point(118, 346), Point(120, 350), Point(117, 354), Point(124, 354), Point(128, 356), Point(129, 361), Point(133, 361), Point(137, 360), Point(141, 358), Point(138, 357), Point(134, 355), Point(131, 352), Point(129, 350), Point(127, 347), Point(125, 344), Point(125, 340), Point(127, 335))
lWingTail.setFill("light slate blue")

#text
inst1 = Text(Point(200, 405), "'w' + 'Enter': change color")
inst1.draw(win)

inst2 = Text(Point(200, 425), "'q' + 'Enter': change color back")
inst2.draw(win)

inst3 = Text(Point(200, 445), "'s' + 'Enter': change horns")
inst3.draw(win)

inst4 = Text(Point(200, 465), "'a' + 'Enter': change horns back")
inst4.draw(win)

inst4 = Text(Point(200, 485), "'x' + 'Enter': change eyes")
inst4.draw(win)

inst5 = Text(Point(200, 505), "'z' + 'Enter': change eyes back")
inst5.draw(win)

inst6 = Text(Point(200, 525), "'r' + 'Enter': change tail")
inst6.draw(win)

inst7 = Text(Point(200, 545), "'e' + 'Enter': change tail back")
inst7.draw(win)


#color
def colorPurple():
    head.setFill("light slate blue")
    headScale1.setFill("slate blue")
    headScale2.setFill("slate blue")
    headScale3.setFill("slate blue")
    headScale4.setFill("slate blue")
    lEar.setFill("light slate blue")
    rEar.setFill("light slate blue")
    body.setFill("light slate blue")
    rWing.setFill("light slate blue")
    lWing.setFill("light slate blue")
    tail.setFill("light slate blue")
    rRearLeg.setFill("light slate blue")
    lRearLeg.setFill("light slate blue")
    lFrontLeg.setFill("light slate blue")
    rFrontLeg.setFill("light slate blue")
    rBigEar.setFill("light slate blue")
    lBigEar.setFill("light slate blue")
    rSmallEar.setFill("light slate blue")
    lSmallEar.setFill("light slate blue")
    tailScale.setFill("light slate blue")
    rWingTail.setFill("light slate blue")
    lWingTail.setFill("light slate blue")
    
def colorRed():
    head.setFill("red2")
    headScale1.setFill("firebrick4")
    headScale2.setFill("firebrick4")
    headScale3.setFill("firebrick4")
    headScale4.setFill("firebrick4")
    lEar.setFill("red2")
    rEar.setFill("red2")
    body.setFill("red2")
    rWing.setFill("red2")
    lWing.setFill("red2")
    tail.setFill("red2")
    rRearLeg.setFill("red2")
    lRearLeg.setFill("red2")
    lFrontLeg.setFill("red2")
    rFrontLeg.setFill("red2")
    rBigEar.setFill("red2")
    lBigEar.setFill("red2")
    rSmallEar.setFill("red2")
    lSmallEar.setFill("red2")
    tailScale.setFill("red2")
    rWingTail.setFill("red2")
    lWingTail.setFill("red2")

def colorGreen():
    head.setFill("yellow green")
    headScale1.setFill("DarkOliveGreen4")
    headScale2.setFill("DarkOliveGreen4")
    headScale3.setFill("DarkOliveGreen4")
    headScale4.setFill("DarkOliveGreen4")
    lEar.setFill("yellow green")
    rEar.setFill("yellow green")
    body.setFill("yellow green")
    rWing.setFill("yellow green")
    lWing.setFill("yellow green")
    tail.setFill("yellow green")
    rRearLeg.setFill("yellow green")
    lRearLeg.setFill("yellow green")
    lFrontLeg.setFill("yellow green")
    rFrontLeg.setFill("yellow green")
    rBigEar.setFill("yellow green")
    lBigEar.setFill("yellow green")
    rSmallEar.setFill("yellow green")
    lSmallEar.setFill("yellow green")
    tailScale.setFill("yellow green")
    rWingTail.setFill("yellow green")
    lWingTail.setFill("yellow green")

def colorGold():
    head.setFill("gold3")
    headScale1.setFill("goldenrod4")
    headScale2.setFill("goldenrod4")
    headScale3.setFill("goldenrod4")
    headScale4.setFill("goldenrod4")
    lEar.setFill("gold3")
    rEar.setFill("gold3")
    body.setFill("gold3")
    rWing.setFill("gold3")
    lWing.setFill("gold3")
    tail.setFill("gold3")
    rRearLeg.setFill("gold3")
    lRearLeg.setFill("gold3")
    lFrontLeg.setFill("gold3")
    rFrontLeg.setFill("gold3")
    rBigEar.setFill("gold3")
    lBigEar.setFill("gold3")
    rSmallEar.setFill("gold3")
    lSmallEar.setFill("gold3")
    tailScale.setFill("gold3")
    rWingTail.setFill("gold3")
    lWingTail.setFill("gold3")

def colorBlack():
    head.setFill("gray25")
    headScale1.setFill("gray7")
    headScale2.setFill("gray7")
    headScale3.setFill("gray7")
    headScale4.setFill("gray7")
    lEar.setFill("gray25")
    rEar.setFill("gray25")
    body.setFill("gray25")
    rWing.setFill("gray25")
    lWing.setFill("gray25")
    tail.setFill("gray25")
    rRearLeg.setFill("gray25")
    lRearLeg.setFill("gray25")
    lFrontLeg.setFill("gray25")
    rFrontLeg.setFill("gray25")
    rBigEar.setFill("gray25")
    lBigEar.setFill("gray25")
    rSmallEar.setFill("gray25")
    lSmallEar.setFill("gray25")
    tailScale.setFill("gray25")
    rWingTail.setFill("gray25")
    lWingTail.setFill("gray25")

def colorTurquoise():
    head.setFill("medium turquoise")
    headScale1.setFill("turquoise4")
    headScale2.setFill("turquoise4")
    headScale3.setFill("turquoise4")
    headScale4.setFill("turquoise4")
    lEar.setFill("medium turquoise")
    rEar.setFill("medium turquoise")
    body.setFill("medium turquoise")
    rWing.setFill("medium turquoise")
    lWing.setFill("medium turquoise")
    tail.setFill("medium turquoise")
    rRearLeg.setFill("medium turquoise")
    lRearLeg.setFill("medium turquoise")
    lFrontLeg.setFill("medium turquoise")
    rFrontLeg.setFill("medium turquoise")
    rBigEar.setFill("medium turquoise")
    lBigEar.setFill("medium turquoise")
    rSmallEar.setFill("medium turquoise")
    lSmallEar.setFill("medium turquoise")
    tailScale.setFill("medium turquoise")
    rWingTail.setFill("medium turquoise")
    lWingTail.setFill("medium turquoise")

def colorPink():
    head.setFill("VioletRed2")
    headScale1.setFill("VioletRed4")
    headScale2.setFill("VioletRed4")
    headScale3.setFill("VioletRed4")
    headScale4.setFill("VioletRed4")
    lEar.setFill("VioletRed2")
    rEar.setFill("VioletRed2")
    body.setFill("VioletRed2")
    rWing.setFill("VioletRed2")
    lWing.setFill("VioletRed2")
    tail.setFill("VioletRed2")
    rRearLeg.setFill("VioletRed2")
    lRearLeg.setFill("VioletRed2")
    lFrontLeg.setFill("VioletRed2")
    rFrontLeg.setFill("VioletRed2")
    rBigEar.setFill("VioletRed2")
    lBigEar.setFill("VioletRed2")
    rSmallEar.setFill("VioletRed2")
    lSmallEar.setFill("VioletRed2")
    tailScale.setFill("VioletRed2")
    rWingTail.setFill("VioletRed2")
    lWingTail.setFill("VioletRed2")

def colorWhite():
    head.setFill("mint cream")
    headScale1.setFill("gray83")
    headScale2.setFill("gray83")
    headScale3.setFill("gray83")
    headScale4.setFill("gray83")
    lEar.setFill("mint cream")
    rEar.setFill("mint cream")
    body.setFill("mint cream")
    rWing.setFill("mint cream")
    lWing.setFill("mint cream")
    tail.setFill("mint cream")
    rRearLeg.setFill("mint cream")
    lRearLeg.setFill("mint cream")
    lFrontLeg.setFill("mint cream")
    rFrontLeg.setFill("mint cream")
    rBigEar.setFill("mint cream")
    lBigEar.setFill("mint cream")
    rSmallEar.setFill("mint cream")
    lSmallEar.setFill("mint cream")
    tailScale.setFill("mint cream")
    rWingTail.setFill("mint cream")
    lWingTail.setFill("mint cream")

def colorOrange():
    head.setFill("dark orange")
    headScale1.setFill("DarkOrange3")
    headScale2.setFill("DarkOrange3")
    headScale3.setFill("DarkOrange3")
    headScale4.setFill("DarkOrange3")
    lEar.setFill("dark orange")
    rEar.setFill("dark orange")
    body.setFill("dark orange")
    rWing.setFill("dark orange")
    lWing.setFill("dark orange")
    tail.setFill("dark orange")
    rRearLeg.setFill("dark orange")
    lRearLeg.setFill("dark orange")
    lFrontLeg.setFill("dark orange")
    rFrontLeg.setFill("dark orange")
    rBigEar.setFill("dark orange")
    lBigEar.setFill("dark orange")
    rSmallEar.setFill("dark orange")
    lSmallEar.setFill("dark orange")
    tailScale.setFill("dark orange")
    rWingTail.setFill("dark orange")
    lWingTail.setFill("dark orange")

def colorBrown():
    head.setFill("sienna3")
    headScale1.setFill("saddle brown")
    headScale2.setFill("saddle brown")
    headScale3.setFill("saddle brown")
    headScale4.setFill("saddle brown")
    lEar.setFill("sienna3")
    rEar.setFill("sienna3")
    body.setFill("sienna3")
    rWing.setFill("sienna3")
    lWing.setFill("sienna3")
    tail.setFill("sienna3")
    rRearLeg.setFill("sienna3")
    lRearLeg.setFill("sienna3")
    lFrontLeg.setFill("sienna3")
    rFrontLeg.setFill("sienna3")
    rBigEar.setFill("sienna3")
    lBigEar.setFill("sienna3")
    rSmallEar.setFill("sienna3")
    lSmallEar.setFill("sienna3")
    tailScale.setFill("sienna3")
    rWingTail.setFill("sienna3")
    lWingTail.setFill("sienna3")

#Eyes
def resetEyes():
    try:
        lEye.draw(win)
        rEye.draw(win)
    except GraphicsError:
        notNeededNum = 0
    lPupil.draw(win)
    rPupil.draw(win)
    rLightEye.draw(win)
    lLightEye.draw(win)


def closedEyes():
    lEye.undraw()
    rEye.undraw()
    lPupil.undraw()
    rPupil.undraw()
    rLightEye.undraw()
    lLightEye.undraw()
    global rEyeClosed
    global lEyeClosed
    rEyeClosed = Polygon(Point(179, 131), Point(182, 127), Point(188, 127), Point(194, 128), Point(198, 131), Point(194, 128),Point(188, 127),Point(182, 127),                      Point(179, 131))                    
    rEyeClosed.setWidth(2)
    rEyeClosed.draw(win)
    lEyeClosed = Polygon(Point(157, 130), Point(153, 126), Point(148, 126), Point(144, 129), Point(148, 126), Point(153, 126), Point(157, 130))
    lEyeClosed.setWidth(2)
    lEyeClosed.draw(win)

def delClosedEyes():
    lEyeClosed.undraw()
    rEyeClosed.undraw()

def crossEyed():
    delClosedEyes()
    resetEyes()
    lPupil.undraw()
    rPupil.undraw()
    rLightEye.undraw()
    lLightEye.undraw()
    global rCrossed
    global lCrossed
    global rCrossedLight
    global lCrossedLight
    rCrossed = Polygon(Point(187, 118), Point(191, 119), Point(193, 121), Point(194, 125), Point(194, 129), Point(193, 134), Point(191, 135), Point(188, 135), Point(186, 130), Point(186, 126), Point(187, 121))
    rCrossed.setFill("black")
    rCrossed.draw(win)
    lCrossed = Polygon(Point(155, 118), Point(152, 118), Point(150, 121), Point(148, 124), Point(147, 128), Point(149, 132), Point(151, 133), Point(153, 131), Point(154, 127), Point(155, 122))
    lCrossed.setFill("black")
    lCrossed.draw(win)
    rCrossedLight = Circle(Point(189, 124), 2)
    rCrossedLight.setFill("white")
    rCrossedLight.draw(win)
    lCrossedLight = Circle(Point(151, 123), 2)
    lCrossedLight.setFill("white")
    lCrossedLight.draw(win)
                        
def delCrossedEyed():
    rCrossed.undraw()
    lCrossed.undraw()
    rCrossedLight.undraw()
    lCrossedLight.undraw()

def evilEyes():
    lPupil.undraw()
    rPupil.undraw()
    rLightEye.undraw()
    lLightEye.undraw()
    lEye.undraw()
    rEye.undraw()
    global rEvilEye
    rEvilEye = Polygon(Point(202, 119), Point(199, 121), Point(197, 124), Point(194, 126), Point(191, 127), Point(189, 129), Point(188, 130), Point(189, 133), Point(194, 136), Point(199, 135), Point(201, 130), Point(203, 127), Point(204, 125), Point(204, 120))
    rEvilEye.setFill("tomato2")
    rEvilEye.draw(win)
    global rEvilPupil
    rEvilPupil = Polygon(Point(195, 126), Point(194, 129), Point(194, 132), Point(195, 135), Point(197, 133), Point(197, 131), Point(197, 128), Point(196, 127))
    rEvilPupil.setFill("black")
    rEvilPupil.draw(win)
    global lEvilEye
    lEvilEye = Polygon(Point(155, 129), Point(152, 128), Point(149, 127), Point(147, 125),Point(145, 123), Point(143, 122), Point(143, 125), Point(142, 128), Point(143, 130), Point(145, 133), Point(147, 134), Point(147, 132),Point(149, 134),  Point(151, 133), Point(154, 131),Point(155, 129))
    lEvilEye.setFill("tomato2")
    lEvilEye.draw(win)
    global lEvilPupil
    lEvilPupil = Polygon(Point(148, 126), Point(147, 127), Point(147, 129), Point(147, 131), Point(148, 133), Point(149, 131), Point(150, 130), Point(150, 128), Point(150, 126)) 
    lEvilPupil.setFill("black")
    lEvilPupil.draw(win)

def delEvilEyes():
    rEvilEye.undraw()
    lEvilEye.undraw()
    rEvilPupil.undraw()
    lEvilPupil.undraw()

def toothlessEyes():
    lPupil.undraw()
    rPupil.undraw()
    rLightEye.undraw()
    lLightEye.undraw()
    lEye.undraw()
    rEye.undraw()
    global rToothEye
    rToothEye = Polygon(Point(181, 129), Point(183, 126), Point(185, 124), Point(188, 121), Point(193, 119), Point(196, 119), Point(199, 121), Point(201, 124), Point(201, 128), Point(200, 132), Point(195, 134), Point(190, 134), Point(185, 134), Point(182, 132))
    rToothEye.setFill("OliveDrab1")
    rToothEye.draw(win)
    global rToothPupil
    rToothPupil= Polygon(Point(187, 123), Point(186, 126), Point(188, 129), Point(190, 130), Point(192, 130), Point(193, 128), Point(193, 125), Point(193, 123), Point(192, 122), Point(191, 121), Point(190, 121), Point(188, 122))
    rToothPupil.setFill("black")
    rToothPupil.draw(win)
    global lToothEye
    lToothEye= Polygon(Point(143, 120), Point(146, 121), Point(149, 122), Point(151, 124), Point(153, 128), Point(154, 131), Point(150, 133), Point(147, 133), Point(142, 133), Point(140, 131), Point(139, 128), Point(139, 125), Point(140, 123)) 
    lToothEye.setFill("OliveDrab1")
    lToothEye.draw(win)
    global lToothPupil
    lToothPupil = Polygon(Point(147, 122), Point(145, 121), Point(144, 123), Point(143, 126), Point(144, 129), Point(147, 129), Point(149, 127), Point(148, 125), Point(148, 123), Point(145, 122))
    lToothPupil.setFill("black")
    lToothPupil.draw(win)

def delToothlessEyes():
    rToothEye.undraw()
    rToothPupil.undraw()
    lToothEye.undraw()
    lToothPupil.undraw()

def lightFuryEyes():
    lPupil.undraw()
    rPupil.undraw()
    rLightEye.undraw()
    lLightEye.undraw()
    lEye.undraw()
    rEye.undraw()
    global rFuryEye
    rFuryEye = Polygon(Point(181, 129), Point(183, 126), Point(185, 124), Point(188, 121), Point(193, 119), Point(196, 119), Point(199, 121), Point(201, 124), Point(201, 128), Point(200, 132), Point(195, 134), Point(190, 134), Point(185, 134), Point(182, 132))
    rFuryEye.setFill("CadetBlue2")
    rFuryEye.draw(win)
    global rFuryPupil
    rFuryPupil= Polygon(Point(187, 123), Point(186, 126), Point(188, 129), Point(190, 130), Point(192, 130), Point(193, 128), Point(193, 125), Point(193, 123), Point(192, 122), Point(191, 121), Point(190, 121), Point(188, 122))
    rFuryPupil.setFill("black")
    rFuryPupil.draw(win)
    global lFuryEye
    lFuryEye= Polygon(Point(143, 120), Point(146, 121), Point(149, 122), Point(151, 124), Point(153, 128), Point(154, 131), Point(150, 133), Point(147, 133), Point(142, 133), Point(140, 131), Point(139, 128), Point(139, 125), Point(140, 123)) 
    lFuryEye.setFill("CadetBlue2")
    lFuryEye.draw(win)
    global lFuryPupil
    lFuryPupil = Polygon(Point(147, 122), Point(145, 121), Point(144, 123), Point(143, 126), Point(144, 129), Point(147, 129), Point(149, 127), Point(148, 125), Point(148, 123), Point(145, 122))
    lFuryPupil.setFill("black")
    lFuryPupil.draw(win)

def delLightFuryEyes():
    rFuryEye.undraw()
    rFuryPupil.undraw()
    lFuryEye.undraw()
    lFuryPupil.undraw()

#Horns
def resetHorns():
    lHorn.draw(win)
    rHorn.draw(win)

def gazelleHorns():
    lHorn.undraw()
    rHorn.undraw()
    global rGazelleHorn
    rGazelleHorn = Polygon(Point(192, 94), Point(193, 90), Point(196, 83), Point(201, 80), Point(205, 74), Point(204, 68), Point(202, 61), Point(205, 55), Point(210, 55), Point(209, 58), Point(211, 63), Point(213, 68), Point(215, 74), Point(215, 79), Point(212, 85), Point(210, 89), Point(210, 96), Point(211, 102), Point(206, 103), Point(199, 103), Point(195, 100))
    rGazelleHorn.setFill("bisque2")
    rGazelleHorn.draw(win)
    global lGazelleHorn
    lGazelleHorn = Polygon(Point(142, 105), Point(146, 106), Point(150, 104), Point(153, 101), Point(155, 98), Point(155, 93), Point(155, 87), Point(153, 82), Point(149, 78), Point(149, 73), Point(152, 67), Point(154, 61),Point(152, 56), Point(147, 54), Point(142, 54), Point(146, 56), Point(147, 59), Point(146, 63), Point(144, 68), Point(140, 74), Point(137, 81), Point(137, 87), Point(138, 92), Point(141, 95), Point(143, 100))
    lGazelleHorn.setFill("bisque2")
    lGazelleHorn.draw(win)

def delGazelleHorns():
    rGazelleHorn.undraw()
    lGazelleHorn.undraw()

def toothlessEars():
    lHorn.undraw()
    rHorn.undraw()
    lEar.undraw()
    rEar.undraw()
    rBigEar.draw(win)
    rSmallEar.draw(win)
    lSmallEar.draw(win)
    lBigEar.draw(win)

def delToothlessEars():
    rBigEar.undraw()
    rSmallEar.undraw()
    lSmallEar.undraw()
    lBigEar.undraw()
    lEar.draw(win)
    rEar.draw(win)

def newHorns():
    rHorn.undraw()
    lHorn.undraw()
    global rNewHorn
    rNewHorn = Polygon(Point(193, 89), Point(196, 84), Point(200, 79), Point(202, 84), Point(203, 90), Point(203, 95), Point(200, 96), Point(194, 93))
    rNewHorn.setFill("bisque2")
    rNewHorn.draw(win)
    global lNewHorn
    lNewHorn = Polygon(Point(147, 83), Point(146, 87), Point(145, 93), Point(145, 99), Point(149, 99), Point(151, 97), Point(153, 93), Point(152, 90), Point(150, 87))
    lNewHorn.setFill("bisque2")
    lNewHorn.draw(win)

def delNewHorns():
    rNewHorn.undraw()
    lNewHorn.undraw()

#tail
def tailScales():
    tailScale.draw(win)

def delTailScales():
    tailScale.undraw()

def wingTail():
    rWingTail.draw(win)
    lWingTail.draw(win)

def delWingTail():
    rWingTail.undraw()
    lWingTail.undraw()

#fix
def toothlessTail():
    rWingTail.draw(win)
    lWingTail.draw(win)
    rWingTail.setFill("red3")
    global tailDesign
    tailDesign = Polygon(Point(136, 332), Point(138, 334), Point(140, 334), Point(142, 333), Point(143, 330), Point(146, 332), Point(145, 336), Point(146, 338), Point(145, 340), Point(142, 340), Point(139, 340), Point(139, 339), Point(138, 337), Point(136, 335), Point(136, 333))
    tailDesign.setFill("white")
    tailDesign.draw(win)

def delToothlessTail():
    tailDesign.undraw()
    rWingTail.undraw()
    lWingTail.undraw()
    
#changing functions
def changeColorForward(colorNum, tailNum):
    colorNum += 1
    if colorNum == 10:
        colorNum = 0
    if colorNum == 0:
        colorRed()
    elif colorNum == 1:
        colorGreen()
    elif colorNum == 2:
        colorGold()
    elif colorNum == 3:
        colorBlack()
    elif colorNum == 4:
        colorTurquoise()
    elif colorNum == 5:
        colorPink()
    elif colorNum == 6:
        colorWhite()
    elif colorNum == 7:
        colorOrange()
    elif colorNum == 8:
        colorBrown()
    else:
        colorPurple()
    if tailNum == 2:
        rWingTail.setFill("red3")
    return colorNum

def changeColorBack(colorNum, tailNum):
    colorNum = colorNum - 1
    if colorNum == -1 or colorNum == -2:
        colorNum = 9   
    if colorNum == 0:
        colorRed()
    elif colorNum == 1:
        colorGreen()
    elif colorNum == 2:
        colorGold()
    elif colorNum == 3:
        colorBlack()
    elif colorNum == 4:
        colorTurquoise()
    elif colorNum == 5:
        colorPink()
    elif colorNum == 6:
        colorWhite()
    elif colorNum == 7:
        colorOrange()
    elif colorNum == 8:
        colorBrown()
    else:
        colorPurple()
    if tailNum == 2:
        rWingTail.setFill("red3")
    return colorNum

def changeHornsForward(hornNum):
    hornNum += 1
    if hornNum == 4:
        hornNum = 0
    if hornNum == 0:
        gazelleHorns()
    elif hornNum == 1:
        delGazelleHorns()
        toothlessEars()
    elif hornNum == 2:
        delToothlessEars()
        newHorns()
    elif hornNum == 3:
        delNewHorns()
        resetHorns()
    return hornNum

def changeHornsBack(hornNum):
    hornNum = hornNum - 1
    if hornNum == -1 or hornNum == -2:
        hornNum = 3
    if hornNum == 0:
        delToothlessEars()
        gazelleHorns()
    elif hornNum == 1:
        delNewHorns()
        toothlessEars()
    elif hornNum == 2:
        newHorns()
    elif hornNum == 3:
        try:
            delGazelleHorns()
            resetHorns()
        except NameError:
            notNeededNum = 0
    return hornNum

def changeEyesForward(eyeNum):
    eyeNum += 1
    if eyeNum == 6:
        eyeNum = 0
    if eyeNum == 0:
        closedEyes()
    elif eyeNum == 1:
        delClosedEyes()
        crossEyed()
    elif eyeNum == 2:
        delCrossedEyed()
        evilEyes()
    elif eyeNum == 3:
        delEvilEyes()
        toothlessEyes()
    elif eyeNum == 4:
        delToothlessEyes()
        lightFuryEyes()
    else:
        delLightFuryEyes()
        resetEyes()
    return eyeNum

def changeEyesBack(eyeNum):
    eyeNum = eyeNum - 1
    if eyeNum == -1 or eyeNum == -2:
        eyeNum = 5
    if eyeNum == 0:
        delCrossedEyed()
        closedEyes()
    elif eyeNum == 1:
        delEvilEyes()
        crossEyed()
    elif eyeNum == 2:
        delToothlessEyes()
        evilEyes()
    elif eyeNum == 3:
        delLightFuryEyes()
        toothlessEyes()
    elif eyeNum == 4:
        lightFuryEyes()
    else:
        try:
            delClosedEyes()
            resetEyes()
        except NameError:
            notNeededNum = 0
    return eyeNum

def changeTailForward(tailNum, colorNum):
    tailNum += 1
    if tailNum == 4:
        tailNum = 0
    if tailNum == 0:
        tailScales()
    elif tailNum == 1:
        delTailScales()
        wingTail()
        if colorNum == 0:
            colorRed()
        elif colorNum == 1:
            colorGreen()
        elif colorNum == 2:
            colorGold()
        elif colorNum == 3:
            colorBlack()
        elif colorNum == 4:
            colorTurquoise()
        elif colorNum == 5:
            colorPink()
        elif colorNum == 6:
            colorWhite()
        elif colorNum == 7:
            colorOrange()
        elif colorNum == 8:
            colorBrown()
        else:
            colorPurple()
    elif tailNum == 2:
        delWingTail()
        toothlessTail()
    elif tailNum == 3:
        delToothlessTail()
    return tailNum

def changeTailBack(tailNum, colorNum):
    tailNum = tailNum - 1
    if tailNum == -1 or tailNum == -2:
        tailNum = 3
    if tailNum == 0:
        delWingTail()
        tailScales()
    elif tailNum == 1:
        delToothlessTail()
        wingTail()
        if colorNum == 0:
            colorRed()
        elif colorNum == 1:
            colorGreen()
        elif colorNum == 2:
            colorGold()
        elif colorNum == 3:
            colorBlack()
        elif colorNum == 4:
            colorTurquoise()
        elif colorNum == 5:
            colorPink()
        elif colorNum == 6:
            colorWhite()
        elif colorNum == 7:
            colorOrange()
        elif colorNum == 8:
            colorBrown()
        else:
            colorPurple()
    elif tailNum == 2:
        delWingTail()
        toothlessTail()
    elif tailNum == 3:
        try:
            delTailScales()
        except NameError:
            notNeededNum = 0
    return tailNum

colorNum = -1
hornNum = -1
eyeNum = -1
tailNum = -1
while True:
    chooseKey = input("")
    if chooseKey == "w":
        colorNum = changeColorForward(colorNum, tailNum)
    elif chooseKey == "q":
        colorNum = changeColorBack(colorNum, tailNum)
    elif chooseKey == "s":
        hornNum = changeHornsForward(hornNum)
    elif chooseKey == "a":
        hornNum = changeHornsBack(hornNum)
    elif chooseKey == "x":
        eyeNum = changeEyesForward(eyeNum)
    elif chooseKey == "z":
        eyeNum = changeEyesBack(eyeNum)
    elif chooseKey == "r":
        tailNum = changeTailForward(tailNum, colorNum)
    elif chooseKey == "e":
        tailNum = changeTailBack(tailNum, colorNum)

