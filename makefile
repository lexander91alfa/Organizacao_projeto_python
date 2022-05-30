all:
	@echo "Scripts para facilitar a vida"

formatar:
	@echo "Formatando código..."
	blue cesar/*
	blue tests/*
	isort cesar/*
	isort tests/*

documentando.new:
	@echo "Documentando..."
	mkdocs new .

documentando.serve:
	@echo "rodando..."
	mkdocs serve -a 127.0.0.1:8980