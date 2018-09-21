-------------------------------------------------------------
                         Introduction
-------------------------------------------------------------
Ce programme est un outil servant à modifier les entrées de
texte du jeu DS "Tottoko Hamtaro : Nazo Nazo Q".
Il ne permet de modifier que le texte, pas les images
contenant du texte.

Avant de l'utiliser, il faut savoir "extraire" des fichiers
d'une ROM nds. Pour cela, il suffit de rechercher sur
internet "nds unpack" et trouver un logiciel permettant
d'"extraire" ces fichiers.

Placez ces fichiers dans un dossier X (vous pouvez
renommer X par n'importe quel nom.).
Ce programme ne peut modifier que ces fichiers, pas la ROM.

Après avoir "extrait" les fichiers, remplacez le fichier
"X/data/Font/StatFontSet.dat" par celui situé dans "Font".
Celui-ci contient des caractères qui n'étaient pas présents
dans le fichier original (comme l'apostrophe).

Maintenant, vous pouvez modifier ces fichiers.
-------------------------------------------------------------
                     Comment ça marche ?
-------------------------------------------------------------
-Lancez "Program/Editor.exe"
-Une fois lancé, ouvrez un fichier (voir ci-dessous pour
une liste de fichiers importants) en cliquant sur le bouton
"Open".
-S'il n'y a pas d'erreur,  vous verrez un arbre avec des
nombres (indices) ou du texte.
-Parcourez l'arbre (en déroulant les lignes avec indices)
pour sélectionner une ligne de texte à modifier, et
modifiez-le dans l'entrée de texte située en bas de la
fenêtre. N'oubliez pas de cliquer sur le bouton "Edit" avant
de passer à une autre ligne, ou les changements ne seront
pas effectués.
-N'oubliez pas de sauvegarder le fichier avant de fermer
la fenêtre.

NB : S'il elle est cochée, la case à cocher "Debug" force
le programme à recharger l'arbre après chaque modification.
C'est plus lent, mais cela permet de vérifier si les
changements ont été effectués correctement.
Pour plus d'informations, ouvrez le fichier
"Doc/Examples.pdf".
-------------------------------------------------------------
                     Caractères spéciaux
-------------------------------------------------------------
Certaines lignes de texte peuvent contenir des caractères
spéciaux. Tous ces caractères spéciaux sont signalés par le
fait qu'ils sont entre deux caractères "|".

Voici la liste de ces caractères : 

|NL| : Retour à la ligne.
|Blue|, |Red| or |Black| : Sont utilisés pour changer la
couleur du texte qui suit.
|Start| : Indique un début de boîte de dialogue. Attention, 
il peut être omis.
|End| : Indique une fin de boîte de dialogue. Attention, 
il peut être omis.
|Pause| : Marque une pause de quelques secondes avant
d'enchaîner sur la boîte de dialogue suivante.
|Next| : Indique la présence d'une autre boîte de dialogue
à la suite de la ligne.

NB : Si vous souhaitez ajouter une autre boîte de dialogue
(notamment pour pouvoir afficher plus de texte you pouvez
insérer "|End||n00||Next||n00|" entre "|Start|" et "|End|",
ce qui finit la précédente boîte de dialogue, indique
la présence d'une nouvelle boîte de dialogue et la
commence.

|nXX| : D'autres caractères spéciaux, ne les supprimez
jamais.
|xXX| : D'autres caractères spéciaux, évitez de les
supprimer. Certains peuvent changer la couleur et la
taille du texte.
|cXX| : Des symboles spéciaux, comme un symbole en forme de
coeur.

NB : N'utilisez JAMAIS |n254| et |n255|.

-------------------------------------------------------------
                      Liste de fichiers
-------------------------------------------------------------
Ceci est une de fichiers contenant du texte pouvant être
modifié. N'oubliez pas que d'autres fichiers peuvent
contenir du texte, mais ces fichiers semblent contenir plus
de 90% du texte du jeu (incluant les énigmes et les
dialogues des cinématiques).

-X/data/QMsg/QMsgDat.dat (où l'on peut trouver les énigmes.)
-X/data/FEvent/FEvData_AS.dat
-X/data/FEvent/FEvData_HN.dat
-X/data/FEvent/FEvData_MM.dat
-X/data/FEvent/FEvData_NH.dat
-X/data/FEvent/FEvData_YM.dat
-X/data/Furniture/FurnitureName.dat
-X/data/Furniture/FurnitureSetName.dat
-X/data/Furniture/FurnitureName.dat
-X/data/House/HouseHamFurnMsg.dat
-X/data/House/HouseHamTouchMsg.dat
-X/data/House/HouseSysMsg.dat
-X/data/MMsg/MSysMsg.dat
-X/data/WMsg/WSysMsg.dat
-X/data/QEvent/NandeQEvMesData.dat
-X/data/QEvent/SorahamQEvMesData.dat
-X/data/UserList/UserList.dat
-X/data/UserList/AreaName.dat

Plus d'info sur certains fichiers : 

-data/QMsg/QMsgDat.dat
Les lignes de texte à l'indice 0 de l'arbre
sont des lignes utilisés lors du menu de
sélection d'énigmes (le livre d'énigmes).
Les lignes de texte à l'indice 1 de l'arbre
sont les noms des différents rangs utilisés
dans le jeu.
Les indices 3 jusqu'à la fin contiennent les
énigmes.
Chaque indice contenant une énigme comporte 6 lignes : 
-La question
-La première réponse (qui est toujours la bonne réponse).
-La deuxième réponse
-La troisième réponse
-L'indice
-L'explication de la réponse.

-data/FEvent/*
Tous ces fichiers ont la même structure.
Ils contiennent une répétition des éléments suivants : 
-Une ou plusieurs lignes (probablement des données pour
les animations).
-Une ligne avec un sous-indice 0 qui contient du texte.
