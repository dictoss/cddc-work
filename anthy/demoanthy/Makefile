#################################################
# Makefile
#################################################
# directorys
SRCDIR=src

# compiler
CC=gcc

# compile and link option(both)
DEBUG=-O0
BIN=a.out
OBJS=$(SRCDIR)/main.o

# compile option
LIBS=

# link option
CFLAGS=
LDFLAGS=-lanthy

#################################################
#
################################################
.PHONY:all
all:$(BIN)

$(BIN):$(OBJS)
	$(CC) $(DEBUG) $(LDFLAGS) -o $(BIN) $(LIBS) $(OBJS)

.PHONY:clean
clean:
	rm -f $(BIN) $(OBJS) *~

#################################################
# suffixes
#################################################
.SUFFIXES: .c .o
.c.o:
	$(CC) $(DEBUG) $(CFLAGS) -c $< -o $@
