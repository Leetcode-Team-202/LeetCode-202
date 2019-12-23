/*
 * @lc app=leetcode id=2 lang=java
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(0), cur = res;
        for(int carry = 0; l1 != null || l2 != null || carry > 0;){
            int n1 = l1 != null ? l1.val : 0;
            l1 = l1 != null ? l1.next : null;
            int n2 = l2 != null ? l2.val : 0;
            l2 = l2 != null ? l2.next : null;

            int sum = n1 + n2 + carry;
            carry = sum / 10;
            cur.next = new ListNode(sum%10);
            cur = cur.next;
        }
        return res.next;
    }
}
// @lc code=end

