# GeradorScripts

## Descrição

O **GeradorScripts** é um programa em Python que cria arquivos de lote (.bat) para ativação do **Windows** e **Office 2021**. É especialmente útil para empresas que trabalham com listas de seriais oficiais OEM. O programa não ativa versões "piratas" do Windows ou do Office.

## Funcionalidade

O programa gera um arquivo de lote para cada máquina, usando o nome presente na segunda coluna da tabela, denominada **numeroTombo**.

### Formato da Tabela XLSX

A tabela deve seguir o formato abaixo:

| indiceQuantidade | numeroTombo | serialWindows               | serialOffice                |
|------------------|-------------|-----------------------------|-----------------------------|
| 1                | 123456      | ABCDE-FGHIJ-KLMNO-PQRST-UVWXY | AAAAA-BBBBB-CCCCC-DDDDD-EEEEE |
| 2                | 654321      | VWXYZ-ABCDE-FGHIJ-KLMNO-PQRST | FFFFF-GGGGG-HHHHH-IIIII-JJJJJ |
| 3                | 789123      | MNOPQ-RSTUV-WXYZ0-ABCDE-FGHIJ | KKKKK-LLLLL-MMMMM-NNNNN-OOOOO |
| 4                | 456789      | UVWXY-ZZZZZ-YYYYY-XXXXX-WWWWW | PPPPP-QQQQQ-RRRRR-SSSSS-TTTTT |

### Validação

O sistema valida a quantidade de caracteres (25) em cada um dos campos da lista e gera o script adequado para cada caso. 

- O nome do arquivo .bat gerado será sempre de 6 caracteres, completando com zeros à esquerda, caso o valor seja inferior a 6 caracteres.

## Compilação

Para gerar o executável que ficará disponível na pasta `DIST`, use o seguinte comando:

```bash
pyinstaller gerador.spec
