public class LeetCode {

    private int[] twoSum(int[] nums, int target) {
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

    private int reverse(int x) {
        return 0;

    }

    public static void main(String[] args)
    {
        LeetCode S = new LeetCode();
        int x = 9;
        int[] rev = S.twoSum(new int[]{2,7,11,15},x);
        System.out.println(rev[0]);
    }

}
