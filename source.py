import argparse
import logging
import os

from deeputils.logger import setup_log


class Source:
    def __init__(self, output):
        self.output = output

    def run(self, path):
        with open(self.output, 'w') as output:
            for p, _, f in os.walk(path):
                for i in f:
                    u = os.path.join(p, i)
                    logging.info(u)
                    output.write('========================================\n')
                    output.write(u)
                    output.write('\n========================================\n')
                    with open(u, 'r') as m:
                        try:
                            for line in m.readlines():
                                output.write(line)
                                output.write('\n')
                        except Exception as exp:
                            logging.error(exp)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true', default=False, help='show debug information')
    parser.add_argument('input', type=str, help='source code root path')
    parser.add_argument('output', type=str, help='output file name')
    args, _ = parser.parse_known_args()
    setup_log(level=logging.DEBUG if args.debug else logging.INFO)
    Source(args.output).run(args.input)
