#define MAX_CHILDS 256

typedef struct trie{
    struct trie *child[MAX_CHILDS];
    bool terminal;     
} Trie;

Trie* trieCreate() {
    Trie* treeInstance = (Trie*)calloc(sizeof(Trie),1);
    return treeInstance;
}

void trieInsert(Trie* obj, char* word) {
    unsigned char *u_word = (unsigned char *)word;
    int len = strlen(word);
    for (int i = 0; i < len; i++){
        if(!obj->child[word[i]]){
            obj->child[word[i]] = trieCreate();
        }
        obj = obj->child[word[i]];
    }
    obj->terminal = true;
}

bool trieSearch(Trie* obj, char* word) {
    unsigned char *u_word = (unsigned char *)word;
    int len = strlen(word);
    for(int i = 0; i<len; i++){
        if(!obj->child[word[i]]){
            return false;
        }
        obj = obj->child[word[i]];
    }
    return obj->terminal;
}

bool trieStartsWith(Trie* obj, char* prefix) {
    unsigned char *u_word = (unsigned char *)prefix;
    int len = strlen(prefix);

    for (int i = 0; i<len; i++){
        if(!obj->child[u_word[i]]){
            return false;
        }
        obj = obj->child[u_word[i]];
    }
    return true;
}
void deleteTrie_child(Trie* obj){
        for (int i = 0; i<MAX_CHILDS; i++){
            if(obj->child[i]){
                deleteTrie_child(obj->child[i]);   
            }
        }
        free(obj);
}

void trieFree(Trie* obj) {
    if(obj){
        deleteTrie_child(obj);
        }
}


/**
 * Your Trie struct will be instantiated and called as such:
 * Trie* obj = trieCreate();
 * trieInsert(obj, word);
 
 * bool param_2 = trieSearch(obj, word);
 
 * bool param_3 = trieStartsWith(obj, prefix);
 
 * trieFree(obj);
*/