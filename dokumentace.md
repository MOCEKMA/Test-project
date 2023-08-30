
### **Popis:**

Program řeší hlavolam kreslené křížovky, známé jako NONOGRAMY. Jde o obdélníkovou mřížku jejíž políčka řešitel vybarvuje podle zadaných čísel. Program nonogramy nenavrhuje, ale řeší a navíc nakreslí výsledek v modulu Python turtle. Nabízí se tedy využití pro tvůrce těchto nonogramů.


### Návod k použití:

Vytvořte v adresáři programu soubor a přepište do něj hodnoty vaší křížovky následujicím způsobem:
Čísla v každém sloupci pište postupně, oddělená mezerami, každý sloupec na nový řádek.
Poté vynechte jeden prázdný řádek a přepište čísla v řádcích tímtéž způsobem jako ve sloupcích. Zakončete jedním či více prázdnymi řádky. Soubor uložte.
Po spuštění programu zadejte jméno souboru a začne strhující řešení nonogramu :)


### Struktura a technický náhled:

Program funguje v prostředí jazyka python.
Mřížka křížovky je reprezentována 2-rozměrným polem (seznamem) ve kterém jsou hodnoty 3 typů - "bílá", "černá", "nevyplněno". Zadání je také uspořádáno do dvou 2-rozměrných polí. Při řešení úlohy se vyskytují řádky a sloupce, dále je budeme označovat jako "celky" (v kódu označení "colrow")

Samotný běh zajišťují funkce *projdi* a funkce *policko*.

Funkce "policko" dostane jako vstup pole celku v nevyplněném nebo částečně vyplněném stavu a dále pole s čísly zadání pro daný celek. Výstupem je seznam indexů které jsou určitě bílé a seznam těch, které jsou určitě černé. Funkce na principu rekurze volá sebe samu a pokaždé doplní postupně různý počet "bílých" polí a rekurze se ukončí právě tehdy, když dojde ke sporu se zadáním (tedy zkoušená kombinace je nevhodná) anebo když je řádek vhodný a zcela vyplněn.
Funkce zaznamenává každou nalezenou vhodnou kombinaci a zároveň jejich počet. Pak vrátí indexy těch polí, která bylá ve všech případech vyplněna stejně. Tyto hodnoty zanese do pole křížovky a v modulu turtle spustí zakreslení příslušných políček.


Funkce "projdi" používá frontu řádků/sloupců a aplikuje na ně výše popsanou funkci "policko". Pokud v daném celku některé prvky změní, připojí do fronty změněné indexy, protože tyto prvky změní i složení celku kolmého na ten aktuální. Pokud je fronta prázdná, funkce končí touto ukončovací podmínkou, protože pak jistě neexistují celky, které by šly nějak doplnit.

Program si udržuje kontrolní pole, udávající kolik políček je v jednotlivých řádcích/sloupcích doplněno. Podle těchto hodnot se na konci vyhodnotí zda je křížovka vyplněna anebo zda výpočet skončil kvůli chybě v zadání. Program byl otestován na křížovkách o velikosti až 30 x 30 polí.

### Shrnutí:
Pokud přepíšete zadání nonogramu do textového souboru, program ho vyřeší. Průběh přitom můžete sledovat v modulu turtle kde budou přibývat barevná políčka. Jsou 2 varianty jak může tento proces skončit:
a) úplným vyplněním křížovky
b) dříve kvůli sporu (tj. nastal spor a políčko nelze správně vyplnit)
c) dříve kvůli nedostatku informací (tj. spor nenastal ale nelze jednoznačně doplnit)

Děkuji že program používáte a přeji Vám s ním přijemnou zábavu.
