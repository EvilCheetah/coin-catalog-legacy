from scrapper.Russia import scrapper


if __name__ == '__main__':
	try:
		scrapper.main()

	except KeyboardInterrupt:
		print('Program has been terminated...')
