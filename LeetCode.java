import java.util.HashMap;
import java.util.Stack;

import javax.print.attribute.standard.MediaSize.Other;

public class LeetCode {

    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        for(int i =0 ;i<nums.length;i++){
            for(int j = i+1;j<nums.length;j++){
                if(nums[i]+nums[j]==target){
                        res[0] = i;
                        res[1] = j;
                }
            }
        }
        //System.out.println("1:"+res[0]+"2:"+res[1]);
        return res;
    }

    public int reverse(int x) {
        return 0;

    }
    //2019/07/16
    public int romanToInt(String s) {//13
        int res = 0;
        HashMap<Character, Integer> m = new HashMap<>();
        m.put('I',1);
        m.put('V',5);
        m.put('X',10);
        m.put('L',50);
        m.put('C',100);
        m.put('D',500);
        m.put('M',1000);
        for(int i=0; i<s.length();i++){
            int val = m.get(s.charAt(i));
            if(i == s.length()-1 ||m.get(s.charAt(i))>= m.get(s.charAt(i+1))){
                res += val;
            }else{
                res -= val;
            }
        }   
        return res;
    }
    public String longestCommonPrefix(String[] strs) {//14
        String res = new String();
        if (strs.length == 0) return "";
        for(int i=0;i<strs[0].length();i++){
            Character c = strs[0].charAt(i);
            for(int j=1;j<strs.length;j++){
                if(i+1>strs[j].length() || c != strs[j].charAt(i)){
                    return res;
                }  
            }
            res += c.toString();
        }
        return res;
    }
    public boolean isValid(String s) {//20
        Stack<Character> m = new Stack<>();
        for(int i=0; i<s.length();i++){
            if(s.charAt(i) == '('||s.charAt(i)=='['||s.charAt(i)=='{'){
                m.push(s.charAt(i));
            }else{
                if(m.empty()){
                    return false;
                }
                switch(s.charAt(i)){
                    case ')':
                        if(m.peek()!='(') return false;
                        m.pop();
                        break;
                    case ']':
                        if(m.peek()!='[') return false;
                        m.pop(); 
                        break;
                    case '}':
                        if(m.peek()!='{') return false;
                        m.pop();  
                        break;
                }
            }
        }
        return m.empty();
    }
    public static void main(String[] args)
    {
        LeetCode S = new LeetCode();
        String x = "III";
        int rev = S.romanToInt(x);
        System.out.println(rev);
    }

}
