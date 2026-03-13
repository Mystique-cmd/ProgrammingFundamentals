# include <stdio.h>
# include <stdlib.h>
# include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <netinet/ip.h>

int main() {
    int sock_raw;
    struct sockaddr_in source;
    unsigned char *buffer = (unsigned char *)malloc(65536);

    sock_raw = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);
    if (sock_raw < 0) {
        perror("Socket creation failed");
        return 1;
    }

    printf("Sniffer started...waiting for packets...\n");

    while (1){
        socklen_t saddr_size = sizeof(source);
        int data_size = recvfrom(sock_raw, buffer, 65536, 0,
                                 (struct sockaddr *)&source, &saddr_size);
        if (data_size < 0) {
            perror("Recvfrom error");
            return 1;
    }

    struct iphdr *ip = (struct iphdr *)buffer;
    struct in_addr src, dest;
    src.s_addr = ip->saddr;
    dest.s_addr = ip->daddr;

    printf("[+]Packet: Src IP: %s, Dest IP: %s | Protocol: %d\n",
           inet_ntoa(src), inet_ntoa(dest), ip->protocol);
    }

    close(sock_raw);
    free(buffer);
    return 0;
}