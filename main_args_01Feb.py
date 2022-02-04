import argparse


def main():
    parser = argparse.ArgumentParser(description="Restful file server")
    parser.add_argument('-d', '--directory', dest="path", help='Root directory', required=True)
    parser.add_argument('-o', dest="optional", help='Some optional arg')
    parser.add_argument('--port', type=int, help='Port to work with', default=8080)
    args = parser.parse_args()
    print(args)
    print(f"dir = {args.path}")
    if args.optional:
        print(f"Optional arg : {args.optional}")
    pass


if __name__ == "__main__":
    main()
