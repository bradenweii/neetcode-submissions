class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();
        List<Integer> list = new ArrayList<>();
        for(int n:nums){
            if(map.containsKey(n)){
                map.put(n,map.get(n)+1);
            }else{
            map.put(n, 1);}
        } 
        for(int n:map.keySet()){
            list.add(n);
        }

        int[] arr = new int[k];
        int j=0;
       for(int i=list.size()-1;i>list.size()-1-k;i--){
        arr[j]=list.get(i);
        j++;
       }
       System.out.println(map);
        return arr;


    }
}
