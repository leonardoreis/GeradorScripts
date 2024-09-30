import argparse
import pandas as pd
import os


def formatar_serial(serial):
    """Formata o serial no formato XXXXX-XXXXX-XXXXX-XXXXX-XXXXX, se tiver 25 caracteres."""
    serial = serial.replace("-", "")
    if len(serial) != 25:
        return None
    return f"{serial[:5]}-{serial[5:10]}-{serial[10:15]}-{serial[15:20]}-{serial[20:]}"


def gerar_scripts(caminho_arquivo):
    if not os.path.isfile(caminho_arquivo):
        print(f"Erro: O caminho {caminho_arquivo} não é um arquivo válido.")
        return

    df_dados = pd.read_excel(caminho_arquivo)
    df_dados = df_dados.drop(0)
    df_dados = df_dados.rename(
        columns={'Unnamed: 0': 'indiceQuantidade', 'Unnamed: 1': 'numeroTombo', 'Unnamed: 2': 'serialWindows',
                 'Unnamed: 3': 'serialOffice'})
    df_dados['indiceQuantidade'] = pd.to_numeric(df_dados['indiceQuantidade'], errors='coerce')
    df_dados['numeroTombo'] = df_dados['numeroTombo'].astype("string")
    df_dados['numeroTombo'] = df_dados['numeroTombo'].apply(lambda x: x.zfill(6) if pd.notna(x) else x)
    df_dados['serialWindows'] = df_dados['serialWindows'].astype("string")
    df_dados['serialOffice'] = df_dados['serialOffice'].astype("string")

    arquivos_gerados = 0

    for idx, row in df_dados.iterrows():
        script = ""
        aviso = False

        if pd.notna(row['serialWindows']):
            serial_windows_formatado = formatar_serial(row['serialWindows'])
            if serial_windows_formatado:
                script += (
                    '@echo off'
                    'echo Ativando Windows...\n'
                    f'slmgr /ipk {serial_windows_formatado}\n'
                    'slmgr /ato\n'
                    'slmgr /xpr\n'
                    'echo.\n'
                    'echo.\n'
                    'timeout 02\n'
                    'cls\n\n'
                )
            else:
                aviso = True
                print(f"Aviso: Serial do Windows inválido na linha {idx + 1}. Ignorando script do Windows.")

        if pd.notna(row['serialOffice']):
            serial_office_formatado = formatar_serial(row['serialOffice'])
            if serial_office_formatado:
                ultimo_bloco_office = serial_office_formatado.split('-')[-1]

                script += (
                    '@echo off'
                    'echo Ativando Office 2021...\n'
                    'cd /d %ProgramFiles%\\Microsoft Office\\Office16\n'
                    'dir /b ..\\root\\Licenses16\\ProPlus2019VL*.xrm-ms\n'
                    'cscript ospp.vbs /setprt:1688\n'
                    f'cscript ospp.vbs /unpkey:{ultimo_bloco_office} >nul\n'
                    f'cscript ospp.vbs /inpkey:"{serial_office_formatado}"\n'
                    'cscript ospp.vbs /sethst:e8.us.to\n'
                    'cscript ospp.vbs /act\n'
                    'echo.\n'
                    'echo.\n'
                    'timeout 02\n'
                    'cls\n\n'
                )
            else:
                aviso = True
                print(f"Aviso: Serial do Office inválido na linha {idx + 1}. Ignorando script do Office.")

        if script:
            script += 'echo Excluindo arquivo...\n'
            script += 'del "%~f0"\n'

            nome_arquivo = f"{row['numeroTombo']}.bat"
            with open(nome_arquivo, 'w') as arquivo:
                arquivo.write(script)

            print(f"Arquivo gerado: {nome_arquivo}")
            arquivos_gerados += 1
        elif aviso:
            print(f"Nenhum script válido gerado na linha {idx + 1} devido a seriais inválidos.")

    print(f"\nTotal de arquivos gerados: {arquivos_gerados}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Gera scripts .bat para ativar Windows e Office usando informações de um arquivo Excel.")
    parser.add_argument("caminho_arquivo", help="Caminho para o arquivo Excel com os dados necessários.")
    args = parser.parse_args()

    gerar_scripts(args.caminho_arquivo)
