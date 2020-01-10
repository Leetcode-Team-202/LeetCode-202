/*
 * @lc app=leetcode id=5 lang=java
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
class Solution {
    public String longestPalindrome(String s) {
        int[] res = new int[2];
        for(int i = 0; i < s.length(); i++){
            helper(s, i-1, i+1, res);
            helper(s, i, i+1, res);
        }
        return s.substring(res[1], res[1]+res[0]);
    }
    private void helper(String s, int left, int right, int[] res){
        for( ; left >= 0 && right < s.length(); left--, right++){
            if(s.charAt(left) != s.charAt(right)){
                break;
            }
        }
        int len = --right - ++left + 1;
        if(len > res[0]){
            res[0] = len;
            res[1] = left;
        }
    }
}
// @lc code=end

