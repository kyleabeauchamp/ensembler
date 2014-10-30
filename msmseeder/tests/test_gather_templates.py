import os
import StringIO
import msmseeder.PDB

def test_extract_residues_by_resnum_from_4CFE():
    # 4CFE contains a 'TPO' residue
    pdb_input_filepath = os.path.join('tests', 'resources', '4CFE.pdb.gz')
    desired_chainID = 'A'
    desired_resnums = [str(x) for x in range(16, 269)]
    ofile = StringIO.StringIO()

    nlines_extracted = msmseeder.PDB.extract_residues_by_resnum(ofile, pdb_input_filepath, desired_resnums, desired_chainID)
    print len(desired_resnums)
    print nlines_extracted
    ofile.close()

    assert nlines_extracted == len(desired_resnums)

def test_extract_residues_by_resnum_from_3HLL():
    # 3HLL contains resnums '56A' and '93B'
    pdb_input_filepath = os.path.join('tests', 'resources', '3HLL.pdb.gz')
    desired_chainID = 'A'
    desired_resnums = [str(x) for x in range(24, 172) + range(183, 309)]
    desired_resnums[desired_resnums.index('56')] = '56A'
    desired_resnums[desired_resnums.index('93')] = '93B'
    ofile = StringIO.StringIO()

    nlines_extracted = msmseeder.PDB.extract_residues_by_resnum(ofile, pdb_input_filepath, desired_resnums, desired_chainID)
    print len(desired_resnums)
    print nlines_extracted
    print ofile.getvalue()
    ofile.close()

    assert nlines_extracted == len(desired_resnums)

def test_extract_residues_by_resnum_output():
    pdb_input_filepath = os.path.join('tests', 'resources', '3HLL.pdb.gz')
    desired_chainID = 'A'
    desired_resnums = [str(x) for x in range(24, 172) + range(183, 309)]
    desired_resnums[desired_resnums.index('56')] = '56A'
    desired_resnums[desired_resnums.index('93')] = '93B'
    ofile = StringIO.StringIO()

    nlines_extracted = msmseeder.PDB.extract_residues_by_resnum(ofile, pdb_input_filepath, desired_resnums, desired_chainID)
    ofile_text = ofile.getvalue()
    first_line = ofile_text[0: ofile_text.index('\n')]

    assert first_line == 'ATOM    175  N   TYR A  24      50.812  43.410  19.390  1.00 38.55           N  '
    ofile.close()