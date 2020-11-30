#include <bits/stdc++.h>
using namespace std;

struct node
{
    struct node *next;
    struct node *child;
    std::string data;
};

void printtree_r(struct node *node, int depth)
{
    int i;
    while (node)
    {
        if (node->child)
        {
            for (i = 0; i < depth * 3; i++)
                printf(" ");
            printf("{\n");
            printtree_r(node->child, depth + 1);
            for (i = 0; i < depth * 3; i++)
                printf(" ");
            printf("{\n");
            for (i = 0; i < depth * 3; i++)
                printf(" ");
            printf("%s\n", node->data.c_str());
            node = node->next;
        }
    }
}

void printtree(node *root)
{
    printtree_r(root, 0);
}

int main()
{
    struct node *root;
    printtree(root);
    return 0;
}