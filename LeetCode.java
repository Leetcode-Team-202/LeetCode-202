import java.util.HashMap;
import java.util.Stack;

import javax.print.attribute.standard.MediaSize.Other;
import Data.ListNode;

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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {//21
        ListNode res = new ListNode(-1);
        ListNode cur = res;
        while(l1!=null&&l2!=null){
            if(l1.val < l2.val){
                cur.next = l1;
                l1 = l1.next;
            }else{
                cur.next = l2;
                l2 = l2.next;
            }
            cur = cur.next;
        }
        cur.next = (l1!=null)? l1:l2;
        return res.next;
    }
    public int removeDuplicates(int[] nums) {//26
        if(nums.length == 0) return 0;
        int pre = 0, cur = 0;
        while(cur<nums.length){
            if(nums[pre]==nums[cur]) cur++;
            else nums[++pre] = nums[cur++];
        }
        return pre + 1;
    }
    //2019/07/17
    public int removeElement(int[] nums, int val) {//27
        int i = 0;
        for (int num : nums){
            if (num != val){  
                nums[i] = num; 
                i++;
            }
        }
        return i;
    }
    public int strStr(String haystack, String needle) {//28
        if (needle.isEmpty()) return 0;
        int begin = 0;
        while(begin<=haystack.length()-needle.length()){
            if(needle.equals(haystack.substring(begin, begin+needle.length()))){
                return begin;
            }
            begin ++;
        }
        return -1;
    }
    public int searchInsert(int[] nums, int target) {//35
        int index = 0;
        while(index<nums.length && target>nums[index]){
            index++;
        }
        return index;
    }
    public String countAndSay(int n) {//38
        String s = "1";
        for(int i = 1; i < n; i++){
            s = countIdx(s);
        }
        return s;
    }   
    public String countIdx(String s){
        StringBuilder sb = new StringBuilder();
        char c = s.charAt(0);
        int count = 1;
        for(int i = 1; i < s.length(); i++){
            if(s.charAt(i) == c){
                count++;
            }
            else
            {
                sb.append(count);
                sb.append(c);
                c = s.charAt(i);
                count = 1;
            }
        }
        sb.append(count);
        sb.append(c);
        return sb.toString();
    }
    //2018/09/05
    public int maxSubArray(int[] nums){
        int res = Integer.MIN_VALUE, curnum = 0;
        for(int num:nums){
            curnum = Math.max(curnum+num, num);
            res = Math.max(curnum, res);
        }
        return res;
    }
    //Medium
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {//2
        ListNode res = new ListNode(-1);
        ListNode dump = res;
        int flag = 0;
        while(l1!=null || l2!= null){
            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;
            dump.next = new ListNode((x + y + flag)%10);
            flag = (x + y + flag )/10;
            dump = dump.next;
            if(l1!=null) l1 = l1.next;
            if(l2!=null) l2 = l2.next;
        }
        if(flag>0){
            dump.next = new ListNode(flag);
        }
        return res.next; 
    }
    
    public static void main(String[] args)
    {
        LeetCode S = new LeetCode();
        int[] nums = {2,3,3,2};
        
        int rev = S.maxSubArray(nums);
        System.out.println(rev);
    }

}
