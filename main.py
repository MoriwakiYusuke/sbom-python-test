import pyfiglet
from colorama import Fore, Style, init

# coloramaを初期化

init()

# pyfigletでASCIIアートのテキストを生成

ascii_banner = pyfiglet.figlet_format("SBOM Test")

# coloramaで色を付けて表示

print(Fore.YELLOW + ascii_banner)

# スタイルをリセット

print(Style.RESET_ALL)