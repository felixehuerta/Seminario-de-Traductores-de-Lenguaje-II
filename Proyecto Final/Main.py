from Analizador_Léxico import analizar_lexico
from Analizador_Sintactico import convertir_tokens, parser_lr

def main():
    entrada = input("Cadena a analizar: ")

    print("\n--- ANÁLISIS LÉXICO ---")
    tokens = analizar_lexico(entrada)

    print("\n--- TOKENS PARA PARSER ---")
    tokens_parser = convertir_tokens(tokens)
    print(tokens_parser)

    print("\n--- ANÁLISIS SINTÁCTICO ---")
    parser_lr(tokens_parser)


if __name__ == "__main__":
    main()