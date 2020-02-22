def car():
	user_in = input('>')

	if user_in == 'help':
		print('''-----------------------
	1.start
	2.stop
	3.quit''')
	menu_opts = input('>')

	def go_again():
		global again
		again = input('>')
		if again.lower() == 'start':
			print('Car started...Ready to go!')
		
		elif again.lower() == 'stop':
			print('Car stopped.')

		elif again.lower() == 'help':
				print('''-----------------------
	1.start
	2.stop
	3.quit''')

		global again_options
		again_options = input('>')	

		if again_options.lower() == 'start':
			print('Car started...Ready to go!')
			go_again()


		elif again_options.lower() == 'stop':
			print('Car stopped.')
			go_again()

		elif again_options.lower() == 'help':
			print('''-----------------------
	1.start
	2.stop
	3.quit''')

		elif again_options == 'quit':
			print('(YOU MAY HAVE TO QUIT MORE THAN 1 TIME \n depending on the number of time that you ran commands')
			quit()

		elif again.lower() == 'quit':
			quit()

		while again != 'quit':

			go_again()

	if menu_opts.lower() == 'start':
		print('Car started...Ready to go!')
		go_again()


	elif menu_opts.lower() == 'stop':
		print('Car stopped.')
		go_again()

	elif menu_opts == 'quit':
		print(' (YOU MAY HAVE TO QUIT MORE THAN 1 TIME \n depending on the number of time that you ran commands')
		quit()

car()
