#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <dirent.h>
#include <ctype.h>

void scan_processes(){
    DIR *proc = opendir("/proc");
    struct dirent *entry;
    if (!proc) {
        perror("opendir /proc");
        return;
    }   

    while ((entry = readdir(proc)) != NULL) {
        if (!isdigit(entry->d_name[0])) continue;

        char path[256], cmd[256];
        snprintf(path, sizeof(path), "/proc/%s/cmdline", entry->d_name);
        FILE *fp = fopen(path, "r");
        if (fp) {
            fgets(cmd, sizeof(cmd), fp);
            cmd[strcspn(cmd, "\n")] = 0; // Remove newline
            fclose(fp);

            if (strcmp(cmd, "bash") == 0 || strcmp(cmd, "netcat") == 0){
                printf("[!] Suspicious: PID %s - %s\n", entry->d_name, cmd);
            }
       }
    closedir(proc);
}
}

int main(){
    printf("====Process Watch Tool====\n");
    scan_processes();
    return 0;
}
