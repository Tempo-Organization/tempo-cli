making a new tempo project is done by using the tempo_cli init command
this init command can also take in a directory like
tempo_cli init --directory ../path/to/dir
it expects the directory to exist and will not generate it on it's own if it does not
This will also generate a uproject if one is not provided, as well as make a git repo if one is not provided
the first is needed for almost all modding setups, the second is needed mainly for the cleanup commands, but also code management

after the setup is done through those questions, the next step is to run the tempo_cli mod add-mod command one or more times depending on how many mods you plan to have for this project.

then you can open the editor, make your mod files in the appropriate locations,
then use the 
tempo_cli run test-mods-all command to make your mods, and test them in game
or the 
tempo_cli run full-run-all command to make your mods, and package them into release zips, for places like github, nexus mods, etc...
