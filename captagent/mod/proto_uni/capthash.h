#ifndef _CAPTHASH_H
#define _CAPTHASH_H

#include "uthash.h"
#include "src/api.h"

extern int expire_hash_value;

typedef struct ipport_items {
  char name[300]; 
  char callid[250];  
  long modify_ts;
  UT_hash_handle hh; 
} ipport_items_t;

void add_ipport(char *key, str *callid);
struct ipport_items *find_ip_port_paar(char *ip, int port);
struct ipport_items *find_ipport(char *name);
int clear_ipport(struct ipport_items *ipport );
int check_ipport(char *name);
int delete_ipport(char *ip, int port);
void clear_ipports();
int find_and_update(char *callid, const char *srcip, int srcport, const char *dstip, int dstport);


#endif
