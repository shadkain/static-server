from pkg.server import Server


def main():
    server = Server('config.json')
    server.run()

if __name__ == '__main__':
    main()