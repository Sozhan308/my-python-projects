import psutil



def main():
    print('MEMORY\n------')
    print(psutil.virtual_memory())
    print('\nSWAP\n----')
    print(psutil.swap_memory())


if __name__ == '__main__':
    main()