class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int n:nums){
            if(map.containsKey(n)){
                map.put(n,map.get(n)+1);
            }else{
                map.put(n,1);
                            }
        }
        for(int n:map.values()){
            if(n!=1){
                return true;
            }
        }
        return false;
    }
}
