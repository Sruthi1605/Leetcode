/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
     struct ListNode* result = NULL;
    struct ListNode* prev = NULL;
    int carry = 0;
    while (l1 || l2) {
        int sum = carry + (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
        carry = (sum >= 10) ? 1 : 0;
        sum = sum % 10;

        struct ListNode* node = malloc(sizeof(struct ListNode));
        node->val = sum;
        node->next = NULL;

        if (!result) result = node;
        else prev->next = node;
        prev = node;

        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
    }
    if (carry > 0) {
        struct ListNode* node = malloc(sizeof(struct ListNode));
        node->val = carry;
        node->next = NULL;
        prev->next = node;
    }
    return result;
}
