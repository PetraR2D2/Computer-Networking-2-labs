#include <stdio.h>
#include <iostream>
#include <arpa/inet.h>
#include <string.h> /* memset() */

#define MAX_MSG 10000
using namespace std;

int main(int argc, char *argv[])
{
    int socketDescriptor, rc, n;
    socklen_t cliLen;
    struct sockaddr_in cliAddr, servAddr;
    char buffer[MAX_MSG];
    char killSwitch[20];
    
    strcpy(killSwitch, "Kill");

    socketDescriptor = socket(AF_INET, SOCK_DGRAM, 0);

    servAddr.sin_family = AF_INET;
    inet_pton(AF_INET, "127.0.0.1", &(servAddr.sin_addr.s_addr));   // server IP address (local-host)
    servAddr.sin_port = htons(8000);                                // server port
    rc = bind(socketDescriptor, (struct sockaddr *)&servAddr, sizeof(servAddr));

    /* fill out buffer with zeros */
    memset(buffer, 0, MAX_MSG);
    
    // Listening for the messages until killed 
    while (strcmp(buffer, killSwitch) != 0)
    {
        /* get message */
        cliLen = sizeof(cliAddr);
        printf("Receiving command from client.\n");        
        n = recvfrom(socketDescriptor, buffer, MAX_MSG, 0, (struct sockaddr *)&cliAddr, &cliLen);
        if (n > 0) /*send message back*/
        {
            printf("Recieved from client %s.\n", buffer);
            sendto(socketDescriptor, buffer, n, 0, (struct sockaddr *)&cliAddr, cliLen);
        }
    }
    printf("Terminating server on %s command.\n", killSwitch);
    return 0;
}