##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-205IQ-tom.hermann
## File description:
## Makefile
##

MAIN = src/main.py

NAME = 205IQ

all: $(NAME)

$(NAME):
	cp $(MAIN) ./$(NAME)
	chmod +x $(NAME)

fclean:
	rm -f $(NAME)

re: fclean all