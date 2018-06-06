import argparse
import os.path


def reparse_cacerts_file(source, output):
    started = False
    with open(output, 'wb') as fout:
        with open(source, 'rb') as fin:
            for line in fin:
                if not started:
                    if not line.rstrip(b'\r\n').strip():
                        continue
                    started = True
                probe = None
                try:
                    _ = line.decode('ascii')
                    probe = line
                except UnicodeDecodeError as ex:
                    pass
                if probe is None:
                    probe = line.decode('utf-8').encode('ascii', 'backslashreplace')
                fout.write(probe)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', nargs=1, type=str, required=True)
    parser.add_argument('--output', nargs=1, type=str, required=True)
    args = parser.parse_args()
    source = os.path.normpath(os.path.abspath(args.source[0]))
    output = os.path.normpath(os.path.abspath(args.output[0]))
    reparse_cacerts_file(source, output)


if __name__ == '__main__':
    main()
