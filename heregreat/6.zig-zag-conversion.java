/*
 * @lc app=leetcode id=6 lang=java
 *
 * [6] ZigZag Conversion
 */

// @lc code=start
import java.util.Arrays;
class Solution {
    public String convert(String s, int numRows) {
        if(numRows == 1){
            return s;
        }
        boolean down = true;
        String[] strs = new String[numRows];
        Arrays.fill(strs, "");
        for(int i = 0, k = 0; k< s.length();k++){
            strs[i] += s.charAt(k);
            if(down == true){
                if(i < numRows - 1){
                    i++;
                }else{
                    i--;
                    down = false;
                }
            }else{
                if(i>0){
                    i--;
                }else{
                    i++;
                    down = true;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for(String str:strs){
            sb.append(str);
        }
        return sb.toString();
    }
}
// @lc code=end

