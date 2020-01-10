import java.util.HashMap;
import java.util.HashSet;

/*
 * @lc app=leetcode id=3 lang=java
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0, left = 0, right = 0;
        HashSet<Character> t = new HashSet<Character>();
        while(right < s.length()){
            if(!t.contains(s.charAt(right))){
                t.add(s.charAt(right++));
                res = Math.max(t.size(), res);
            }else{
                t.remove(s.charAt(left++));
            }
        }
        return res;
    }
}
// @lc code=end

