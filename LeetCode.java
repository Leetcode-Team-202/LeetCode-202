import java.util.*;
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
    public int maxSubArray(int[] nums){//最大子串
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
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        for(int i=n-1; i>=0; i--){
            if (digits[i]<9){
                digits[i]++;
                return digits;
            } 
            digits[i] = 0;
        }
        int[] res = new int[n+1];
        res[0]=1;
        return res;
    }
    //2019/09/06
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m-1, j = n-1, k = m+n-1;
        while(i>=0 && j>=0){
            if(nums1[i]>nums2[j]){
                nums1[k] = nums1[i];
                k--;i--;
            }else{
                nums1[k] = nums2[j];
                k--;j--;
            }
        }
        while(j>=0){
            nums1[k] = nums2[j];
            k--;j--;
        }
    }
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        ArrayList<Integer> row = new ArrayList<>();
        for(int i = 0; i<numRows; i++){
            row.add(0,1);
            for(int j =1; j<row.size()-1; j++){
                row.set(j, row.get(j)+row.get(j+1));
            }
            res.add(new ArrayList<>(row));
        }
        return res;
    }
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<>();
        for(int i =0; i<= rowIndex; i++){
            row.add(0,1);
            for(int j =1; j<row.size()-1; j++){
                row.set(j, row.get(j)+row.get(j+1));
            }
        }   
        return row;
    }
    public int maxProfit(int[] prices) {//121
        int maxprofit = 0, min = Integer.MAX_VALUE;
        for(int price : prices){
            int profit = price - min;
            if(profit > maxprofit){
                maxprofit = profit;
            }
            min = Math.min(min, price);
        }
        return maxprofit;   
    }
    public int maxProfit2(int[] prices) {//122
        int profit = 0;
        for(int i = 1; i<prices.length; i++){
            if(prices[i] > prices[i-1]){
                profit += prices[i] - prices[i-1];
            }
        }
        return profit;
    }
    public int maxArea(int[] height) {//11
        int i=0, j=height.length-1, res = 0;
        while(i<j){
            res = Math.max(res, Math.min(height[i], height[j]) * (j -i));
            if(height[i] < height[j]){
                i++;
            }else j--;
        }
        return res;
    }
    //2019/09/08
    public List<List<Integer>> threeSum(int[] nums) {//15. 3sum
        Arrays.sort(nums);
        List<List<Integer>> res = new LinkedList<>();
        for(int i = 0;i<nums.length; i++){
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            for(int j = i + 1, k = nums.length - 1; j < k;){
                int sum = nums[i] + nums[j] + nums[k];
                if(sum > 0){
                    k--;
                }else if(sum < 0){
                    j++;
                }else{
                    res.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    while(j<k && nums[j] == nums[j+1]) j++;
                    while(j<k && nums[k] == nums[k-1]) k--;
                    j++;
                    k--;
                }
            }
        }
        return res;
    }
    public int threeSumClosest(int[] nums, int target) {//16. 3sum Closest
        Arrays.sort(nums);
        int min_diff = Integer.MAX_VALUE, res = 0;
        for(int i = 0; i< nums.length - 2; i++){
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            for(int j = i + 1, k = nums.length - 1; j < k;){
                int sum = nums[i] + nums[j] + nums[k];
                if(sum < target){
                    j++;
                }else if(sum > target){
                    k--;
                }else return sum;
                int diff = Math.abs(sum - target);
                if(diff < min_diff){
                    min_diff = diff;
                    res = sum;
                }
            }
        }
        return res;
    }
    public List<List<Integer>> fourSum(int[] nums, int target) {//18. 4sum
        Arrays.sort(nums);
        List<List<Integer>> res = new LinkedList<>();
        for(int i = 0; i< nums.length-3; i++){
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            for(int j = i +1; j < nums.length-2; j++){
                if(j > i+1 && nums[j] == nums[j-1]){
                    continue;
                }
                for(int l = j + 1, r = nums.length - 1; l < r;){
                    int sum = nums[i] + nums[j] + nums[l] + nums[r];
                    if(sum < target){
                        l++;
                    }else if(sum > target){
                        r--;
                    }else{
                        res.add(Arrays.asList(nums[i], nums[j], nums[l], nums[r]));
                        while(l < r && nums[l] == nums[l+1]) l++;
                        while(l < r && nums[r] == nums[r-1]) r--;
                        l++;
                        r--;
                    }
                }
            }
        }
        return res;
    }
    public void nextPermutation(int[] nums) {//31 Next Permutation
        
    }
    
    public static void main(String[] args)
    {
        LeetCode S = new LeetCode();
        int[] nums = {2,3,3,2};
        
        int rev = S.maxProfit(nums);
        System.out.println(rev);
    }

}
