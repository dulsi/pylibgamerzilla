%module gamerzilla
%{
#include "gamerzilla.h"
%}

typedef struct
{
	char *name;
	char *desc;
	int max_progress;
	char *true_image;
	char *false_image;
} GamerzillaTrophy;

typedef struct
{
	char *short_name;
	char *name;
	char *image;
	int version;
	int numTrophy;
	int szTrophy;
	GamerzillaTrophy *trophy;
} Gamerzilla;

extern bool GamerzillaStart(bool server, const char *savedir);
extern bool GamerzillaConnect(const char *url, const char *username, const char *password);
extern void GamerzillaInitGame(Gamerzilla *g);
extern int GamerzillaSetGame(Gamerzilla *g);
extern void GamerzillaGameAddTrophy(Gamerzilla *g, char *name, char *desc, int max_progress, char *true_image, char *false_image);
%include "typemaps.i"
extern bool GamerzillaGetTrophy(int game_id, const char *name, bool *OUTPUT);
extern bool GamerzillaGetTrophyStat(int game_id, const char *name, int *OUTPUT);
extern bool GamerzillaSetTrophy(int game_id, const char *name);
extern bool GamerzillaSetTrophyStat(int game_id, const char *name, int progress);
extern void GamerzillaServerProcess(struct timeval *timeout);
extern void GamerzillaQuit();

%include <carrays.i>
%array_functions(GamerzillaTrophy, GamerzillaTrophyArray);
