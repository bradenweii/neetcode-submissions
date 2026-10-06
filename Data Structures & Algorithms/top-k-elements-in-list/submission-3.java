class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();
        List<int[]> list = new ArrayList<>();
        for(int n:nums){
            if(map.containsKey(n)){
                map.put(n,map.get(n)+1);
            }else{
            map.put(n, 1);}
        } 
        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            list.add(new int[]{entry.getValue(),entry.getKey()});
        }

       System.out.println(Arrays.toString(list.get(0)));

        int[] arr = new int[k];
        int j=0;
        return arr;


    }
}
