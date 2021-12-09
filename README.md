# discord_dynamic_status
automatically changes your discord statust

maked in Mar 28, 2021

в основе лежит https://github.com/Akkihi/ds-7 <-parent class

имеет несколько режимов:

	1.бегущая строка (dynamic_status) - создаёт статус длинны dynamic_status_len, в начале статуса dynamic_status_len пробелов. Так как дискорд удаляет пробелыв начале статуса, все пробелы заменяются на '.'
	
	2.замена нескольких строк (multi_status) - поочерёдно заменяет статусы из multi_status_text_list, можно задавать emoji для каждого статуса в multi_status_emoji_list (количество элемнтов в multi_status_text_list должно быть равно количеству элементов multi_status_emoji_list! Можно просто добавлять " ")
	
	3.goul_status - режим из https://github.com/Akkihi/ds-7
	
	4.status_reset - сбрасывает статус на значения из efault_status, efault_emoji и завершает работу скрипта
	
После запуска вы можете написать в консоль "end" (без кавычек), тогда программа запустит status_reset и завершится
