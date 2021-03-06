#!/usr/bin/env python
#
# Refine models with implicit-solvent MD simulations
#
# Daniel L. Parton <daniel.parton@choderalab.org> - 21 Mar 2014
#

import argparse
import ensembler
import ensembler.refinement

def main():
    # ========
    # Parse command-line arguments
    # ========

    argparser = argparse.ArgumentParser(description='Conducts implicit-solvent MD refinement on a set of models.', formatter_class=argparse.RawTextHelpFormatter)

    argparser.add_argument('--openmm_platform', choices=['CUDA', 'OpenCL', 'CPU', 'Reference'], default='CUDA', help='(Default: CUDA) Choose the OpenMM Platform to use.')
    argparser.add_argument('-gpupn', type=int, default=1, help='(Default: 1) If using GPUs, select how many are available per node.')
    argparser.add_argument('--targets', nargs='+', help='(Default: all targets) Optionally define a subset of targets to work on by providing one or more target IDs separated by spaces (e.g. "ABL1_HUMAN_D0")')
    argparser.add_argument('--targetsfile', type=str, help='Optionally define a filename containing a list of newline-separated target IDs. Comment targets out with "#".')
    argparser.add_argument('--templates', nargs='+', help='(Default: all templates) Optionally define a subset of templates to work on by providing one or more template IDs separated by spaces (e.g. "ABL1_HUMAN_D0_1OPL_A")')
    argparser.add_argument('-v', '--verbose', action='store_true', help='Verbose')
    args = argparser.parse_args()

    ensembler.core.check_project_toplevel_dir()

    # ========
    # Process args
    # ========
    if args.targetsfile != None:
        with open(args.targetsfile, 'r') as targetsfile:
            process_only_these_targets = [line.strip() for line in targetsfile.readlines() if line[0] != '#']
    elif args.targets != None:
        process_only_these_targets = args.targets
    else:
        process_only_these_targets = None

    # ========
    # Run simulations
    # ========

    ensembler.refinement.refine_implicit_md(openmm_platform=args.openmm_platform, gpupn=args.gpupn, process_only_these_targets=process_only_these_targets, process_only_these_templates=args.templates, verbose=args.verbose)

if __name__ == '__main__':
    main()
