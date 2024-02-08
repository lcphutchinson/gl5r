# GL5R Development Documentation

"Game Lieutenant" is a programmable toolsuite for authors of tabletop roleplaying games operating on the Discord social media platform. Its objective is to deliver four interconnected services--Character Data Storage, Game System Data Storage, Resolver Management, and Scene Management--as defined by "Game Systems" created and customized by authors using the Game Lieutenant web API.

"GL5R" is a requirements elicitation project and prototype of Game Lieutenant's Services components using Fantasy Flight Games' 'Legend of the Five Rings' Roleplaying game as its underlying system. 

Development is still in its earliest stages, so documentation \(including this Readme\) will be sparse until I verify the workability of my architecture. 

## Services

Game Lieutenant's services are the project's central deliverable, and are defined roughly as follows.

> - **Character Data Storage**: Provides an interface for the construction, maintenance, and formatted full or partial retrieval of character records. Constitutive fields of the character record are determined by the game syster, as are the interface interactions governing the exact character creation and update processes.
>
> - **Game System Data Storage**: Provides a simple lookup tool for predefined rules and game features defined in the game system. 
>
> - **Resolver Management**: Provides an interface for the execution of a game process for resolving uncertainty, called a Resolver. Resolvers are defined in the game system and draw component data from the Character Record.
>
> - **Scene Management**: Provides a framework for the turn-by-turn execution of a game scenario, called a Scene. Scenes are defined in the game system and structure resolver calls and character rewards.
>
