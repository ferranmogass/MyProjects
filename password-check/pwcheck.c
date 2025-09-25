#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MIN_LENGTH 8
#define MAX_LENGTH 256
#define SUGGESTION_THRESHOLD 3 // Minimum criteria met for a valid password

int in_blacklist(const char *pwd, const char *blacklist_path) {
    if (!blacklist_path) return 0;
    FILE *f = fopen(blacklist_path, "r");
    if (!f) return 0; // Can't be opened
    char line[MAX_LENGTH];
    while (fgets(line, sizeof(line), f)) {
        line[strcspn(line, "\n")] = 0; // Remove newline character 
        if (strcmp(line, pwd) == 0) {
            fclose(f);
            return 1; // Found in blacklist
        }
    }
    fclose(f);
    return 0; 
}


void analyze_password(const char *pwd, const char *blacklist_path) {
    int length = strlen(pwd);
    int has_upper = 0, has_lower = 0, has_digit = 0, has_special = 0;
    
    printf("\n=== ANÁLISIS DE CONTRASEÑA ===\n");
    printf("Contraseña: %s\n", pwd);
    printf("Longitud: %d caracteres\n", length);
    
    // Verificar longitud
    if (length < MIN_LENGTH) {
        printf("Longitud insuficiente (mínimo %d caracteres)\n", MIN_LENGTH);
    } else {
        printf("Longitud adecuada\n");
    }
    
    // Verificar si está en lista negra
    if (in_blacklist(pwd, blacklist_path)) {
        printf("Contraseña en lista negra (muy común)\n");
    } else {
        printf("No está en lista de contraseñas comunes\n");
    }
    
    // Analizar tipos de caracteres
    for (int i = 0; i < length; i++) {
        if (isupper(pwd[i])) has_upper = 1;
        else if (islower(pwd[i])) has_lower = 1;
        else if (isdigit(pwd[i])) has_digit = 1;
        else has_special = 1;           
    }
    
    printf("\nTipos de caracteres:\n");
    printf("%s Mayúsculas (A-Z)\n", has_upper ? "✅" : "❌");
    printf("%s Minúsculas (a-z)\n", has_lower ? "✅" : "❌");
    printf("%s Números (0-9)\n", has_digit ? "✅" : "❌");
    printf("%s Símbolos (!@#$%%...)\n", has_special ? "✅" : "❌");
    
    int criteria_met = has_upper + has_lower + has_digit + has_special;
    int score = 0;
    
    // Calcular puntuación
    if (length >= MIN_LENGTH) score += 2;
    if (length >= 12) score += 1;
    score += criteria_met;
    if (!in_blacklist(pwd, blacklist_path)) score += 2;
    
    printf("\nPuntuación: %d/10\n", score);
    
    // Determinar nivel de seguridad
    if (score >= 8) {
        printf("NIVEL: FUERTE\n");
    } else if (score >= 5) {
        printf("NIVEL: MEDIO\n");
    } else {
        printf("NIVEL: DÉBIL\n");
    }
    
    // Recomendaciones
    if (score < 8) {
        printf("\nRecomendaciones:\n");
        if (length < MIN_LENGTH) printf("• Usa al menos %d caracteres\n", MIN_LENGTH);
        if (length < 12) printf("• Considera usar 12+ caracteres\n");
        if (!has_upper) printf("• Incluye letras mayúsculas\n");
        if (!has_lower) printf("• Incluye letras minúsculas\n");
        if (!has_digit) printf("• Incluye números\n");
        if (!has_special) printf("• Incluye símbolos especiales\n");
        if (in_blacklist(pwd, blacklist_path)) printf("• Evita contraseñas comunes\n");
    }
    
    printf("\n");
}

void print_usage(const char *prog_name) {
    printf("Uso: %s <contraseña> [archivo_lista_negra]\n", prog_name);
    printf("Analiza la fortaleza de una contraseña.\n\n");
    printf("Parámetros:\n");
    printf("  <contraseña>        La contraseña a verificar (entre comillas si tiene espacios)\n");
    printf("  [archivo_lista_negra] Archivo opcional con contraseñas comunes a evitar\n\n");
    printf("Ejemplos:\n");
    printf("  %s \"MiContraseña123!\"\n", prog_name);
    printf("  %s \"password123\" common_passwords.txt\n", prog_name);
}   

int main(int argc, char *argv[]) {
    printf("🔐 DETECTOR DE CONTRASEÑAS DÉBILES\n");
    printf("==================================\n");
    
    if (argc < 2 || argc > 3) {
        print_usage(argv[0]);
        return EXIT_FAILURE;
    }

    const char *password = argv[1];
    const char *blacklist_path = (argc == 3) ? argv[2] : NULL;
    
    // Mostrar análisis detallado
    analyze_password(password, blacklist_path);

    return EXIT_SUCCESS;
}


