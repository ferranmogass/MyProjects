CC = gcc
CFLAGS = -Wall -Wextra -std=c99
TARGET = pwcheck
SOURCE = pwcheck.c

all: $(TARGET)

$(TARGET): $(SOURCE)
	$(CC) $(CFLAGS) -o $(TARGET) $(SOURCE)

clean:
	rm -f $(TARGET)

test: $(TARGET)
	@echo "Probando contraseña débil:"
	./$(TARGET) "123456" common_passwords.txt
	@echo "\nProbando contraseña media:"
	./$(TARGET) "Password123"
	@echo "\nProbando contraseña fuerte:"
	./$(TARGET) "MiContraseña123!" common_passwords.txt

.PHONY: all clean test