# GeradorScripts
Gerador de Scripts em PYTHON que cria arquivos de LOTE (.bat) para ativação do WINDOWS e OFFICE 2021 - para empresas que trabalham com listas de seriais oficiais OEM. O programa não ativa windows ou office "pirata"!
O programa cria um arquivo de lote para cada máquina com o nome constante na segunda coluna "numeroTombo".

O formato da tabela XLSX é conforme está abaixo:

O sistema valida a quantidade de caracteres (25) em cada um dos campos da lista, gerando o script adequado para cada caso.

O nome do arquivo .bat GERADO será de 6 caracteres - completando com 0 (zeros) à esquerda, caso sejam abaixo de 6 caracteres.


| indiceQuantidade | numeroTombo | serialWindows           | serialOffice            |
|------------------|-------------|-------------------------|-------------------------|
| 1                | 123456      | ABCDE-FGHIJ-KLMNO-PQRST-UVWXY | AAAAA-BBBBB-CCCCC-DDDDD-EEEEE |
| 2                | 654321      | VWXYZ-ABCDE-FGHIJ-KLMNO-PQRST | FFFFF-GGGGG-HHHHH-IIIII-JJJJJ |
| 3                | 789123      | MNOPQ-RSTUV-WXYZ0-ABCDE-FGHIJ | KKKKK-LLLLL-MMMMM-NNNNN-OOOOO |
| 4                | 456789      | UVWXY-ZZZZZ-YYYYY-XXXXX-WWWWW | PPPPP-QQQQQ-RRRRR-SSSSS-TTTTT |
