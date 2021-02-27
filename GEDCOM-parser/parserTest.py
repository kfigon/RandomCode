import unittest
from parser import *

#0 HEAD
#  1 SOUR PAF
#    2 NAME Personal Ancestral File
#    2 VERS 5.0
#  1 DATE 30 NOV 2000
#  1 GEDC
#    2 VERS 5.5
#    2 FORM LINEAGE-LINKED
#  1 CHAR ANSEL
#  1 SUBM @U1@
#0 @I1@ INDI
#  1 NAME John /Smith/
#  1 SEX M
#  1 FAMS @F1@
#0 @I2@ INDI
#  1 NAME Elizabeth /Stansfield/
#  1 SEX F
#  1 FAMS @F1@
#0 @I3@ INDI
#  1 NAME James /Smith/
#  1 SEX M
#  1 FAMC @F1@
#0 @F1@ FAM
#  1 HUSB @I1@
#  1 WIFE @I2@
#  1 MARR
#  1 CHIL @I3@
#0 @U1@ SUBM
#  1 NAME Submitter
#0 TRLR


sample='''0 HEAD
1 SOUR PAF
2 NAME Personal Ancestral File
2 VERS 5.0
1 DATE 30 NOV 2000
1 GEDC
2 VERS 5.5
2 FORM LINEAGE-LINKED
1 CHAR ANSEL
1 SUBM @U1@
0 @I1@ INDI
1 NAME John /Smith/
1 SEX M
1 FAMS @F1@
0 @I2@ INDI
1 NAME Elizabeth /Stansfield/
1 SEX F
1 FAMS @F1@
0 @I3@ INDI
1 NAME James /Smith/
1 SEX M
1 FAMC @F1@
0 @F1@ FAM
1 HUSB @I1@
1 WIFE @I2@
1 MARR
1 CHIL @I3@
0 @U1@ SUBM
1 NAME Submitter
0 TRLR'''

class Test1(unittest.TestCase):
    def testMetadata(self):
        model: GedcomModel = parse(sample)
        self.assertEqual('5.5', model.version)
        self.assertEqual('ANSEL', model.encoding)
        self.assertEqual('PAF', model.source)
        self.assertEqual('Personal Ancestral File', model.fullSource)

if __name__ == '__main__':
    unittest.main()