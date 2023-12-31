#include<stdio.h>
#include<arpa/inet.h>

struct addrinfo {
    int              ai_flags;     // AI_PASSIVE, AI_CANONNAME, etc.
    int              ai_family;    // AF_INET, AF_INET6, AF_UNSPEC
    int              ai_socktype;  // SOCK_STREAM, SOCK_DGRAM
    int              ai_protocol;  // use 0 for "any"
    size_t           ai_addrlen;   // size of ai_addr in bytes
    struct sockaddr *ai_addr;      // struct sockaddr_in or _in6
    char            *ai_canonname; // full canonical hostname

    struct addrinfo *ai_next;      // linked list, next node
};

struct sockaddr {
    unsigned short    sa_family;    // address family, AF_xxx, AF_INET(ipv4), AF_INET6(ipv6)
    char              sa_data[14];  // 14 bytes of protocol address
}; 


//sockaddr for ipv4
struct sockaddr_in {
    short int          sin_family;  // Address family, AF_INET
    unsigned short int sin_port;    // Port number,in  network byte order using htons() function (host to network short)
    struct in_addr     sin_addr;    // Internet address
    unsigned char      sin_zero[8]; // Same size as struct sockaddr, should be set to 0 using memset(&sockaddr_in.sin_zero, 0, sizeof(sockaddr_in.sin_zero))
};

// Internet address (a structure for historical reasons) ipv4
struct in_addr {
    uint32_t s_addr; // 32-bit int (4 bytes) to store ip address, eg 192.168.1.112
}

//ipv6
struct sockaddr_in6 {
    u_int16_t       sin6_family;   // address family, AF_INET6
    u_int16_t       sin6_port;     // port number, Network Byte Order
    u_int32_t       sin6_flowinfo; // IPv6 flow information
    struct in6_addr sin6_addr;     // IPv6 address
    u_int32_t       sin6_scope_id; // Scope ID
};

//ipv6
struct in6_addr {
    unsigned char   s6_addr[16];   // IPv6 address
};


//can hold ipv4 or ipv6 if unsure, later cast to the resepcttive version
struct sockaddr_storage {
    sa_family_t  ss_family;     // address family

    // all this is padding, implementation specific
    char      __ss_pad1[_SS_PAD1SIZE];
    int64_t   __ss_align;
    char      __ss_pad2[_SS_PAD2SIZE];
};

struct sockaddr_in sa; // IPv4
struct sockaddr_in6 sa6; // IPv6

//converts ip adress to allow it to be stored in either sockaddr_in(ipv4) or sockaddr_in6(ipv6)
inet_pton(AF_INET, "10.12.110.57", &(sa.sin_addr)); // IPv4
inet_pton(AF_INET6, "2001:db8:63b3:1::3490", &(sa6.sin6_addr)); // IPv6

// IPv4:

char ip4[INET_ADDRSTRLEN];  // space to hold the IPv4 string
struct sockaddr_in sa;      // pretend this is loaded with something

inet_ntop(AF_INET, &(sa.sin_addr), ip4, INET_ADDRSTRLEN);

printf("The IPv4 address is: %s\n", ip4);


// IPv6:

char ip6[INET6_ADDRSTRLEN]; // space to hold the IPv6 string
struct sockaddr_in6 sa6;    // pretend this is loaded with something

inet_ntop(AF_INET6, &(sa6.sin6_addr), ip6, INET6_ADDRSTRLEN);

printf("The address is: %s\n", ip6);
